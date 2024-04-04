"""this package helps give a shortcut for creating snippets"""


from time import sleep
from threading import Thread
from colorama import Fore as f

from utils import message, handelMultiLineInput, nameReplacement

optionalMessage = f"{f.GREEN}(optional){f.RESET}"
requiredMessage = f"{f.RED}(required){f.RESET}"
newline = '\n    '
longLine = '\n        '
longLineWithQuotes = '"\n        "'

