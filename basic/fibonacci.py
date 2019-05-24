from midiutil import MIDIFile
from math import sqrt

midi_file = MIDIFile(1) # Create MIDI file with one track.
midi_file.addTempo(0, 0, 160) # set the tempo to 120 BPM on track 0, at time 0.

def get_fibonacci_number(n):
    PHI = (1 + sqrt(5)) / 2
    return round(pow(PHI, n) / sqrt(5))

N = 20

# generate note mapping
notes = {}
for i in range(10):
    # i semitones from D5-Sharp (75)
    notes[i] = 75 + i

# N is some positive integer greater than one.
for i in range(N):
    # get_fibonacci_number(n) returns the n-th fibonacci number (one-based)
    note = notes[get_fibonacci_number(i + 1) % 10]
    midi_file.addNote(0, 0, note, i, 1, 100)

def save_midi(midi_handle, filename):
    with open(f'{filename}.mid', 'wb') as output_file:
        midi_handle.writeFile(output_file)

save_midi(midi_file, 'fibonacci')