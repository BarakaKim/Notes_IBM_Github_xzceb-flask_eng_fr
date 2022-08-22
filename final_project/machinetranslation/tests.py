""" unit tests for translator"""
import unittest
#from translator.py import englishToFrench, frenchToEnglish
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour") # test for E to F
        self.assertEqual(english_to_french(""),"Null input") # test for null input


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello") # test for F to E
        self.assertEqual(french_to_english(""),"Null input") # test for null input

unittest.main()