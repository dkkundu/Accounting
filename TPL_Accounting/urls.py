from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'TPL_Accounting.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # admin/
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('accounting.apps.connect.urls',
        namespace="connect")),
    url(r'^books/', include('accounting.apps.books.urls',
        namespace="books")),
    url(r'^people/', include('accounting.apps.people.urls',
        namespace="people")),
    url(r'^reports/', include('accounting.apps.reports.urls',
        namespace="reports")),

    # third party
    url(r'^select2/', include('django_select2.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
