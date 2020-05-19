from .models import Student
from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'age', 'gpa']


class RawStudentForm(forms.Form):
    student_id = forms.CharField(label='id',widget=forms.TextInput(attrs={'placeholder':'example 12-1234'}))
    gpa = forms.DecimalField()
    age = forms.DecimalField()
    name = forms.CharField()

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if  '0' in name or '1' in name or '2' in name or '3' in name or '4' in name or '5' in name or '6' in name or '7' in name or '8' in name or '9' in name:
            raise forms.ValidationError('This is not valid name, a name can\'t have a number in it')
        return name



