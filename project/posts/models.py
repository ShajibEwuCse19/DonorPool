from django.db import models
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse

User = settings.AUTH_USER_MODEL


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)


class Post(TimeStamp):
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    body = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)

    def get_absolute_url(self):
        return reverse('posts-detail', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return f'{self.title}'



class Comment(TimeStamp, MPTTModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    status = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['-created_at']
    
    def get_absolute_url(self):
        return reverse('posts-detail', kwargs={'pk': self.post.pk})

    def __str__(self) -> str:
        return f'Comment by {self.user.username}'



class ReviewRating(TimeStamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=0)
    subject = models.CharField(max_length=255)
    review  = models.TextField()
    ip_address = models.GenericIPAddressField()

    def __str__(self) -> str:
        return f"{self.subject}"


