'''ASCII Assets for a nice CLui'''
import os

from colorama import init, Fore, Back
init()

class Assets():
    '''Filler'''
    def __init__(self):
        self.banner = str("                                         _|          \n"
                          "             _|_|    _|    _|_|_|_|_|  _|    _|_|_|   \n"
                          "           _|    _|  _|        _|            _|    _|  \n"
                          "           _|_|_|_|  _|        _|            _|_|_|    \n"
                          "           _|    _|  _|        _|            _|    _|  \n"
                          "           _|    _|  _|_|_|_|  _|            _|    _|   \n"
                          "         ==============================================")
        self.banner_2 = str("\n"
        f"           {Fore.YELLOW} ██████╗ ██╗   ██╗██████╗     ██████╗ ███████╗██╗   ██╗██████╗ ██████╗ ███████╗ {Fore.RESET}\n"
        f"           {Fore.YELLOW} ██╔══██╗██║   ██║██╔══██╗    ██╔══██╗██╔════╝██║   ██║██╔══██╗██╔══██╗██╔════╝ {Fore.RESET}\n"
        f"           {Fore.YELLOW} ██████╔╝██║   ██║██████╔╝    ██████╔╝█████╗  ██║   ██║██████╔╝██████╔╝█████╗   {Fore.RESET}\n"
        f"           {Fore.YELLOW} ██╔═══╝ ██║   ██║██╔══██╗    ██╔══██╗██╔══╝  ██║   ██║██╔══██╗██╔══██╗██╔══╝   {Fore.RESET}\n"
        f"           {Fore.YELLOW} ██║     ╚██████╔╝██║  ██║    ██████╔╝███████╗╚██████╔╝██║  ██║██║  ██║███████╗ {Fore.RESET}\n"
        f"           {Fore.YELLOW} ╚═╝      ╚═════╝ ╚═╝  ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ {Fore.RESET}\n"
        f"           {Fore.YELLOW}  =============================================================================={Fore.RESET}\n")
    def cls(self):
        '''Clear console on multiple os'''
        os.system('cls' if os.name == 'nt' else 'clear')

ASSET = Assets()
