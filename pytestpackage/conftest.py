import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setUp(request):
    print("Starting driver")
    driver = webdriver.Firefox()
    driver.get("https://www.avanade.com")
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    print("Stop driver")
    driver.close()

@pytest.fixture(scope="module")
def oneTimeSetUp():
    print("Running conftest demo one time setUp")
    yield
    print("Running conftest demo one time tearDown")


