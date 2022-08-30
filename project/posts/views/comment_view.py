from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Comment, Post
from posts.forms import CreateCommentForm


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CreateCommentForm

    def form_valid(self, form):
        post = Post.objects.get(pk=self.kwargs["pk"])
        print('valid data')
        form.instance.post = post
        form.instance.user = self.request.user
        return super(CommentCreateView, self).form_valid(form)
    
    def form_invalid(self, form):
        print('Not valid data')
        return super(CommentCreateView, self).form_invalid(form)