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

The Android Settings page shown up and then scroll down to click the Battery section.   
<video src="https://github.com/user-attachments/assets/fc0016d8-66a6-440c-9054-87764ee24f03" width="352" height="720"></video>


#### Run test_calculator.py

- terminal 1
  `$ appium`
- terminal 2
  `$ adb start-server`
  `$ emulator -avd Medium_Phone_API_36.0`
- terminal 3
  `$ python test_calculator.py`