import sys


class Scale:
    name = ''
    steps = []
    intervals = []

    @property
    def intervals(self):
        return self.intervals

    @property
    def steps(self):
        return self._steps

    def __str__(self):
        return '{} scale: steps: {}'.format(self.name, self.steps)

    def __repr__(self):
        return '{} scale:\n  steps: {}\n  intervals: {}'.format(
                self.name, self.steps, self.intervals)

class Major(Scale):
    name = 'Major'
    steps = [2, 2, 1, 2, 2, 2, 1]
    intervals = [2, 4, 5, 7, 9, 11, 12]


class NaturalMinor(Scale):
    name = 'Natural Minor'
    steps = [2, 1, 2, 2, 1, 2, 2]
    intervals = [2, 3, 5, 7, 8, 10, 12]


class HarmonicMinor(Scale):
    name = 'Harmonic Minor'
    steps = [2, 1, 2, 2, 1, 3, 1]
    intervals = [2, 3, 5, 7, 8, 11, 12]


class MelodicMinor(Scale):
    name = 'Melodic Minor'
    steps = [2, 1, 2, 2, 2, 2, 1]
    intervals = [2, 3, 5, 7, 9, 11, 12]


class Pentatonic(Scale):
    name = 'Pentatonic'
    steps = [2, 2, 3, 2]
    intervals = [2, 4, 7, 9]


class WholeTone(Scale):
    name = 'Whole Tone'
    steps = [2, 2, 2, 2, 2, 2]
    intervals = [2, 4, 6, 8, 10, 12]


class MajorPentatonic(Scale):
    name = 'Major Pentatonic'
    steps = [2, 1, 2, 1]
    intervals = [2, 3, 5, 6]


class MinorPentatonic(Scale):
    name = 'Minor Pentatonic'
    steps = [3, 1, 1, 2]
    intervals = [3, 4, 5, 7]


class Blues(Scale):
    name = 'Blues'
    steps = [3, 2, 1, 1, 3]
    intervals = [3, 5, 6, 7, 10]


def __setup():
    setattr(sys.modules[__name__], 'SCALE_CLASSES', Scale.__subclasses__())
    scales = {}
    for ScaleClass in SCALE_CLASSES:
        scale = ScaleClass()
        scales[scale.name] = scale
    setattr(sys.modules[__name__], 'SCALES', scales)


__setup()


if __name__ == '__main__':
    for scale in SCALES.values():
        print(repr(scale))
