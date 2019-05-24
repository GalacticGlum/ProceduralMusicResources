from midiutil import MIDIFile
from math import sin, pi
from random import randint

midi_file = MIDIFile(1) # Create MIDI file with one track.
midi_file.addTempo(0, 0, 240) # set the tempo to 120 BPM on track 0, at time 0.

multiples = {
    2: 60, # C4
    3: 62, # D4
    4: 65, # F4
    5: 67, # G4
    6: 67, # G4
    7: 69, # A4
    8: 72, # C5
    9: 72, # C5
    10: 74 # D5
}

N = 200
time = 0

# N is some positive integer greater than one.
for i in range(1, N + 1):
    duration = 0.45 * sin(i) + 0.55
    for multiple in multiples:
        if i % multiple == 0:
            note = multiples[multiple]

            midi_file.addNote(0, 0, note, time, duration, 100)

    time += max_duration

def save_midi(midi_handle, filename):
    with open(f'{filename}.mid', 'wb') as output_file:
        midi_handle.writeFile(output_file)

save_midi(midi_file, 'periodic_duration')