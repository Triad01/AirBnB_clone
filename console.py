#!/usr/bin/python3

""" This module contains the implementation of the interactive shell
    for the HBNB console - The command Interpreter.
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
        This is the class definition for the HBNB interactive shell.
    """
    prompt = "(hbnb) "

    """Basic commands (CRUD) For interpreter"""
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
        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """
            Prints all the string representation of all
            instances based or not on the class name
        """
        args = line.split()
        if not args:
            print([str(obj) for obj in storage.all().values()])
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        else:
            filtered_objects = []
            for obj in storage.all().values():
                if obj.__class__.__name__ == args[0]:
                    filtered_objects.append(str(obj))
            print(filtered_objects)

    def do_update(self, line):
        """
            Updates an instance based on the class name
            and id by adding or updating attribute
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
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value_str = args[3]

        # Convert attribute value to the correct type based on the attribute
        attribute_value = None
        try:
            attribute_value = eval(attribute_value_str)
        except Exception as e:
            print("** value missing **")
            return

        setattr(storage.all()[key], attribute_name, attribute_value)
        storage.save()

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

    def do_help(self, line_arg: str) -> bool | None:
        """This class metod handles the implementations of the Help
            command.
            Attributes:
                line_arg (str): this represents the line argument of which
                       the command is to be executed by the shell console.
        """
        return super().do_help(line_arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
