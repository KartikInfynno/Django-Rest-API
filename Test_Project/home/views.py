
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import APISerializer
from .models import ApiTest
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view
from home import serializer
# from rest_framework.generics import ListAPIView

# def response(data, error, message):
#     res = {
#         'error' : error,
#         'data' : data,
#         'message' : message,
#     }
#     return res

class TestApiView(APIView):

    def get_object(self,pk):
        try:
            return ApiTest.objects.filter(pk=pk)
        except ApiTest.DoesNotExist:
            pass

    def get(self, request, pk=None):
        if pk:
            menu = self.get_object(pk)
        else:
            menu = ApiTest.objects.all()
        ser = APISerializer(menu,many= True)
        return Response(ser.data,status=status.HTTP_200_OK)


    def post(self, request):
        serialize = APISerializer(data= request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk=None):

        print(pk)
        update = ApiTest.objects.get(id=pk)
        print(update)
        serializer = APISerializer(instance=update, data= request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()

        response.data = {
            'message': 'Todo Updated Successfully',
            'data': serializer.data
        }

        return response

    def delete(self, request, pk, format=None):
        data =  ApiTest.objects.get(pk=pk)

        data.delete()

        return Response({
            'message': 'Todo Deleted Successfully'
        })
