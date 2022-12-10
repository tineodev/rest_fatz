from projects.models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    permission_classes = [permissions.AllowAny] #! cualquier persona solicita info
    serializer_class = ProjectSerializer

