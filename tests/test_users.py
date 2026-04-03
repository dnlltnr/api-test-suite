
import pytest
from api.user_api import create_user, get_users


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com/users"

