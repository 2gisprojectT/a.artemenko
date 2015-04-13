__author__ = 'andrejartemenko'


class Lion:
    def __init__(self, rel):
        self.state = 'голодный'
        self.reactions = rel

    # Method for printing Lions decisions
    def decide(self, obj):
        value = self.reactions[obj, self.state][1]  # Saving input parameter for comfortable work inside of method
        state = self.state  # Saving previous value of state, for returning decision to main method
        if value != 'голодный' and value != 'сытый':
            return 'Словарь содержит неверное состояние Льва'
        else:
            self.state = value  # Applying new Lion state
            return self.reactions[obj, state][0]  #  Returning Lions decision to main method


if __name__ == '__main__':
    param = {
        ('антилопа', 'голодный'): ('Лев съедает антилопу', 'сытый'),
        ('антилопа', 'сытый'): ('Лев сыт, ему не интересна антилопа, поэтому он спокойно засыпает', 'голодный'),
        ('охотник', 'голодный'): ('Льву страшно и он убегает', 'голодный'),
        ('охотник', 'сытый'): ('Льву страшно и он убегает', 'голодный'),
        ('дерево', 'голодный'): ('Лев видит дерево, дающее спасительную тень. Он с радостью отправляется спать с надеждой, что после сна он отыщет себе пропитание', 'голодный'),
        ('дерево', 'сытый'): ('Лев смотрит на дерево без всякого интереса', 'голодный')
    }
    Lion = Lion(param)
    print('Если Вы устанете издеваться надо Львом, Вы можете закрыть приложение с помощью команды "уйти"')
    while True:
        print('\n')
        if Lion.state == 'голодный':
            print('Лев бредет по пустыне. Он голоден и мечтает поесть. Неожиданно он видит вдали какой-то объект…')
        elif Lion.state == 'сытый':
            print('Лев бредет по пустыне. Он сыт и счастлив. Неожиданно он видит вдали какой-то объект…')
        else:
            print('Лев прибывает в неопознанном состоянии…')
        print('Скажите, что это за таинственный объект? (антилопа, охотник или дерево)')
        obj = input()
        obj = obj.lower()
        try:
            print (Lion.decide(obj))
        except:
            print('Лев не знаком с таким объектом и игнорирует его')
        if obj == 'уйти':
            break

