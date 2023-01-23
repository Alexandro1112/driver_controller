
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=Alexandro1112&layout=compact)](https://github.com/anuraghazra/github-readme-stats)

# pyTerminalproccesosx
Hello everyone!This module will help you change brightness, output , connecting to wifi-network, bluetooth device.You can use this utility for your python project.
In the github repository local submodules, install them - not need. For start work with this library need install by using 
# Installation
git clone https://github.com/Alexandro1112/pyTerminalproccesosx/
     After, import them. Explore main abillity this library. Lets try outputting all bluetooth/microphones in python.
```
import pyTerminalproccesosx

print(pyTerminalproccesosx.OutputListsDevises().get_list_audio_devises(), pyTerminalproccesosx.OutputListsDevises().get_list_bluetooth_devises())
```

Thats nice, what about conncet to wifi network?

```
import pyTerminalproccesosx

print(pyTerminalproccesosx.Connector().connect_wifi_network(wifi_network='<WIFI_NAME>', password='<PASSWORD>'))
```

Try get info about your mac-os

```
import pyTerminalproccesosx

print(pyTerminalproccesosx.SystemConfig().devise_battery,
      pyTerminalproccesosx.SystemConfig().macos_version,
      pyTerminalproccesosx.SystemConfig().screen_size,
      pyTerminalproccesosx.SystemConfig().current_connected_wifi_network)
```
Easy!

Send text alert you can with

```
import pyTerminalproccesosx

pyTerminalproccesosx.Notifier().send_lateral_message(label='<YOUR_LABEL>',
                                                     subtitle='<YOUR_SUBTITLE>',
                                                     text='<TEXT>', file_icon='<FILE_ICON>',
                                                     sound=pyTerminalproccesosx.CONSTANT_SOUNDS.Popsound)
```                                                     
                                 
