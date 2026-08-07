---
name: self-hosted-web-deployment
description: "Deploy web services with Tailscale, auth, and systemd."
version: 1.0.0
author: Hermes Agent
tags: [deployment, tailscale, systemd, web-service, self-hosted, linux]
---

# Self-Hosted Web Deployment

Deploy a Python web service on a Linux machine, secure it with password auth, make it accessible over Tailscale (with HTTPS), and ensure it survives reboots via systemd.

## Overview

This skill covers the end-to-end deployment pattern for Python web services on Linux:

1. **Clone & install** the service  
2. **Password auth** — never bind to a non-loopback address without it  
3. **Askpass cleanup** — delete the password helper immediately after use  
4. **Tailscale** — VPN tunnel with automatic HTTPS via `tailscale serve`  
5. **Systemd auto-start** — survive reboots  
6. **Verification** — health check over the wire

## Pitfalls

- **Verify the service type.** Users often assume a repo is Node.js because of a `package.json`. Always check: if `server.py` or `bootstrap.py` exists, it's Python. The `package.json` may be dev-only ESLint tooling.
- **Don't pipe passwords into `sudo -S`.** The Hermes security guard blocks this. Use `SUDO_ASKPASS` with a helper script instead (write `~/askpass.sh` with `echo "$PASSWORD"`, chmod it, then `SUDO_ASKPASS=~/askpass.sh sudo -A <command>`). **Delete the askpass script immediately** after finishing — it contains the plaintext password. Do not leave it in `~/.hermes/scripts/` or anywhere persistent.
- **Tailscale must be authenticated before `tailscale serve` works.** The `tailscale up` command prints a URL. The user must visit it in a browser and sign in with their Tailscale account before the machine shows up on their tailnet.
- **`tailscale serve` is disabled on some tailnets** (Tailscale admin console -> Serve -> enable). If it fails, the fallback is binding to `0.0.0.0`. **Only do this after confirming password auth is active** — never expose an unauthenticated WebUI.
- **The server may auto-detect the Hermes Agent venv.** hermes-webui finds `~/.hermes/hermes-agent/venv/bin/python` automatically and uses it; no need to force a specific Python path.
- **systemd `After=` ordering matters.** Add `tailscaled.service` as a `Wants=` dependency so the web service starts after Tailscale is up.
- **Shallow clone.** Repos with 7,500+ commits (like hermes-webui) will time out on a full clone. Use `git clone --depth 1` instead.

## Step-by-Step

### 1. Clone & Install

```bash
git clone --depth 1 <repo-url> ~/<app-name>
cd ~/<app-name>
pip install -r requirements.txt
```

### 2. Password Auth

Create an `.env` file in the repo root (or pass env vars directly):

```
HERMES_WEBUI_PASSWORD=<generate-with: python3 -c "import secrets; print(secrets.token_urlsafe(24))">
HERMES_WEBUI_HOST=127.0.0.1
HERMES_WEBUI_PORT=8787
```

### 3. Tailscale

**Install:**

See `references/tailscale-install-ubuntu.md` for the exact Ubuntu/Mint procedure — the apt repo must be added by downloading key and list files separately (the `curl | sudo tee` pattern is blocked).

Or use the automated script:

**Authenticate:** `sudo tailscale up` — tell the user to visit the printed URL.

**Serve (HTTPS):** `tailscale serve --bg 8787` gives a `https://<machine>.<tailnet>.ts.net` URL.

**Fallback (no HTTPS):** Set `HERMES_WEBUI_HOST=0.0.0.0` and access via `http://<tailscale-ip>:8787`.

### 4. Systemd Service

Create a wrapper script (`~/<app-name>/start-server.sh`):

```bash
#!/bin/bash
cd /home/<user>/<app-name>
python3 server.py
```

Service file at `/etc/systemd/system/<app-name>.service`:

```ini
[Unit]
Description=<App Name>
After=network-online.target tailscaled.service
Wants=tailscaled.service
BindsTo=tailscaled.service    # stop if tailscaled stops (stronger than Wants=)

[Service]
Type=simple
User=<user>
WorkingDirectory=/home/<user>/<app-name>
ExecStart=/home/<user>/<app-name>/start-server.sh
Restart=on-failure
RestartSec=5
Environment=HERMES_WEBUI_PASSWORD=<password>
Environment=HERMES_WEBUI_HOST=127.0.0.1
Environment=HERMES_WEBUI_PORT=8787
LimitNOFILE=4096

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now <app-name>
```

### 5. Verification

```bash
# Local health check
curl http://127.0.0.1:8787/health

# Over Tailscale (direct IP — works when bound to 0.0.0.0)
curl http://$(tailscale ip -4):8787/health

# Over Tailscale Serve HTTPS — from the serving machine itself,
# the *.ts.net hostname may not resolve locally. Use --resolve or --connect-to:
TAIL_IP=$(tailscale ip -4)
curl -sk --resolve hostname.tailNNNN.ts.net:443:${TAIL_IP} https://hostname.tailNNNN.ts.net/health
# Or:
curl -sk --connect-to ::${TAIL_IP}: https://hostname.tailNNNN.ts.net/health
```

The `--resolve` / `--connect-to` is only needed when testing from the serving machine. On another device on the tailnet, the DNS resolves correctly through Tailscale's MagicDNS.

## Usage with Hermes

When the user asks to "set up Hermes Web UI for iPhone access," this is the workflow. Load the `hermes-agent` skill's `references/configuration.md` for `.env` reference details, but follow this deployment skill for the infrastructure.

The Hermex iPhone app connects to the server via:
- **Server URL**: `http://<tailscale-ip>:8787` or the `*.ts.net` hostname
- **Password**: The `HERMES_WEBUI_PASSWORD` value
