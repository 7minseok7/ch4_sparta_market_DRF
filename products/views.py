from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from .models import Product

# Django Rest Framework 관련
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer

def product_list_html(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products/products.html", context)


def json_01(request):
    products = Product.objects.all()
    json_res = []

    for product in products:
        json_res.append(
            {
                "title": product.title,
                "content": product.content,
                "created_at": product.created_at,
                "updated_at": product.updated_at,
            }
        )

    return JsonResponse(json_res, safe=False)

def json_02(request):
    products = Product.objects.all()
    res_data = serializers.serialize("json", products)
    return HttpResponse(res_data, content_type="application/json")

@api_view(["GET"])
def json_drf(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)