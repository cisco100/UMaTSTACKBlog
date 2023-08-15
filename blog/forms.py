from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from blog.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')




# class CommentForm(forms.Form):
#       title=forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#             "placeholder":"title",
#             "class":"form-control",
#                     }))

#       email=forms.EmailField(
#         widget=forms.EmailInput(
#             attrs={
#             "placeholder":"email",
#             "class":"form-control"
#             }))
 

#       content=forms.CharField(
#         widget=CKEditorUploadingWidget(
#             attrs={
#             "placeholder":"comment",
#             "class":"form-control",
#             }))





