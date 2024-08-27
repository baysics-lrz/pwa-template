from django.urls import path, include
from .views import DocumentationShortView, show_APIDocumentation_Full

urlpatterns = [
    path('observations/', include('observations.api_urls')),
    path('accounts/', include('accounts.api_urls')),
    path('lexicon/', include('lexicon.api_urls')),
    path('doc-short', DocumentationShortView.as_view()),
    path('doc-full', show_APIDocumentation_Full)
]
