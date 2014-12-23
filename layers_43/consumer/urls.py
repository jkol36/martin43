from django.conf.urls import patterns, url
from django.conf import settings
from layers_43.consumer.views import add_photo, find_designer, logout_view, signup, login, submit_design, messages, inspiration_view, index, idea_bored, send_a_message, my_account
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns(
    '',
    url(r'^$',index, name='index'),
    url(r'^submit_design', submit_design, name="submit_design"),
    url(r'^login', login, name="login"),
    url(r'^signup', signup, name="signup"),
    url(r'^logout', logout_view, name='logout'),
    url(r'^find_designer', find_designer, name="find_designer"),
    url(r'^idea_bored', idea_bored, name="idea_bored"),
    url(r'^send_message', send_a_message, name="send_message"),
    url(r'^submit_photo', add_photo, name="submit_photo"),
    url(r'^inspiration', inspiration_view, name='inspiration_view'),
    url(r'^account', my_account, name="my_account"),
    url(r'^messages', messages, name="messages")
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )