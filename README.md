# musicpy
Musical notes, chords, scales, and keys, represented in python

## Figure out which key fits a known set of notes
```
from musicpy.key import estimate_key

known_notes = ['G', 'D', 'B', 'E']
estimate_key(known_notes)
```

See example usage in `musicpy/main.py`
