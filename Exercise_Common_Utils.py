from configparser import ConfigParser
import argparse
import subprocess
import re
import xml.etree.ElementTree as et
import csv
import time
csv_columns = ['testcase','Results']
mapper = {}

def getaccess(filename):
    global url
    global password
    global ip 
    config = ConfigParser()
    config.read(filename)
    url = config.get('required','url')
    password = config.get('required','password')
    ip = config.get('required','ip')

    return url , password

def createXML(XMLFileName):
    system_out = 0
    error = 0
    temp = ""
    global mapper
    txtFile = open("log.txt","r")
    content = txtFile.read()
    first_index = content.find("Diagnostics Test Summary")
    contents = content[first_index:]
    last_index = contents.find("Press Enter")
    content = contents[:last_index]
    f = open("log-text.txt","w+")
    f.write(str(content))
    f.close()
    f2 = open("selected-log-text.txt", "w+")
    f = open("log-text.txt","r")
    cont = f.readlines()
    f.close()
    for num, line in enumerate(cont, 1):
        if "Total run count" in line:
            match = re.search(r" \d+", line)
            if int(match.group()) > 0:
                num = num - 6
                for j in range(num, num+16):
                    if cont[j].find("PASS") != -1:
                        system_out = system_out + 1
                        x = cont[j-11].lstrip(" 0123456789)")
                        mapper[x] = "PASS"
                    elif cont[j].find("FAIL") != -1:
                        error = error + 1
                        x = cont[j-11].lstrip(" 0123456789)")
                        mapper[x] = "FAIL"
                    content2 = cont[j]
                    f2.write(content2)
  
    print(mapper)
    root = et.Element('testsuites')
    a = et.Element('testsuite', {"errors": str(error), "name":"TestResults","tests":str(system_out)})
    root.append(a)
    for num, line in enumerate(cont, 1):
        for i,j in mapper.items():
            if i in line: 
                temp = ""
                if j == "PASS":
                    b = et.Element('testcase', {"name": str(i)})
                    root.append(b)
                    c = et.SubElement(b, 'system-out')
                    for j in range(num, num+6):
                        temp = temp + cont[j]
                    c.text = str(temp)
                elif j == "FAIL":
                    b = et.Element('testcase', {"name": str(i)})
                    root.append(b)
                    c = et.SubElement(b, 'error')
                    for j in range(num, num+6):
                        temp = temp + cont[j]
                    c.text = str(temp)
    tree = et.ElementTree(root)
    with open(XMLFileName, 'wb') as files:
        tree.write(files)


    mapper = dict(map(str.strip, x) for x in mapper.items())        

        
def WriteDictToCSV(csv_file,csv_columns,dict_data):
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for key in dict_data.keys():
            csvfile.write("%s,%s\n"%(key, dict_data[key]))
 
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("filename",help="Enter config file.")
    args = parser.parse_args()

    getaccess(args.filename)
    
    command = 'scp ' + url + ' log.txt'
    subprocess.Popen(command,shell=True)
    time.sleep(5)

      
                
    createXML('TestResults.xml')


    WriteDictToCSV('TestResults.csv',csv_columns,mapper)





     

    
        




