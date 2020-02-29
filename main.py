import parselmouth as pm
import graphing as g
import numpy as np

def find_pitch(pitch):
  pitch_values = pitch.selected_array['frequency']
  print(pitch_values)

if __name__ == "__main__":
  snd = pm.Sound("audio/peak.wav")
  pitch = snd.to_pitch()

  find_pitch(pitch)

#g.graph(pitch)