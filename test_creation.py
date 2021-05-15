import creation as cr
import unittest

def test_creation():
    """
    Testing create functions
    """
    assert cr.create_prof(10000, 'x', 3, 'q')
    assert cr.create_students(4, 'z', 1, 'infosci', 'yes', 49292, 'y', 4, 'infosci', 'x')
    assert cr.create_classes(326, 'abc', 7, 4, 'B')
    assert cr.create_degrees(7, 'bd', '245, 326, 344, 222', 'y', 'x')
    