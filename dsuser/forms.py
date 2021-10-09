from django import forms
from django.contrib.auth.hashers import check_password 
from .models import Dsuser 

class RegisterForm(forms.Form):
    user_id=forms.CharField(
        error_messages={
            'required':'모든값을 입력해야 합니다.'
        },
        max_length=222,label='아이디'
    )

    email=forms.EmailField(
        error_messages={
            'required':'모든값을 입력해야 합니다.'
        },
        max_length=222, label='이메일'
    )

    password=forms.CharField(
        error_messages={
            'required':'모든값을 입력해야 합니다.'
        },
        widget=forms.PasswordInput,label='비밀번호'
    )

    re_password=forms.CharField(
        error_messages={
            'required':'모든값을 입력해야 합니다.'
        },
        widget=forms.PasswordInput,label='비밀번호 확인'
    )

    def clean(self):
        cleaned_data=super().clean()
        user_id=cleaned_data.get('user_id')
        email=cleaned_data.get('email')
        password=cleaned_data.get('password')
        re_password=cleaned_data.get('re_password')

        if password and re_password:
            if password!=re_password:
                self.add_error('password','비밀번호가 다릅니다.')
                self.add_error('re_password','비밀번호가 다릅니다.')


class LoginForm(forms.Form):
    user_id=forms.CharField(
        error_messages={
            'required':'아이디를 입력해 주세요'
        },
        max_length=222,label='아이디'
    )
    password=forms.CharField(
        error_messages={
            'required':'비밀번호를 입력해 주세요.'
        },
        widget=forms.PasswordInput,label='비밀번호'
    )

    def clean(self):
        cleaned_data=super().clean()
        user_id=cleaned_data.get('user_id')
        password=cleaned_data.get('password')

        if user_id and password:
            try:
                dsuser=Dsuser.objects.get(user_id=user_id)
            except Dsuser.DoesNotExist:
                self.add_error('user_id','아이디가 없습니다')
                return
            if not check_password(password,dsuser.password):
                self.add_error('password','비밀번호가 틀렸습니다.')



        