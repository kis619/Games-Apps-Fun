import os
from json import dumps
from tkinter import *

from authentication_checks import checking_password_policies, username_is_valid, user_already_exists
from authentication_checks import user_name_matches_password
from canvas import canvas
from helpers import clear_view, back_to_main_view
from products import render_products_view


def render_main_view():
    canvas.title("Product shop")
    Button(canvas, text="Login", bg="pink", fg="red",
           command=render_login_view).grid(row=0, column=0, pady=15, padx=15)
    Button(canvas, text="Register", bg="yellow", fg="green",
           command=render_register_view).grid(row=0, column=2, pady=15, padx=15)


def render_login_view(error=None):
    clear_view()
    canvas.title("Login")
    Label(canvas, text="Username").grid(row=0, column=0, pady=15, padx=15)
    Label(canvas, text="Password").grid(row=1, column=0, padx=15)

    username = Entry(canvas)
    password = Entry(canvas, show="*")
    username.grid(row=0, column=1, pady=15, padx=15)
    password.grid(row=1, column=1, padx=15)

    Button(canvas,
           text="Login",
           bg="light green",
           command=lambda: login(username=username.get(), password=password.get())
           ).grid(row=2, column=1)
    Button(canvas,
           text="Back",
           bg="cyan",
           command=back_to_main_view).grid(row=3, column=1, pady=5)

    if error:
        Label(canvas, text="Wrong username or password", fg="Red").grid(row=4, column=1, pady=5)


def func(event):
    print("You hit return.")


canvas.bind('<Return>', func)


def login(**user_data):
    username = user_data.get("username")
    password = user_data.get("password")
    with open(os.path.join("db", "user_credentials_db.txt")) as file:
        text = file.readlines()

    if user_name_matches_password(username, password, text):
        render_products_view(username)

    else:
        render_login_view(error=True)


def render_register_view(error=None, bad_password=None, bad_username=None):
    clear_view()
    canvas.title("Registration page")
    labels_entries = [
        ((Label(canvas, text="Username")), ("username", Entry(canvas))),
        ((Label(canvas, text="Password")), ("password", Entry(canvas, show="*"))),
        ((Label(canvas, text="First_name")), ("first_name", Entry(canvas))),
        ((Label(canvas, text="Last_name")), ("last_name", Entry(canvas)))
    ]

    for idx, ((label_widget), (entry_widget)) in enumerate(labels_entries):
        label_widget.grid(row=idx, column=0, padx=15)
        entry_widget[1].grid(row=idx, column=1, padx=40)
    # Label(canvas, text="Username").grid(row=0, column=0, padx=15)
    # Label(canvas, text="Password").grid(row=1, column=0, padx=15)
    # Label(canvas, text="First_name").grid(row=2, column=0, padx=15)
    # Label(canvas, text="Last_name").grid(row=3, column=0, padx=15)

    # username = Entry(canvas)
    # password = Entry(canvas)
    # first_name = Entry(canvas)
    # last_name = Entry(canvas)
    # username.grid(row=0, column=1, padx=15)
    # password.grid(row=1, column=1, padx=15)
    # first_name.grid(row=2, column=1, padx=15)
    # last_name.grid(row=3, column=1, padx=15)

    Button(canvas,
           text="Register",
           bg="light green",
           command=lambda: register({user_info: widget.get() for label, (user_info, widget) in labels_entries})
           ).grid(row=(len(labels_entries) + 1), column=1)
    Button(canvas,
           text="Back",
           bg="cyan",
           command=back_to_main_view
           ).grid(row=(len(labels_entries) + 2), column=1, pady=5)

    if error:
        Label(canvas, text="The user name already exists.", fg="Red").grid(row=(len(labels_entries) + 4), column=1,
                                                                           pady=5)

    if bad_username:
        Label(canvas, text=bad_username, fg="Red").grid(row=(len(labels_entries) + 4), column=1, pady=5)

    if bad_password:
        Label(canvas, text=bad_password, fg="Red").grid(row=(len(labels_entries) + 4), column=1, pady=5)


def register(user_data: dict):
    username = user_data.get("username")
    password = user_data.get("password")
    with open(os.path.join("db", "user_credentials_db.txt")) as file:
        text = file.readlines()

    if user_already_exists(username, text):
        return render_register_view(error=True)

    if not username_is_valid(username):
        error = "The username does not meet the username criteria."  # TODO create add a little questionmark widget where the policies are listed and show which policy is not met
        return render_register_view(bad_username=error)

    error = checking_password_policies(password)
    if error:  # TODO add a little question mark widget where the policies are listed
        return render_register_view(bad_password=error)
    run_all_authentication_checks(username, password, text)

    with open(os.path.join("db", "users.txt"), "a") as file:
        new_info = dumps(user_data)
        file.write(new_info + "\n")

    with open(os.path.join("db", "user_credentials_db.txt"), "a") as file:
        del user_data["last_name"]
        del user_data["first_name"]
        new_info = dumps(user_data)
        file.write(new_info + "\n")
        render_login_view()


def run_all_authentication_checks(username, password, text):  # TODO does not work
    if user_already_exists(username, text):
        return render_register_view(error=True)

    if not username_is_valid(username):
        error = "The username does not meet the username criteria."  # TODO create add a little questionmark widget where the policies are listed and show which policy is not met
        return render_register_view(bad_username=error)

    error = checking_password_policies(password)
    if error:  # TODO add a little questionmark widget where the policies are listed
        return render_register_view(bad_password=error)
