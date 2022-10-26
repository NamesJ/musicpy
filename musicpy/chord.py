import sys

from .note import NOTES

class Chord:
    def __init__(self, name, tonic, intervals):
        self.name = name
        self.tonic = tonic
        self.tonic_idx = NOTES.index(self.tonic)
        self.notes = [self.tonic]
        self.intervals = intervals
        for interval in intervals:
            note_idx = (self.tonic_idx + interval) % len(NOTES)
            note = NOTES[note_idx]
            self.notes.append(note)

    def __add__(self, other):
        return set(self.notes) | set(other.notes)

    def __str__(self):
        return '{}: {}'.format(self.name, self.notes)


class Major(Chord):
    def __init__(self, tonic):
        super().__init__('{}maj'.format(tonic), tonic, [4, 7])


class Minor(Chord):
    def __init__(self, tonic):
        super().__init__('{}min'.format(tonic), tonic, [3, 7])


class Diminished(Chord):
    def __init__(self, tonic):
        super().__init__('{}dim'.format(tonic), tonic, [3, 6])


class Major7(Chord):
    def __init__(self, tonic):
        super().__init__('{}maj7'.format(tonic), tonic, [4, 7, 11])


class Minor7(Chord):
    def __init__(self, tonic):
        super().__init__('{}min7'.format(tonic), tonic, [3, 7, 10])


class Dominant7(Chord):
    def __init__(self, tonic):
        super().__init__('{}dom7'.format(tonic), tonic, [4, 7, 10])


class Suspended2(Chord):
    def __init__(self, tonic):
        super().__init__('{}sus2'.format(tonic), tonic, [2, 7])


class Suspended4(Chord):
    def __init__(self, tonic):
        super().__init__('{}sus4'.format(tonic), tonic, [5, 7])


class Augmented(Chord):
    def __init__(self, tonic):
        super().__init__('{}aug'.format(tonic), tonic, [4, 8])

class Major9(Chord):
    def __init__(self, tonic):
        super().__init__('{}ext9'.format(tonic), tonic, [4, 7, 11, 14])


class Minor9(Chord):
    def __init__(self, tonic):
        super().__init__('{}ext11'.format(tonic), tonic, [3, 7, 10, 14])


class Dominant9(Chord):
    def __init__(self, tonic):
        super().__init__('{}dom9'.format(tonic), tonic, [4, 7, 10, 14])


class Major11(Chord):
    def __init__(self, tonic):
        super().__init__('{}maj11'.format(tonic), tonic, [4, 7, 11, 14, 17])


class Minor11(Chord):
    def __init__(self, tonic):
        super().__init__('{}min11'.format(tonic), tonic, [3, 7, 10, 14, 17])


CHORD_CLASSES = {Major, Minor, Diminished, Major7, Minor7, Dominant7,
                Suspended2, Suspended4, Augmented, Major9, Dominant9, Major11,
                Minor11}


def __setup():
    chords = {}
    for note in NOTES:
        for ChordClass in CHORD_CLASSES:
            chord = ChordClass(note)
            chords[chord.name] = chord
            setattr(sys.modules[__name__], chord.name, chord)
    setattr(sys.modules[__name__], 'CHORDS', chords)

__setup()
