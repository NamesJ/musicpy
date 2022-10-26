import sys


class Scale:
    name = ''
    steps = []
    intervals = []
    def __init__(self):
        self.intervals.append(self.steps[0])
        for idx in range(1, len(self.steps)-1):
            self.intervals.append(self.intervals[-1]+self.steps[idx])

    def __str__(self):
        return '{} scale: {}'.format(self.name, self.steps)

    def __repr__(self):
        return '{} scale:\n  steps: {}\n  intervals: {}'.format(
                self.name, self.steps, self.intervals)

class Major(Scale):
    name = 'Major'
    steps = [2, 2, 1, 2, 2, 2, 1]


class NaturalMinor(Scale):
    name = 'Natural Minor'
    steps = [2, 1, 2, 2, 1, 2, 2]


class HarmonicMinor(Scale):
    name = 'Harmonic Minor'
    steps = [2, 1, 2, 2, 1, 3, 1]


class MelodicMinor(Scale):
    name = 'Melodic Minor'
    steps = [2, 1, 2, 2, 2, 2, 1]


class Pentatonic(Scale):
    name = 'Pentatonic'
    steps = [2, 2, 3, 2]


class WholeTone(Scale):
    name = 'Whole Tone'
    steps = [2, 2, 2, 2, 2, 2]


class MajorPentatonic(Scale):
    name = 'Major Pentatonic'
    steps = [2, 1, 2, 1]


class MinorPentatonic(Scale):
    name = 'Minor Pentatonic'
    steps = [3, 1, 1, 2]


class Blues(Scale):
    name = 'Blues'
    steps = [3, 2, 1, 1, 3]


def __setup():
    setattr(sys.modules[__name__], 'SCALE_CLASSES', Scale.__subclasses__())
    scales = {}
    for ScaleClass in SCALE_CLASSES:
        scale = ScaleClass()
        scales[scale.name] = scale
    setattr(sys.modules[__name__], 'SCALES', scales)


__setup()
