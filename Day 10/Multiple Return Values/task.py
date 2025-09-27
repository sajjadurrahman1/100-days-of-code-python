def format_name(f_name, l_name):
    """here the purpose of the code will be taking the forst input and will provide the title case output"""
    formated_f_name= f_name. title()
    formated_l_name= l_name. title()
    return formated_f_name , formated_l_name
formated_name= format_name(input("enter your first name"), input("enter your last name"))
print (formated_name)