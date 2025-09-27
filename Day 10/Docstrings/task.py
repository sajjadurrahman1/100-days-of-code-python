def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
"""with this function we have used return statement and print the output of the function 
 similiarly we have also tried that docstring is allowed to commit write comment with threeee commas """


formatted_name = format_name("sajjadur", "rahman")
length = len(formatted_name)
print(formatted_name)
print(length)



