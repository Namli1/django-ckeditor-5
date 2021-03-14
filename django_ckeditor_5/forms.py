from django import forms
from django.http import JsonResponse

def validate_file_size(value):
    filesize= value.size
    
    if filesize > 102400:
        raise ValidationError("hello")
        # return JsonResponse({
        #         "error": {
        #             "message": "The image was too big",
        #         }
        # })
    else:
        return value

class UploadFileForm(forms.Form):
    upload = forms.FileField()#validators=[validate_file_size])
