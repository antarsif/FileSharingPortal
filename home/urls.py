from django.urls import path, reverse_lazy
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('course/reg/<int:pk>', views.RegView.as_view(url = reverse_lazy('home:home')), name='register'),
    path('course/<int:pk>', views.CourseView.as_view(),name='course_home'),
    ]