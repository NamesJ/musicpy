import sys

NOTE_NAMES = ['C', 'CzDb', 'D', 'DzEb', 'E', 'F', 'FzGb', 'G', 'GzAb', 'A', 'AzBb', 'B']
TUNING_FREQUENCY = 440 # hertz
ALL_FREQUENCIES = [TUNING_FREQUENCY*2**(n/12) for n in range(-57, 50)]

class Tone:
    f = 0.0 # frequency (hertz)

class Note:
    name = ''
    freqs = []

    def __init__(self):
        i_base = NOTE_NAMES.index(self.name)
        self.freqs = [f for i, f in enumerate(ALL_FREQUENCIES) if i%12==i_base]

    def __str__(self):
        return '{}: {}'.format(self.name, self.freqs)

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        for f in self.freqs:
            yield f


def note_factory(note_name):
    class NoteSubclass(Note):
        name = note_name
        freqs = []
    return NoteSubclass



def __setup():
    # Generate note subclass singletons via note_factory and add them as
    # attributes to the module
    # Note order is important
    notes = []
    for note_name in NOTE_NAMES:
        NoteClass = note_factory(note_name)
        note = NoteClass()
        notes.append(note)
        # Replace class attributes with singleton instance of that class
        setattr(sys.modules[__name__], note.name, note)
    setattr(sys.modules[__name__], 'NOTES', notes)


__setup()



if __name__ == '__main__':
    print(C)
    print(AzBb)
    for note in NOTES:
        print(note)
