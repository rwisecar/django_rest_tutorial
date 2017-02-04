from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from snippets import views


# Create a router and register viewsets with that router

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = format_suffix_patterns([
    url(r'^$', include(router.urls)),
    url(r'api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
])
