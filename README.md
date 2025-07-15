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
  output result: edium_Phone_API_36.0 (avd name) 

`$ emulator -avd edium_Phone_API_36.0`

#### Run test.py

`$ python test.py`

The Android Settings page shown up and then scroll down to click the Battery section.

<video controls src="Screencast From 2025-07-15 20-44-45.webm" title="Title"></video>