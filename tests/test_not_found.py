def test_get_nonexistent_risk(test_client):
    res = test_client.get("/risks/999")
    assert res.status_code == 404
    assert res.json()["detail"] == "Risk not found"
