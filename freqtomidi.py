import math

def freq2midi(freq):
  return round(12 * (math.log2(freq) - math.log2(440)) + 69) 
def midi2freq(midi):
  return round(440 * 2 ** ((midi - 69) * (1./12.)))