from django.urls import path
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'office'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('plan/', PlanView.as_view(), name='plan'),
    path('user/', UserIdView.as_view(), name='user'),

    path('sitings/manage', SitingView.as_view(), name='manage_lessons'),
    path('sitings/add', SitingAddView.as_view(), name='add_Siting'),
    path('sitings/<int:id>', SitingEditView.as_view(), name='edit_Siting'),
    path('sitings/delete/<int:id>', SitingDeleteView.as_view(), name='delete_Siting'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)