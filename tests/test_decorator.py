import allure
from selene import be, have, by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def test_decorator_allure_step_should_issue_title_text():
    open_github()
    search_allure_repo('eroshenkoam/allure-example')
    open_repo('eroshenkoam/allure-example')
    open_issues_tab()
    open_issue('Issue for HW qa.guru')
    check_issue_title('Issue for HW qa.guru')


@allure.step('Open github')
def open_github():
    browser.open('/')


@allure.step('Search allure {repo}')
def search_allure_repo(repo):
    s('.input-button').click()
    s('#query-builder-test').type(repo).press_enter()


@allure.step('Open {repo}')
def open_repo(repo):
    s(by.link_text(repo)).click()


@allure.step('Open issues tab')
def open_issues_tab():
    s('#issues-tab').click()


@allure.step('Open {issie_title}')
def open_issue(issie_title):
    ss('.js-navigation-open').element_by(have.text(issie_title)).click()


@allure.step('Check {issie_title}')
def check_issue_title(issie_title):
    s('.js-issue-title').should(have.text(issie_title)).should(be.visible)
