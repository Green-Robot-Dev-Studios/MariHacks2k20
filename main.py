import parselmouth as pm
import graphing as g
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

def find_pitch(pitch):
    pitch_values = pitch.selected_array['frequency']
    print(pitch_values)

snd = pm.Sound("audio/peak.wav")
pitch = snd.to_pitch()

find_pitch(pitch)

#g.graph(pitch)