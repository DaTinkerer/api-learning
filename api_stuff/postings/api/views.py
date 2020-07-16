from rest_framework import generics, mixins
from postings.models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field            = 'id'
    queryset                = BlogPost.objects.all()         
    serializer_class        = BlogPostSerializer

    def get_queryset(self):
        return BlogPost.objects.all() 

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field            = 'id'
    queryset                = BlogPost.objects.all()         
    serializer_class        = BlogPostSerializer

    def get_queryset(self):
        return BlogPost.objects.all()     