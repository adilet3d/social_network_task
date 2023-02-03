from django.urls  import path
from rest_framework.routers import DefaultRouter    as DR
from mainapp.views import (
    UserView,PostView, RegistrationView,AuthorizationView
    )

router=DR()

router.register('user', UserView , basename='user')
router.register('post', PostView, basename='post')

urlpatterns = [ 
    path('reg/',RegistrationView.as_view()),
    path('login/',AuthorizationView.as_view()),
    ]

urlpatterns += router.urls