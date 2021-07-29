from django.contrib import admin
from django.urls import path,include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from hotel import views
urlpatterns = [

    path('listing',views.Listing.as_view()),
    path('description/<int:pk>',views.Description.as_view()),
    ###path for schema and docs
    path('docs/', include_docs_urls(title='Hotel Api')),
    path('schema', get_schema_view(
        title="Hotel Api",
        description="API for glorify hotel Registration and authentication …",
        version="1.0.0"
    ), name='openapi-schema'),

]
