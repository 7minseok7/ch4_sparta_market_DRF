from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    # as_view() 메서드를 사용하여 클래스 내 호출 가능한 함수로 변환할 수 있다.
    path("", views.ProductListAPIView.as_view(), name="product_list"),
    path("<int:productId>/", views.ProductDetailAPIView.as_view(), name="product_detail"),
]
