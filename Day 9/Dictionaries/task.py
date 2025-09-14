programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary["Bug"])

#print(programming_dictionary["Function"])

programming_dictionary ["Loop"] = "The action of code that repeates again and again"

#print(programming_dictionary)
#print(programming_dictionary["Loop"])

#wipe existing dictionary
#empty_dictionary = {}
#programming_dictionary = {}

#print(programming_dictionary)


#edit dictionary

programming_dictionary ["Bug"] = "A moth in computer"
#print(programming_dictionary ["Bug"])


# loop through dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])