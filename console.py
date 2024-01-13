#!/usr/bin/python3
"""Our console"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handle the End-Of-File condition"""
        print("")  # Print a newline for a cleaner output
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
