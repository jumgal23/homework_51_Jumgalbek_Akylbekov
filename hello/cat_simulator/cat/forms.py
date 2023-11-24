from django import forms


class NameForm(forms.Form):
    name = forms.CharField(label='Имя кота', max_length=50)


class InteractionForm(forms.Form):
    ACTIONS = [
        ('feed', 'Покормить'),
        ('play', 'Поиграть'),
        ('sleep', 'Поспать'),
    ]
    action = forms.ChoiceField(choices=ACTIONS, label='Выберите действие')



