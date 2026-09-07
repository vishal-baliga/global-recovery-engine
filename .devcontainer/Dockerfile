# syntax=docker/dockerfile:1
# Keep these defaults aligned with devcontainer.json build.args.
ARG PYTHON_VERSION=3.14.7
ARG NODE_VERSION=24.20.0
ARG UV_VERSION=0.12.10

FROM node:${NODE_VERSION}-bookworm-slim AS node_toolchain
FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv_toolchain
FROM python:${PYTHON_VERSION}-slim-bookworm

ARG PNPM_VERSION=11.10.0

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        bash build-essential ca-certificates curl git openssh-client \
        procps ripgrep unzip xz-utils \
    && rm -rf /var/lib/apt/lists/*

# Copy Node and npm together without importing unrelated global executable links.
COPY --from=node_toolchain /usr/local/bin/node /usr/local/bin/node
COPY --from=node_toolchain /usr/local/lib/node_modules /usr/local/lib/node_modules
COPY --from=uv_toolchain /uv /uvx /usr/local/bin/

RUN ln -s ../lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm \
    && ln -s ../lib/node_modules/npm/bin/npx-cli.js /usr/local/bin/npx \
    && npm install --global --no-audit --no-fund "pnpm@${PNPM_VERSION}" \
    && npm cache clean --force \
    && groupadd --gid 1000 vscode \
    && useradd --uid 1000 --gid vscode --create-home --shell /bin/bash vscode

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_LINK_MODE=copy \
    PNPM_HOME=/home/vscode/.local/share/pnpm
ENV PATH="/home/vscode/.local/bin:/home/vscode/.local/share/pnpm:${PATH}"

USER vscode
RUN python -c "import ssl, sqlite3" \
    && node --version \
    && npm --version \
    && pnpm --version \
    && uv --version \
    && mkdir -p /home/vscode/.cache/uv /home/vscode/.local/share/pnpm

WORKDIR /workspaces/global-recovery-engine
CMD ["sleep", "infinity"]
