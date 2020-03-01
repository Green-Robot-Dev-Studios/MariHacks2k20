from midiutil import MIDIFile

midi = MIDIFile(1)

def set_tempo(time, bpm):
  midi.addTempo(0, time, bpm)

def add_note(notePitch, time, duration, vol):
  midi.addNote(0, 0, notePitch, time, duration, vol)

def add_bass_note(notePitch, time, duration, vol):
  midi.addNote(0, 0, notePitch, time, duration, vol)

def add_root_triad(notePitch, time, duration, vol):
  midi.addNote(0, 0, notePitch, time, duration, vol)
  midi.addNote(0, 0, notePitch+4, time, duration, vol)
  midi.addNote(0, 0, notePitch+7, time, duration, vol)



def write(path):
  with open("exports/"+path, "wb") as output:
    midi.writeFile(output)
