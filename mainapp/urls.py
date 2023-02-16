from django.urls  import path
from rest_framework.routers import DefaultRouter    as DR
from mainapp.views import (
    UserView,PostView,
    )
from mainapp.views import LikesModelViewSet, DisLikesModelViewSet


router=DR()

router.register('user', UserView , basename='user')
router.register('post', PostView, basename='post')

urlpatterns = [ 
    path('likes/', LikesModelViewSet.as_view(), name='list_likes'),
    path('dislikes/', DisLikesModelViewSet.as_view(), name='list_dislikes'),
  
    ]

urlpatterns += router.urls