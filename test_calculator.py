from appium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options


# Desired capabilities for calculator app
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Medium_Phone_API_36.0'
)

appium_server_url = 'http://localhost:4723'


# Wait for the app to launch
time.sleep(2)

class TestCalculatorOperations(unittest.TestCase):

    def setUp(self) -> None:
        options = UiAutomator2Options().load_capabilities(capabilities)
        self.driver = webdriver.Remote(
            command_executor=appium_server_url,
            options=options
        )

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_addition(self):
        # Test case: 7 + 9 = 16
        # Click digit 7
        self.driver.find_element(By.ID, "com.android.calculator2:id/digit_7").click()

        # Click plus operator
        self.driver.find_element(By.ID, "com.android.calculator2:id/op_add").click()

        # Click digit 9
        self.driver.find_element(By.ID, "com.android.calculator2:id/digit_9").click()

        # Click equals
        self.driver.find_element(By.ID, "com.android.calculator2:id/eq").click()

        # Verify result
        result = self.driver.find_element(By.ID, "com.android.calculator2:id/result")
        assert "16" in result.text
    print("Test passed: 7 + 9 = 16")

    def test_subtraction(self):
        # Test case: 10 - 5 = 5
        # Click digit 1
        self.driver.find_element(By.ID, "com.android.calculator2:id/digit_1").click()
        # Click digit 0
        self.driver.find_element(By.ID, "com.android.calculator2:id/digit_0").click()
        # Click minus operator
        self.driver.find_element(By.ID, "com.android.calculator2:id/op_sub").click()
        # Click digit 5 
        self.driver.find_element(By.ID, "com.android.calculator2:id/digit_5").click()
        # Click equals
        self.driver.find_element(By.ID, "com.android.calculator2:id/eq").click()
        
        # Verify result
        result = self.driver.find_element(By.ID, "com.android.calculator2:id/result")
        assert "5" in result.text   
    print("Test passed: 10 - 5 = 5")    

    def test_multiplication(self):
        # Test case: 3 * 4 = 12
        # Click digit 3
        self.driver.find_element(By.ID, "com.android.calculator2:id/digit_3").click()
        # Click multiply operator
        self.driver.find_element(By.ID, "com.android.calculator2:id/op_mul").click()
        # Click digit 4
        self.driver.find_element(By.ID, "com.android.calculator2:id/digit_4").click()
        # Click equals
        self.driver.find_element(By.ID, "com.android.calculator2:id/eq").click()
        
        # Verify result
        result = self.driver.find_element(By.ID, "com.android.calculator2:id/result")
        assert "12" in result.text
    print("Test passed: 3 * 4 = 12")

    def test_division(self):
        # Test case: 20 / 4 = 5
        # Click digit 2
        self.driver.find_element(By.ID, "com.android.calculator2:id/digit_2").click()
        # Click digit 0
        self.driver.find_element(By.ID, "com.android.calculator2:id/digit_0").click()
        # Click divide operator
        self.driver.find_element(By.ID, "com.android.calculator2:id/op_div").click()
        # Click digit 4
        self.driver.find_element(By.ID, "com.android.calculator2:id/digit_4").click()
        # Click equals
        self.driver.find_element(By.ID, "com.android.calculator2:id/eq").click()
        
        # Verify result
        result = self.driver.find_element(By.ID, "com.android.calculator2:id/result")
        assert "5" in result.text
    print("Test passed: 20 / 4 = 5")

    def test_clear(self):
        # Test case: Clear the calculator
        # Click digit 5
        self.driver.find_element(By.ID, "com.android.calculator2:id/digit_5").click()
        # Click clear button
        self.driver.find_element(By.ID, "com.android.calculator2:id/clr").click()
        
        # Verify result is cleared
        result = self.driver.find_element(By.ID, "com.android.calculator2:id/result")
        assert result.text == ""
    print("Test passed: Calculator cleared successfully")

    
