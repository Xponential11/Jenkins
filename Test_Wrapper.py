import unittest
import pytest
import subprocess
import os
import xmlrunner
import HtmlTestRunner





class Test_Class(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        @pytest.fixture()
        def tuple_data():
            return ('test',True,False,34,{'size':1024})

    def test_to_fail(tuple_data):
        assert tuple_data[4]['size'] == 1023 #Pass

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
        subprocess.Popen("python3 Exercise_6.py alice.txt",shell=True)

    def test_Google_Babynames(self):
        subprocess.Popen("python3 Exercise_babynames.py --summaryfile baby2008.html",shell=True)
        print("...............Google Test Completed................")

    def test_Commom_Utils(self):
        subprocess.Popen("python3 Exercise_Common_Utils.py config.ini",shell=True)
        print("...............Common Utils Test Completed................")

    # def test_Numpy_1(self):
    #     subprocess.Popen("python3 Exercise_numpy_1.py",shell=True)

    # def test_Numpy_2(self):
    #     subprocess.Popen("python3 Exercise_numpy_2.py",shell=True)

    # def test_Numpy_3(self):
    #     subprocess.Popen("python3 Exercise_numpy_3.py",shell=True)

    # def test_Numpy_4(self):
    #     subprocess.Popen("python3 numpy_masking_exercise.py",shell=True)
    #     print("...............Numpy Test Completed................")

    # def test_to_fail(tuple_data):
    #     assert tuple_data[4]['size'] == 1023 #Fail


    def test_Python_OOP(self):
        subprocess.Popen("python3 Exercise_runBabyName.py",shell=True)
        sum = 5+6
        assert sum == 10

        print("...............Python OOP Test Completed................")

    def test_Python_Pytest(self):
        subprocess.Popen("pytest -v Exercise_Pytest.py",shell=True)
        print("...............Pytest Test Completed................")

    @classmethod
    def tearDownClass(cls):
        subprocess.Popen("python3 csvgen.py",shell=True)
        


if __name__ == '__main__':
    html_report_dir = './html_report' 
    xml_report_dir = './reports/xml_report'  
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=html_report_dir))#,testRunner=xmlrunner.XMLTestRunner(output=xml_report_dir))
    #unittest.main(testRunner=xmlrunner.XMLTestRunner(output=xml_report_dir))
    unittest.main()
    
