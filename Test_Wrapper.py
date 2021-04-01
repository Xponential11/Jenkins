import unittest
import pytest
import subprocess
import os

class Test_Class(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        @pytest.fixture()
        def tuple_data():
            return ('test',True,False,34,{'size':1024})

    def test_Google_Exercise_1(self):
        subprocess.Popen("python3 Exercise_1.py",shell=True)
    
    def test_Google_Exercise_2(self):
        subprocess.Popen("python3 Exercise_2.py",shell=True)

    def test_Google_Exercise_3(self):
        subprocess.Popen("python3 Exercise_3.py",shell=True)
    
    def test_Google_Exercise_4(self):
        subprocess.Popen("python3 Exercise_4.py",shell=True)

    def test_Google_Exercise_5(self):
        subprocess.Popen("python3 Exercise_5.py",shell=True)

    def test_Google_Exercise_6(self):
        subprocess.Popen("python3 Exercise_6.py",shell=True)

    def test_Google_Babynames(self):
        subprocess.Popen("python3 Exercise_babynames.py",shell=True)
        print("...............Google Test Completed................")

    def test_Commom_Utils(self):
        subprocess.Popen("python3 Exercise_Commom_Utils.py config.ini",shell=True)
        print("...............Common Utils Test Completed................")

    def test_Numpy_1(self):
        subprocess.Popen("python3 Exercise_numpy_1.py",shell=True)

    def test_Numpy_2(self):
        subprocess.Popen("python3 Exercise_numpy_2.py",shell=True)

    def test_Numpy_3(self):
        subprocess.Popen("python3 Exercise_numpy_3.py",shell=True)

    def test_Numpy_4(self):
        subprocess.Popen("python3 numpy_masking_exercise.py",shell=True)
        print("...............Numpy Test Completed................")

    def test_Python_OOP(self):
        subprocess.Popen("python3 Exercise_runBabyName.py",shell=True)
        print("...............Python OOP Test Completed................")

    def test_Python_Pytest(self):
        subprocess.Popen("python3 pytest -v Exercise_Pytest.py",shell=True)
        print("...............Pytest Test Completed................")

    @classmethod
    def tearDownClass(cls):
        print("...............Test Completed................")

if __name__ == "__main__":
    unittest.main()