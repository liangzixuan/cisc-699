.PHONY: help smoke test api

PYTHON ?= python3
PYTHONPATH := src

help:
	@echo "SafeExec W5 baseline targets:"
	@echo "  make smoke  - run one local execution through the service layer"
	@echo "  make test   - run the committed unittest suite"
	@echo "  make api    - start the local JSON API on 127.0.0.1:8080"

smoke:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) scripts/smoke_safeexec.py

test:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m unittest discover -s tests/functional -p 'test_*.py'

api:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m safeexec.api.server --host 127.0.0.1 --port 8080
