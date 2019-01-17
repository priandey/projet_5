'''This module sets-up user interface navigation logic'''
from math import ceil

from .assets import ASSET


class ChoiceMenu():
    ''' The user interface'''
    def __init__(self, to_choose, first_panel=False):
        self.full_choice = self.get_list_from_query(to_choose)
        self.first_panel = first_panel
        self.list_size = 15
        self.initial_position = 0
        self.final_position = 15
        self.temp_choice = self.full_choice[self.initial_position:
                                            self.final_position]
        self.page_indicator = ceil((self.initial_position/self.list_size)+1)
        self.page_total = ceil(len(self.full_choice)/self.list_size)
        self.chosen_result = ''
        self.navigate_list()

    def __repr__(self):
        print(ASSET.banner)
        output_str = str()
        choice_list = self.temp_choice
        for line in choice_list:
            output_str += "    {}.\t{}\n".format(choice_list.index(line), line)
        output_str += "\n   Page {}/{}\t\t(A/P = 1 | Q/M = 10 | W/N = 100)\n".\
                      format(self.page_indicator, self.page_total)
        if not self.first_panel:
            output_str += "\n\tChoose (0 -> {}), navigate (<-A P->) or go "\
                          "to main menu (E)\n>> ".format(len(choice_list)-1)
        else:
            output_str += "\n\tChoose (0 -> {}), navigate (<-A P->)\n>> ".\
                                                     format(len(choice_list)-1)
        return output_str

    def refresh_attr(self):
        '''Refresh object attribute'''
        self.temp_choice = self.full_choice[self.initial_position:
                                            self.final_position]
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
            ASSET.clear()
            interface = input(self)
            if interface.isdigit():
                command = int(interface)
                stop_loop = self.handle_digit_result(command)
            elif interface.isalpha():
                if interface.upper() in ['A', 'P', 'Q', 'M', 'W', 'N', 'E']:
                    stop_loop = self.turn_page(interface.upper())
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
        elif alpha == 'P':
            if self.final_position+self.list_size <= self.page_total * \
                                                                self.list_size:
                self.initial_position += self.list_size
                self.final_position += self.list_size
        elif alpha == 'Q':
            if self.initial_position-(self.list_size*10) >= 0:
                self.initial_position -= self.list_size*10
                self.final_position -= self.list_size*10
        elif alpha == 'M':
            if self.final_position+(self.list_size*10) <= self.page_total * \
                                                                self.list_size:
                self.initial_position += self.list_size*10
                self.final_position += self.list_size*10
        elif alpha == 'W':
            if self.initial_position-(self.list_size*100) >= 0:
                self.initial_position -= self.list_size*100
                self.final_position -= self.list_size*100
        elif alpha == 'N':
            if self.final_position+(self.list_size*100) <= self.page_total * \
                                                                self.list_size:
                self.initial_position += self.list_size*100
                self.final_position += self.list_size*100
        elif alpha == "E":
            if not self.first_panel:
                return True
        self.refresh_attr()
