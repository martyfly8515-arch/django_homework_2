from captcha.fields import CaptchaField
from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Имя'
    )
    email = forms.EmailField(
        label='E-mail'
    )
    message = forms.CharField(
        widget=forms.Textarea,
        label='Сообщение'
    )
    captcha = CaptchaField(
        label='Введите код с картинки'
    )
