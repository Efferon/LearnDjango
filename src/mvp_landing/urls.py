from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mvp_landing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #Set signup.html as the main homepage
    # keep all the signup stuff in the signups folder (i.e. keep same stuff together)
    url(r'^$', 'signups.views.home', name='home'),
    url(r'^thank-you$', 'signups.views.thankyou', name='thankyou'),
    url(r'^about-us$', 'signups.views.aboutus', name='aboutus'),


)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,
		document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,
		document_root=settings.MEDIA_ROOT)
	