

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) 
# driver_controller
This lib will help you change brightness, output available gadgets for mac, connecting to wifi-network, bluetooth device.You can use this utility for your python project.
In the github repository local submodules, install them - not need.However code not working - install them, run script
> install_deepindensies.sh
# Installation
> git clone https://github.com/Alexandro1112/driver-controler


    
<h3>After, import them. Explore main abillity this library. <h3>
     
# Lets try outputting all bluetooth/microphones in python.

```
import driver_controller

print(driver_controller.OutputListsDevises().get_list_audio_devises(), driver_controller.OutputListsDevises().get_list_bluetooth_devises())
```

# Thats nice, what about conncet to wifi network?

```
import driver_controller

print(driver_controller.Connector().connect_wifi_network(wifi_network='<WIFI_NAME>', password='<PASSWORD>'))
```

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
                                                     sound=driver_controller.CONSTANT_SOUNDS.Popsound)
``` 
     
# Click on buttons? It is possiable.

``` 
import driver_controller

print(driver_controller.MacCmd().Clicker().press(button='a')
``` 
     
# Set brightness of screen.
* You must install brew and brightness.  
* Use increase/dicrease brightness if brew is not install.
     
``` 
import driver_controller

print(driver_controller.MacCmd().Brightness().set_brightness(20))
``` 

# Enable/unplug wifi/bluetooth.
``` 
     
import driver_controller

print(driver_controller.MacCmd().Switching().enable_wifi(),
      driver_controller.MacCmd().Switching().unplug_wifi(),
      driver_controller.MacCmd().Switching().enable_bluetooth(),
      driver_controller.MacCmd().Switching().unplug_bluetooth())
``` 
# Try make Screenshot.
     
``` 
import driver_controller

print(driver_controller.MacCmd().ScreenCapture().screenshot(filename='screenshot', extension='jpg', pause=2))
``` 

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

# Get some info about your noutbook
``` 
from driver_controller import MacCmd

print(MacCmd().SystemConfig().get_processor_name,# Intel(R) Core(TM) i7-4850HQ CPU @ 2.30GHz
      MacCmd().SystemConfig().current_connected_wifi_network,# Gavrilova_60_87_2.4ghz
      MacCmd().SystemConfig().screen_size,# ['2880', 'x', '1800']
      MacCmd().SystemConfig().macos_version,# Version your Mac os devise: 10.15.7
     MacCmd(). SystemConfig().devise_battery)# Battery percent: 90%
``` 

# Stream video in your webcamera 
> record_time : time of recording(seconds)
> camera_index: camera index
> filename: name of created file
> extensions, maybe mkv, mp4, mpg

``` 
from driver_controller import MacCmd

MacCmd().WebCameraCapture.webcam_capture(record_time=20, camera_index=0, filename='Out-Video', extension='mkv')
```

Play sounds, available in mac-os
```
from driver_controller import MacCmd

Sound.pop_sound(iters=1),     MacCmd().Sound.ping_sound(iters=1),     MacCmd().Sound.blow_sound(iters=1),      MacCmd().Sound.funk_sound(iters=1),      MacCmd().Sound.glass_sound(iters=1),     MacCmd().Sound.sosumi_sound(iters=1),     MacCmd().Sound.submarine_sound(iters=1)
```

# Practical application
<p>Write code for check clicked determined button in alert.

```
import driver_controller._mac_engine
choice  = driver_controller._mac_engine.MacCmd().Notifier().send_warning_alert(labeltext='Buy new mac?', button1='Yes', button2='No')
if choice == 'Yes':
     driver_controller.MacCmd().Notifier().send_text_alert('Thanks!')
else:
     print('Ok!')

```
# Set volume with input 

```
import driver_controller._mac_engine
percent = int(input())

driver_controller.MacCmd().Volume().set_volume(percent)
```
![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) 

<h1> That was main methods this python library. Exist even linux version. windows, while there less possibilities.<h1>

![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) 
