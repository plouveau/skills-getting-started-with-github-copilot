import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


BASELINE_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture
def client() -> TestClient:
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities_state(monkeypatch):
    """Ensure tests do not leak in-memory activity state across runs."""
    monkeypatch.setattr(app_module, "activities", copy.deepcopy(BASELINE_ACTIVITIES))
