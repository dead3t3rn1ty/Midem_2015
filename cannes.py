#!/usr/bin/python

import time
import dbus
import jack
from mididings import *

bus = dbus.SessionBus()

proxy = bus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
interface = dbus.Interface(proxy, dbus_interface='org.mpris.MediaPlayer2.Player')
jackclient = jack.Client("Hackday")


def controllerfy(ev):
   if ev.type == PROGRAM:
      if ev.data2 == 0:
         interface.OpenUri("spotify:track:3H94aUCpXRXG1HvWiSRuQq")
         time.sleep(0.1)
         interface.Stop()
         return ev
      elif ev.data2 == 40:
         interface.OpenUri("spotify:track:3OYiqgiXQ4h6OI5v26ee2V")
         time.sleep(0.1)
         interface.Stop()
         return ev
      elif ev.data2 == 78:
         interface.OpenUri("spotify:track:3PT0k3OSezJ2LDJp4ZCS5q")
         time.sleep(0.1)
         interface.Stop()
         return ev
      elif ev.data2 == 95:
         interface.OpenUri("spotify:track:4UeuoNaP2KfmtIgpcB1mt1")
         time.sleep(0.1)
         interface.Stop()
         return ev
      elif ev.data2 == 7:
         interface.OpenUri("spotify:track:7Jx1kzhvTpJexmejFFt08t")
         time.sleep(0.1)
         interface.Stop()
         return ev
      else:
         print("Program change not parsed")
         print(ev.data1)
         print(ev.data2)
         return None
   elif ev.type == CTRL:
      if ev.data1 == 92:
         interface.PlayPause()
         return ev
      else:
         return None
   else:
      return None

config (
   backend='alsa',
   client_name='hackday',
)

jackclient.disconnect("PulseAudio JACK Sink:front-left", "system:playback_1")
jackclient.disconnect("PulseAudio JACK Sink:front-right", "system:playback_2")

run(Process(controllerfy))
