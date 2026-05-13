import pytest


@pytest.mark.registration
@pytest.mark.regression
def test_successful_registration(registration_page, dashboard_page):
    registration_page.open_registration_page()
    registration_page.fill_registration_form(
        email="domikvderevne@gmail.com",
        username="domikvderevne",
        password="domikvderevne12@",
    )
    registration_page.click_registration_button()
    dashboard_page.check_visibility_dashboard_title()