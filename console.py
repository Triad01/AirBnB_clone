#!/usr/bin/python3
"""our console"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing for empty line"""
        pass

if __name__ == '__main__':
    if not sys.stdin.isatty():
        # Read commands from standard input
        commands = sys.stdin.read().splitlines()
        HBNBCommand().onecmd('\n'.join(commands))
    else:
        HBNBCommand().cmdloop()
