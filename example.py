import time
import musicpy
import musicpy.note
from musicpy.note import C, CzDb, D, DzEb, E, F, FzGb, G, GzAb, A, AzBb, B
# Init notes will take a little while
print('Initalizing tones (octaves 3-4) -- this might take a little while')
musicpy.note.init_stream()
musicpy.note.init_tones(3, 4)
#musicpy.note.init_mixer()
#musicpy.note.init_tones(3, 4)
# Import notes which happen to be in GMajor scale, 3rd and 5th octaves
from musicpy.note import (G3, A3, B3, C3, D3, E3, FzGb3, G4, A4, B4, C4, D4, E4,
    FzGb4)

from musicpy.note import NOTES
from musicpy import chord, key, scale
from musicpy.key import Key, estimate_key
from musicpy.chord import Gmaj, Emin, Amin, Bmaj




if __name__ == '__main__':
    print('\nTones')
    default_duration = 'eighth'
    melody = [E3, FzGb3, G3, B3, (A3, 'quarter'), (B3, 'quarter'), A3, B3, C4,
        D4, (C4, 'eighth'), (B3, 'half')]
    print(melody)
    print('Press [CTRL]+C to stop melody')
    try:
        while True:
            for tone in melody:
                if isinstance(tone, musicpy.note.Tone):
                    tone.play(default_duration)
                elif isinstance(tone, tuple):
                    tone, duration = tone
                    tone.play(duration)
            time.sleep(0.5)
    except KeyboardInterrupt as e:
        pass

    # Because '#' is not a valid character for object names in Python,
    # the 'z' character is used in it's place.
    print('\nNotes')
    print(NOTES)
    print(C)
    print(CzDb)
    # Play notes of Gmaj chord
    #for note in Gmaj.notes:
    #    note.play(120, 'half', 4)
    print('Gmaj notes: {}'.format(Gmaj.notes))
    #G.play(120, 'half', 4)
    #A.play(120, 'half', 4)
    #D.play(120, 'half', 4)
    print('Press [CTRL]+C to stop melody')
    try:
        while True:
            G3.play('sixteenth')
            A4.play('sixteenth')
            D4.play('sixteenth')
            A4.play('sixteenth')
    except KeyboardInterrupt as e:
        pass


    print('\nChords')
    g_major = chord.Major(G) # can also use chord.Gmaj
    print(g_major)
    e_minor = Emin
    print(e_minor)
    print(chord.Amaj)
    print('g_major + e_minor: {}'.format(g_major + e_minor))
    print('Amin + Bmaj: {}'.format(Amin + Bmaj))

    print('\nFew notes key estimation:')
    few_notes = [A, B]
    estimate_key(few_notes)

    print('\nMessin key estimation:')
    messin_notes = [FzGb, G, E, A, B, C, D]
    #messin_notes = ['F#/Gb', 'G', 'E', 'A', 'B', 'C', 'D']
    estimate_key(messin_notes)
    print('\nShady Grove key estimation:')
    shady_grove_notes = [A, B, D, E, FzGb, G]
    #shady_grove_notes = ['A', 'B', 'D', 'E', 'F#/Gb', 'G']
    estimate_key(shady_grove_notes, min_score=1)

    print('\nHard Times are Coming Now key estimation:')
    #hard_times_notes = ['B', 'D', 'E', 'G']
    hard_times_notes = g_major + e_minor # returns a NoteHolder object
    estimate_key(hard_times_notes.notes)

    print('\nScales')
    print(Key(C, scale.MinorPentatonic()))
    print(Key(C, scale.SCALES['Blues']))

    print('\nKeys')
    print(key.CMelodicMinor)
    print(key.AMinorPentatonic)
    print(key.GBlues)

    print('\nEstimate chords from intervals')
    print('Chords containing the intervals [4, 7]')
    chords = chord.get_chords_by_intervals([4, 7])
    for c in chords:
        print('{}: {}'.format(c.name_suffix, c.intervals))
    print('Chords containing the intervals: [7]')
    print(','.join([c.name_suffix for c in chord.get_chords_by_intervals([7])]))

    musicpy.note.close_stream()
