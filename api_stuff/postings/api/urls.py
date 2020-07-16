from .views import BlogPostRudView, BlogPostAPIView
from django.urls import path
app_name = 'api-postings'

urlpatterns = [
    path('', BlogPostAPIView.as_view(), name='post-create'),
    path('<int:id>/', BlogPostRudView.as_view(), name='post-rud'),
]