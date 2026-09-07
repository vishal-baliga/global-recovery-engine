#!/usr/bin/env bash
# Run on the Mac host from any working directory. Never mounts Docker into GRE.
set -euo pipefail
repo_dir="$(cd "$(dirname "$0")/.." && pwd)"
compose=(docker compose -f "$repo_dir/.devcontainer/compose.postgres.yaml")
attach() {
  local container_id="${1:?Supply the GRE development container ID}"
  # Reject an unrelated container before attaching it to the database network.
  local workspace
  workspace="$(docker inspect --format '{{range .Mounts}}{{if eq .Destination "/workspaces/global-recovery-engine"}}{{.Source}}{{end}}{{end}}' "$container_id")"
  if [[ "$workspace" != "$repo_dir" ]]; then
    echo 'Container does not mount this checkout at the GRE workspace path.' >&2
    exit 1
  fi
  if [[ "$(docker inspect --format '{{if index .NetworkSettings.Networks "gre-database"}}yes{{end}}' "$container_id")" != yes ]]; then
    docker network connect gre-database "$container_id"
  fi
  echo "GRE development container attached to gre-database: $container_id"
}
case "${1:-}" in
  up)
    umask 077
    mkdir -p "$repo_dir/local-data/postgres"
    if [[ ! -e "$repo_dir/local-data/postgres/password" ]]; then
      openssl rand -hex 32 > "$repo_dir/local-data/postgres/password"
    fi
    # Compose mounts file-backed secrets without remapping UID/mode. PostgreSQL
    # must read the mounted file; the host parent directory stays private.
    chmod 700 "$repo_dir/local-data/postgres"
    chmod 644 "$repo_dir/local-data/postgres/password"
    "${compose[@]}" up -d --wait --wait-timeout 90 postgres
    if [[ -n "${2:-}" ]]; then attach "$2"; fi
    docker image inspect postgres:18.6-bookworm --format '{{.Os}}/{{.Architecture}} {{json .RepoDigests}}'
    "${compose[@]}" exec -T postgres postgres --version
    ;;
  attach) attach "${2:-}" ;;
  restart)
    "${compose[@]}" restart postgres
    "${compose[@]}" up -d --wait --wait-timeout 90 postgres
    ;;
  stop) "${compose[@]}" stop postgres ;;
  status)
    "${compose[@]}" ps
    docker network inspect gre-database --format 'Internal={{.Internal}}'
    postgres_id="$("${compose[@]}" ps -a -q postgres)"
    if [[ -z "$postgres_id" ]]; then
      echo 'PostgreSQL container has not been created.' >&2
      exit 1
    fi
    docker inspect "$postgres_id" --format 'Host port bindings={{json .HostConfig.PortBindings}}'
    docker inspect "$postgres_id" --format '{{range .Mounts}}{{if eq .Type "volume"}}Volume={{.Name}} -> {{.Destination}}{{end}}{{end}}'
    ;;
  *) echo "Usage: bash $0 {up [GRE_CONTAINER_ID]|attach GRE_CONTAINER_ID|restart|stop|status}" >&2; exit 2 ;;
esac
