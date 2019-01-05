'''This module sets-up user interface navigation logic'''
import os
from .assets import ASSET
from .entities import Product, Category, UserHistory

def cls():
    '''Clear console on multiple os'''
    os.system('cls' if os.name == 'nt' else 'clear')

class ChoiceMenu():
    ''' The user interface'''
    def __init__(self, to_choose, first_panel=False):
        self.type_object = to_choose[0]
        self.full_choice = self.get_list_from_query(to_choose) # Must be an ordered Query object
        self.first_panel = first_panel
        self.list_size = 15
        self.initial_position = 0
        self.final_position = 15
        self.temp_choice = self.full_choice[self.initial_position:self.final_position]
        self.page_indicator = round((self.initial_position/self.list_size)+1)
        self.page_total = round(len(self.full_choice)/self.list_size)
        self.chosen_result = ''

    def __repr__(self):
        print(ASSET.banner)
        output_str = str()
        choice_list = self.temp_choice
        for line in choice_list:
            output_str += "    {}. {}\n".format(choice_list.index(line), line)
        output_str += "\n   Page {}/{}           (A/P = 1 | Q/M = 10 | W/N = 100)\n".\
                                                        format(self.page_indicator, self.page_total)
        if not self.first_panel:
            output_str += "\n   Pick a choice (0 -> {}), navigate (<-A P->) or exit (E): ".\
                                                                          format(len(choice_list)-1)
        else:
            output_str += "\n   Pick a choice (0 -> {}), navigate (<-A P->): ".\
                                                                          format(len(choice_list)-1)
        return output_str

    def refresh_attr(self):
        '''Refresh object attribute'''
        self.temp_choice = self.full_choice[self.initial_position:self.final_position]
        self.page_indicator = round((self.initial_position/self.list_size)+1)
        self.page_total = round(len(self.full_choice)/self.list_size)

    def get_list_from_query(self, to_choose):
        '''Transform any indexable objet in exploitable list'''
        result = []
        for entry in to_choose:
            result.append(entry)
        return result

    def navigate_list(self):
        '''Main loop of the menu '''
        stop_loop = False
        while not stop_loop:
            cls()
            command = input(self)
            if command.isdigit():
                command = int(command)
                stop_loop = self.handle_digit_result(command)
            elif command.isalpha():
                if command.capitalize() in ['A', 'P', 'Q', 'M', 'W', 'N', 'E']:
                    stop_loop = self.turn_page(command.capitalize())
                else:
                    continue
            else:
                continue

    def handle_digit_result(self, digit):
        '''Isolate chosen object from list using index'''
        if digit < len(self.temp_choice):
            self.chosen_result = self.temp_choice[digit]
            return True

    def turn_page(self, alpha):
        '''Handle autorized alphabetic character'''
        if alpha == 'A':
            if self.initial_position-self.list_size >= 0:
                self.initial_position -= self.list_size
                self.final_position -= self.list_size
        if alpha == 'P':
            if self.final_position+self.list_size <= self.page_total*self.list_size:
                self.initial_position += self.list_size
                self.final_position += self.list_size
        if alpha == 'Q':
            if self.initial_position-(self.list_size*10) >= 0:
                self.initial_position -= self.list_size*10
                self.final_position -= self.list_size*10
        if alpha == 'M':
            if self.final_position+(self.list_size*10) <= self.page_total*self.list_size:
                self.initial_position += self.list_size*10
                self.final_position += self.list_size*10
        if alpha == 'W':
            if self.initial_position-(self.list_size*100) >= 0:
                self.initial_position -= self.list_size*100
                self.final_position -= self.list_size*100
        if alpha == 'N':
            if self.final_position+(self.list_size*100) <= self.page_total*self.list_size:
                self.initial_position += self.list_size*100
                self.final_position += self.list_size*100
        if alpha == "E":
            if not self.first_panel:
                return True
        self.refresh_attr()
