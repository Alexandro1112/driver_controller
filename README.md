

# pyTerminalproccesosx
Hello everyone!This module will help you change brightness, output , connecting to wifi-network, bluetooth device.You can use this utility for your python project.
In the github repository local submodules, install them - not need. For start work with this library need install by using 
# Installation
<p> git clone https://github.com/Alexandro1112/pyTerminalproccesosx/<p>
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

# Try get info about your mac-os

```
import pyTerminalproccesosx

print(pyTerminalproccesosx.SystemConfig().devise_battery,
      pyTerminalproccesosx.SystemConfig().macos_version,
      pyTerminalproccesosx.SystemConfig().screen_size,
      pyTerminalproccesosx.SystemConfig().current_connected_wifi_network)
```
# Create message...

<h4> Make Lateral message with:<br>
 :param label: Main title on message<br>
 :param subtitle: Subtitle of message<br>
 :param text: Description of message<br>
 :param file_icon: Icon in message (Path to image)<br>
 (must local in project-folder) Point out [None]<br>
 if you don't want used icon.<h4>

```
import pyTerminalproccesosx

pyTerminalproccesosx.Notifier().send_lateral_message(label='<YOUR_LABEL>',
                                                     subtitle='<YOUR_SUBTITLE>',
                                                     text='<TEXT>', file_icon='<FILE_ICON>',
                                                     sound=pyTerminalproccesosx.CONSTANT_SOUNDS.Popsound)
``` 
     
# Click on buttons? It is possiable.

``` 
import pyTerminalproccesosx

print(pyTerminalproccesosx.Clicker().press(button='a', register=pyTerminalproccesosx.UPPER.UPPER))
``` 
     
# Set brightness of screen.
     
     
``` 
import pyTerminalproccesosx

print(pyTerminalproccesosx.Brightness().set_brightness(number))
``` 

# Enable/unplug wifi/bluetooth.
``` 
     
import pyTerminalproccesosx

print(pyTerminalproccesosx.Switching().enable_wifi(),
      pyTerminalproccesosx.Switching().unplug_wifi(),
      pyTerminalproccesosx.Switching().enable_bluetooth(),
      pyTerminalproccesosx.Switching().unplug_bluetooth())
``` 
# Try make Screenshot.
     
``` 
import pyTerminalproccesosx

print(pyTerminalproccesosx.ScreenCapture().screenshot(filename='screenshot', extension='jpg', pause=2))
``` 

<h1> That was main methods this python library. Exist even linux version.<h1>

