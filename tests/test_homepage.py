from PageObject.home_page import HomePage
from selenium.webdriver.common.by import By

"""Verify that the title contains 'Entrata'"""
def test_title_contains_entrata(setup):
    assert "Entrata" in setup.title

"""Scroll and navigate to Careers page and assert URL"""
def test_navigate_to_careers(setup):
    page = HomePage(setup)
    page.go_to_careers()
    assert "careers" in setup.current_url.lower()

"""Hover and navigate to ProspectPortal page and assert URL"""
def test_navigate_to_prospect_portal(setup):
    page = HomePage(setup)
    page.go_to_prospect_portal()
    assert "prospectportal" in setup.current_url.lower()

def test_enter_username_in_login(setup):
    """Click Sign In > Property Manager Login > Enter username only"""
    page = HomePage(setup)
    page.go_to_property_manager_login_and_enter_username("testuser")
    entered = setup.find_element(*page.USERNAME_FIELD).get_attribute("value")
    assert entered == "testuser"

# def test_debug_check_elements(setup):
#     setup.get("https://www.entrata.com")
#     print("Page title:", setup.title)
#     print("Sign In exists:",
#           setup.find_elements(By.XPATH, "//a[contains(text(), 'Sign in')]") != [])



