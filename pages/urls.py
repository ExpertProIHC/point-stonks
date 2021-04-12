from django.urls import path
from .views import DashboardView, UserView

app_name = 'pages'
urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('user', UserView.as_view(), name='user'),
]