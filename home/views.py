from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from home.forms import *
from home.models import Course, File, Image

'''
class HomeView(generic.FormView):
    template_name = "home/base_home.html"
    form_classes = {'login': CustomAuthenticationForm,
                    'signup': SignUpForm,
                    }

    success_urls = {
        'login': reverse_lazy('home:home'),
        'signup': reverse_lazy('home:home'),
    }

    def login_form_valid(self, form):
        user = authenticate(username=form.username, password=form.password)
        if user:
            if user.is_active:
                login(self.request, user)
                messages.success(self.request, 'Logged in successfully')
                return redirect('home:home')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(form.username, form.password))
            return HttpResponse("Invalid login details given")

    def subscription_form_valid(self, form):
        'subscription form processing goes in here'
'''

'''
def home(request):
    context = {'login_form': CustomAuthenticationForm, 'signup_form':SignUpForm,}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('home:home')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        #return redirect('home:home')
        return render(request,'home/base_home.html',context)
'''


def home(request):
    courses = Course.objects.all()
    context = {'login': Login_form, 'signup':SignUpForm, 'course':CreateCourseForm, 'courses':courses }
    if request.method == 'POST':
        login_form = Login_form(request.POST)
        signup_form = SignUpForm(request.POST)
        print(login_form.is_valid())
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username,password = password)
            if user:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Logged in successfully')
                    print("logged in successfully")
                    return redirect('home:home')
                else:
                    return HttpResponse("Your account was inactive.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username, password))
                return HttpResponse("Invalid login details given")
        elif signup_form.is_valid():
            signup_form.save(commit=False)
            username = signup_form.cleaned_data.get('username')
            password1 = signup_form.cleaned_data.get('password1')
            password2 = signup_form.cleaned_data.get('password2')
            if(password1!=password2):
                raise forms.ValidationError("Passwords do not match")
                return redirect('home:home')
            email = signup_form.cleaned_data.get('email')
            try:
                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                login(request, user)
            except:
                pass
            return redirect('home:home')
        else:
            return redirect('home:home')
        #return redirect('home:home')
    elif request.method == 'GET':
        form = CreateCourseForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            print(name)
            crs = Course.objects.create(name=name, admin=request.user)
            if crs is not None:
                print("Course Created Successfully")
                crs.save()
                return redirect('home:home')

    return render(request,'home/base_home.html',context)


class RegView(generic.RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'home:register'

    def get_redirect_url(self, *args, **kwargs):
        crs = get_object_or_404(Course, pk=kwargs['pk'])
        print(crs.members.all())
        crs.register(self.request.user)
        return super().get_redirect_url(*args, **kwargs)


class CourseView(generic.TemplateView):
    template_name = 'home/course.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        crs = get_object_or_404(Course, pk=kwargs['pk'])
        file = File.objects.order_by('uploaded_at').filter(course=crs)
        img = Image.objects.order_by('uploaded_at').filter(course=crs)
        print(crs.admin, self.request.user)
        context['logger'] = self.request.user
        context['course'] = crs
        context['files'] = file
        context['images'] = img
        context['fform'] = FileForm
        context['iform'] = ImageForm
        return context