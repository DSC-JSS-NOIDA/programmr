from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
	url(r'^login_page', views.login_page, name='login_page'),
	url(r'^login/', views.login_google, name='login_google'),
	url(r'^google_login/', views.google_login, name='google_login'),
	url(r'^logout', views.logout_view, name='logout_view'),
	url(r'^profile/',views.profile,name='profile'),
    url(r'^rules$',views.rules,name='rules'),
    url(r'^announcements$',views.announcements,name='announcements'),
    url(r'^question_detail/(?P<id>[0-9]+)$',views.question_detail,name='question_detail'),
	url(r'^submission/$',views.submission,name='submission'),
	url(r'^leaderboard/$',views.leaderboard,name='leaderboard'),

]
