import math
import sys
import os
import pyaudio
import numpy as np

SAMPLE_RATE = 44100
DEFAULT_BPM = 120
NOTE_NAMES = ['C', 'CzDb', 'D', 'DzEb', 'E', 'F', 'FzGb', 'G', 'GzAb', 'A', 'AzBb', 'B']
TUNING_FREQUENCY = 440 # hertz
ALL_FREQUENCIES = [TUNING_FREQUENCY*2**(n/12) for n in range(-57, 50)]
STREAM = None


class Tone:
    def __init__(self, name, freq, bpm=DEFAULT_BPM):
        self.name = name
        self.freq = freq
        self.bpm = bpm
        self.whole_duration = 240/bpm
        self.whole = self._gen_sound(self.whole_duration)
        self.half_duration = 120/bpm
        self.half = self._gen_sound(self.half_duration)
        self.dotted_quarter_duration = 90/bpm
        self.dotted_quarter = self._gen_sound(self.dotted_quarter_duration)
        self.quarter_duration = 60/bpm
        self.quarter = self._gen_sound(self.quarter_duration)
        self.dotted_eighth_duration = 45/bpm
        self.dotted_eighth = self._gen_sound(self.dotted_eighth_duration)
        self.triplet_quarter_duration = 40/bpm
        self.triplet_quarter = self._gen_sound(self.triplet_quarter_duration)
        self.eighth_duration = 30/bpm
        self.eighth = self._gen_sound(self.eighth_duration)
        self.dotted_sixteenth_duration = 22.5/bpm
        self.dotted_sixteenth = self._gen_sound(self.dotted_sixteenth_duration)
        self.triplet_eighth_duration = 20/bpm
        self.triplet_eighth = self._gen_sound(self.triplet_eighth_duration)
        self.sixteenth_duration = 15/bpm
        self.sixteenth = self._gen_sound(self.sixteenth_duration)
        self.triplet_sixteenth_duration = 10/bpm
        self.triplet_sixteenth = self._gen_sound(self.triplet_sixteenth_duration)

    def _gen_sound(self, duration=1):
        frames = int(SAMPLE_RATE * duration)
        #s = int(SAMPLE_RATE * duration)
        #part = lambda x : 4096 * np.sin(2*np.pi*self.freq*x/SAMPLE_RATE)
        #arr = np.array([part(x) for x in range(s)]).astype(np.float32).tostring()
        #sound = np.c_[arr, arr]
        samples = np.sin(2*self.freq*np.pi*np.arange(frames*2)/SAMPLE_RATE)
        fade_out = np.linspace(1, 0, len(samples))
        sound = samples * fade_out
        return sound.astype(np.float32).tostring()

    def play(self, duration):
        if isinstance(duration, str):
            sound = getattr(self, duration)
            duration = getattr(self, '{}_duration'.format(duration))
        elif isinstance(duration, int) or isinstance(duration, float):
            sound = self._gen_sound(duration)
        else:
            raise Exception('Must provide either duration as note length name \
or duration in seconds')
        delay = int(duration*1000)
        STREAM.write(sound)

    def __str__(self):
        return '{}: {}Hz @ {}bpm'.format(self.name, self.freq, self.bpm)

    def __repr__(self):
        return self.__str__()



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

    def __getitem__(self, index):
        return self.freqs[index]

    @property
    def octaves(self):
        return len(self.freqs)

    def play(self, bpm, duration, octave):
        Tone(self.freqs[octave], bpm).play(duration)


def note_factory(note_name):
    class NoteSubclass(Note):
        name = note_name
        freqs = []
    return NoteSubclass


def init_tones(min_octave=0, max_octave=7):
    # Setting up all of the Tone module attributes takes a little while
    tones = []
    for note in NOTES:
        for octave in range(min_octave, min(note.octaves, max_octave+1)):
            tone_name = '{}{}'.format(note.name, octave)
            tone = Tone(tone_name, note[octave], DEFAULT_BPM)
            tones.append(tone)
            setattr(sys.modules[__name__], tone.name, tone)
    setattr(sys.modules[__name__], 'TONES', tones)


def init_notes():
    # Generate note subclass singletons via note_factory and add them as
    # attributes to the module
    # Note order is important
    notes = []
    for note_name in NOTE_NAMES:
        NoteClass = note_factory(note_name)
        note = NoteClass()
        notes.append(note)
        setattr(sys.modules[__name__], note.name, note)
    setattr(sys.modules[__name__], 'NOTES', notes)


def init_stream():
    p = pyaudio.PyAudio()
    stream = p.open(format = pyaudio.paFloat32,
            frames_per_buffer=1024,
            channels = 2,
            rate = SAMPLE_RATE,
            output = True)
    stream.p = p
    setattr(sys.modules[__name__], 'STREAM', stream)


def close_stream():
    STREAM.stop_stream()
    STREAM.close()
    STREAM.p.terminate()


def _setup():
    init_notes()


_setup()


if __name__ == '__main__':
    # Initalize tone attributes for each of the notes (C0, C1, ..., B7, B8)
    init_stream()
    init_tones()
    print(C)
    print(AzBb)
    for note in NOTES:
        print(note)
    print(A4)
    a4_tone = Tone('A4', A[4])
    a4_tone.play('half')
    A4.play('half')
    for octave in range(2, min([n.octaves for n in NOTES])-3):
        for note in NOTES:
            print('{}{}'.format(note.name, octave))
            note.play(120, 'sixteenth', octave)
