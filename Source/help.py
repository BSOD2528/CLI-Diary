import colorama as colour

red = colour.Fore.RED
green = colour.Fore.GREEN
magenta = colour.Fore.MAGENTA
reset_colour = colour.Style.RESET_ALL

cli_help = f"""
{red}┍-------------------------------------------------------------------{reset_colour}
{red}|{reset_colour}{colour.Fore.BLUE}CLI DIARY HELP{reset_colour}                   
{red}|{reset_colour}To get started, just type out the command down below.
{red}|{reset_colour}
{red}|{reset_colour}The following list showcases and explains the commands present :
{red}|{reset_colour}{green}1 : {magenta}create diary ->{reset_colour} Creates a diary table.
{red}|{reset_colour}{green}2 : {magenta}make entry ->{reset_colour} Make a diary entry.
{red}|{reset_colour}{green}3 : {magenta}view entries ->{reset_colour} View diary entries.
{red}┕-------------------------------------------------------------------{reset_colour}
"""