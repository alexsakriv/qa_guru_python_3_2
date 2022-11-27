from selene.support.shared import browser
from selene import be, have


def test_search_1(open_browser, size_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative_search_2(open_browser, size_browser):
    browser.element('[name="q"]').should(be.blank).type('selene123selene4').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))



# browser.open('https://google.com')
# browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
# browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))