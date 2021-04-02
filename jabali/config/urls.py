"""school_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import routers
from rest_framework.authtoken import views
from grades.views import GradeClassViewSet, GradeScoreViewSet, GradeSubjectViewSet
from users.views import UserViewSet
from teachers.views import TeacherViewSet
from students.views import StudentViewSet
from django.urls import include, path
router = routers.SimpleRouter()

router.register(r'accounts', UserViewSet)
router.register(r'students', StudentViewSet)
router.register(r'tutors', TeacherViewSet)
router.register(r'subjects', GradeSubjectViewSet)
router.register(r'class', GradeClassViewSet)
router.register(r'grading', GradeScoreViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]
