import unittest

from safeexec.models import ExecutionRequest
from safeexec.service import execute_code


class LocalSubprocessBackendTests(unittest.TestCase):
    def test_executes_small_python_program(self):
        request = ExecutionRequest.from_mapping(
            {
                "backend": "local",
                "code": "print(sum([1, 2, 3]))",
                "limits": {"wall_seconds": 2.0},
            }
        )

        result = execute_code(request)

        self.assertEqual(result.status, "ok")
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.stdout, "6\n")
        self.assertEqual(result.backend, "local")

    def test_timeout_is_reported_as_contained(self):
        request = ExecutionRequest.from_mapping(
            {
                "backend": "local",
                "code": "while True:\n    pass\n",
                "limits": {"wall_seconds": 0.2},
            }
        )

        result = execute_code(request)

        self.assertEqual(result.status, "timeout")
        self.assertTrue(result.contained)
        self.assertEqual(result.containment_reason, "wall_timeout")


if __name__ == "__main__":
    unittest.main()
