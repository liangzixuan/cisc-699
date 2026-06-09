import unittest

from safeexec.backends.docker import DockerBackend
from safeexec.models import ExecutionRequest


class DockerCommandTests(unittest.TestCase):
    def test_hardened_docker_command_contains_planned_controls(self):
        request = ExecutionRequest.from_mapping({"code": "print('x')", "backend": "docker"})
        command = DockerBackend().build_command(request)
        command_text = " ".join(command)

        self.assertIn("--network none", command_text)
        self.assertIn("--read-only", command)
        self.assertIn("--cap-drop ALL", command_text)
        self.assertIn("--security-opt no-new-privileges", command_text)
        self.assertIn("--pids-limit 64", command_text)
        self.assertIn("--user 65534:65534", command_text)
        self.assertEqual(command[-4:], ["python:3.11-slim", "python", "-I", "-"])

    def test_gvisor_command_selects_runsc_runtime(self):
        request = ExecutionRequest.from_mapping({"code": "print('x')", "backend": "gvisor"})
        command = DockerBackend(runtime="runsc", name="gvisor").build_command(request)

        self.assertIn("--runtime", command)
        self.assertIn("runsc", command)


if __name__ == "__main__":
    unittest.main()
