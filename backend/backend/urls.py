from django.conf.urls import patterns, include, url
from django.contrib import admin
from middleware.token_authentication import EmailUserObtainAuthToken

urlpatterns = patterns('',
    url(r'^api-token-auth/', EmailUserObtainAuthToken.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
