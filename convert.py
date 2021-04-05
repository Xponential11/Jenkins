import xml.etree.ElementTree as ET
import xmltodict
import json
import csv
import pandas as pd 


tree = ET.parse('reports/xml_report/TEST-Test_Class-20210401111358.xml')
xml_data = tree.getroot()
#here you can change the encoding type to be able to set it to the one you need
xmlstr = ET.tostring(xml_data, encoding='utf-8', method='xml')

data_dict = dict(xmltodict.parse(xmlstr))
print(data_dict)

header = data_dict.keys()
no_rows = len(data_dict[list(header)[0]])

df = pd.DataFrame(data_dict).to_csv("output.csv")

