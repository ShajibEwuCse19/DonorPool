from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import ReviewRating
from posts.forms import ReviewRatingForm
from posts.utils import get_ip_address


class ReviewRatingCreateAndListView(LoginRequiredMixin, generic.CreateView, generic.ListView):
    model = ReviewRating
    form_class = ReviewRatingForm
    context_object_name = 'reviews'
    template_name = 'review/list.html'
    success_url = reverse_lazy('reviews')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.ip_address = get_ip_address(self.request)
        return super(ReviewRatingCreateAndListView, self).form_valid(form)