from django import forms


class UserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"myfield"}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"myfield"}))
    # name = forms.CharField(min_length=3)
    # age = forms.IntegerField(min_value=1, max_value=100)
    # required_css_class = "field"
    # error_css_class = "error"
    # name=forms.CharField(label="Имя", initial="undefined", help_text="ведите свое имя", required=True, min_length=2, max_length=20)
    # age=forms.IntegerField(label="Возраст", initial=18,help_text="ведите свой возраст",required=False)
    # comment=forms.CharField(label="Комментарий",widget=forms.Textarea,help_text="ведите  комментарий")
    # email=forms.EmailField(label="почта",help_text="Введите почту",required=False, initial="example.com",min_length=17)
    # weight=forms.DecimalField(min_value=3,max_value=100,decimal_places=3)
    # field_order=["age","name", "comment","email","weight"]
