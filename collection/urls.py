from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # path('pipeline', PipelineView.as_view(), name='pipeline_apiview'),
    path('movies', MovieView.as_view(), name='movies'),
    path('collection', CollectionView.as_view(), name='collection'),
    path('collection/<uuid:uuid>', Collection_detail.as_view(), name='collection-detail'),
    path('request-count', RequestCountView.as_view(), name='request-count'),

]

urlpatterns = format_suffix_patterns(urlpatterns)