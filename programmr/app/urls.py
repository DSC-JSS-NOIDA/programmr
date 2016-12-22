from django.conf.urls import url, include
from . import views

import oauth2client.contrib.django_util.site as django_util_site

urlpatterns = [
	url(r'^$', views.login, name='login'),
	url(r'^google_login/', views.google_login, name='google_login'),
	url(r'^profile_enabled/', views.get_profile_optional),
	url(r'^oauth2/', include(django_util_site.urls)),
]