from fastapi.testclient import TestClient
from support.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'login is broken', **{'payload': {'message': 'cannot login'}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["reply"] == "reset_link"
    refused = client.post("/agent/run", json={"goal": 'refund this invoice'}).json()
    assert refused["refused"] is True
