import sys

from .note import NOTES
from .scale import SCALES


class Key:
    def __init__(self, root, scale):
        self.root = root
        self.scale = scale
        self.name = '{} {}'.format(self.root.name, self.scale.name)
        self.root_idx = NOTES.index(self.root)
        self.notes = [self.root]
        # Initialize notes
        for interval in scale.intervals:
            note_idx = (self.root_idx + interval) % len(NOTES)
            note = NOTES[note_idx]
            self.notes.append(note)

    def __str__(self):
        note_names = ', '.join([note.name for note in self.notes])
        return '{}: {}'.format(self.name, note_names)

    def __repr__(self):
        return self.__str__()


def estimate_key(notes, min_found=0.8, min_score=0.8):
    possibilities = []
    for root in NOTES:
        #for name, scale in SCALES:
        for name, scale in SCALES.items():
            d = {'found': [], 'not-found': []}
            key = KEYS[(root, scale.name)]
            for note in notes:
                if note in key.notes:
                    d['found'].append(note)
                else:
                    d['not-found'].append(note)
            # Don't consider those with less notes found than not found
            if len(d['found']) < len(d['not-found']):
                continue
            # Don't consider those with less than {min_found}% of notes found
            if len(d['found']) / len(notes) < min_found:
                continue
            score = len(d['found']) - len(d['not-found'])
            score = 1 - (len(d['not-found']) / len(d['found']))
            if score < min_score:
                continue
            possibilities.append((key, d, score))
    # Sort possibilities by highest match
    possibilities = sorted(possibilities, key=lambda x: x[2], reverse=True)
    note_names = ', '.join([note.name for note in notes])
    print('Possible keys: notes=[{}] found>={:.2f}% score>={:.2f}%'.format(
            note_names, min_found*100, min_score*100))
    for key, stats, score in possibilities:
        print('{0}: score={2:.2f}'.format(key, stats, score))


def __setup():
    keys = {}
    for root in NOTES:
        for name, scale in SCALES.items():
            key = Key(root, scale)
            keys[(root, scale.name)] = key
            attr_name = '{}{}'.format(root.name, scale.name).replace(' ', '')
            setattr(sys.modules[__name__], attr_name, key)
    setattr(sys.modules[__name__], 'KEYS', keys)


__setup()


if __name__ == '__main__':
    print(GMajor)
    for key in KEYS.values():
        print(key)
