from django.conf.urls import url

from . import views


urlpatterns = [

    # Step by step
    url(r'^getting-started/$',
        views.GettingStartedView.as_view(),
        name="getting-started")
]
