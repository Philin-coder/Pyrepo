"""
URL configuration for stip project.

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
from django.urls import path, re_path, include
from stip_app import views

product_patterns = [
    path("", views.products),
    path("new", views.new),
    path("top", views.top),
    path("comments", views.comments),
    path("questions", views.questions)
]


urlpatterns = [
    #path('index/<int:id>', views.index),
    path('', views.index),
    # path('about',views.about,kwargs={"name":"Tom", "age": 38}),
    path('about/', views.about),
    path('contact/', views.contact),
    # re_path(r"^user/(?P<name>\D+)/(?P<age>\d+)",views.user),
    path("user/", views.user),
    path("products/<int:id>", include(product_patterns)),
    path("details", views.details),
    #path("access/<int:age>", views.access),
]
