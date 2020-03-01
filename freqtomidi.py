import math

def freq2midi(freq):
  if freq == 0:
    return 0
  return round(12 * (math.log2(freq) - math.log2(440)) + 69) 
def midi2freq(midi):
  return round(440 * 2 ** ((midi - 69) * (1./12.)))