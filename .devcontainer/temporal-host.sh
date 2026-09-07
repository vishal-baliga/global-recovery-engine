#!/usr/bin/env bash
# Docker orchestration belongs on the Mac host.
set -euo pipefail
repo_dir="$(cd "$(dirname "$0")/.." && pwd)"
compose=(docker compose -f "$repo_dir/.devcontainer/compose.temporal.yaml")
attach() {
  local container_id="${1:?Supply the GRE development container ID}"
  local workspace
  workspace="$(docker inspect --format '{{range .Mounts}}{{if eq .Destination "/workspaces/global-recovery-engine"}}{{.Source}}{{end}}{{end}}' "$container_id")"
  if [[ "$workspace" != "$repo_dir" ]]; then
    echo 'Container does not mount this checkout at the GRE workspace path.' >&2
    exit 1
  fi
  if [[ "$(docker inspect --format '{{if index .NetworkSettings.Networks "gre-temporal"}}yes{{end}}' "$container_id")" != yes ]]; then
    docker network connect gre-temporal "$container_id"
  fi
  echo "GRE development container attached to gre-temporal: $container_id"
}
status() {
  local temporal_id image_id
  temporal_id="$("${compose[@]}" ps -a -q temporal)"
  if [[ -z "$temporal_id" ]]; then
    echo 'Temporal container has not been created.' >&2
    exit 1
  fi
  "${compose[@]}" ps
  docker network inspect gre-temporal --format 'Internal={{.Internal}}'
  docker inspect "$temporal_id" --format 'Host port bindings={{json .HostConfig.PortBindings}}'
  docker inspect "$temporal_id" --format '{{range .Mounts}}{{if eq .Type "volume"}}Volume={{.Name}} -> {{.Destination}}{{end}}{{end}}'
  image_id="$(docker inspect "$temporal_id" --format '{{.Image}}')"
  docker image inspect "$image_id" --format '{{.Os}}/{{.Architecture}} {{json .RepoDigests}}'
  # Shared ignored receipt lets the SDK probe reject verification without restart.
  umask 077
  mkdir -p "$repo_dir/local-data/temporal"
  docker inspect "$temporal_id" --format '{"container_id":{{json .Id}},"started_at":{{json .State.StartedAt}}}' > "$repo_dir/local-data/temporal/server.json"
  cat "$repo_dir/local-data/temporal/server.json"
}
case "${1:-}" in
  up)
    "${compose[@]}" up -d --wait --wait-timeout 120 temporal
    if [[ -n "${2:-}" ]]; then attach "$2"; fi
    "${compose[@]}" exec -T temporal temporal --version
    "${compose[@]}" exec -T temporal uname -m
    "${compose[@]}" exec -T temporal id
    status
    ;;
  attach) attach "${2:-}" ;;
  restart)
    "${compose[@]}" restart temporal
    "${compose[@]}" up -d --wait --wait-timeout 120 temporal
    status
    ;;
  stop) "${compose[@]}" stop temporal ;;
  status) status ;;
  *) echo "Usage: bash $0 {up [GRE_CONTAINER_ID]|attach GRE_CONTAINER_ID|restart|stop|status}" >&2; exit 2 ;;
esac
