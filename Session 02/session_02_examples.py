"""
In this file you will find general and basic examples of topics learned in session 02.
You can see the session recording here: https://drive.google.com/file/d/1Ss6PnwFjpxtBHK4rDZF6fJdRQtyQxWsl/view
"""


class GeneralExample:
    session_name = "Python Fundamentals 02"

    def __init__(self):
        self.level = 2
        self.day = "Tuesday"

    def string_example(self, msg):
        print("================= STRING EXAMPLE =================")

        print("'{}'".format(msg))
        print('\"{}\"'.format(msg))

        repeated_msg = 4 * msg
        print("Repeated message = ", repeated_msg)
        print("First letter of message = ", repeated_msg[0])
        print("Last letter of message = ", repeated_msg[-1])
        print("Part of message 1:3= ", repeated_msg[1:3])
        print("First part of message :4 = ", repeated_msg[:4])
        print("Last part of message 2: = ", repeated_msg[2:])
        print("Capitalize message:", repeated_msg.capitalize())
        print("Upper Message:", repeated_msg.upper())

    def number_example(self, num1, num2):
        division = num1 / num2

        int_division = num1 // num2

        mod = num1 % num2

        pow = num1 ** num2

        print("================= NUMBER EXAMPLE =================")

        print("Division result = ", division)
        print("Int Division result = ", int_division)
        print("Mod result = ", mod)
        print("Pow result = ", pow)

    def list_example(self, values):
        new_list = ["welcome", "to", "python"] + values

        print("================= LIST EXAMPLE =================")
        print("New list = ", new_list)
        print("Last element of list = ", new_list[-1])
        print("Range of element of list from 1:3 = ", new_list[1:3])
        print("New list [:] = ", new_list[:])

        new_list[2:4] = ["class", "people"]
        print("New list (replace) = ", new_list)

        new_list.append(80)
        print("New list (append)= ", new_list)

        new_list.reverse()

        print("Reversed list = ", new_list)

    def args_example(self, msj, *args, **kwargs):
        print("================= ARGS EXAMPLE =================")
        print("What is my message? ", msj)
        30 * "="
        print("Did I receive *args?, let's take a look at them")
        print(args)

        30 * "="
        print("Did I receive **kwarg?, let's take a look at them")
        print(kwargs)

        print("Show me kwargs keys: ", kwargs.keys())


my_example = GeneralExample()

# my_example.string_example("Python is great!")
# my_example.number_example(10, 3)
# my_example.list_example([1, 2, 3, 4, 5])
#
my_example.args_example("Do you like Python?",
                        "yes", "I", "love", "it", "aed",
                        why="it's easy", version=3.7, hello=123)
