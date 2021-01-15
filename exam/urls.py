from django.contrib import admin
from django.urls import path, include
from .views import Index
from exam import views
from rest_framework import routers
router = routers.DefaultRouter()
# routers.register('api', views.MultipleChoiceCRUDCBV,base_name='api')
# router.register('userapi',views.UserCRUDCBV)
router.register('multiplechoiceapi',views.MultipleChoiceCRUDCBV)
router.register('shortansapi',views.ShortAnsCRUDCBV)
router.register('imageansapi',views.ImageAnsCRUDCBV)

urlpatterns = [
    path('', Index.as_view()),
    path('', include(router.urls)),
]
