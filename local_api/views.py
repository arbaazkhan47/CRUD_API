from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissions


class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]





