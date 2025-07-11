import pytest

def test_create_risk_validation_error(test_client):
    response = test_client.post("/risks/", json={
        "description": "no title",
        "category": "general"
    })
    assert response.status_code == 422
    assert "title" in response.text

@pytest.mark.parametrize("payload,missing_field", [
    ({"description": "desc", "category": "cat"}, "title"),
    ({"title": "t", "category": "cat"}, "description"),
    ({"title": "t", "description": "desc"}, "category"),
])
def test_missing_required_fields(test_client, payload, missing_field):
    response = test_client.post("/risks/", json=payload)
    assert response.status_code == 422
    assert missing_field in response.text
