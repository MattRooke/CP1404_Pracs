user_names = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
              'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_login = input("Enter your user name:")
if user_login in user_names:
    print("Access granted.")
else:
    print("Access denied!")
