from __future__ import annotations

import argparse
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any

from safeexec.models import ExecutionRequest
from safeexec.service import execute_code


def make_handler(default_backend: str = "local"):
    class SafeExecHandler(BaseHTTPRequestHandler):
        server_version = "SafeExecHTTP/0.1"

        def do_GET(self) -> None:
            if self.path != "/health":
                self._send_json({"error": "not_found"}, status=404)
                return
            self._send_json({"status": "ok", "service": "safeexec", "backend": default_backend})

        def do_POST(self) -> None:
            if self.path != "/execute":
                self._send_json({"error": "not_found"}, status=404)
                return

            try:
                payload = self._read_json()
                payload.setdefault("backend", default_backend)
                request = ExecutionRequest.from_mapping(payload)
                result = execute_code(request)
            except Exception as exc:
                self._send_json({"error": str(exc)}, status=400)
                return

            self._send_json(result.to_dict())

        def log_message(self, format: str, *args: Any) -> None:
            return

        def _read_json(self) -> dict[str, Any]:
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length)
            value = json.loads(raw.decode("utf-8"))
            if not isinstance(value, dict):
                raise ValueError("JSON request body must be an object")
            return value

        def _send_json(self, value: dict[str, Any], status: int = 200) -> None:
            body = json.dumps(value, indent=2, sort_keys=True).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    return SafeExecHandler


def run(host: str, port: int, backend: str) -> None:
    httpd = HTTPServer((host, port), make_handler(backend))
    print(f"SafeExec API listening on http://{host}:{port} using backend={backend}")
    httpd.serve_forever()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the SafeExec W5 API shell.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8080)
    parser.add_argument("--backend", default="local")
    args = parser.parse_args(argv)
    run(args.host, args.port, args.backend)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
