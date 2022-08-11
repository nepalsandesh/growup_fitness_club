from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import CustomUser
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from rest_framework import generics
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated 



# API Root 
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'token_obtain_pair':reverse('token_obtain_pair', request=request),
        'token_refresh':reverse('token_refresh', request=request),
        'token_verify':reverse('token_obtain_pair', request=request),
        'changepassword':reverse('changepassword', request=request),
    })


#  # This view is commented because we dont need registeration from frontend
# class RegisterView(GenericAPIView):
#     authentication_classes = []
#     permission_classes = [AllowAny]
#     serializer_class = UserSerializer

#     def post(self, request, *args, **kwargs):
#         # print("request data---------------->", request.data)
#         serializer = UserSerializer(data=request.data)
        
#         if serializer.is_valid():
#             # print(serializer.data)
#             serializer.save()
#             return Response({"email":request.data["email"],"message":"account created"},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



#change password
  


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = CustomUser
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        # print(obj)
        return obj

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
