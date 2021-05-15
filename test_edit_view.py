import edit_view as ev
import unittest

def test_edit_view():
    """
    Testing class attributes and user input in functions
    """
    assert ev.student(1, "John", 3, "infosci")
    assert ev.student(1000, "Bill", 4, "infosci")
    assert ev.prof(1000000, "Mac", 2)
    assert ev.prof(5, "aksldj alksjd", 2)
    assert ev.degree(7, 'Math', ['i3', 'i2'], True)
    assert ev.c(81, 'i3', 1, 6, 'A')
    assert ev.edit_students('no', 7, 10, 'Jake', 3, 'infosci')
    assert ev.edit_prof('yes', 7, 10, 'Prof Boris', 1)