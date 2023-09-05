from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["task"]
        labels = {
            "task": "Task"
        }
        widgets = {
            "task": forms.TextInput(attrs={'class': 'myfieldclass'})
        }


    def clean(self):
        super(TodoForm, self).clean()
        task = self.cleaned_data.get('task')
        if len(task) < 3:
            self._errors['task'] = self.error_class([ 'Please enter todo item.'])
        return self.cleaned_data