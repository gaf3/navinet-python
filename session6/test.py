import unittest

import tally

import shutil
import os

class TestTally(unittest.TestCase):

    def wipe(self):
        if os.path.isdir("unittest_data"):
            shutil.rmtree("unittest_data")

    def setUp(self):
        self.wipe()
        os.makedirs("unittest_data")

    def tearDown(self):
        self.wipe()
        
    def test_tally_file(self):

        file_name = os.path.join("unittest_data","test.txt")

        file = open(file_name,"wb")

        file.write("1\n")
        file.write("2\n")
        file.write("3\n")

        file.close()

        self.assertEqual(tally.tally_file(file_name),6.0)


    def test_tally_directory(self):

        file = open(os.path.join("unittest_data","1.txt"),"wb")

        file.write("1\n")
        file.write("2\n")
        file.write("3\n")

        file.close()

        file = open(os.path.join("unittest_data","2.txt"),"wb")

        file.write("1\n")
        file.write("2\n")

        file.close()

        self.assertEqual(tally.tally_directory("unittest_data"),9.0)

        os.makedirs(os.path.join("unittest_data","dir1"))

        file = open(os.path.join("unittest_data","dir1","1.txt"),"wb")

        file.write("1\n")

        file.close()

        self.assertEqual(tally.tally_directory("unittest_data"),10.0)

if __name__ == '__main__':
    unittest.main()
