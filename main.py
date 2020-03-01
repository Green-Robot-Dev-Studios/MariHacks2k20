import parselmouth as pm
import graphing as g  ## needed for graphing
import gen
import sample
import freqtomidi as f
import numpy as np  ## needed for other libs

#print(f.midi2freq(f.freq2midi(480)))


def find_pitch(pitch):
  pitch_values = pitch.selected_array['frequency']
  #print(pitch_values)
  gen.set_tempo(0, 5990)

  print("Before Pitch Values " + str(pitch_values))
  pitches, lengths = sample.create_sample(pitch_values)
  print("After Pitch Change " + str(pitches) + str(lengths))

  loop = 0
  beat = 0
  for x in pitches:
    if (loop < len(lengths) - 1):
      print("Adding note " + str(f.freq2midi(x)) + " at time " + str(beat) + " for " + str(lengths[loop + 1]))
      if(lengths[loop + 1] > 5):
        gen.add_note(f.freq2midi(x), beat, lengths[loop + 1], 100)
        gen.add_note(f.freq2midi(x/2), beat, lengths[loop + 1], 90)
      loop = loop + 1

      beat = beat + lengths[loop]
  gen.write("exports/export.mid")

if __name__ == "__main__":
  snd = pm.Sound("audio/townroad.wav")
  pitch = snd.to_pitch()

  find_pitch(pitch)

#g.graph(pitch)

#hello my name is austin i like rubiks cube and anime girls my favourite hentai is euphoria
