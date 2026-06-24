from typing import Generator, Any

import pytest
from playwright.sync_api import Playwright, Page, Browser
from DataGenerator.datagenerator import DataGenerator


@pytest.fixture
def chromium_page(playwright: Playwright) -> Generator[Page, Any, None]:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()

@pytest.fixture(scope="session")
def initialize_browser_state(browser: Browser):
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_btn = page.get_by_test_id("registration-page-registration-button")

    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    email_input.fill(DataGenerator.generate_random_email())

    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    username_input.fill(DataGenerator.generate_random_username())

    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    password_input.fill(DataGenerator.generate_random_password())

    registration_btn.click()
    page.wait_for_url("**/dashboard**")
    context.storage_state(path="browser-state.json")
    context.close()

@pytest.fixture()
def chromium_page_with_state(initialize_browser_state, browser: Browser):
    context = browser.new_context(storage_state="browser-state.json")
    page =context.new_page()
    yield page
    context.close()