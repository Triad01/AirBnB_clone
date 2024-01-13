#!/usr/bin/python3

""" This module contains the implementation of the interactive shell
    for the HBNB console - The command Interpreter.
"""
import cmd
from models.base_model import BaseModel
from models import storage
import sys


class HBNBCommand(cmd.Cmd):
    """
        This is the class definition for the HBNB interactive shell.
    """
    prompt = "(HBNB) "


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

    def do_create(self, line):
        """
        Creates a new insance of the base model, saves it and prints the id

        Args:
            line (str): The command line argument entered
        """
        if not line:
            print("** class name missing **")
        elif line not in storage.classes:
            print("** class name doesn't exist **")
        else:
            new_instance = storage.classes[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Prints string representation of an instance based on name and id

        Args:

            line (str): The command line argument entered
        """

        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        and saves the change into the JSON file

            Args:

            line (str): The command line argument entered
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]

if __name__ == '__main__':
    if not sys.stdin.isatty():
        # Read commands from standard input
        commands = sys.stdin.read().splitlines()
        HBNBCommand().onecmd('\n'.join(commands))
    else:
        HBNBCommand().cmdloop()
