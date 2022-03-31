'''
to use color.py you must:
import color.py
print(f'{color.blue}text') sets color blue.
print(color.bgreen,'text') sets backgroundcolor green. 
print(color.normal) sets all normal.
'''

NORMAL = "\033[0m"
END = "\033[0m"

BOLD = "\033[1m"
THIN = "\033[2m"
CURSIV = "\033[3m"
UNDERLINE = "\033[4m"

GRAY = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

#backgroundcolor:
BBLACK = "\033[40m"
BRED = "\033[41m"
BGREEN = "\033[42m"
BYELLOW = "\033[43m"
BBLUE = "\033[44m"
BMAGENTA = "\033[45m"
BCYAN = "\033[46m"
BWHITE = "\033[47m"