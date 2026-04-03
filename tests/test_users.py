
import pytest
from api.user_api import create_user, get_users


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com/users"


def test_create_user_valid(base_url):

    response, data = create_user(base_url, {
        "name": "Daniel",
        "email": "dan@test.com"
    })

    assert response.status_code == 201
    assert "id" in data
    assert "name" in data
    assert "email" in data
    assert data["name"] == "Daniel"
    assert data["email"] == "dan@test.com"


@pytest.mark.parametrize("payload", [
    {"name": "A" * 1000, "email": "long@test.com"},
    {"name": "()@&()!$&%^.", "email": "special@test.com"},
    {"name": "Daniel, Eli, Jack, James", "email": "multi@test.com"},
    {"name": "😈", "email": "emoji@test.com"},
    {}
], ids=[
    "long_name",
    "special_chars",
    "multi_name",
    "emoji",
    "empty_payload"
])

def test_create_user_parametrized(base_url, payload):

    response, data = create_user(base_url, payload)

    assert response.status_code == 201
    assert "id" in data

    if payload:
        assert data["name"] == payload["name"]
        assert data["email"] == payload["email"]


def test_fail(base_url):
    # Expected: 400 (invalid email type)
    # Actual: 201 (API does not validate email type)

    response, data = create_user(base_url, {
        "name": "Daniel",
        "email": "not-an-email"
    })

    assert response.status_code == 400

