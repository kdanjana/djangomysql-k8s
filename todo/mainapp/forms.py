rom django import forms

from .models import Item

class ExForm(forms.Form):
    myfield = forms.CharField(widget=forms.TextInput(attrs={'class': 'myfieldclass'}))

class TodoForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["todo"]
        labels = {
            "todo": "Todo"
        }
        widgets = {
            "todo": forms.TextInput(attrs={'class': 'myfieldclass'})
        }


    def clean(self):
        super(TodoForm, self).clean()
        todo = self.cleaned_data.get('todo')
        if len(todo) < 3:
            self._errors['todo'] = self.error_class([rom django import forms

from .models import Item

class ExForm(forms.Form):
    myfield = forms.CharField(widget=forms.TextInput(attrs={'class': 'myfieldclass'}))

class TodoForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["todo"]
        labels = {
            "todo": "Todo"
        }
        widgets = {
            "todo": forms.TextInput(attrs={'class': 'myfieldclass'})
        }


    def clean(self):
        super(TodoForm, self).clean()
        todo = self.cleaned_data.get('todo')
        if len(todo) < 3:
            self._errors['todo'] = self.error_class([ 'Please enter todo item.'])
        return self.cleaned_data