from django.conf.urls import url, include
from . import views

import oauth2client.contrib.django_util.site as django_util_site

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^profile_required/', views.get_profile_required),
	url(r'^profile_enabled/', views.get_profile_optional),
	url(r'^oauth2/', include(django_util_site.urls)),
]
