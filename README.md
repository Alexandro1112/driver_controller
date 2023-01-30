

# pyTerminalproccesosx
This lib will help you change brightness, output , connecting to wifi-network, bluetooth device.You can use this utility for your python project.
In the github repository local submodules, install them - not need. For start work with this library need install by using 
# Installation
<p> git clone https://github.com/Alexandro1112/pyTerminalproccesosx<p>
     <h3>After, import them. Explore main abillity this library. <h3>
     
# Lets try outputting all bluetooth/microphones in python.

```
import pyTerminalproccesosx

print(pyTerminalproccesosx.OutputListsDevises().get_list_audio_devises(), pyTerminalproccesosx.OutputListsDevises().get_list_bluetooth_devises())
```

# Thats nice, what about conncet to wifi network?

```
import pyTerminalproccesosx

print(pyTerminalproccesosx.Connector().connect_wifi_network(wifi_network='<WIFI_NAME>', password='<PASSWORD>'))
```

# Create message...

<h4> Make Lateral message with:<br>
 label: Main title on message<br>
  subtitle: Subtitle of message<br>
  text: Description of message<br>
 :param file_icon: Icon in message (Path to image)<br>
 (must local in project-folder) Point out [None]<br>
 if you don't want used icon.<h4>

```
import pyTerminalproccesosx

pyTerminalproccesosx.MacCmd().Notifier().send_lateral_message(label='<YOUR_LABEL>',
                                                     subtitle='<YOUR_SUBTITLE>',
                                                     text='<TEXT>', file_icon='<FILE_ICON>',
                                                     sound=pyTerminalproccesosx.CONSTANT_SOUNDS.Popsound)
``` 
     
# Click on buttons? It is possiable.

``` 
import pyTerminalproccesosx

print(pyTerminalproccesosx.MacCmd().Clicker().press(button='a')
``` 
     
# Set brightness of screen.
     
     
``` 
import pyTerminalproccesosx

print(pyTerminalproccesosx.MacCmd().Brightness().set_brightness(number))
``` 

# Enable/unplug wifi/bluetooth.
``` 
     
import pyTerminalproccesosx

print(pyTerminalproccesosx.MacCmd().Switching().enable_wifi(),
      pyTerminalproccesosx.MacCmd().Switching().unplug_wifi(),
      pyTerminalproccesosx.MacCmd().Switching().enable_bluetooth(),
      pyTerminalproccesosx.MacCmd().Switching().unplug_bluetooth())
``` 
# Try make Screenshot.
     
``` 
import pyTerminalproccesosx

print(pyTerminalproccesosx.MacCmd().ScreenCapture().screenshot(filename='screenshot', extension='jpg', pause=2))
``` 

#  Create photo in your webcam
<h2> Method make image trough web-camera
     cam_index: index where local camera
     extension: extension of created image
     filename: name of created file.
<h2>

     
     
``` 
import pyTerminalproccesosx
pyTerminalproccesosx.MacCmd().PhotoCapture().capture(cam_index=0,
                                            filename='<NAME_OF_FILE',
                                            extension='<FILE_EXTENSION>')
``` 

# Get some info about your noutbook
``` 
from pyTerminalproccesosx import MacCmd

print(MacCmd().SystemConfig().get_processor_name,# Intel(R) Core(TM) i7-4850HQ CPU @ 2.30GHz
      MacCmd().SystemConfig().current_connected_wifi_network,# Gavrilova_60_87_2.4ghz
      MacCmd().SystemConfig().screen_size,# ['2880', 'x', '1800']
      MacCmd().SystemConfig().macos_version,# Version your Mac os devise: 10.15.7
     MacCmd(). SystemConfig().devise_battery)# Battery percent: 90%
``` 

# Stream video in your webcamera 
# record_time : time of recording(seconds)
# camera_index: camera index
# filename: name of created file
# extensions, maybe mkv, mp4, mpg

``` 
from pyTerminalproccesosx import MacCmd

MacCmd().WebCameraCapture.webcam_capture(record_time=20, camera_index=0, filename='Out-Video', extension='mkv')
```

Play sounds, available in mac-os
```
from pyTerminalproccesosx import MacCmd

Sound.pop_sound(iters=1),\
     MacCmd().Sound.ping_sound(iters=1),\
     MacCmd().Sound.blow_sound(iters=1), \
     MacCmd().Sound.funk_sound(iters=1), \
     MacCmd().Sound.glass_sound(iters=1),\
     MacCmd().Sound.sosumi_sound(iters=1),\
     MacCmd().Sound.submarine_sound(iters=1)
```

# Practical application
<p>Write code for check clicked determined button in alert.

```
import pyTerminalproccesosx._mac_engine
choice  = pyTerminalproccesosx._mac_engine.MacCmd().Notifier().send_warning_alert(labeltext='Buy new mac?', button1='Yes', button2='No')
if choice == 'Yes':
     pyTerminalproccesosx.MacCmd().Notifier().send_text_alert('Thanks!')
else:
     print('Ok!')

```
# Set volume with input 

```
import pyTerminalproccesosx._mac_engine
percent = int(input())

pyTerminalproccesosx.MacCmd().Volume().set_volume(percent)
```
<h1> That was main methods this python library. Exist even linux version.<h1>


