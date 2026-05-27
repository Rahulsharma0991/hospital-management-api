from django.contrib import admin
from django.urls import path,include
from  rest_framework_simplejwt.views import TokenRefreshView
from .views import Patient_viewset,Appointment_viewset,Doctor_viewset,Register,Login,Check
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('Patient',Patient_viewset)
router.register("Doctor",Doctor_viewset)
router.register("Appointment",Appointment_viewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('register/', Register.as_view()),
    path('login/', Login.as_view() ),
    path('Check/', Check.as_view() ),
    path('token/refresh/', TokenRefreshView.as_view()),
]


