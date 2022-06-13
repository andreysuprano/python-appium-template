from pytest import fixture
from dotenv import dotenv_values
from infra import DriverFactory

@fixture
def env():
    return dotenv_values(".env") 

@fixture
def driver(env):
    return DriverFactory().get_driver(env)