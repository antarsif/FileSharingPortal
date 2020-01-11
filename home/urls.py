from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, reverse_lazy
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('course/reg/<int:pk>', views.RegView.as_view(url = reverse_lazy('home:home')), name='register'),
    path('course/<int:pk>', views.fileupload,name='course_home'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)