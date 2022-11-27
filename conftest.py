import pytest
from selene.support.shared import browser
from selene.support.shared import config


@pytest.fixture(scope="session")
def open_browser():
    browser.open('https://google.com/ncr')

