
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

