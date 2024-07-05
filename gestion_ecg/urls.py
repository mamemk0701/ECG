from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('medecins/', include('medecins.urls')),  # Inclure les URLs des médecins
    path('patient/', include('patients.urls')),  # Inclure les URLs des patients
]