import math

def freq2midi(freq):
  return 12 * (math.log2(freq) - math.log2(440)) + 69