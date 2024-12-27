from .models import Product

from django.shortcuts import get_object_or_404

# Django Rest Framework 관련
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework import status  # 조금 더 읽기 쉬운 status code 구성을 제공함.

# 아무것도 적지 않으면 `GET` 만 허용, 이외의 요청일 경우 `405 Method Not Allowed`
# DRF의 함수형 뷰의 경우 필수적으로 작성이 필요함.
# 여기서는 GET, POST로 메서드 제한
@api_view(["GET", "POST"])
def product_list(request):
    # Serializer를 마치 데이터가 바인딩된 폼처럼 생각하면 된다.
    if request.method == "GET":  # GET일 때에 대한 처리
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":  # POST일 때에 대한 처리
        serializer = ProductSerializer(data=request.data)

        # is_valid() 메서드의 raise_exception=True 옵션을 주면,
        # 조건 불만족 시 serializers.ValidationError를 발생하게 되고
        # 이렇게 되면 DRF 내부의 예외처리 로직에 의해 처리되어 400(Bad Request) 응답을 반환
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# GET, DELETE로 메서드 제한
@api_view(["GET", "PUT", "DELETE"])
def product_detail(request, productId):
    product = get_object_or_404(Product, id=productId)

    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == "DELETE":
        product.delete()
        data = {"delete": f"Product({productId}) is deleted."}
        return Response(data, status=status.HTTP_200_OK)
