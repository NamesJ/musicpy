import sys


class Scale:
    def __init__(self, name, steps):
        self.name = name
        self.steps = steps
        self.intervals = [steps[0]]
        for idx in range(1, len(steps)-1):
            self.intervals.append(self.intervals[-1]+steps[idx])

    def __str__(self):
        return '{} scale: {}'.format(self.name, self.steps)

    def __repr__(self):
        return '{} scale:\n  steps: {}\n  intervals: {}'.format(
                self.name, self.steps, self.intervals)

class Major(Scale):
    def __init__(self):
        super().__init__('Major', [2, 2, 1, 2, 2, 2, 1])


class NaturalMinor(Scale):
    def __init__(self):
        super().__init__('Natural Minor', [2, 1, 2, 2, 1, 2, 2])


class HarmonicMinor(Scale):
    def __init__(self):
        super().__init__('Harmonic Minor', [2, 1, 2, 2, 1, 3, 1])


class MelodicMinor(Scale):
    def __init__(self):
        super().__init__('Melodic Minor', [2, 1, 2, 2, 2, 2, 1])


class Pentatonic(Scale):
    def __init__(self):
        super().__init__('Pentatonic', [2, 2, 3, 2])


class WholeTone(Scale):
    def __init__(self):
        super().__init__('Whole Tone', [2, 2, 2, 2, 2, 2])


class MajorPentatonic(Scale):
    def __init__(self):
        super().__init__('Major Pentatonic', [2, 1, 2, 1])


class MinorPentatonic(Scale):
    def __init__(self):
        super().__init__('Minor Pentatonic', [3, 1, 1, 2])


class Blues(Scale):
    def __init__(self):
        super().__init__('Blues', [3, 2, 1, 1, 3])


def __setup():
    setattr(sys.modules[__name__], 'SCALE_CLASSES', Scale.__subclasses__())
    scales = {}
    for ScaleClass in SCALE_CLASSES:
        scale = ScaleClass()
        scales[scale.name] = scale
    setattr(sys.modules[__name__], 'SCALES', scales)


__setup()
