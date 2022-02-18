import os
from json import loads, dumps
from tkinter import *

from PIL import Image, ImageTk

from canvas import canvas
from helpers import clear_view, back_to_main_view, fix_data

ROW_SIZE = 6


def render_products_view(username):
    canvas.title("Products")
    clear_view()

    with open(os.path.join("db", "products_list.txt")) as file:
        txt = file.readlines()

    curr_row = curr_col = 0

    for idx, line in enumerate(txt):

        if idx % ROW_SIZE == 0 and not idx == 0:
            curr_row += 4
            curr_col = 0

        line = loads(line)

        Label(canvas, text=f"{line.get('name')}").grid(row=curr_row, column=curr_col)
        render_photos(curr_row + 1, curr_col, line)
        Label(canvas, text=f"{line.get('quantity')}").grid(row=curr_row + 2, column=curr_col)

        if line.get('quantity') > 0:
            Button(canvas, text="buy", command=lambda product_id=line.get('id'): on_click_buy(username, product_id)).grid(row=curr_row + 3, column=curr_col)
        else:
            Label(canvas, text="Sold Out", fg="Red").grid(row=curr_row + 3, column=curr_col)

        curr_col += 1
    Button(canvas, text="Back", command=back_to_main_view).grid(row=curr_row + 5, column=ROW_SIZE - 1, pady=20)


def render_photos(row_idx, column_idx, line):
    my_image = Image.open(os.path.join("pics", line.get('img_path')))
    my_image = my_image.resize((50, 50))
    render = ImageTk.PhotoImage(my_image)
    img = Label(canvas, image=render)
    img.image = render
    img.grid(row=row_idx, column=column_idx)


def on_click_buy(username, product_id):
    update_users(username, product_id)
    update_quantity(username, product_id)


def update_users(username, product_id):
    with open(os.path.join('db', "users.txt"), "r+") as file:
        data = file.readlines()
        file.seek(0)
        for line in data:
            line = loads(line[:-1])
            if username == line.get("username"):
                if not line.get('products'):
                    line['products'] = []
                line['products'].append(product_id)
            file.write(dumps(line) + "\n")
    #
    # render_products_view(username)


def update_quantity(username, product_id):  # TODO still have to think about this
    with open(os.path.join('db', "products_list.txt"), "r+") as file:
        products = file.readlines()
        file.seek(0)

        for idx, line in enumerate(products):
            curr_product = loads(line)
            if curr_product['id'] == product_id and curr_product['quantity'] > 0:
                curr_product['quantity'] -= 1

            if not idx == len(products) - 1:
                file.write(dumps(curr_product) + "\n")
            else:
                file.write(dumps(curr_product))
        ################################################# TODO: that's just a workaround, need to figure out why json adds '}' at the end of my file.
        file.seek(0)
        products = file.read()
        if products[-1] == products[-2]:
            fix_data()
        ################################################
    render_products_view(username)


