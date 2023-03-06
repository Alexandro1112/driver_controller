<img style="display: block; align-items: center; justify-content: center; width: 365px; height: 355px;" src='https://github.com/Alexandro1112/driver_controller/blob/main/45dd60cb7ef14bd4bfeb4c9061919e67.png'>


![#c5f015](https://placehold.co/15x20/c5f015/c5f015.png)<br>
<img src='https://shields.io/badge/-Tested:%20Windows%2010-green'>
<img src='https://shields.io/badge/-Tested:%20Mac%20os%20Big Sur(+)11.7.4-green'>
<img src='https://shields.io/badge/-Tested:%20Mac%20os%20Catalina(+)10.15.7-green'><br>
<img src='https://shields.io/badge/-Tested:%20Mac%20os%20High Siera(+)10.13-green'>
<img src='https://shields.io/badge/-LinuxOS:%20no%20tested-darkred'>
[![Platforms WindowsOS](https://img.shields.io/badge/Platforms-macOS-lightgray.svg?style=flat)](https://www.microsoft.com/en-us/windows)
[![Platforms MacOS](https://img.shields.io/badge/Platforms-macOS-lightgray.svg?style=flat)](http://www.apple.com/macos)<br>
[![Platforms LinuxOS](https://img.shields.io/badge/Platforms-macOS-lightgray.svg?style=flat)](https://www.linux.org/pages/download/)
<img src='https://shields.io/badge/-MIT%20Lisence-gold'>
<p><strong>DRIVER_CONTROLLER<strong><p>

This lib will help you change system settings such as brightness, volume, color- mode, control your mouse,send notification,open windows, outputing available gadgets , connecting to wifi-network, enable/disable bluetooth device.You can use this utility for your python project.
In the github repository local submodules, install them - not need.However code not working - install them, run script
> install_depindensies.sh
# Installation
> git clone https://github.com/Alexandro1112/driver_controller

    
<h3>After, import them. Explore main opportunities this library. <h3>

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) 

# Lets try outputting all bluetooth/microphones in python.

```
import driver_controller

print(driver_controller.OutputListsDevises().get_list_audio_devises(), driver_controller.OutputListsDevises().get_list_bluetooth_devises())
```

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) 
# Thats nice, Trying get data about wifi, and connect/disconnect to them.

```
import driver_controller._mac_engine

channel = driver_controller._mac_engine.MacCmd().Wifi().wifiChannel()# 10
print(channel)


security = driver_controller._mac_engine.MacCmd().Wifi().SecurityType()#  wpa2-psk
print(security)

speed = driver_controller._mac_engine.MacCmd().Wifi().get_last_speed_by_current_network()
print(speed) # 59



rssi = driver_controller._mac_engine.MacCmd().Wifi().RssiChannelValue()
print(rssi) # -61

# driver_controller._mac_engine.MacCmd().Wifi().connectToMacAddress() # Connect to wi-fi, which used your devise(Mac).



boolean = driver_controller._mac_engine.MacCmd().Wifi().isUsedProxy()# False
print(boolean)


noise = driver_controller._mac_engine.MacCmd().Wifi().WifiNetworkNoise()
print(noise) # -78



# driver_controller._mac_engine.MacCmd().Wifi().connectTo(wifi_network='Redmi Note 10 Pro', password='a404f46f67a')



print(driver_controller._mac_engine.MacCmd().Wifi().InfoNetwork())
'''[interfaceName=en0, ipv4State={
    ARPResolvedHardwareAddress = "##:##:##:##:##:##";
    ARPResolvedIPAddress = "192.168.1.1";
    AdditionalRoutes =     (
                {
            DestinationAddress = "192.168.1.66";
            SubnetMask = "255.255.255.255";
        },
                {
            DestinationAddress = "##########";
            SubnetMask = "###########";
        }
    );
    Addresses =     (
        "192.168.1.66"
    );
    ConfirmedInterfaceName = en0;
    InterfaceName = en0;
    
}, ipv6GlobalSetup=(null)]'''
```

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) 
# Create message...

<h4> Make Lateral message with:<br>
 label: Main title on message<br>
  subtitle: Subtitle of message<br>
  text: Description of message<br>
 :param file_icon: Icon in message (Path to image)<br>
 (must local in project-folder), Point out [None]<br>
 if you don't want used icon.<h4>

```
import driver_controller

driver_controller.MacCmd().Notifier().send_lateral_message(label='<YOUR_LABEL>',
                                                     subtitle='<YOUR_SUBTITLE>',
                                                     text='<TEXT>', file_icon='<FILE_ICON>',
                                                     sound=driver_controller.CONSTANT_SOUNDS.SOUND_POP_SOUND)
``` 

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png)     
# is it possible to automotize keystrokes?Yes, you can even write the word.

``` 
import driver_controller

driver_controller.MacCmd().Clicker().press(key='a')
driver_controller.MacCmd().Clicker().write(text='hello')
``` 
![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png)      
# Set brightness of screen.
* You must install brew and brightness.  
* Use increase/dicrease brightness if homebrew and "birghtness" is not install.
     
``` 

import driver_controller._mac_engine

br = driver_controller._mac_engine.MacCmd().Brightness()
br.set_birghtness(20) # Set birghtness
br.increase_brightness(3) # increase brightness by 3 division 

br.decrease_brightness(3) # decrease brightness by 3 division 
print(br.get_brightness) # Print brightness percent

br.set_max_brightness()

br.set_min_brightness()

``` 

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) 
# Enable/unplug wifi/bluetooth.
``` 
     
import driver_controller

print(driver_controller.MacCmd().Switching().enable_wifi(),
      driver_controller.MacCmd().Switching().unplug_wifi(),
      driver_controller.MacCmd().Switching().enable_bluetooth(),
      driver_controller.MacCmd().Switching().unplug_bluetooth())
``` 

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) 
# Try make Screenshot.
  

``` 
import driver_controller

print(driver_controller.MacCmd().ScreenCapture().screenshot(filename='screenshot', extension='jpg', pause=2))
``` 
![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) 
#  Create photo in your webcamera.
<h4> Method make image trough web-camera
     cam_index: index where local camera
     extension: extension of created image
     filename: name of created file.
<h4>

     
     
``` 
import driver_controller
driver_controller.MacCmd().PhotoCapture().capture(cam_index=0,
                                            filename='<NAME_OF_FILE',
                                            extension='<FILE_EXTENSION>')
``` 

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) 
# Get some info about your noutbook
``` 
from driver_controller import MacCmd

print(MacCmd().SystemConfig().get_processor_name,# Intel(R) Core(TM) i7-4850HQ CPU @ 2.30GHz
      MacCmd().SystemConfig().current_connected_wifi_network,# Gavrilova_60_87_2.4ghz
      MacCmd().SystemConfig().screen_size,# ['2880', 'x', '1800']
      MacCmd().SystemConfig().macos_version,# Version your Mac os devise: 10.15.7
     MacCmd(). SystemConfig().devise_battery)# Battery percent: 90%
``` 

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) 
# Stream video from webcamera .
> record_time : time of recording(seconds)
> camera_index: camera index
> filename: name of created file
> extensions, maybe mkv, mp4, mpg

