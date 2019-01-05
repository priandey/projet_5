import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class ChoiceMenu():
    ''' '''
    def __init__(self, to_choose):
        self.full_choice = self.get_list(to_choose) # Must be an ordered Query object
        self.temp_choice = ['coucou','je','suis','une','liste','restreinte']
    def __repr__(self):
        output_str = str()
        choice_list = self.temp_choice
        for line in choice_list:
             output_str += "{}. {}\n".format(choice_list.index(line),line)
        output_str += "\nPick a choice (0 -> {}) or navigate (<-A P->) : ".format(len(choice_list)-1)
        return output_str

    def get_list(self, to_choose):
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
                condition = True
            elif command.isalpha():
                condition = True
            else:
                continue
