import parselmouth as pm
import graphing as g ## needed for graphing
import gen
import freqtomidi as f
import numpy as np ## needed for other libs
import fluidsynth
import time

#print(f.midi2freq(f.freq2midi(480)))

def find_pitch(pitch):
  pitch_values = pitch.selected_array['frequency']   
  print(pitch_values)
  gen.set_tempo(0, 100)
  loop = 0
  for x in pitch_values:
    gen.add_note(f.freq2midi(x), loop, 1, 50)
    loop = loop + 1
  gen.write("export.mid")

if __name__ == "__main__":
  snd = pm.Sound("audio/peak.wav")
  pitch = snd.to_pitch()

  find_pitch(pitch)

#g.graph(pitch)

#hello my name is austin i like rubiks cube and anime girls my favourite hentai is euphoria