from django.conf.urls import url

from . import views

urlpatterns = (
    
    #url(r'^$', 'django_social_app.views.login'),
    #url(r'^home/$', 'django_social_app.views.home'),
    #url(r'^logout/$', 'django_social_app.views.logout'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^dashboard/$',views.dashboard,name='dashboard'),
    url(r'^home/$',views.home,name='home'),
    url(r'^rules/$',views.rules,name='rules'),
    url(r'^announcements/$',views.announcements,name='announcements'),





)
