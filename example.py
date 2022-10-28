from musicpy.note import C, CzDb, D, DzEb, E, F, FzGb, G, GzAb, A, AzBb, B
from musicpy.note import NOTES
from musicpy import chord, key, scale
from musicpy.key import Key, estimate_key
from musicpy.chord import Gmaj, Emin, Amin, Bmaj




if __name__ == '__main__':
    # Because '#' is not a valid character for object names in Python,
    # the 'z' character is used in it's place.
    print('\nNotes')
    print(NOTES)
    print(C)
    print(CzDb)

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
