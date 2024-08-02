from django import forms


class UserForm(forms.Form):
    name=forms.CharField(label="Имя", initial="undefined", help_text="ведите свое имя")
    age=forms.IntegerField(label="Возраст", initial=18,help_text="ведите свой возраст")
    comment=forms.CharField(label="Комментарий",widget=forms.Textarea,help_text="ведите  комментарий" )
field_order=["age","name","comment"]

    
