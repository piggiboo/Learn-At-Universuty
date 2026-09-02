StudentTest = {
    "Peter": {
    "Age": 40,
    "Gender" : "Male",
    "Test" : {
        "First" : 20,
        "Second" : 18,
        "Third" : 19
    }
},


"Paul" : {
    "Age" : 25,
    "Gender" : "Male",
    "Test" : {
        "First" : 19,
        "Second" : 20,
         "Third" : 19
        }
},

"Mary" : {
    "Age" : 18,
    "Gender" : "Female",
    "Test" : {
        "First" : 10,
        "Second" : 5,
        "Third" : 4
        }
},
 "Jenny" : {
    "Age" : 60,
    "Gender" : "Female",
    "Test" : {
        "First" : 5,
        "Second" : 3,
        "Third" : 1
        }
}
}

StudentTest ["Robert"] = {
    "Age" : 30,
    "Gender" : "Male",
    "Test" : {
        "First" : 10,
        "Second" : 18,
        "Third" : 5
        }
}


print (f'''"Peter" is {StudentTest["Peter"]["Gender"]}''')
print (f'''The 1st test score of "Jenny" is {StudentTest["Jenny"]["Test"]["First"]}''')
print (f'''The 2nd test score of "Jenny" is {StudentTest["Jenny"]["Test"]["Second"]}''')
print (f'''The 3rd test score of "Paul" is {StudentTest["Paul"]["Test"]["Third"]}''')
print (f'''"Robert" is {StudentTest["Robert"]["Gender"]}''')
print (f"The dictionary to solve this problem was designed as:{StudentTest}")