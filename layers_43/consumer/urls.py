from django.conf.urls import patterns, url
from django.conf import settings
from layers_43.consumer import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^submit_design', views.submit_design, name="submit_design"),
    url(r'^login', views.login, name="login"),
    url(r'^signup', views.signup, name="signup"),
    url(r'^logout', views.logout_view, name='logout'),
    url(r'^find_designer', views.find_designer, name="find_designer"),
    url(r'^idea_bored', views.idea_bored, name="idea_bored"),
    url(r'^send_message', views.send_message, name="send_message"),
    url(r'^submit_photo', views.add_photo, name="submit_photo"),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )