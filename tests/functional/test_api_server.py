import json
import threading
import unittest
from http.server import HTTPServer
from urllib.request import Request, urlopen

from safeexec.api.server import make_handler


class ApiServerTests(unittest.TestCase):
    def test_post_execute_returns_structured_result(self):
        server = HTTPServer(("127.0.0.1", 0), make_handler("local"))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            url = f"http://127.0.0.1:{server.server_port}/execute"
            request = Request(
                url,
                data=json.dumps({"code": "print('api ok')"}).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urlopen(request, timeout=5) as response:
                payload = json.loads(response.read().decode("utf-8"))
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)

        self.assertEqual(payload["status"], "ok")
        self.assertEqual(payload["backend"], "local")
        self.assertEqual(payload["stdout"], "api ok\n")
        self.assertIn("duration_ms", payload)


if __name__ == "__main__":
    unittest.main()
