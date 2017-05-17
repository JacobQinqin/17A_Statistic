#!/usr/bin/env python
import os
import sys
import xml.etree.ElementTree as ET

full_file = os.path.abspath(sys.argv[1])

tree = ET.parse(full_file).getroot()
measData = tree.getchildren()[1]
GxMeasurement = None
RxMeasurement = None
GlobalMeasurement = measData.getchildren()[2]
try:
    GxMeasurement = measData.getchildren()[3]
except IndexError:
    print "No Gx Measurements for this file"
try:
    RxMeasurement = measData.getchildren()[4]
except IndexError:
    print "No Rx Measurements for this file"
  
print "#####GlobalMeasurment#####"
for i in GlobalMeasurement.iter():
    if i.tag == "{http://www.3gpp.org/ftp/specs/archive/32_series/32.435#measCollec}r":
        if i.attrib == {'p': '1'}:
            print "afActiveSessions=" + i.text
        if i.attrib == {'p': '2'}:
            print "fixedActiveSessions=" + i.text
        if i.attrib == {'p': '3'}:
            print "mobileActiveSessions=" + i.text 
        if i.attrib == {'p': '4'}:
            print "subscribers=" + i.text 

if GxMeasurement <> None:    
    print ""    
    print "#####GxMeasurment#####"
    typelist = []
    for i in GxMeasurement.iter():
        if i.tag == "{http://www.3gpp.org/ftp/specs/archive/32_series/32.435#measCollec}measType":
            temptype = str(i.attrib).replace("{'", "").replace("': '", "").replace("'}", ""), i.text
            typelist.append(temptype)
    
    plist = []
    for i in GxMeasurement.iter():
        if i.tag == "{http://www.3gpp.org/ftp/specs/archive/32_series/32.435#measCollec}r":
            listp = str(i.attrib).replace("{'", "").replace("': '", "").replace("'}", ""), i.text
            plist.append(listp)    
              
    final_result = []
    for index, item in typelist:
		count = 0
		for j, k in plist:
			if j == index:
				count = count + int(k)
		result_index = index, str(count)
		final_result.append(result_index)
    
    for i_type, i_value in typelist:
        for x, y in final_result:
            if x == i_type:
                print i_value + ":" + str(y)

if RxMeasurement <> None:
    print ""         
    print "#####RxMeasurment#####"
    typelist = []
    for i in RxMeasurement.iter():
        if i.tag == "{http://www.3gpp.org/ftp/specs/archive/32_series/32.435#measCollec}measType":
            temptype = str(i.attrib).replace("{'", "").replace("': '", "").replace("'}", ""), i.text
            typelist.append(temptype)
    
    plist = []
    for i in RxMeasurement.iter():
        if i.tag == "{http://www.3gpp.org/ftp/specs/archive/32_series/32.435#measCollec}r":
            listp = str(i.attrib).replace("{'", "").replace("': '", "").replace("'}", ""), i.text
            plist.append(listp)
    
    
    final_result = []
    for index, item in typelist:
		count = 0
		for j, k in plist:
			if j == index:
				count = count + int(k)
		result_index = index, str(count)
		final_result.append(result_index)
    
    for i_type, i_value in typelist:
        for x, y in final_result:
            if x == i_type:
                print i_value + ":" + str(y)
         