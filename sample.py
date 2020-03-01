bpm = 100

def create_sample(pitches):
  fixed_pitches = []
  fixed_durations = []
  total_time = len(pitches)/bpm
  #sample 1 note for every (len(pitch_values)/bpm) pitches
  
  threshold = 5
  duration = 1
  cur = -11
  for i in range(len(pitches)):
    if pitches[i] <= cur-threshold and pitches[i] >= cur+threshold:
      duration = duration + 1
      continue
    else:
      fixed_durations.append(duration)
      duration = 1
      cur = pitches[i]
      fixed_pitches.append(cur)
  
  

  return fixed_pitches, fixed_durations