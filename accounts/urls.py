from django.urls import path
from .views import RegisterView, CustomLoginView, ProfileView, EditProfileView, home, logout

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(next_page='home'), name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),
    path('', home, name='home'),
]
