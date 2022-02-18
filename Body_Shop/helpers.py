from canvas import canvas
from re import match
from json import loads, dumps
import os


def clear_view():
    for slave in canvas.grid_slaves():
        slave.destroy()


def back_to_main_view():
    from authentication import render_main_view
    clear_view()
    render_main_view()


def fix_data():
    """
    removes the additional '}' at the end of my data file
    :return: nothing
    """
    with open(os.path.join('db', "products_list.txt"), "r+") as file:
        txt = file.readlines()

    with open(os.path.join('db', "products_list.txt"), "w") as file:
        for idx, line in enumerate(txt):
            line = loads(line[:-1])
            if not idx == len(txt) - 1:
                file.write(dumps(line) + "\n")
            else:
                file.write(dumps(line))
