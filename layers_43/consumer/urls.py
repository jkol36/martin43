from django.conf.urls import patterns, url

from layers_43.consumer import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^submit_design', views.submit_design, name="submit_design"),
    url(r'^login', views.login, name="login"),
    url(r'^signup', views.signup, name="signup"),
    url(r'^logout', views.logout_view, name='logout'),
    url(r'^find_designer', views.find_designer, name="find_designer"),
    url(r'^idea_bored', views.idea_bored, name="idea_bored"),
)
