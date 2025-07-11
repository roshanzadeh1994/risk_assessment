from unittest.mock import patch

@patch("routers.risk_router.run_risk_workflow")
def test_create_risk(mock_workflow, test_client):
    mock_workflow.return_value = None
    response = test_client.post("/risks/", json={
        "title": "Test Risk",
        "description": "Test description",
        "category": "Safety"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Risk"
    assert data["status"] == "in process"
