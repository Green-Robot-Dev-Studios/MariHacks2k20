import parselmouth as pm

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#make stuff look nice
sns.set()

def draw_spectrogram(spectrogram, dynamic_range=70):
    X, Y = spectrogram.x_grid(), spectrogram.y_grid()
    sg_db = 10 * np.log10(spectrogram.values)
    plt.pcolormesh(X, Y, sg_db, vmin=sg_db.max() - dynamic_range, cmap='afmhot')
    plt.ylim([spectrogram.ymin, spectrogram.ymax])
    plt.xlabel("time [s]")
    plt.ylabel("frequency [Hz]")

plt.figure()
snd = pm.Sound("audio/peak.wav")
spectrogram = snd.to_spectrogram()
draw_spectrogram(spectrogram)
plt.show()