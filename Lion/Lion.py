__author__ = 'andrejartemenko'


class Lion:
    def __init__(self, rel):
        # Possible states: 0 - hungry, 1 - fed
        self.state = 0
        self.reactions = rel

    # Getter for Lion's state
    def get_state(self):
        return self.state

    # Setter for Lion's state (Inverts Lion's state)
    def set_state(self, value):
        if value != 0 and value != 1:
            print("Вы ввели некорректное значение")
        else:
            self.state = value

    # Method for printing Lions decisions
    def decide(self, obj):
        print(self.reactions[obj, self.get_state()][0])
        Lion.set_state(self.reactions[obj, self.get_state()][1])


if __name__ == '__main__':
    param = {
        ('антилопа', 0): ('Лев съедает антилопу', 1),
        ('антилопа', 1): ('Лев сыт, ему не интересна антилопа, поэтому он спокойно засыпает', 0),
        ('охотник', 0): ('Льву страшно и он убегает', 0),
        ('охотник', 1): ('Льву страшно и он убегает', 0),
        ('дерево', 0): ('Лев видит дерево, дающее спасительную тень. Он с радостью отправляется спать с надеждой, что после сна он отыщет себе пропитание', 0),
        ('дерево', 1): ('Лев смотрит на дерево без всякого интереса', 0)
    }
    Lion = Lion(param)
    print('Если Вы устанете издеваться надо Львом, Вы можете закрыть приложение с помощью команды "уйти"')
    while True:
        print('\n')
        if Lion.get_state() == 0:
            print('Лев бредет по пустыне. Он голоден и мечтает поесть. Неожиданно он видит вдали какой-то объект…')
        elif Lion.get_state() == 1:
            print('Лев бредет по пустыне. Он сыт и счастлив. Неожиданно он видит вдали какой-то объект…')
        else:
            print('Лев прибывает в неопознанном состоянии…')
        print('Скажите, что это за таинственный объект? (антилопа, охотник или дерево)')
        obj = input()
        obj = obj.lower()
        try:
            Lion.decide(obj)
        except:
            print('Лев не знаком с таким объектом и игнорирует его')
        if obj == 'уйти':
            break

