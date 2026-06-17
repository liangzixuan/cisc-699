import tempfile
import unittest
from pathlib import Path

from scripts.run_validation_workflow import run_api_trace, summarize


class ValidationWorkflowTests(unittest.TestCase):
    def test_api_trace_executes_against_local_handler(self):
        with tempfile.TemporaryDirectory() as tmp:
            trace = run_api_trace(Path(tmp))

        self.assertTrue(trace["passed"])
        self.assertEqual(trace["status_code"], 200)
        self.assertEqual(trace["response"]["stdout"], "api validation\n")

    def test_summary_marks_failed_records(self):
        records = [
            {"backend": "local", "passed": True},
            {"backend": "local", "passed": False},
        ]
        summary = summarize(records, {"passed": True})

        self.assertFalse(summary["all_passed"])
        self.assertEqual(summary["by_backend"]["local"]["passed"], 1)
        self.assertEqual(summary["by_backend"]["local"]["failed"], 1)


if __name__ == "__main__":
    unittest.main()
