from django.shortcuts import render

# Create your views here.
#GenericAPIView and Model Mixin
from .models  import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

class StudentList(GenericAPIView, ListModelMixin):
    queryset=Student.objects.all()
    serializer_class= StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
from  rest_framework.mixins import CreateModelMixin
class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer

    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)


from  rest_framework.mixins import RetrieveModelMixin
class  StudentRetreive(GenericAPIView, RetrieveModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
from rest_framework.mixins import UpdateModelMixin

class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def put(self,request, *args , **kwargs):
        return self.update(request, *args, **kwargs)
from rest_framework.mixins import DestroyModelMixin

class StudentDestroy(GenericAPIView,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def delete(self,request, *args , **kwargs):
        return self.destroy(request, *args, **kwargs)


# LIST and CREATE View Combine
class LCStudent(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request,*args,  **kwargs):
        return self.create(request, *args, **kwargs)    
class RUDStudent(GenericAPIView, RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self,request,*args,  **kwargs):
        return self.update(request, *args, **kwargs)  
    def delete(self,request,*args,  **kwargs):
        return self.destroy(request, *args, **kwargs)