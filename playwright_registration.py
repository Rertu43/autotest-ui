from playwright.sync_api import sync_playwright, expect

email_input_locator = '//div[@data-testid="registration-form-email-input"]//input'
password_input_locator = '//div[@data-testid="registration-form-password-input"]//input'
username_input_locator = '//div[@data-testid="registration-form-username-input"]//input'
registration_btn_locator = '//button[@data-testid="registration-page-registration-button"]'
dashboard_text_locator = "//div/h6[@data-testid='dashboard-toolbar-title-text']"

email = "hardocded@email.com"
password = "dlsjkfls4322@#"
username = "mynameishardcode"

registration_link = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"

slow_mo = 1000

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=slow_mo)
    page = browser.new_page()

    email_input = page.locator(email_input_locator)
    password_input = page.locator(password_input_locator)
    username_input = page.locator(username_input_locator)
    registration_btn = page.locator(registration_btn_locator)
    dashboard_text = page.locator(dashboard_text_locator)

    page.goto(registration_link)

    email_input.fill(email)
    expect(email_input).to_have_value(email)

    password_input.fill(password)
    expect(password_input).to_have_value(password)

    username_input.fill(username)
    expect(username_input).to_have_value(username)

    registration_btn.click()

    page.wait_for_load_state(state="load")

    expect(dashboard_text).to_be_visible()

