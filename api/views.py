from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def root(request):
    return Response({'message': "server is running"})


