import time
import dotenv
import psycopg2 as psql
import colorama as colour

import help

colour.init()
dotenv.load_dotenv()
CONFIG = dotenv.dotenv_values(".env")

try:
    db = psql.connect(dsn = CONFIG.get("DSN"))
    cursor = db.cursor()
    print(f"{colour.Fore.LIGHTCYAN_EX}Connected to Diary Database {colour.Style.RESET_ALL}")
except Exception as exception:
    print(f"{colour.Fore.RED} Couldn't connect to database due to : {exception} {colour.Style.RESET_ALL}")

def create_personal_diary():
    username = input("Enter your name : ")
    cursor.execute(f"CREATE TABLE {username} (id SERIAL PRIMARY KEY, title TEXT NOT NULL, content TEXT NOT NULL)")
    db.commit()
    print(help.cli_help)
    get_command()

def enter_into_diary():
    username = input("Enter your diary name : ")
    title = input(f"\nEnter your entry name :")
    content = input(f"\nEnter your entry content below :\n")
    cursor.execute(f"INSERT INTO {username} (title, content) VALUES (%s, %s)",(title, content))
    db.commit()
    print(f"")
    print(help.cli_help)
    get_command()

def view_entries():
    username = input("Enter your diary name: ")
    cursor.execute(f"SELECT * FROM {username}")
    for i in cursor:
        print(i)
    print(help.cli_help)
    get_command()


primary_functions_dict = {
    "create diary"  :   create_personal_diary,
    "make entry"    :   enter_into_diary,
    "view entries"  :   view_entries}

def get_command():
    command = input()   
    if command == "create diary":
        primary_functions_dict["create diary"]()
    elif command == "make entry":
        primary_functions_dict["make entry"]()
    elif command == "view entries":
        primary_functions_dict["view entries"]()
    else:
        print(help.cli_help)
        get_command()

print(help.cli_help)
get_command()