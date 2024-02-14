from selene import be, have, by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def test_should_issue_title_text():
    browser.open('/')
    s('.input-button').click()
    s('#query-builder-test').type('eroshenkoam/allure-example').press_enter()
    s(by.link_text('eroshenkoam/allure-example')).click()
    s('#issues-tab').click()
    ss('.js-navigation-open').element_by(have.text('Issue for HW qa.guru')).click()
    s('.js-issue-title').should(have.text('Issue for HW qa.guru')).should(be.visible)