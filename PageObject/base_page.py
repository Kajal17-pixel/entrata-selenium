from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger  #Only if using logging
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        # Initialize the page with WebDriver and WebDriverWait (5 seconds)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        logger.info(f"Clicking on: {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))

        try:
            element.click()
        except ElementClickInterceptedException:
            logger.warning(f"Click intercepted for {locator}, scrolling and retrying.")
            self.scroll_to_element(locator)
            self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        logger.info(f"Typing '{text}' into: {locator}")
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def is_visible(self, locator):
        logger.info(f"Checking visibility of: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def scroll_to_element(self, locator):
        logger.info(f"Scrolling to element: {locator}")
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        ActionChains(self.driver).move_to_element(element).perform()


