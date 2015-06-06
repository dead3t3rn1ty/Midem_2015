# Kaossify

Some code to expand my Kaossilator pro capabilites

## How it works

The workflow is the same as the kaossilator, but using spotify and real time effects on LADSPA instead of the internal sound processor.

Selecting the instruments from the program memory switches from on track to another.
Tapping the touchscreen plays the song, it keeps playing until you don't remove your finger.
The x axes of the touchscreen controls the cutoff frequency of a low pass filter.
The y axes of the touchscreen controls the resonance.
Selecting a different time using the "TAP TEMPO" button will trigger a query on echonest to find new songs.

## Dependencies

Spotify linux desktop client (it uses the dbus interface to control the spotify playback).
Jack
Jack-rack to apply LADSPA filters
Python libraries: time, dbus, jack, datetime, json, requests, mididings.

