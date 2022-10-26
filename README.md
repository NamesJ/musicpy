# musicpy
Musical notes, chords, scales, and keys, represented in python

## Find which key fits a known set of notes
```
from musicpy.key import estimate_key

known_notes = ['G', 'D', 'B', 'E']
estimate_key(known_notes)
```

## Find all notes for some set of chords (union)
```
from musicpy.chord import Gmaj, Cmin, Adim

print(Gmaj + Cmin + Adim)
```

## Find all chord qualities (classes) that contain a known set of intervals
```
from musicpy.chord import get_chords_by_intervals

intervals = [4, 7] # perfect 3rd, perfect 5th
chords = get_chords_by_intervals(intervals)

for c in chords:
    print('{}: {}'.format(c.name_suffix, c.intervals))
```

See example usage in `example.py`
