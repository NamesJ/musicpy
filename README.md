# musicpy
Musical notes, chords, scales, and keys, represented in python

See example usage in `example.py`

## Setup
```
pip install numpy
pip install pyaudio

```


## Find which key fits a known set of notes
```
from musicpy.key import estimate_key
from musicpy.note import G, D, B, E

known_notes = [G, D, B, E]
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

## Play a melody
```
import time # for delay

import musicpy.note
# Initalize audio stream
musicpy.note.init_stream()
# Initalize tones
musicpy.note.init_tones()

default_duration = 'eighth'
melody = [E3, FzGb3, G3, B3, (A3, 'quarter'), (B3, 'quarter'), A3, B3, C4,
          D4, (C4, 'eighth'), (B3, 'half')]
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

# Close audio stream
musicpy.note.close_stream()
```
