#### Install Appium

`$ npm i --location=global appium`

#### Install Appium driver

`$ appium driver install uiautomator2`

#### Create Python Virtual environment

`$ python3 -m vevn vevn`
`$ source venv/bin/activate`

`$ pip install -r requirements.txt`

#### Start Appium Server

`$ appium`

#### Start Android Vitual Device

`$ adb start-server`
`$ emulator -list-avds`
  output result: Medium_Phone_API_36.0 (avd name)

`$ emulator -avd Medium_Phone_API_36.0`

#### Run test.py

`$ python test.py`

The Android app Calculator automation testing demo:  


https://github.com/user-attachments/assets/9c90afad-9bc9-4220-b9e6-910d52ebb67a




#### Run test_calculator.py

- terminal 1
  `$ appium`
- terminal 2
  `$ adb start-server`
  `$ emulator -avd Medium_Phone_API_36.0`
- terminal 3
  `$ python test_calculator.py`
