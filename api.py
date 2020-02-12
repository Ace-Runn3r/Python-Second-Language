# Author: Cole Clements, cclements2016@my.fit.edu
# Course: CSE 2050, Fall 2018
# Project: Schedule Api

from sys import (stdin, stdout)
from urllib.request import urlopen
from json import loads
from re import (compile, match)

def output(classData):
    for item in classData:
        crn = item.get("crn")
        subject = item.get("subject")
        course_number = item.get("course_number")
        section = item.get("section")
        days = item.get("days")
        begin_time = item.get("begin_time")
        end_time = item.get("end_time")
        instructor = item.get("instructor")
        stdout.write("{} {} {} {} {} {} {} {}\n".format(
            crn, subject, course_number, section, days,
            begin_time, end_time, instructor))
    stdout.write("\n")

url = urlopen("http://api.fit.edu/courses/v1/courses?term=spring")
data = loads(url.read().decode())

for line in stdin:
    classMatch = data["records"]
    keyRegList = []

    arguments = line.split()
    keyRegList = [arg.split('=') for arg in arguments]

    for i in range(0,len(keyRegList)):
        key = keyRegList[i][0]
        reg = keyRegList[i][1]
        classMatch = [item for item in classMatch 
                        if match(reg, str(item.get(key)))]

    if len(classMatch) is 0:
        stdout.write("NO MATCHING RECORDS\n\n")
    else:
        output(classMatch)
