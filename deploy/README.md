# Deployment Notes

The W5 baseline keeps deployment deliberately small:

1. `make api` starts the local development API on `127.0.0.1:8080`.
2. `docker compose -f deploy/docker-compose.yaml up` starts the same API in a
   read-only project mount for API-shell inspection.
3. The execution backend target for W6 remains hardened Docker on the Ubuntu
   droplet recorded in `engineering-log.md`.

The container hardening command shape is implemented in
`src/safeexec/backends/docker.py` and covered by
`tests/functional/test_docker_command.py`. The compose file is not the final
sandbox boundary; it is only a convenient service wrapper for the API shell.

## Reproducibility check path

For W10, the documented independent setup path is:

```bash
git clone https://github.com/liangzixuan/cisc-699.git
cd cisc-699
cp .env.example .env
make smoke
make test
make validate
make repro-audit
```

On a Linux target host with Docker and gVisor:

```bash
docker pull python:3.11-slim
PYTHONPATH=src python3 scripts/run_validation_workflow.py --output-dir docs/10-hard-stop-5/evidence-target --repeat 3 --include-docker
```

If `make` is unavailable, use the equivalent direct Python commands in
`docs/reproducibility/runbook.md`.
