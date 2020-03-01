import freqtomidi as fm
import cfgman

bpm = 100

def create_sample(pitches):
  fixed_pitches = []
  fixed_durations = []
  total_time = len(pitches)/bpm
  #sample 1 note for every (len(pitch_values)/bpm) pitches

  threshold = cfgman.threshold
  duration = 1
  cur = -11
  prevNote = 0
  for i in range(len(pitches)):
    note = fm.freq2midi(pitches[i])
    if prevNote == 0 or (note < prevNote+0 and note > prevNote-0):
        prevNote = note
        duration = duration + 1
        continue
    if (pitches[i] <= cur+threshold and pitches[i] >= cur-threshold) or pitches[i] == 0:
      duration = duration + 1
      continue
    else:
      fixed_durations.append(duration)
      duration = 1
      cur = pitches[i]
      fixed_pitches.append(cur)
    prevNote = note



  return fixed_pitches, fixed_durations
