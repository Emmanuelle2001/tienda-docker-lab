import pytest
from api import app, read_root, listar_productos, health

def test_read_root():
    data = read_root()
    assert isinstance(data, dict)
    assert data["version"] == "1.0.0"
    assert "pod_hostname" in data

def test_listar_productos():
    productos = listar_productos()
    assert isinstance(productos, list)
    assert len(productos) >= 3
    assert productos[0]["nombre"] == "Laptop Pro"

def test_health():
    data = health()
    assert data["status"] == "ok"

try:
    from fastapi.testclient import TestClient
    client = TestClient(app)

    def test_http_root():
        response = client.get("/")
        assert response.status_code == 200
        assert response.json()["version"] == "1.0.0"

    def test_http_productos():
        response = client.get("/productos")
        assert response.status_code == 200
        assert len(response.json()) >= 3

    def test_http_health():
        response = client.get("/health")
        assert response.status_code == 200
except (ImportError, RuntimeError):
    pass
