from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.dashboard_redirect, name='dashboard_redirect'),
    path("__debug__/", include("debug_toolbar.urls")),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('dashboard/download', views.download, name='download'),
    path('dashboard/preview', views.preview, name='preview'),
    path('dashboard/upload/students', views.upload_student_excel, name='upload_student_excel'),
    path('dashboard/upload/grades', views.upload_grade_excel, name='upload_grade_excel'),
    path('dashboard/preview-student-dataset', views.student_preview_dataset, name='preview-dataset'),
    path('dashboard/preview-grades-dataset', views.grade_preview_dataset, name='preview-dataset'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
