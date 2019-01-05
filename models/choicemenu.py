import os
from .assets import asset
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class ChoiceMenu():
    ''' '''
    def __init__(self, to_choose):
        self.full_choice = self.get_list_from_query(to_choose) # Must be an ordered Query object
        self.list_size = 15
        self.initial_position = 0
        self.final_position = 15
        self.temp_choice = self.full_choice[self.initial_position:self.final_position]
        self.page_indicator = round((self.initial_position/self.list_size)+1)
        self.page_total = round(len(self.full_choice)/self.list_size)

    def __repr__(self):
        print(asset.banner)
        output_str = str()
        choice_list = self.temp_choice
        for line in choice_list:
             output_str += "{}. {}\n".format(choice_list.index(line),line)
        output_str += "\nPage {}/{}           (A/P = 1 | Q/M = 10 | W/N = 100)\n".format(self.page_indicator, self.page_total)
        output_str += "\nPick a choice (0 -> {}) or navigate (<-A P->) : ".format(len(choice_list)-1)
        return output_str

    def get_list_from_query(self, to_choose):
        result = []
        for entry in to_choose:
            result.append(entry)
        return result

    def navigate_list(self):
        condition = False
        while not condition:
            cls()
            command = input(self)
            if command.isdigit():
                command = int(command)
                condition = self.hande_digit_result(command)
            elif command.isalpha():
                if command.capitalize() in ['A', 'P', 'Q', 'M', 'W', 'N']:
                    self.handle_alpha_result(command.capitalize())
                else:
                    continue
            else:
                continue

    def hande_digit_result(self, digit):
        if digit < len(self.temp_choice):
            print("in range")
            return True
        else:
            print("not in range")
            return False

    def handle_alpha_result(self, alpha):
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
        self.temp_choice = self.full_choice[self.initial_position:self.final_position]
        self.page_indicator = round((self.initial_position/self.list_size)+1)
        self.page_total = round(len(self.full_choice)/self.list_size)
