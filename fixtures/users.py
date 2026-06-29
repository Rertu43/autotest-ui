import pytest

from DataGenerator.datagenerator import DataGenerator
from models.base_user import BaseUser


@pytest.fixture(scope="session")
def base_user() -> BaseUser:
    return BaseUser(
        email=DataGenerator.generate_random_email(),
        password=DataGenerator.generate_random_password(),
        username=DataGenerator.generate_random_username()
    )