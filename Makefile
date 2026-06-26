.PHONY: help smoke test api env validate validate-docker midpoint midpoint-target

PYTHON ?= python3
PYTHONPATH := src

help:
	@echo "SafeExec W5 baseline targets:"
	@echo "  make smoke  - run one local execution through the service layer"
	@echo "  make test   - run the committed unittest suite"
	@echo "  make api    - start the local JSON API on 127.0.0.1:8080"
	@echo "  make env    - capture environment/toolchain snapshot"
	@echo "  make validate - run repeatable local/API validation workflow"
	@echo "  make validate-docker - run Docker/gVisor validation workflow"
	@echo "  make midpoint - run local W8 midpoint evidence workflow"
	@echo "  make midpoint-target - run Docker/gVisor W8 midpoint evidence workflow"

smoke:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) scripts/smoke_safeexec.py

test:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m unittest discover -s tests/functional -p 'test_*.py'

api:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m safeexec.api.server --host 127.0.0.1 --port 8080

env:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) scripts/capture_environment.py --output-dir docs/06-hard-stop-3/evidence

validate:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) scripts/run_validation_workflow.py --output-dir docs/06-hard-stop-3/evidence --repeat 3

validate-docker:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) scripts/run_validation_workflow.py --output-dir docs/06-hard-stop-3/evidence --repeat 3 --include-docker

midpoint:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) scripts/run_midpoint_evidence.py --output-dir docs/08-hard-stop-4/evidence-local --repeat 5 --backends local

midpoint-target:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) scripts/run_midpoint_evidence.py --output-dir docs/08-hard-stop-4/evidence-target --repeat 5 --backends local docker gvisor
