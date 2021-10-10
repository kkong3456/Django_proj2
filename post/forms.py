from django import forms

class PostForm(forms.Form):
    
    contents=forms.CharField(
        label="내용",
        widget=forms.Textarea,
        error_messages={
            'required':'내용을 입력하세요',
        }
    )

    img_url=forms.CharField(
        label='태그',
        error_messages={
            'required':'이미지주소를 입력하세요'
        }
    )

    tags=forms.CharField(
        required=False,
        label='태그'
    )
