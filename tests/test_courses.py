import pytest
from playwright.sync_api import expect

courses_link = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    page = chromium_page_with_state

    page.goto(courses_link)

    courses_text = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_text).to_have_text("Courses")

    no_results_text = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(no_results_text).to_have_text("There is no results")

    empty_view_icon = page.get_by_test_id("courses-list-empty-view-icon")
    expect(empty_view_icon).to_be_visible()

    empty_view_description = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(empty_view_description).to_have_text("Results from the load test pipeline will be displayed here")