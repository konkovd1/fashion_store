from django.urls import path

from fashion_store.web.views import HomePageView, UserRegisterView, UserLoginView, ProductListView, ProfileDetailsView, \
    UserLogoutView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('products/', ProductListView.as_view(), name='product list'),
    path('profile/<int:pk>/', ProfileDetailsView.as_view(), name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
