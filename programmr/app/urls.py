from django.conf.urls import url,include
from . import views

import oauth2client.contrib.django_util.site as django_util_site

urlpatterns = [
	url(r'^$', views.login, name='login'),
	url(r'^google_login/', views.google_login, name='google_login'),
	url(r'^profile_enabled/', views.get_profile_optional),
	url(r'^oauth2/', include(django_util_site.urls)),
	url(r'^profile/$',views.profile,name='profile'),
    url(r'^dashboard/$',views.dashboard,name='dashboard'),
    url(r'^rules/$',views.rules,name='rules'),
    url(r'^announcements/$',views.announcements,name='announcements'),
    url(r'^(?P<id>[0-9]+)/$',views.question_detail,name='question_detail'),

]
