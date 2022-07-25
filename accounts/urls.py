from django.urls import path

from accounts.views import AccountLoginView, AccountCreateView, CustomLogoutView


urlpatterns = [
    path("login/", AccountLoginView.as_view(), name="login"),
    path("create/", AccountCreateView.as_view(), name="create-account"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]
