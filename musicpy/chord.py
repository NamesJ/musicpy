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


def __setup():
    setattr(sys.modules[__name__], 'CHORD_CLASSES', Chord.__subclasses__())
    chords = {}
    for note in NOTES:
        for ChordClass in CHORD_CLASSES:
            chord = ChordClass(note)
            chords[chord.name] = chord
            # Work around for attribute name where '#' in chord name
            if '#' in chord.name:
                #'A#/Bbmaj' => 'Az/Bb'
                alt_name = chord.name.replace('#', 'z')
                setattr(sys.modules[__name__], alt_name, chord)
            else:
                setattr(sys.modules[__name__], chord.name, chord)
    setattr(sys.modules[__name__], 'CHORDS', chords)

__setup()


def get_chords_by_intervals(intervals):
    possible_chords = []
    num_intervals = len(intervals)
    for chord in CHORD_CLASSES:
        # Check if all intervals are contained within the chord
        matches = sum([interval in chord.intervals for interval in intervals])
        if matches == num_intervals:
            possible_chords.append(chord)
    return possible_chords


if __name__ == '__main__':
    print('CHORD_CLASSES: {}'.format(CHORD_CLASSES))
    print('dir(sys.modules[__name__]):')
    print(dir(sys.modules[__name__]))
    print('Get chords by intervals: [4, 10]')
    print(get_chords_by_intervals([4, 10]))
    print('Get chords by intervals: [7]')
    print(get_chords_by_intervals([7]))
