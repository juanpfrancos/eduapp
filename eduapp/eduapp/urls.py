from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("4dm/", admin.site.urls),
    path("", include("accounts.urls")),
    path("", include("schools.urls")),
    path("", include("field_journal.urls")),
]
