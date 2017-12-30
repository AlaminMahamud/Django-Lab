from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.models import User

from rest_framework import (
    routers,
    serializers,
    viewsets
)

# serializers define the API representations
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User,
        fields = (
            'url',
            'username',
            'email',
            'is_staff'
        )

# viewsets define the view behavior
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide and easy way of automatically determining the URL Conf
router = routers.DefaultRouter()
rotuer.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'api-auth/', include('rest_framework.urls')),
    url(r'^', include(router.urls))
]
