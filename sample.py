bpm = 100

def create_sample(pitches):
  fixed_pitches = []
  fixed_durations = []
  total_time = len(pitches)/bpm
  #sample 1 note for every (len(pitch_values)/bpm) pitches
  
  threshold = 10
  duration = 0
  cur = -11
  for i in range(len(pitches)):
    if i <= cur-threshold and i >= cur+threshold:
      duration+=1
      continue
    else:
      fixed_durations.append(duration)
      duration = 0
      cur = i
      fixed_pitches.append(i)

  return fixed_pitches, fixed_durations