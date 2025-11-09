from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),  # Root path redirects to a test room
    path('chat/<int:receiver_id>/', views.chat_view, name='chat_view'),  # updated
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