``` 
from driver_controller import MacCmd

MacCmd().WebCameraCapture.webcam_capture(record_time=20, camera_index=0, filename='Out-Video', extension='mkv')
```

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) 
Play sounds, available in mac-os
```
from driver_controller import MacCmd

Sound.pop_sound(iters=1),     MacCmd().Sound.ping_sound(iters=1),     MacCmd().Sound.blow_sound(iters=1),      MacCmd().Sound.funk_sound(iters=1),      MacCmd().Sound.glass_sound(iters=1),     MacCmd().Sound.sosumi_sound(iters=1),     MacCmd().Sound.submarine_sound(iters=1)
```
![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) 
# Practical application
<p>Write code for check clicked determined button in alert.

```
import driver_controller._mac_engine
choice  = driver_controller._mac_engine.MacCmd().Notifier().send_warning_alert(labeltext='Buy new mac?', button1='Yes', button2='No')
if choice == 'Yes':
     driver_controller.MacCmd().Notifier().send_text_alert('Thanks!', 'Wow!')
else:
     print('Ok!')

```
![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) 
# Set volume with input , get volume percent and etc.

```
import driver_controller._mac_engine
percent = int(input())

driver_controller.MacCmd().Volume().set_volume(percent)

vol = driver_controller._mac_engine.MacCmd().Volume()
print(vol.get_alert_volume,
      vol.get_input_volume_percent)
vol.decrease_volume()
vol.increase_volume()
vol.set_min_volume()
vol.set_max_volume()
```

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) 
# Change Mac theme.

```
import driver_controller._mac_engine

driver_controller._mac_engine.MacCmd().Theme().change_color_mode(pause=1)# Change color mode for Mac.

```
![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) 
# Open something url. Second argument - browser,and Link.Also we can open spotlight, and application.

```
import driver_controller._mac_engine

driver_controller._mac_engine.MacCmd().Open().url('https://github.com/Alexandro1112', 'Safari')


driver_controller._mac_engine.MacCmd().Open().open_spotlight()# Entry menu



channel = driver_controller._mac_engine.MacCmd().Open().application('FaceTime')
```
![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) 
# Play sound by name using:

```
import driver_controller._mac_engine

sound = driver_controller._mac_engine.MacCmd().Sound()

sound.playSoundByName(soundfile='yoursound.mp3')# sound name 
```

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) 
# Is support Mouse? Of course. Move, Click, get possition automatically.

```
import driver_controller._mac_engine


mouse = driver_controller._mac_engine.MacCmd().Mouse()

mouse.mouse_click(200, 200) # Click in position x=200, y=200
print(mouse.mouse_position) # Return mouse position (x,y)
mouse.mouse_move(1300, 300) # Move mouse in position x=1300, y=300

mouse.move_click(600, 70) # Move, and click in position x=600, y=70
```
![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) 
# Get some data about applications
```
import driver_controller._mac_engine

size = driver_controller._mac_engine.MacCmd().AppConfigure().get_app_size('Yandex')
d = driver_controller._mac_engine.MacCmd().FileConfig().get_date_create_file('/Applications/Yandex.app')
path = driver_controller._mac_engine.MacCmd().AppConfigure().get_full_path_by_app_name('Safari')
print(size, ',', path, ',', d)
# 295M , /Applications/Safari.app , Thu Dec  5 22:30:38 2019


```

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) 

<h1> That was main methods this python library. Exist even linux version. windows, while there less possibilities.<h1>


