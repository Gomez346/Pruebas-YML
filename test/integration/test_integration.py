import pytest, json, os

pytestmark = pytest.mark.integration

def test_leer_db_json():
    ruta = os.path.join(os.path.dirname(__file__), "..", "..", "db.json")
    with open(ruta, encoding="utf-8") as f:
        data = json.load(f)
    assert isinstance(data, (dict, list))