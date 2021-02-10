
#Write a failing test first
#Then make the test pass
#Then refactor original code
#Etc 

import unittest

class TestClass(unittest.TestCase):

    #this will auto-run before every test
    def setUp(self):
        self.test_object = ClassToTest()
   
    def test_name_of_original_function(self):
        test_object.original_function()
        self.assertEqual(quality, test_object.quality)

    #runs after each test, could be used to print/pipe/delete any results
    #code coverage = code under test
    
    def tearDown(self):
        print('test is done')
unittest.main()

