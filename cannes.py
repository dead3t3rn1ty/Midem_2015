#!/usr/bin/python

import time
import dbus
import jack
import datetime
from mididings import *


bus = dbus.SessionBus()
pend = 0
bpm_g = 0

proxy = bus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
interface = dbus.Interface(proxy, dbus_interface='org.mpris.MediaPlayer2.Player')
jackclient = jack.Client("Hackday")

tracks=["spotify:track:3H94aUCpXRXG1HvWiSRuQq","spotify:track:3OYiqgiXQ4h6OI5v26ee2V","spotify:track:3PT0k3OSezJ2LDJp4ZCS5q","spotify:track:4UeuoNaP2KfmtIgpcB1mt1","spotify:track:7Jx1kzhvTpJexmejFFt08t"]


def controllerfy(ev):
   if ev.type == PROGRAM:
      global tracks
      if ev.data2 == 0:
         interface.OpenUri(tracks[0])
         time.sleep(0.1)
         interface.Stop()
         return ev
      elif ev.data2 == 40:
         interface.OpenUri(tracks[1])
         time.sleep(0.1)
         interface.Stop()
         return ev
      elif ev.data2 == 78:
         interface.OpenUri(tracks[2])
         time.sleep(0.1)
         interface.Stop()
         return ev
      elif ev.data2 == 95:
         interface.OpenUri(tracks[3])
         time.sleep(0.1)
         interface.Stop()
         return ev
      elif ev.data2 == 7:
         interface.OpenUri(tracks[4])
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

def temporead(ev):
   if ev.type == SYSRT_CLOCK:
      global pend
      global t1
      global t2
      global bpm_g
      if pend == 0:
         t1 = datetime.datetime.now()
         pend = 1
      else:
         t2 = datetime.datetime.now()
         pend = 0
         delta = t2 - t1
         bpm = ( 60000000 / delta.microseconds ) / 24
         diff = abs( bpm_g - bpm )
         if ( diff / bpm) * 100 > 2 and bpm < 280 and bpm > 60:
            bpm_g = bpm
            print("New tempo!")
            print(bpm_g)
      return ev
   else:
      return None


config (
   backend='alsa',
   client_name='hackday',
)

jackclient.disconnect("PulseAudio JACK Sink:front-left", "system:playback_1")
jackclient.disconnect("PulseAudio JACK Sink:front-right", "system:playback_2")

run(
   [
      Process(controllerfy),
      Filter(SYSRT_CLOCK) % Process(temporead)
   ]
)
