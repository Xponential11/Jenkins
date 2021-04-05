import sys
from myTestCase import myTestCase
import babynamesmodified


class testBabyName(myTestCase):
    def __init__(self,html,summary):
        self.data = html
        self.summary = summary

    # def checkFile(self):
    #     self.check = self.data.readlines()
    #     if self.check:
    #         pass
    #     else:
    #         print("HTML file is empty")
    #         sys.exit()

    def setup(self):
        with open(self.summary) as f:
            print(f.readlines()) 

    def run(self):
        # checkFile(self)
        babynamesmodified.main(self.data)

    def checkoutput(self,summaryfile):
        with open(self.summary) as f:
            self.summary_content = f.readlines()
        with open(summaryfile) as f:
            self.summaryfile_content = f.readlines()
        if self.summary_content == self.summaryfile_content:
            self.result = True
        else:
            self.result = False
    def teardown(self):
        print(self.result)
    
