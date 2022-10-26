from musicpy.note import NOTES
from musicpy import chord, key, scale
from musicpy.key import Key, estimate_key
from musicpy.chord import Gmaj, Emin, Amin, Bmaj




if __name__ == '__main__':
    print('\nChords')
    g_major = chord.Major('G') # can also use chord.Gmaj
    print(g_major)
    e_minor = Emin
    print(e_minor)
    print('g_major + e_minor: {}'.format(g_major + e_minor))
    print('Amin + Bmaj: {}'.format(Amin + Bmaj))

    print('\nFew notes key estimation:')
    few_notes = ['A', 'B']
    estimate_key(few_notes)

    print('\nMessin key estimation:')
    messin_notes = ['F#/Gb', 'G', 'E', 'A', 'B', 'C', 'D']
    estimate_key(messin_notes)
    print('\nShady Grove key estimation:')
    shady_grove_notes = ['A', 'B', 'D', 'E', 'F#/Gb', 'G']
    estimate_key(shady_grove_notes, min_score=1)

    print('\nHard Times are Coming Now key estimation:')
    #hard_times_notes = ['B', 'D', 'E', 'G']
    hard_times_notes = g_major + e_minor
    estimate_key(hard_times_notes)

    print('\nScales')
    print(Key('C', scale.MinorPentatonic()))
    print(Key('C', scale.SCALES['Blues']))

    print('\nKeys')
    print(key.CMelodicMinor)
    print(key.AMinorPentatonic)
    print(key.GBlues)
