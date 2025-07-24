# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from selenium.webdriver.common.by import By
# from appium.options.uiautomator2 import UiAutomator2Options
import unittest
import time



# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

options = AppiumOptions()
options.load_capabilities({
	"appium:automationName": "uiautomator2",
	"platformName": "Android",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def click_digit(self, digit):
        self.driver.find_element(By.ID, f"com.simplemobiletools.calculator.debug:id/btn_{digit}").click()
        self.driver.implicitly_wait(3)  # Wait for the button to be processed

    def click_plus(self):
        self.driver.find_element(By.ID, "com.simplemobiletools.calculator.debug:id/btn_plus").click()
        self.driver.implicitly_wait(3)  # Wait for the button to be processed

    def click_minus(self):
        self.driver.find_element(By.ID, "com.simplemobiletools.calculator.debug:id/btn_minus").click()
        self.driver.implicitly_wait(3)  # Wait for the button to be processed

    def click_multiply(self):
        self.driver.find_element(By.ID, "com.simplemobiletools.calculator.debug:id/btn_multiply").click()
        self.driver.implicitly_wait(3)  # Wait for the button to be processed

    def click_divide(self):
        self.driver.find_element(By.ID, "com.simplemobiletools.calculator.debug:id/btn_divide").click()
        self.driver.implicitly_wait(3)  # Wait for the button to be processed

    def click_equals(self):
        self.driver.find_element(By.ID, "com.simplemobiletools.calculator.debug:id/btn_equals").click()
        self.driver.implicitly_wait(3)  # Wait for the button to be processed

    def get_result(self):
        return self.driver.find_element(By.ID, "com.simplemobiletools.calculator.debug:id/result").text

    def click_clear(self, times):
        for _ in range(times):
            self.driver.find_element(By.ID, "com.simplemobiletools.calculator.debug:id/btn_clear").click()
        self.driver.implicitly_wait(3)  # Wait for the button to be processed

    

class TestCalculatorOperations(unittest.TestCase):

    def setUp(self) -> None:
        # Use the global 'options' defined above
        self.driver = webdriver.Remote(
            command_executor="http://127.0.0.1:4723",
            options=options
        )
        # Wait for the app to launch
        time.sleep(2)
        self.calculator = CalculatorPage(self.driver)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_addition(self):
        self.calculator.click_clear(3) # Clear the calculator before starting a new test
        """Test case: 7 + 9 = 16"""
        self.calculator.click_digit(7)
        self.calculator.click_plus()
        self.calculator.click_digit(9)
        self.calculator.click_equals()
        
        result = self.calculator.get_result()
        self.assertIn("16", result, f"Expected 16 in result, but got {result}")
        self.calculator.click_clear(2)

    def test_subtraction(self):
        """Test case: 10 - 5 = 5"""
        self.calculator.click_digit(1)
        self.calculator.click_digit(0)
        self.calculator.click_minus()
        self.calculator.click_digit(5)
        self.calculator.click_equals()

        result = self.calculator.get_result()
        self.assertIn("5", result, f"Expected 5 in result, but got {result}")
        self.calculator.click_clear(2)

    def test_multiplication(self):
        """Test case: 3 * 4 = 12"""
        self.calculator.click_digit(3)
        self.calculator.click_multiply()
        self.calculator.click_digit(4)
        self.calculator.click_equals()

        result = self.calculator.get_result()
        self.assertIn("12", result, f"Expected 12 in result, but got {result}")
        self.calculator.click_clear(2)


    def test_division(self):
        """Test case: 20 / 4 = 5"""
        self.calculator.click_digit(2)
        self.calculator.click_digit(0)
        self.calculator.click_divide()
        self.calculator.click_digit(4)
        self.calculator.click_equals()

        result = self.calculator.get_result()
        self.assertIn("5", result, f"Expected 5 in result, but got {result}")
        self.calculator.click_clear(2)

    def test_clear(self):
        """Test case: Clear the calculator"""
        self.calculator.click_digit(5)
        self.calculator.click_clear(2)

        result = self.calculator.get_result()
        self.assertEqual("0", result, f"Expected 0 after clear, but got '{result}'")
        self.calculator.click_clear(2)

   
if __name__ == "__main__":
    unittest.main()
