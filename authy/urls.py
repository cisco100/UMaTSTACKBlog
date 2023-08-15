from django.urls import path
from authy.views import signin_view,signup_view,signout_view
urlpatterns = [
    path('login/',signin_view,name="login"),
    path('register/',signup_view,name="register"),
    path('logout/',signout_view,name="logout"),
]
