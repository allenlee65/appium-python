import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        options = UiAutomator2Options().load_capabilities(capabilities)
        self.driver = webdriver.Remote(
            command_executor=appium_server_url,
            options=options
        )

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_battery(self) -> None:
        self.driver.implicitly_wait(10)
        self.driver.swipe(
            start_x=500, start_y=1500,
            end_x=500, end_y=300,
            duration=1000
        )
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
        el.click()

if __name__ == '__main__':
    unittest.main()