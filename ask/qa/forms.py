from django import forms
from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=250)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        q = Question(**self.cleaned_data)
        q.save()
        return q


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput())

    def save(self):
        a = Answer(text=self.cleaned_data['text'],
                   question_id=self.cleaned_data['question'])
        a.save()
        return a