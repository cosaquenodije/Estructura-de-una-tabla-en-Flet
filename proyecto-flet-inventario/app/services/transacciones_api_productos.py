import requests
from app.components.error import ApiError

BASE = "http://localhost:8000/productos"
TIME_OUT = 10

def list_products(limit: int = 20, offset: int = 0) -> dict:
    try:
        r = requests.get(f"{BASE}/", params={"limit": limit, "offset": offset}, timeout=TIME_OUT)
        if 200 <= r.status_code < 300:
            return r.json() if r.content else {}
        raise ValueError(f"Error {r.status_code}", r.status_code, r.text)
    except requests.exceptions.RequestException as e:
        raise ValueError("Error de conexión", None, str(e))

def get_product(product_id: str) -> dict:
    try:
        r = requests.get(f"{BASE}/{product_id}", timeout=TIME_OUT)
        if 200 <= r.status_code < 300:
            return r.json() if r.content else {}
        raise ValueError(f"Error {r.status_code}", r.status_code, r.text)
    except requests.exceptions.RequestException as e:
        raise ValueError("Error de conexión", None, str(e))

def create_product(data: dict) -> dict:
    try:
        r = requests.post(f"{BASE}/", json=data, timeout=TIME_OUT)
        if 200 <= r.status_code < 300:
            return r.json() if r.content else {}
        raise ValueError(f"Error {r.status_code}", r.status_code, r.text)
    except requests.exceptions.RequestException as e:
        raise ValueError("Error de conexión", None, str(e))

def update_product(product_id: str, data: dict) -> dict:
    try:
        r = requests.put(f"{BASE}/{product_id}", json=data, timeout=TIME_OUT)
        if r.status_code >= 400:
            try:
                payload = r.json()
                detail = payload.get("error") or payload.get("detail") or r.text
            except Exception:
                detail = r.text
            raise ApiError(detail, r.status_code)
        return r.json()
    except requests.Timeout:
        raise ApiError("El servidor tardó demasiado en responder", 0)
    except requests.ConnectionError:
        raise ApiError("No se pudo conectar al servidor", 0)
    except requests.RequestException as e:
        raise ApiError(f"Error de red {str(e)}", 0)

def delete_product(product_id: str):
    try:
        r = requests.delete(f"{BASE}/{product_id}", timeout=TIME_OUT)
        if 200 <= r.status_code < 300:
            return r.json() if r.content else {}
        raise ValueError(f"Error {r.status_code}", r.status_code, r.text)
    except requests.exceptions.RequestException as e:
        raise ValueError("Error de conexión", None, str(e))

print(list_products())