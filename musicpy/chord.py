import sys

from .note import NOTES

class Chord:
    intervals = []
    name_suffix = ''
    def __init__(self, tonic):
        self.tonic = tonic
        self.name = '{}{}'.format(tonic, self.name_suffix)
        self.note_indices = []
        self.notes = []
        tonic_idx = NOTES.index(self.tonic)
        for i in self.intervals:
            note_idx = (tonic_idx + i) % len(NOTES)
            self.note_indices.append(note_idx)
            self.notes.append(NOTES[note_idx])

    def __add__(self, other):
        return set(self.notes) | set(other.notes)

    def __str__(self):
        return '{}: {}'.format(self.name, self.notes)


class Major(Chord):
    intervals = [4, 7]
    name_suffix = 'maj'


class Minor(Chord):
    intervals = [3, 7]
    name_suffix = 'min'


class Diminished(Chord):
    intervals = [3, 6]
    name_suffix = 'dim'


class Major7(Chord):
    intervals = [4, 7, 11]
    name_suffix = 'maj7'


class Minor7(Chord):
    intervals = [3, 7, 10]
    name_suffix = 'min7'


class Dominant7(Chord):
    intervals = [4, 7, 10]
    name_suffix = 'dom7'


class Suspended2(Chord):
    intervals = [2, 7]
    name_suffix = 'sus2'


class Suspended4(Chord):
    intervals = [5, 7]
    name_suffix = 'sus4'


class Augmented(Chord):
    intervals = [4, 8]
    name_suffix = 'aug'


class Major9(Chord):
    intervals = [4, 7, 11, 14]
    name_suffix = 'maj9'


class Minor9(Chord):
    intervals = [3, 7, 10, 14]
    name_suffix = 'min9'


class Dominant9(Chord):
    intervals = [4, 7, 10, 14]
    name_suffix = 'dom9'


class Major11(Chord):
    intervals = [4, 7, 11, 14, 17]
    name_suffix = 'maj11'


class Minor11(Chord):
    intervals = [3, 7, 10, 14, 17]
    name_suffix = 'min11'


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
