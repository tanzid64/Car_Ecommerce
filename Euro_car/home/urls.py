from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
    path('brand/<slug:brand_slug>/', views.HomeView.as_view(), name='brand_wise_car'),
    path('brand/details/<pk>/', views.DetailsView.as_view(), name='details'),
    path('brand/details/buy/<int:id>/', views.buy_now, name='buy_now'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
