from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('token/', views.UserObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('create/', views.AccountCreateView.as_view(), name='create_account'),
    path('get/<int:pk>/', views.RetrieveAccountView.as_view(), name='get_account'),
    path('update/<int:pk>/', views.AccountUpdateView.as_view(), name='update_account'),
    path('profile/basic/', views.BasicProfileCreateView.as_view(), name='basic_profile'),
    path('profile/basic/get/<int:pk>/', views.RetrieveBasicProfile.as_view(), name='get_basic_profile'),
    path('image-upload/', views.UploadProfilePictureCreateView.as_view(), name='upload_profile_pic_on_s3'),
]
