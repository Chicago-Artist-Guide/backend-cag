from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('token/', views.UserObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('createaccount/', views.AccountCreateView.as_view(), name='create_account'),
    path('get-some-details/', views.GetSomeDetailsCreateView.as_view(), name='get_some_details'),
    path('what-you-like-doing/', views.WhatDoYouLikeDoingView.as_view(), name='what_you_like_doing'),
    path('almost-done/', views.AlmostDoneView.as_view(), name='almost_done'),
    path('update-account/<int:pk>/', views.AccountUpdateView.as_view(), name='update_account'),
]
