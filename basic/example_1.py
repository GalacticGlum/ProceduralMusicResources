from midiutil import MIDIFile

midi_file = MIDIFile(1) # Create MIDI file with one track.
midi_file.addTempo(0, 0, 120) # set the tempo to 120 BPM on track 0, at time 0.
for i in range(10):
    # midi_file.addNote(track, channel, note, time, duration, volume)
    midi_file.addNote(0, 0, 60 + i, i, 1, 100) # Play the note (given by f(x) = 60 + x) for 1 quarter note

def save_midi(midi_handle, filename):
    with open(f'{filename}.mid', 'wb') as output_file:
        midi_handle.writeFile(output_file)

save_midi(midi_file, 'example1')