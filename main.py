import parselmouth as pm
import graphing as g ## needed for graphing
import freqtomidi as f
import numpy as np ## needed for other libs
import json
import fluidsynth
import time

print(f.freq2midi(480))

with open('freq.json', 'r') as f:
    freq = json.load(f)

def find_pitch(pitch):
  pitch_values = pitch.selected_array['frequency']
  print(pitch_values)

if __name__ == "__main__":
  snd = pm.Sound("audio/peak.wav")
  pitch = snd.to_pitch()

  find_pitch(pitch)

#g.graph(pitch)