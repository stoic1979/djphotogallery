"""gallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static

import album.views as album_views
import reg.views as reg_views
import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', album_views.home, name='home'),
    url(r'^add_album/$', album_views.add_album, name='add_album'),
    url(r'^save_album/$', album_views.save_album, name='save_album'),
    url(r'^show_album/(?P<pk>[0-9]+)/$', album_views.show_album),

    # login/logout
    url(r'^login/$', album_views.login_page, name='login_page'),
    url(r'^logout/$', album_views.logout_page, name='logout_page'),
    url(r'^accounts/logout/$', album_views.logout_page, name='logout_page'),
    url(r'^accounts/login/$', album_views.login_page, name='login_page'),

    # registration
    url(r'^register/$', reg_views.regform, name='regform'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
