def format_name(f_name, l_name):
    return f_name.title() + " "+l_name.title()



print(format_name("aastha","yuLi"))
print(format_name("AASTHA", "yuLI"))

formated_name = format_name("aastha", "yuli")
print(formated_name)

def function1(text):
    return text+text

def function2(text):
    return text.title()


print(function2(function1("hello")))