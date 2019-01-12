from django.urls import path, include

from .views import IndexView, ProgrammerLoginView, ProgrammerRegistrationView, ProgrammerLogoutView, ProgrammListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', ProgrammerLoginView.as_view(), name='login'),
    path('logout/', ProgrammerLogoutView.as_view(), name='logout'),
    path('registration/', ProgrammerRegistrationView.as_view(), name='registration'),
    path('programs/', ProgrammListView.as_view(), name='programs'),
]
