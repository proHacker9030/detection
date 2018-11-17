from django import forms


class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField()
    method_id = forms.CharField()

    class Meta:
        db_table = 'upload_file_form'
        app_label = 'upload_file_form'
