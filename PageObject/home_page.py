from utils.logger import logger
from selenium.webdriver.common.by import By
from PageObject.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)

class HomePage(BasePage):
    # Locators for Home Page
    PRODUCTS_DROPDOWN_TOGGLE = (By.ID, "w-dropdown-toggle-0")
    PROSPECT_PORTAL_LINK = (By.LINK_TEXT, "ProspectPortal")
    CAREERS_LINK = (By.LINK_TEXT, "Careers")
    #Locators for signin
    SIGN_IN_BUTTON = (By.XPATH, "//a[normalize-space(text())='Sign in']")
    PROPERTY_MANAGER_LOGIN_BUTTON = ( By.XPATH,"//a[contains(@class, 'button') and contains(text(), 'Property Manager Login')]")
    USERNAME_INPUT = (By.ID, "entrata-username")
    #CONTACT_LINK = (By.LINK_TEXT, "Contact")
    #SLIDER = (By.CSS_SELECTOR, "div.hero-slider, div.hero-wrapper")
    print("HomePage loaded with PROPERTY_MANAGER_LOGIN_BUTTON")

    """Hover over 'Products' and click on 'ProspectPortal'"""
    def go_to_prospect_portal(self):
        logger.info("Hovering over Products dropdown to reveal links")
        dropdown = self.wait.until(EC.visibility_of_element_located(self.PRODUCTS_DROPDOWN_TOGGLE))
        ActionChains(self.driver).move_to_element(dropdown).perform()

        logger.info("Clicking on ProspectPortal link")
        self.click(self.PROSPECT_PORTAL_LINK)

    """Scroll and click on the 'Careers' link in the footer."""
    def go_to_careers(self):
        self.scroll_to_element(self.CAREERS_LINK)  # Optional: scroll if it's in the footer
        self.click(self.CAREERS_LINK)

    def click_sign_in_button(self):
        logger.info("Clicking on 'Sign in' button")
        try:
            element = self.wait.until(EC.element_to_be_clickable(self.SIGN_IN_BUTTON))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            element.click()
        except Exception as e:
            logger.warning(f"Standard click on 'Sign in' failed, trying JS click: {e}")
            try:
                element = self.wait.until(EC.presence_of_element_located(self.SIGN_IN_BUTTON))
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                self.driver.execute_script("arguments[0].click();", element)
            except Exception as inner_e:
                logger.error(f"JS click on 'Sign in' also failed: {inner_e}")
                raise

    def click_property_manager_login(self):
        logger.info("Waiting for 'Property Manager Login' button")
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(self.PROPERTY_MANAGER_LOGIN_BUTTON)
            )
            logger.info("Scrolling and clicking 'Property Manager Login'")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            logger.error(f"Failed to click 'Property Manager Login': {e}")
            raise

    # def go_to_property_manager_login_and_enter_username(self, username):
    #     self.click_sign_in_button()  # uses above method
    #
    #     self.click_property_manager_login()  # your separate method
    #
    #     logger.info("Entering username")
    #     self.send_keys(self.USERNAME_INPUT, username)
    def go_to_property_manager_login_and_enter_username(self, username):
        logger.info("Clicking on 'Sign In' button")

        # 🔍 Step 1: Detect and switch to the correct iframe
        iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
        logger.info(f"Number of iframes on page: {len(iframes)}")

        for index, iframe in enumerate(iframes):
            try:
                self.driver.switch_to.default_content()
                self.driver.switch_to.frame(iframe)
                logger.info(f"Switched to iframe[{index}]")

                sign_in_button = self.driver.find_element(By.XPATH, "//a[normalize-space(text())='Sign in']")
                if sign_in_button.is_displayed():
                    logger.info(f"'Sign In' button found in iframe[{index}]")
                    break
            except Exception as e:
                logger.info(f"'Sign In' not in iframe[{index}]: {e}")
        else:
            logger.error("Sign In button not found in any iframe")
            raise Exception("Sign In button not found")

        # ✅ Step 2: Try scrolling and clicking the button
        try:
            self.scroll_to_element(self.SIGN_IN_BUTTON)
            self.click(self.SIGN_IN_BUTTON)
        except Exception as e:
            logger.warning(f"Standard click on 'Sign In' failed, trying JS click: {e}")
            element = self.wait.until(EC.presence_of_element_located(self.SIGN_IN_BUTTON))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

        # 🔁 Step 3: Switch back to main page if needed
        self.driver.switch_to.default_content()

        logger.info("Clicking on 'Property Manager Login' button")
        try:
            self.scroll_to_element(self.PROPERTY_MANAGER_LOGIN_BUTTON)
            self.click(self.PROPERTY_MANAGER_LOGIN_BUTTON)
        except Exception as e:
            logger.warning(f"Standard click on 'Property Manager Login' failed, trying JS click: {e}")
            element = self.wait.until(EC.presence_of_element_located(self.PROPERTY_MANAGER_LOGIN_BUTTON))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

        logger.info("Entering username")
        self.send_keys(self.USERNAME_INPUT, username)

        # then proceed to Property Manager Login, etc.

    # def go_to_contact(self):
    #     self.click(self.CONTACT_LINK)

    # def is_slider_visible(self):
    #     return self.is_visible(self.SLIDER)
