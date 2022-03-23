from django import forms
from .models import Post
from django.contrib.auth import get_user_model
from profiles.models import Connection, CONNECTION_STATUS_CONFIRMED


class PostCreateForm(forms.ModelForm):
    viewers = forms.ModelMultipleChoiceField(queryset=None)


    class Meta:
        model = Post
        exclude = ("author",)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["viewers"].queryset =  get_user_model().objects.filter(id__in=[ x.user2.id for x in Connection.objects.filter(
            user1=user, status=CONNECTION_STATUS_CONFIRMED
        )])