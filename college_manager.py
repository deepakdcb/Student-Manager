# -*- coding: utf-8 -*-
"""groupproject326.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F7OmgEXvENBsR4kVP7iUxJM80jp4R4-h
"""

#CLASSES
class student:
  def __init__(self, name, year, grades):
    """
    name expects string
    year expects int, should be what year student is in (1, 2, 3, 4)
    grades expects list of strings, contating all grades
    """
    self.name = name
    self.year = year
    self.grades = grades

class prof:
  def __init__(self, name , classes):
    """
    name expects string
    classes expects list of objects, containg every object class they teach
    """
    self.name = name
    self.classes = classes

class degree:
  def __init__(self, d_name, req_classes, undergrad):
    """
    d_name expects string, name of degree (Bachelor in Information Science)
    req_classes expects list of classes(c) objects
    undergrad expects a boolean true or false, used to indicate whether the degree is a undergrad degree or not
    """

    self.d_name = d_name
    self.req_classes = req_classes
    self.undergrad = undergrad

class c:
  def __init__(self, name, professor, students):
    """
    name expects String, following a specific format (INST326 instead of inst 326 or just programming)
    professor expects string, name of professor teaching the class
    students expects list of student objects 
    """
    self.name = name
    self.professor = professor
    self.students = students

#FUNCTIONS

def student_print(s):
  """
  prints student, primarly used for testing 
  """
  print(s.name + "\n" + str(s.year) + "\n" + str(s.grades))

def class_print():
  """
  insert code here to print class information out
  """

#MAIN

s1 = student("John Smith", 3, ['A', 'B', 'C'])
student_print(s1)