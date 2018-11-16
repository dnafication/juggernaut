from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework import routers
from jugapp import views
from djangorest import settings

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

router.register(r'scripts', views.ScriptViewSet)
router.register(r'hosts', views.HostViewSet)
router.register(r'mappings', views.MappingViewSet)
router.register(r'tests', views.TestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tests/<test_id>/execute', views.execute_test, name='executetest'),
    path('scripts/<script_id>/validate', views.validate_script, name='validatescript'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
