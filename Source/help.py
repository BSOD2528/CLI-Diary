import os
import time
import colorama as colour

red = colour.Fore.RED
blue = colour.Fore.BLUE
green = colour.Fore.GREEN
magenta = colour.Fore.MAGENTA
reset_colour = colour.Style.RESET_ALL

cli_init_help = f"""
{red}┍------------------------------------------------------------------┑{reset_colour}
{red}|{reset_colour}{colour.Fore.BLUE}CLI DIARY HELP{reset_colour}                                                    {red}|{reset_colour}             
{red}|------------------------------------------------------------------|{reset_colour}
{red}|{reset_colour}To get started, just type out the command down below.             {red}|{reset_colour}
{red}|{reset_colour}                                                                  {red}|{reset_colour}
{red}|{reset_colour}The following list showcases and explains the commands present :  {red}|{reset_colour}
{red}|{reset_colour}                                                                  {red}|{reset_colour}
{red}|{reset_colour}{green}1 : {magenta}signup ->{reset_colour} Sign up for the diary.                              {red}|{reset_colour}
{red}|{reset_colour}{green}2 : {magenta}login ->{reset_colour} Login into your diary.                               {red}|{reset_colour}
{red}|{reset_colour}{green}3 : {magenta}delete ->{reset_colour} Deletes everything.                                 {red}|{reset_colour}
{red}|{reset_colour}                                                                  {red}|{reset_colour}
{red}|{reset_colour}{green}1 : {magenta}make entry ->{reset_colour} Make a diary entry.                             {red}|{reset_colour}
{red}|{reset_colour}{green}2 : {magenta}view entries ->{reset_colour} View diary entries.                           {red}|{reset_colour}
{red}|{reset_colour}{green}3 : {magenta}edit entry ->{reset_colour} Edits the content of a entry.                   {red}|{reset_colour}
{red}|{reset_colour}{green}4 : {magenta}exit ->{reset_colour} Exits the application.                                {red}|{reset_colour}
{red}┕------------------------------------------------------------------┘{reset_colour}
"""

cli_help = f"""
{red}┍------------------------------------------------------------------┑{reset_colour}
{red}|{reset_colour}{colour.Fore.BLUE}CLI DIARY HELP{reset_colour}                                                    {red}|{reset_colour}             
{red}|------------------------------------------------------------------|{reset_colour}
{red}|{reset_colour}To get started, just type out the command down below.             {red}|{reset_colour}
{red}|{reset_colour}                                                                  {red}|{reset_colour}
{red}|{reset_colour}The following list showcases and explains the commands present :  {red}|{reset_colour}
{red}|{reset_colour}                                                                  {red}|{reset_colour}
{red}|{reset_colour}{green}1 : {magenta}signout ->{reset_colour} Sign out of the diary.                             {red}|{reset_colour}
{red}|{reset_colour}{green}2 : {magenta}delete ->{reset_colour} Deletes everything.                                 {red}|{reset_colour}
{red}|{reset_colour}                                                                  {red}|{reset_colour}
{red}|{reset_colour}{green}1 : {magenta}make entry ->{reset_colour} Make a diary entry.                             {red}|{reset_colour}
{red}|{reset_colour}{green}2 : {magenta}view entries ->{reset_colour} View diary entries.                           {red}|{reset_colour}
{red}|{reset_colour}{green}3 : {magenta}edit entry ->{reset_colour} Edits the content of a entry.                   {red}|{reset_colour}
{red}|{reset_colour}{green}4 : {magenta}exit ->{reset_colour} Exits the application.                                {red}|{reset_colour}
{red}┕------------------------------------------------------------------┘{reset_colour}
"""

def progress_bar():
    print("\r╠ ", end = "")
    time.sleep(0.1)
    print("\r╠═", end = "")
    time.sleep(0.1)
    print("\r╠══", end = "")
    time.sleep(0.1)
    print("\r╠═══", end = "")
    time.sleep(0.1)
    print("\r╠════ ", end = "")
    time.sleep(0.1)
    print("\r╠═════ ", end = "")
    time.sleep(0.1)
    print("\r╠══════ ", end = "")
    time.sleep(0.1)
    print("\r╠═══════ ", end = "")
    time.sleep(0.1)
    print("\r╠════════ ", end = "")
    time.sleep(0.1)
    print("\r╠═════════ ", end = "")
    time.sleep(0.1)
    print("\r╠══════════ ", end = "")
    time.sleep(0.1)
    print("\r╠═══════════ ", end = "")
    time.sleep(0.1)
    print("\r╠════════════ ", end = "")
    time.sleep(0.1)
    print("\r╠════════════╣ ", end = "")    

def typing():
    print("\r.", end = "")
    time.sleep(0.1)
    print("\r..", end = "")
    time.sleep(0.1)
    print("\r...", end = "")
    time.sleep(0.1)
    os.system("cls")