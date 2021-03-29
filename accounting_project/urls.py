from django.conf import settings
from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('accounting.apps.connect.urls',
    #     namespace="connect")),
    path('books/', include(('accounting.apps.books.urls',
                           'books'),namespace="books")),
    # path('people/', include('accounting.apps.people.urls',
    #     namespace="people")),
    #
    # path('reports/', include('accounting.apps.reports.urls',
    #     namespace="reports")),
    #
    # path('reports/', include('django_select2.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

