#!/usr/bin/python3
"""Console module"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class represents the console"""
    prompt = '(hbnb) '
    __classes = [
        "BaseModel"
    ]

    def do_create(self, arg):
        """Usage: create <class>
        Create command to create a new instance"""
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Usage: show <class> <id>
        Prints the string representation of an instance
        based on the class name and id"""
        cmd_args = arg.split(" ")
        if len(cmd_args) == 0:
            print("** class name missing **")
        elif cmd_args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(cmd_args) == 1:
            print("** instance id missing **")
        elif f"{cmd_args[0]}.{cmd_args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{cmd_args[0]}.{cmd_args[1]}"])

    def do_destroy(self, arg):
        """usage: destroy <class> <id>
        Deletes an instance based on the class name and id"""
        cmd_args = arg.split(" ")
        if len(cmd_args) == 0:
            print("** class name missing **")
        elif cmd_args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(cmd_args) == 1:
            print("** instance id missing **")
        elif f"{cmd_args[0]}.{cmd_args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[f"{cmd_args[0]}.{cmd_args[1]}"]
            storage.save()

    def do_all(self, arg):
        """Usage: all [class]
        Prints all string representation of all
        instances based or not on the class name"""
        cmd_args = arg.split(" ")
        storage_objects = storage.all()
        to_print = ""
        if len(cmd_args) == 0:
            for v in storage_objects.values():
                to_print += str(v) + "\n"
        elif cmd_args[0] not in HBNBCommand.__classes:
            to_print = "** class doesn't exist **\n"
        else:
            for v in storage_objects.values():
                if v.__class__.__name__ == cmd_args[0]:
                    to_print += str(v) + "\n"
        print(to_print, end="")

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value>
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        cmd_args = arg.split(" ")
        storage_objects = storage.all()

        if len(cmd_args) == 0:
            print("** class name missing **")
        elif cmd_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(cmd_args) == 1:
            print("** instance id missing **")
        elif f"{cmd_args[0]}.{cmd_args[1]}" not in storage.all():
            print("** no instance found **")
        elif len(cmd_args) == 2:
            print("** attribute name missing **")
        elif len(cmd_args) == 3:
            print("** value missing **")
        else:
            setattr(storage_objects[
                f"{cmd_args[0]}.{cmd_args[1]}"
                ],
                cmd_args[2], cmd_args[3])
            storage.save()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
