import unittest
import subprocess
import os
import pytest



class Test_all(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        @pytest.fixture(scope='session')
        def tuple_data():
            return ('test',True,False,34,{'size':1024})


    def test_google_course_1(self):
        subprocess.Popen("python3 Exercise_1.py",shell=True)
    def test_google_course_2(self):
        subprocess.Popen("python3 Exercise_2.py",shell=True)
    def test_google_course_3(self):
        subprocess.Popen("python3 Exercise_3.py",shell=True)
    def test_google_course_4(self):
        subprocess.Popen("python3 Exercise_4.py",shell=True)
    def test_google_course_5(self):
        subprocess.Popen("python3 Exercise_5.py",shell=True)
    def test_google_course_6(self):
        subprocess.Popen("python3 Exercise_6.py",shell=True)
    def test_google_course_7(self):
        subprocess.Popen("python3 babynames.py --summaryfile baby2008.html",shell=True)

    # def test_commom_utils(self):
    #     subprocess.Popen("python3 Task_Python_Commom_utils.py config.ini",shell=True)

    def test_OOP(self):
        subprocess.Popen("python3 runBabyNam.py",shell=True)
        sum = 5+6
        assert sum == 10

    def test_pytestFramework(self):
        subprocess.Popen("pytest -v test_fixture.py",shell=True)

    def test_Numpy(self):
        subprocess.Popen("python3 num_1.py",shell=True)
        subprocess.Popen("python3 num_2.py",shell=True)
        # subprocess.Popen("python3 num_3.py",shell=True)
        subprocess.Popen("python3 numpy_masking_exercise.py",shell=True)
    
    def test_to_fail(tuple_data):
        assert tuple_data[4]['size'] == 1023 #Fail

    @classmethod
    def tearDownClass(cls):
        print("Test Complete")


if __name__ == '__main__':
    unittest.main()
