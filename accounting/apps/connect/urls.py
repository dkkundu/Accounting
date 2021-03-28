from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(

    # Step by step
    url(r'^getting-started/$',
        views.GettingStartedView.as_view(),
        name="getting-started")
)
