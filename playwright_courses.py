from playwright.sync_api import sync_playwright, expect


registration_link = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
courses_link = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
path = "browser-state.json"

slow_mo = 1000

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=slow_mo)
    context = browser.new_context()
    page = context.new_page()

    page.goto(registration_link)

    registration_btn = page.get_by_test_id("registration-page-registration-button")

    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    email_input.fill("user.name@gmail.com")

    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    username_input.fill("username")

    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    password_input.fill("password")

    registration_btn.click()
    page.wait_for_url("**/dashboard**")
    context.storage_state(path=path)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=slow_mo)
    context = browser.new_context(storage_state=path)
    page = context.new_page()

    page.goto(courses_link)

    courses_text = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_text).to_have_text("Courses")

    no_results_text = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(no_results_text).to_have_text("There is no results")

    empty_view_icon = page.get_by_test_id("courses-list-empty-view-icon")
    expect(empty_view_icon).to_be_visible()

    empty_view_description = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(empty_view_description).to_have_text("Results from the load test pipeline will be displayed here")


