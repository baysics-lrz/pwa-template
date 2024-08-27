"""webportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
                  re_path(r'^admin/', admin.site.urls),
                  re_path('accounts/', include('django.contrib.auth.urls')),
                  # newly added for the accounts app, please comment out when using AppHook
                  re_path('accounts/', include('accounts.urls')),
                  # newly added for the observations app, please comment out when using AppHook
                  re_path('observations/', include('observations.urls')),
                  # newly added for the contact app
                  re_path('contact/', include('contact.urls', namespace='contact')),
                  # newly added for pages app
                  re_path('', include('pages.urls')),
                  # newly added for map app
                  re_path('', include('map.urls')),
                  # newly added for lexicon app
                  re_path('lexicon/', include('lexicon.urls')),
                  # newly added for capcha
                  re_path(r'^captcha/', include('captcha.urls')),
                  # newly added for Django CMS
                  re_path(r'^', include('cms.urls')),
                  # newly added for Django pwa
                  re_path('', include('pwa.urls')),
                  re_path('api/', include('api.urls')),
                  re_path('offline/', include('offline.urls')),
                  re_path('news/', include('news.urls')),
                  re_path('messages/', include('messenger.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = 'pages.views.error_500'
handler404 = 'pages.views.error_404'