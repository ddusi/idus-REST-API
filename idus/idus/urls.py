
from django.contrib import admin
from django.urls import path, include
from member import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('signup/', views.signuppage),
    path('member/<int:id>', views.signup),
    path('rest-api-test/', include('rest_api_test.urls'))
]
