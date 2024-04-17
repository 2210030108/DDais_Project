"""
URL configuration for washing_machine_recommendation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recommender.views import washing_machine_list
from recommender.views import washing_machine_filter
urlpatterns = [
path('admin/', admin.site.urls),
    # URL pattern for the washing machine list page
    path('', washing_machine_list, name='washing_machine_list'),

    # URL pattern for the filtering page
    path('filter/', washing_machine_filter, name='washing_machine_filter'),

    # Additional URL patterns for specific filtering actions or result pages can be added here
]
