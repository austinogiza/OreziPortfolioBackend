from django.urls import path
from rest_framework import views
from . import views

urlpatterns = [
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('blog/<slug>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('work/', views.WorkListView.as_view(), name="work"),
    path('work/product/', views.ProductFilterListView.as_view(), name="work-product"),
    path("work/flyer/", views.FlyersFilterListView.as_view(), name=""),
    path("work/brand/", views.BrandFilterListView.as_view(), name=""),
    path("work/package/", views.PackageFilterListView.as_view(), name=""),
    path("work/campaign/", views.CampaignFilterListView.as_view(), name=""),
    path("work/communication/", views.CommunicationFilterListView.as_view(), name=""),
    path('search/', views.SearchView.as_view(), name="search"),
    path('tags/', views.TagsView.as_view(), name="tags"),



]
