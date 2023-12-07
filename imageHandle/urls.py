from django.urls import path
from imageHandle import views
urlpatterns = [
    path('',views.camera_view, name="camera"),
    path('save_screenshot/', views.save_screenshot, name='save_screenshot'),
    path('view_images/', views.view_images, name='view_images'),
]