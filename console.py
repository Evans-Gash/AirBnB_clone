#!/usr/bin/python3

import cmd
from shlex import split
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

def arguments_parser(args):
    curly = re.search(r"\{(.*?)\}", args)
    square = re.search(r"\[(.*?)\]", args)
    
    if not curly:
        if not square:
            return [item.strip(",") for item in split(args)]
        else:
            parsed = split(args[:square.span()[0]])
            ret_values = [item.strip(",") for item in parsed]
            ret_values.append(square.group())
            return ret_values
    else:
        parsed = split(args[:curly.span()[0]])
        ret_values = [item.strip(",") for item in parsed]
        ret_values.append(curly.group())
        return ret_values


class CustomConsole(cmd.Cmd):
    prompt = "(hbnb) "
    SUPPORTED_CLASSES = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        pass

    def default(self, args):
        functions_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        found = re.search(r"\.", args)
        if found:
            split_args = [args[:found.span()[0]], args[found.span()[1]:]]
            found = re.search(r"\((.*?)\)", split_args[1])
            if found:
                command = [split_args[1][:found.span()[0]], found.group()[1:-1]]
                if command[0] in functions_dict:
                    formatted = "{} {}".format(split_args[0], command[1])
                    return functions_dict[command[0]](formatted)
        print("*** Unknown syntax: {}".format(args))
        return False

    # ... [Other functions go here with modified variable names and possibly restructured code]

    def do_create(self, args):
        parsed_args = arguments_parser(args)
        if not parsed_args:
            print("** class name missing **")
        elif parsed_args[0] not in CustomConsole.SUPPORTED_CLASSES:
            print("** class doesn't exist **")
        else:
            print(eval(parsed_args[0])().id)
            storage.save()

    # ... [Rest of the code remains but with potential variable renaming and slight restructuring]

if __name__ == "__main__":
    CustomConsole().cmdloop()
