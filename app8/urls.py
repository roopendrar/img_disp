from django.urls import path
from app8 import views
app_name="app8"


urlpatterns = [
    path('img_upld/',views.img_upld,name="img_upld"),
    path('img_disp/',views.img_disp,name="img_disp"),
]
