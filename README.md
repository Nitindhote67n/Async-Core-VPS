# 🛡️ Node-Sentinel-Base
> A lightweight, containerized monitoring engine for VPS environments.

![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)

## Features
- **Async Execution:** Handles multiple monitoring tasks without blocking.
- **Dockerized:** Deploy instantly on any VPS or Linux instance.
- **Automated Logging:** Saves activity history to `node_activity.log`.

## Quick Start
```bash
docker build -t node-sentinel .
docker run -d --name sentinel-instance node-sentinel

