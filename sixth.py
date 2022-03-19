def shut_down(s):
    if s == 'yes':
        return "Shutting down"
    elif s == 'No':
        return "Shutdown aborted"
    else:
        return "Sorry"


argument_of_function = "No"
storing_function_in_variable = shut_down
output = storing_function_in_variable(argument_of_function)
print(output)

