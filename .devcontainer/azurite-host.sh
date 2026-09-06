#!/usr/bin/env bash
# Docker orchestration belongs on the Mac host.
set -euo pipefail
repo_dir="$(cd "$(dirname "$0")/.." && pwd)"
compose=(docker compose -f "$repo_dir/.devcontainer/compose.azurite.yaml")
attach() {
  local container_id="${1:?Supply the GRE development container ID}"
  local workspace
  workspace="$(docker inspect --format '{{range .Mounts}}{{if eq .Destination "/workspaces/global-recovery-engine"}}{{.Source}}{{end}}{{end}}' "$container_id")"
  if [[ "$workspace" != "$repo_dir" ]]; then
    echo 'Container does not mount this checkout at the GRE workspace path.' >&2
    exit 1
  fi
  if [[ "$(docker inspect --format '{{if index .NetworkSettings.Networks "gre-azurite"}}yes{{end}}' "$container_id")" != yes ]]; then
    docker network connect gre-azurite "$container_id"
  fi
  echo "GRE development container attached to gre-azurite: $container_id"
}
status() {
  local azurite_id image_id
  azurite_id="$("${compose[@]}" ps -a -q azurite)"
  if [[ -z "$azurite_id" ]]; then
    echo 'Azurite container has not been created.' >&2
    exit 1
  fi
  "${compose[@]}" ps
  docker network inspect gre-azurite --format 'Internal={{.Internal}}'
  docker inspect "$azurite_id" --format 'Host port bindings={{json .HostConfig.PortBindings}}'
  docker inspect "$azurite_id" --format '{{range .Mounts}}{{if eq .Type "volume"}}Volume={{.Name}} -> {{.Destination}}{{end}}{{end}}'
  image_id="$(docker inspect "$azurite_id" --format '{{.Image}}')"
  docker image inspect "$image_id" --format '{{.Os}}/{{.Architecture}} {{json .RepoDigests}}'
  # Shared ignored receipt lets the SDK probe reject verification without restart.
  umask 077
  mkdir -p "$repo_dir/local-data/azurite"
  docker inspect "$azurite_id" --format '{"container_id":{{json .Id}},"started_at":{{json .State.StartedAt}}}' > "$repo_dir/local-data/azurite/server.json"
  cat "$repo_dir/local-data/azurite/server.json"
}
case "${1:-}" in
  up)
    umask 077
    mkdir -p "$repo_dir/local-data/azurite"
    if [[ ! -e "$repo_dir/local-data/azurite/.env" ]]; then
      printf 'AZURITE_ACCOUNTS=gredev:' > "$repo_dir/local-data/azurite/.env"
      openssl rand -base64 48 >> "$repo_dir/local-data/azurite/.env"
    fi
    "${compose[@]}" up -d --wait --wait-timeout 120 azurite
    if [[ -n "${2:-}" ]]; then attach "$2"; fi
    "${compose[@]}" exec -T azurite azurite-blob --version
    "${compose[@]}" exec -T azurite uname -m
    "${compose[@]}" exec -T azurite id
    status
    ;;
  attach) attach "${2:-}" ;;
  restart)
    "${compose[@]}" restart azurite
    "${compose[@]}" up -d --wait --wait-timeout 120 azurite
    status
    ;;
  stop) "${compose[@]}" stop azurite ;;
  status) status ;;
  *) echo "Usage: bash $0 {up [GRE_CONTAINER_ID]|attach GRE_CONTAINER_ID|restart|stop|status}" >&2; exit 2 ;;
esac
