import time
import dotenv
import psycopg2 as psql
import colorama as colour

dotenv.load_dotenv()
CONFIG = dotenv.dotenv_values(".env")

def connect():
    try:
        global db 
        global cursor
        db = psql.connect(dsn = CONFIG.get("DSN"))
        print(colour.Fore.GREEN + f"-> {time.strftime('%c', time.gmtime())} : Successfully connected to Database." +  colour.Style.RESET_ALL)
        cursor = db.cursor()
    except Exception as exception:
        print(colour.Fore.RED + f"-> {time.strftime('%c', time.gmtime())} : Couldn't connect to Database due to : {exception}" + colour.Style.RESET_ALL)
connect()

def login():
    cursor.execute("SELECT * FROM login")
    credentials = cursor.fetchone()
    
    username = input("Enter your username : ")
    password = input("Enter your password : ")
    
    if username == credentials[0] and credentials[1]:
        print(f"Welcome {username}!")
    else:
        print(colour.Fore.RED + f"{username} : is not a registered user." + colour.Style.RESET_ALL) 
    if password != credentials[1]:
        print(colour.Fore.RED + f"Please enter the right password {username}!" + colour.Style.RESET_ALL)
    else:
        print(f"Welcome {username}!")

def signup():
    username = input(str("Enter your username : "))
    password = input(str("Enter your password : "))
    cursor.execute(f"INSERT INTO login (username, password) VALUES('{username}', '{password}')")
    db.commit()
    print(f"Successfully registered with the following details :\n1. Username : {username}\n2. Password : {password}")

def init():
    choice = input(str("1. Login : 1\n2. Sign Up : 2\n"))
    if choice == "1":
        login()
    elif choice == "2":
        signup()
    else:
        print("Your options are either 1 or 2")
init()