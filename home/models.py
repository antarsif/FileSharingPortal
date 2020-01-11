from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

'''class User(AbstractBaseUser):
    name = models.CharField(verbose_name="Name",max_length=75)
    email = models.EmailField(verbose_name="E-mail",max_length=55,unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def create_course(self, name):
        crs = Course.objects.create(name=name,admin=self);
        crs.save()

    def __str__(self):
        return self.email'''



class Course(models.Model):
    name = models.CharField(verbose_name="Course Name", max_length=75)
    created_at = models.DateTimeField(verbose_name="Creation Date", auto_now_add=True)
    admin = models.ForeignKey(User,related_name='Course_admin',on_delete=models.CASCADE)
    members = models.ManyToManyField(User)

    def register(self, user):
        self.members.add(user)

    def remove(self,user):
        self.members.remove(user)

    def add_file(self,doc,file_name):
        file = File.objects.create(doc=doc,file_name=file_name)
        file.save()

    def add_img(self,img,img_name):
        image = Image.objects.create(img=img,img_name=img_name)
        image.save()


    def __str__(self):
        return self.name

class File(models.Model):
    doc = models.FileField(verbose_name="Content", upload_to='files/')
    file_name = models.CharField(verbose_name='File Name', blank = True,max_length=25)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.file_name

class Image(models.Model):
    img = models.ImageField(verbose_name="Content", upload_to='images/')
    img_name = models.CharField(verbose_name='File Name', blank=True,max_length=25)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.img_name





