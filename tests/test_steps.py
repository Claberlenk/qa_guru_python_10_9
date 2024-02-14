import allure
from selene import be, have, by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def test_with_allure_step_should_issue_title_text():
    with allure.step('Open github'):
        browser.open('/')
        allure.attach(browser.driver.get_screenshot_as_png(), name="Open GitHub",
                      attachment_type=allure.attachment_type.PNG)

    with allure.step('Search allure repository'):
        s('.input-button').click()
        s('#query-builder-test').type('eroshenkoam/allure-example').press_enter()

    with allure.step('Open repo'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Open issues tab'):
        s('#issues-tab').click()

    with allure.step('Open issue num 87'):
        ss('.js-navigation-open').element_by(have.text('Issue for HW qa.guru')).click()

    with allure.step('Check issue title'):
        s('.js-issue-title').should(have.text('Issue for HW qa.guru')).should(be.visible)