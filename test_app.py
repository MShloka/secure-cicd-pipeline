from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["project"] == "Secure CI/CD Pipeline"


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_unknown_route():
    client = app.test_client()
    response = client.get("/unknown")

    assert response.status_code == 404