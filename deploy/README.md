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
