#Author - Gundeep Vohra

import json
from builtins import print
import ast

# read file
file = open('test_results.json').read()
# convert in list    
data = json.loads(file)
# print data  
for i in data['test_suites']:  # traverse at first level
    pass_counter = 0
    fail_counter = 0
    blocked_counter = 0
    time_counter = 0
    
    print("Suite Name: ", i['suite_name'])
    print("-------------------------")
    
    for j in i['results']:  # traverse at second level
        if j['status'] == "pass":
            print ("Test Name : ", j['test_name'])
            print ("Test Time : ", j['time'])
            print ("Test Status : ", j['status'])
            print()
            pass_counter = pass_counter + 1
        
        if j['status'] == "fail":
            print ("Test Name : ", j['test_name'])
            print ("Test Time : ", j['time'])
            print ("Test Status : ", j['status'])
            print()
            fail_counter = fail_counter + 1
            
        if j['status'] == "blocked":
            blocked_counter = blocked_counter + 1
            
        try:    
            if ast.literal_eval(j['time']) > 10:  # convert string value into something numeric that can be compared
                time_counter = time_counter + 1
        except (SyntaxError, ValueError) as e:  # catching multiple exceptions that can arise
            pass
        
    print("#####################")        
    print("Total tests passed: ", pass_counter)
    print("Total tests failed: ", fail_counter)
    print("Total tests blocked: ", blocked_counter)
    print("Total tests that took more than 10 secs to execute: ", time_counter)
    print()    
