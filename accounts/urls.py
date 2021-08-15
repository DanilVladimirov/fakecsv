from django.urls import path
from accounts.views import (RegUserView,
                            LoginUserView,
                            logout_user)

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login-page'),
    path('register/', RegUserView.as_view(), name='reg-page'),
    path('logout/', logout_user, name='logout-page'),
]
