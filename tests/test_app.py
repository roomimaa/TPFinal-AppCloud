import os
from pathlib import Path

# --- Configuración de la base de datos de pruebas --- #

TEST_DB_FILE = "test.db"

# Si existe una base de datos vieja de tests, la borramos para empezar limpio
if Path(TEST_DB_FILE).exists():
    Path(TEST_DB_FILE).unlink()

# Usamos esta DB solo para pruebas
os.environ["DATABASE_URL"] = f"sqlite:///./{TEST_DB_FILE}"

from fastapi.testclient import TestClient  # noqa: E402
from app.main import app  # noqa: E402

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_create_product_ok():
    data = {
        "nombre": "Mouse Gamer",
        "categoria": "Perifericos",
        "precio": 9999.99,
        "descripcion": "Mouse con luces RGB",
    }
    r = client.post("/products", json=data)
    assert r.status_code == 201
    body = r.json()
    assert body["id"] > 0
    assert body["nombre"] == data["nombre"]


def test_create_product_validation_error():
    # Precio negativo → debe fallar la validación (422)
    data = {
        "nombre": "Teclado",
        "categoria": "Perifericos",
        "precio": -100,
        "descripcion": "No debería crearse",
    }
    r = client.post("/products", json=data)
    assert r.status_code == 422
    body = r.json()
    assert body["error"]["code"] == 422


def test_list_products():
    r = client.get("/products")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
