import parselmouth as pm
import graphing as g ## needed for graphing
import gen
import sample
import freqtomidi as f
import numpy as np ## needed for other libs
import fluidsynth
import time

#print(f.midi2freq(f.freq2midi(480)))

def find_pitch(pitch):
  pitch_values = pitch.selected_array['frequency']   
  print(pitch_values)
  gen.set_tempo(0, 100)

  pitches, lengths = sample.create_sample(pitch_values)

  loop = 0
  for x in pitches:
    if x == 0:
      loop = loop + 1
      continue
    gen.add_note(f.freq2midi(x), loop, lengths[loop], 50)
    loop = loop + 1
  gen.write("export.mid")

if __name__ == "__main__":
  snd = pm.Sound("audio/peak.wav")
  pitch = snd.to_pitch()

  find_pitch(pitch)

#g.graph(pitch)

#hello my name is austin i like rubiks cube and anime girls my favourite hentai is euphoria  
