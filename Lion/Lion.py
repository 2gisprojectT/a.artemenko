__author__ = 'andrejartemenko'


class Lion:
    def __init__(self):
        # Initially Lion is hungry
        self.hungry = True

    # Getter for Lion's state
    def get_state(self):
        return self.hungry

    # Setter for Lion's state (Inverts Lion's state)
    def change_state(self):
        if self.hungry:
            self.hungry = False
        else:
            self.hungry = True

    def decision(self, a):
        # If Lion is hungry
        if self.get_state():
            # Look into dictionary for reaction
            print(Info.relations_hungry[a])
            # Look into dictionary to find out if need to change state of Lion or not
            if Info.reaction_hungry[a]:
                self.change_state()
        # If Lion is NOT hungry
        else:
            print(Info.relations_not_hungry[a])
            if Info.reaction_not_hungry[a]:
                self.change_state()


# This class contains all dictionaries
class Info:
    # This dictionary contains info about Lion's reactions on different objects, when it is hungry
    relations_hungry = {
        'антилопа': 'Лев съедает антилопу',
        'охотник': 'Льву страшно и он убегает',
        'дерево': 'Лев видит дерево, дающее спасительную тень. Он с радостью отправляется спать с надеждой, что после сна он отыщет себе пропитание'
    }
    # This dictionary contains info about Lion's reactions on different objects, when it is NOT hungry
    relations_not_hungry = {
        'антилопа': 'Лев сыт, ему не интересна антилопа, поэтому он спокойно засыпает',
        'охотник': 'Льву страшно и он убегает',
        'дерево': 'Лев смотрит на дерево без всякого интереса'
    }
    # This dictionary contains info if different objects change Lion's state or not, when it is hungry
    reaction_hungry = {
        'антилопа': True,
        'охотник': False,
        'дерево': False
    }
    # This dictionary contains info if different objects change Lion's state or not, when it is NOT hungry
    reaction_not_hungry = {
        'антилопа': True,
        'охотник': True,
        'дерево': True
    }


if __name__ == '__main__':
    Lion = Lion()
    print('Если Вы устанете издеваться надо Львом, Вы можете закрыть приложение с помощью команды "уйти"')
    while True:
        print('\n')
        if Lion.get_state():
            print('Лев бредет по пустыне. Он голоден и мечтает поесть. Неожиданно он видит вдали какой-то объект…')
        else:
            print('Лев бредет по пустыне. Он сыт и счастлив. Неожиданно он видит вдали какой-то объект…')
        print('Скажите, что это за таинственный объект? (антилопа, охотник или дерево)')
        obj = input()
        obj = obj.lower()
        if obj == 'уйти':
            break
        try:
            Lion.decision(obj)
        except:
            print('Лев не знаком с таким объектом и игнорирует его')

