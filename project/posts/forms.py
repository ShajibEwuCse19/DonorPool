from django import forms
from mptt.forms import TreeNodeChoiceField
from .models import Post, Comment, ReviewRating


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'status']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'id': 'body', 'rows': "3"}),
            'status': forms.Select(attrs={'class': 'form-select', 'id': 'status'})
        }


class CreateCommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].widget.attrs.update(
            {'class': 'd-none'})
        self.fields['parent'].label = ''
        self.fields['parent'].required = False

    class Meta:
        model = Comment
        fields = ('content', 'parent')

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def save(self, *args, **kwargs):
        Comment.objects.rebuild()
        return super(CreateCommentForm, self).save(*args, **kwargs)


class ReviewRatingForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ('rating', 'subject', 'review')
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'review': forms.Textarea(attrs={'class': 'form-control'}),
        }