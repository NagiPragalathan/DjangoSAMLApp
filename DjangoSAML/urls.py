from django.contrib import admin
from django.urls import path, include
from django_saml2_auth.views import signin

urlpatterns = [
    path("admin/", admin.site.urls),
]

SAML = [
    path('accounts/', include('allauth.urls')),
    path('sso/', include('django_saml2_auth.urls')),
    path('accounts/sso-login/', signin, name="sso-login"),
]

# Including SAML URLs in the main urlpatterns
urlpatterns += SAML
