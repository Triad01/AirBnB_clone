#!/usr/bin/python3

""" This module contains the implementation of the interactive shell
    for the HBNB console.
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
        This is the class definition for the HBNB interactive shell.
    """


    prompt = "(hbnb)"

    def do_quit(self, line):
        """This class method handles the implementation of qutting the shell
            line (str): this represents the command entered on the shell
        """

        return True

    def emptyline(self):
        """ This class method handles the implementation if user does
            not enter a command.
        """

        pass

    def do_EOF(self, line):
        """ This class method handles the implementation of End-Of-File
            condition.
        Attributes:
            line (str): this represents the command entered on the shell
        """

        return True
    
    # this metod is to be updated and documented later.
    def do_help(self, line_arg: str) -> bool | None:
        """ This class metod handles the implementations of the Help
            command.

            Attributes:
                line_arg (str): this represents the line argument of which
                the command is to be executed by the shell console.
        """
        return super().do_help(line_arg)
    

if __name__ == "__main__":
    HBNBCommand().cmdloop()