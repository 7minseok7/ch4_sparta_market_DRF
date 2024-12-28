from .models import Product

from django.shortcuts import get_object_or_404

# Django Rest Framework 관련
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework import status  # 조금 더 읽기 쉬운 status code 구성을 제공함.

# 로그인 여부에 따른 기능 제한 관련
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# 특정 Http Method에 대한 처리를 함수로 분리하기 위해 클래스형 뷰로 변환
class ProductListAPIView(APIView):

    # 로그인을 하지 않았을 경우,
    # IsAuthenticated 클래스는 클래스형 뷰 전체에 대해 전부 차단하나
    # IsAuthenticatedOrReadOnly 클래스는 Read에 해당하는 GET 요청은 허용해 준다.
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):  # GET 메서드에 대한 처리
        # Serializer를 마치 데이터가 바인딩된 폼처럼 생각하면 된다.
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):  # POST 메서드에 대한 처리
        serializer = ProductSerializer(data=request.data)

        # is_valid() 메서드의 raise_exception=True 옵션을 주면,
        # 조건 불만족 시 serializers.ValidationError를 발생하게 되고
        # 이렇게 되면 DRF 내부의 예외처리 로직에 의해 처리되어 400(Bad Request) 응답을 반환
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProductDetailAPIView(APIView):
    def get_object(self, productId):
        return get_object_or_404(Product, id=productId)

    def get(self, request, productId):
        product = self.get_object(productId)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
        
    def put(self, request, productId):
        product = self.get_object(productId)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
            
    def delete(self, request, productId):
        product = self.get_object(productId)
        product.delete()
        data = {"delete": f"Product({productId}) is deleted."}
        return Response(data, status=status.HTTP_200_OK)
