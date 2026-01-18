from django.urls import path, re_path

from department.views import index, slug_view, path_view, uuid_view, show_archive

urlpatterns = [
    # ORDER MATTERS
    re_path(r'^archive/(?P<archive_year>202[0-4])/$', show_archive),
    path('department/<int:id>/', index),
    path('department/<uuid:uuid>/', uuid_view),
    path('department/<slug:slug>/', slug_view),
    path('department/<id>/', index),  #defaults to <str:id>
    path('department/<path:path>/', path_view),
]