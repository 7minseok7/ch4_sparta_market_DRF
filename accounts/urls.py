from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "accounts"
urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),  # 로그인 요청 주소. POST 요청으로 보내야 한다.
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # 토큰 발급 주소
]
