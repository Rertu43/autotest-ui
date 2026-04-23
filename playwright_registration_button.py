from playwright.sync_api import sync_playwright, expect


slow_mo = 1000
registration_link = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=slow_mo)
    page = browser.new_page()

    page.goto(registration_link)

    registration_btn = page.get_by_test_id("registration-page-registration-button")
    expect(registration_btn).to_be_disabled()

    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    email_input.fill("user.name@gmail.com")

    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    username_input.fill("username")

    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    password_input.fill("password")

    expect(registration_btn).to_be_enabled()
