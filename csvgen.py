import csv
import xml.etree.ElementTree as ET 
import pandas as pd 




def parseXML(xmlfile):

    #creating ET object
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    temp = ""
    testresultitems = {}
    for tag in root.findall('testcase'):
        if(tag.getchildren()):
            child = tag.getchildren()
            for i in child:
                temp = str("FAIL," + i.get('type')) + ":" + str(i.get('message'))
        else:
            temp = str("PASS")
        
        testresultitems[str(tag.get('name'))] = str(tag.get('time')) + "," + temp 
        temp = ""
    #print(testresults)
    print(testresultitems)
    return testresultitems
    #print(testresultitems)

def savetocsv(testresultitems,filename):
    sr = 1
    with open(filename,'w') as csvfile:
        csvfile.write("SrNO, TestCase, Time, Status, Remark/Message\n")
        for e in testresultitems.keys():
            csvfile.write("%d, %s,%s\n"%(sr, e, testresultitems[e]))
            sr += 1
   


def main():

    testresultitems = parseXML(r'reports/xml_report/TEST-Test_Class-20210405104304.xml')
    savetocsv(testresultitems,'Test_Results.csv')
    a = pd.read_csv("Test_Results.csv")
    a.to_html("./html_report/Table_Report.html",index=False)
    html_file = a.to_html()


if __name__ == "__main__":
    main()
