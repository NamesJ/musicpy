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

See example usage in `example.py`
