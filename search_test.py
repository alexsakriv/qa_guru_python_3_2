from selene import be, have
from selene.support.shared import browser
from fixture_test import open_browser_with_size_1920_1080


def test_search_1(open_browser_with_size_1920_1080):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative_search_2(open_browser_with_size_1920_1080):
    browser.element('[name="q"]').should(be.blank).type('selene123selene4').press_enter()
    browser.element('[id="topstuff"]').should(have.text('No results containing all your search terms were found.'))
