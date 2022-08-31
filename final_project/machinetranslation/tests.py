import unittest
from translator import englishtofrench, frenchtoenglish
 
class testEnglish1(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishtofrench('Hello'),'Bonjour')
        return('frenchtranslation')
 
class testEnglish2(unittest.TestCase):
    def test2(self):
        self.assertNotEqual(englishtofrench('Hello'),'Bonjour')
        return()
 
class testFrench1(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchtoenglish('Bonjour'),'Hello')
        return('englishtranslation')
 
class testFrench2(unittest.TestCase):
   def test2(self):
        self.assertNotEqual(frenchtoenglish('Bonjour'),'Hello')  
        return()
 
unittest.main()
