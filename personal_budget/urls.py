
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name="home", permanent=True)),
    path('accounts/', include('accounts.urls')),
    path('budgets/', include('budgets.urls'), name="budgets", kwargs={"namespace": "budgets"}),
]