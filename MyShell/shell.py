#!/usr/bin/python3

import cmd

"""
create my own command interpreter
"""

class MyShell(cmd.Cmd):
    intro = "Welcome to MyShell. Type help or ? to list commands.\n"
    prompt = "(@>) "

    def do_greet(self, line):
        if name:
            print(f"Hello, {name}!")
        else:
            print("Hello!")


    def do_EOF(self, line):
        print()
        return True     
    

if __name__ == "__main__":
    MyShell().cmdloop()
