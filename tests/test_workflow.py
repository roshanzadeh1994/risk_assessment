import time
from unittest.mock import AsyncMock, patch

@patch("routers.risk_router.asyncio.sleep", new_callable=AsyncMock)
def test_risk_status_completed(mock_sleep, test_client):
    response = test_client.post("/risks/", json={
        "title": "Completion Check",
        "description": "Test workflow",
        "category": "Experimental"
    })
    assert response.status_code == 200
    risk_id = response.json()["id"]
    time.sleep(1)  # allow background task to run
    res = test_client.get(f"/risks/{risk_id}")
    assert res.status_code == 200
    assert res.json()["status"] == "completed"
