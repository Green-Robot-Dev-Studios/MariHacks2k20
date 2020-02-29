from midiutil import MIDIFile

midi = MIDIFile(1)

def set_tempo(time, bpm):
  midi.addTempo(0, time, bpm)

def add_note(notePitch, time, duration, vol):
  midi.addNote(0, 0, notePitch, time, duration, vol);

def write(path):
  with open(path, "wb") as output:
    midi.write_file(output)
    