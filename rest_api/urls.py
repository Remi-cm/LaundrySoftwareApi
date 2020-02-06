from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet, basename='profile')
router.register('agency', views.AgencyViewSet, basename='agency')
router.register('clients', views.ClientViewSet, basename='clients')
router.register('shipper', views.ShipperViewSet, basename='shipper')
router.register('shipper-nested', views.ShipperNestedViewSet, basename='shipper-nested')
router.register('laundry', views.LaundryViewSet, basename='laundry')
router.register('laundries', views.LaundryListViewSet, basename='laundries')
router.register('clothe', views.ClotheViewSet, basename='clothe')
router.register('order', views.OrderViewSet, basename='order')
router.register('order-nested', views.OrderDetailViewSet, basename='order-nested')
router.register('order-line', views.OrderLineViewSet, basename='order-line')
router.register('order-line-nested', views.OrderLineDetailViewSet, basename='order-line-nested')
router.register('login', views.LoginViewSet, basename='login')



#router.register('current', views.CurrentUserView.as_view(), basename='current')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('current/', views.CurrentUserView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
