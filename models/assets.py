'''ASCII Assets for a nice CLui'''
import os

from colorama import init, Fore

init()


class Assets():
    '''Graphical assets for the program'''
    def __init__(self):
        self.banner = self.yellow(str("                                         _|            \n"
                                      "             _|_|    _|    _|_|_|_|_|  _|    _|_|_|    \n"
                                      "           _|    _|  _|        _|            _|    _|  \n"
                                      "           _|_|_|_|  _|        _|            _|_|_|    \n"
                                      "           _|    _|  _|        _|            _|    _|  \n"
                                      "           _|    _|  _|_|_|_|  _|            _|    _|  \n"
                                      "         ============================================== by Pur Beurre\n"))
        self.banner_2 = self.yellow(str("\n"
                                        f"           █████╗ ██╗   ██╗██████╗     ██████╗ ███████╗██╗   ██╗██████╗ ██████╗ ███████╗ \n"
                                        f"           █╔══██╗██║   ██║██╔══██╗    ██╔══██╗██╔════╝██║   ██║██╔══██╗██╔══██╗██╔════╝ \n"
                                        f"           █████╔╝██║   ██║██████╔╝    ██████╔╝█████╗  ██║   ██║██████╔╝██████╔╝█████╗   \n"
                                        f"           █╔═══╝ ██║   ██║██╔══██╗    ██╔══██╗██╔══╝  ██║   ██║██╔══██╗██╔══██╗██╔══╝   \n"
                                        f"           █║     ╚██████╔╝██║  ██║    ██████╔╝███████╗╚██████╔╝██║  ██║██║  ██║███████╗ \n"
                                        f"           ═╝      ╚═════╝ ╚═╝  ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ \n"
                                        f"           ==============================================================================\n"))

    def clear(self):
        '''Clear console on multiple os'''
        os.system('cls' if os.name == 'nt' else 'clear')

    def green(self, text):
        '''return text in green'''
        return Fore.GREEN + text + Fore.RESET

    def red(self, text):
        '''return text in red'''
        return Fore.RED + text + Fore.RESET

    def yellow(self, text):
        '''return text in yellow'''
        return Fore.YELLOW + text + Fore.RESET


ASSET = Assets()
