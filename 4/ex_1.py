import math
import itertools
import helpers


class Segment:

    def __init__(self, name, length):
        self.name = name
        self.length = length

    def __add__(self, other):
        if isinstance(other, Segment):
            return self.length + other.length
        else:
            return 0

    def __str__(self):
        return self.name


class Triangle:

    def __init__(self, seg1: Segment, seg2: Segment, seg3: Segment):
        self.seg1 = seg1
        self.seg2 = seg2
        self.seg3 = seg3

        half_perimeter = (seg1 + seg2 + seg3.length) / 2
        self.square = math.sqrt(half_perimeter * (half_perimeter + seg1.length) * (half_perimeter + seg2.length)
                                * (half_perimeter + seg3.length))

    def __str__(self):
        return "Triangle({}, {}, {}) = {}".format(self.seg1.name, self.seg2.name, self.seg3.name, self.square)


def input_segments(segments_names: list):
    res = []
    for segment_name in segments_names:
        length = helpers.cycled_input("Input segment {}:".format(segment_name), float, lambda v: v > 0)
        res.append(Segment(segment_name, length))

    return res


def can_form_triangle(seg1: Segment, seg2: Segment, seg3: Segment):
    if seg1 + seg2 > seg3.length and seg3 + seg2 > seg1.length and seg1 + seg3 > seg2.length:
        return True
    else:
        return False


segments = input_segments(["a", "b", "c", "d"])
for combination in list(itertools.combinations(segments, 3)):
    if can_form_triangle(combination[0], combination[1], combination[2]):
        print(str(Triangle(combination[0], combination[1], combination[2])))
