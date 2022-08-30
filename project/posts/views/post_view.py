from django.views import generic
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post
from posts.forms import PostForm
from app.models import User

class PostCreateAndListView(LoginRequiredMixin, generic.CreateView, generic.ListView):
    model = Post
    form_class = PostForm
    context_object_name = 'posts'
    template_name = 'post/list.html'
    success_url = reverse_lazy('posts')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateAndListView, self).form_valid(form)


class PostDetailview(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = 'post/detail.html'



class ProfileListView(LoginRequiredMixin, generic.ListView):
    template_name = 'profile/list.html'
    model = User

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(Q(phone_number__icontains=query) | Q(present_address__icontains=query) )
        else:
            object_list = self.model.objects.none()
        return object_list