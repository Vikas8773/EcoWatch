from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('auth/', views.auth, name='auth'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.main, name='main'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('results/', views.results, name='results'),
    path('report/', views.report, name='report'),
    path('predict/', views.predict, name='predict'),
    path('forest/', views.forest, name='forest'),
    path('change/', views.change, name='change'),
    path('dataset/', views.dataset, name='dataset'),
    path('change/analyze_changes/', views.analyze_changes, name='analyze_changes'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
