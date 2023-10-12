from django.urls import path

from . import views

urlpatterns = (
    path("", views.ProvisioningListView.as_view(), name="list"),
    path("<int:pk>/", views.ProvisioningView.as_view(), name="view"),
    path("<int:pk>/provision/", views.ProvisioningProvisionView.as_view(), name="provision"),
    path("provision/", views.ProvisioningBulkProvisionView.as_view(), name="bulk_provision"),
)
