from django.conf.urls import patterns, url

from layers_43.consumer import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^submit_design', views.submit_design, name="submit_design"),
    url(r'^save_project/', views.save_project, name="save_project"),
    url(r'^login', views.login, name="login"),
    url(r'^signup', views.signup, name="signup"),
)
