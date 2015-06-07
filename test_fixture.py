from selenium.webdriver import Firefox
import pytest


@pytest.fixture(scope="session")
def webdriver(request):
    driver = Firefox()
    request.addfinalizer(driver.quit)
    return driver


def test_pug_website_title(webdriver):
    webdriver.get("http://pycon.pug.pe/XXXVIII/")
    assert "Encontro do PUG-PE" in webdriver.title


def test_python_website_title(webdriver):
    webdriver.get("http://python.org/")
    assert "Python" in webdriver.title

