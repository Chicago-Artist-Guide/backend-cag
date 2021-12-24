from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('token/', views.UserObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('createaccount/', views.AccountCreateView.as_view(), name='createaccount'),
]
