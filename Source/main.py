import os
import dotenv
import datetime
import psycopg2 as psql
import colorama as colour

import help

colour.init()
dotenv.load_dotenv()
CONFIG = dotenv.dotenv_values(".env")

os.system("cls")

try:
    db = psql.connect(dsn = CONFIG.get("DSN"))
    cursor = db.cursor()
    print(f"{colour.Fore.LIGHTCYAN_EX}Connected to Diary Database {colour.Style.RESET_ALL}")
except Exception as exception:
    print(f"{colour.Fore.RED} Couldn't connect to database due to : {exception} {colour.Style.RESET_ALL}")

class InitUser:
    def signup():
        signup_username = input("Enter your username : ")
        signup_password = input("Enter your password : ")
        try:
            try:
                cursor.execute("INSERT INTO credentials (username, password) VALUES (%s, %s)", (signup_username, signup_password))
                cursor.execute(f"SELECT * FROM credentials WHERE username = %s AND password = %s", (signup_username, signup_password))
            except psql.ProgrammingError as duplicate:
                print(duplicate)
                print(help.cli_init_help)
                get_command()
            except psql.IntegrityError as unique:
                print(unique)
                print(help.cli_init_help)
                get_command()        
            id = cursor.fetchone()
            cursor.execute(f"CREATE TABLE {signup_username} (id BIGSERIAL PRIMARY KEY, title TEXT NOT NULL, content TEXT NOT NULL)")
            db.commit()
            print(f"Your ID is : {id[0]}")
            print(help.cli_help)
            get_command()
        except psql.Error as exception:
            print(exception)
            print(help.cli_init_help)
            get_command()

    def login():
        global login_username, login_password, logged_in
        logged_in = False
        login_username = input("Enter your username : ")
        login_password = input("Enter your password : ")
        cursor.execute(f"SELECT * FROM credentials WHERE username = %s AND password = %s", (login_username, login_password))  
        check = cursor.fetchone()
        try:
            if login_username == check[1] and login_password == check[2]:
                logged_in = True
                print(f"\n{help.green}Successfully logged in as {login_username} on {datetime.datetime.utcnow()}{help.reset_colour}")
                input("\nPress any key to key to continue... ")
                help.typing()
                print(help.cli_help)
                get_command()
            else:
                pass
            if login_username != check[1]:
                print(f"\n{help.red}{login_username} :{help.reset_colour} is not a registered user! Please enter the correct username.")
                input("\nPress any key to key to continue... ")
                print(help.cli_init_help)
                init_get_command()
            else:
                pass        
            if login_password != check[2]:
                print(f"\n{help.red}{login_password} :{help.reset_colour} is an incorrect password! Please enter the correct password.")
                input("\nPress any key to key to continue... ")
                help.typing()
                print(help.cli_init_help)
                init_get_command()
            else:
                pass
            if login_username != check[1] and login_password != check[2]:
                print(f"\n{help.red}{login_username} :{help.reset_colour} is not a registered user! Please enter the correct username.")
                input("\nPress any key to key to continue... ")
                help.typing()
                print(help.cli_init_help)
                init_get_command()
            else:
                pass
        except:
            print("Try again...")
            help.typing()
            print(help.cli_init_help)
            init_get_command()
    
    def signout():
        choice = input("Are you sure you want to sign out?\nYes = You will be signed out\nNo = You will continue using the program\n")
        if choice == "Yes":
            help.progress_bar()
            print("Successfully signed out\r")
            login_username = None
            help.typing()
            print(help.cli_init_help)
            init_get_command()
        elif choice == "No":
            help.typing()
            print(help.cli_help)
            get_command()

    def delete():
        choice = input("Are you sure you want to delete your account?\nYes = Your account will be terminated\nNo = You will continue using the program\n")
        if choice == "Yes":
            help.progress_bar()
            cursor.execute(f"DROP TABLE {login_username}")
            cursor.execute(f"DELETE FROM credentials WHERE username = %s AND password = %s", (login_username, login_password))
            db.commit()
            print("Successfully deleted account out\r")
            login_username = None
            help.typing()
            print(help.cli_help)
            init_get_command()
        elif choice == "No":
            help.typing()
            print(help.cli_help)
            get_command()

class Diary:
    def enter_into_diary():
        title = input(f"\nEnter your entry name : ")
        content = input(f"\nEnter your entry content below :\n")
        cursor.execute(f"INSERT INTO {login_username} (title, content) VALUES (%s, %s)", (title, content))
        db.commit()
        print(f"")
        help.typing()
        input("\nPress any key to key to continue... ")
        print(help.cli_help)
        get_command()   

    def view_entries():
        #print(f"\n{help.red}You must be logged in to view any entry{help.reset_colour}")
        id = input("Enter entry ID : ")
        cursor.execute(f"SELECT * FROM {login_username} WHERE id = %s", (id))
        entry_title = cursor.fetchone()
        print(f"""{help.magenta}ID :{help.reset_colour} {entry_title[0]}
{help.magenta}Title :{help.reset_colour} {entry_title[1]}
{help.magenta}Content :{help.reset_colour} {entry_title[2]}""")
        input("\nPress any key to key to continue... ")
        help.typing()
        print(help.cli_help)
        get_command()   

    def edit_entry():
        id = input("Enter the Entry Id : ")
        content = input(f"Enter the latest edited content.\n{help.red}NOTE : The entire content will be erased and updated with the latest given.{help.reset_colour}\n")
        cursor.execute(f"UPDATE {login_username} SET content = %s WHERE id = %s", (content, id))
        db.commit()
        cursor.execute(f"SELECT * FROM {login_username}")
        edited = cursor.fetchone()
        print(f"""{help.magenta}ID :{help.reset_colour} {edited[0]}
{help.magenta}Title :{help.reset_colour} {edited[1]}
{help.magenta}Content :{help.reset_colour} {edited[2]}""")
        input("Press any key to key to continue... ")
        help.typing()
        print(help.cli_help)
        get_command()   
    
    def exit_diary():
        print("You are now going to exit the diary :)\nThank you for using this application!")
        exit()

Init = InitUser
Diary = Diary

primary_functions = {
    "login"         :   Init.login,
    "signup"        :   Init.signup,
    "signout"       :   Init.signout,
    "delete"        :   Init.delete,
    "exit"          :   Diary.exit_diary,
    "edit entry"    :   Diary.edit_entry,
    "view entries"  :   Diary.view_entries,
    "make entry"    :   Diary.enter_into_diary}    

def init_get_command():
    command = input()   
    if command == "signup":
        primary_functions["signup"]()
    elif command == "login":
        primary_functions["login"]()
    elif command == "make entry":
        primary_functions["make entry"]()
    elif command == "view entries":
        primary_functions["view entries"]()
    elif command == "edit entry":
        primary_functions["edit entry"]()
    elif command == "exit":
        primary_functions["exit"]()
    else:
        help.typing()
        print(help.cli_init_help)
        init_get_command()

def get_command():
    command = input()   
    if command == "make entry":
        primary_functions["make entry"]()
    elif command == "view entries":
        primary_functions["view entries"]()
    elif command == "edit entry":
        primary_functions["edit entry"]()
    elif command == "signout":
        primary_functions["signout"]()
    elif command == "delete":
        primary_functions["delete"]()
    elif command == "exit":
        primary_functions["exit"]()
    else:
        help.typing()
        print(help.cli_init_help)
        get_command()

help.typing()
print(help.cli_init_help)
init_get_command()