from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from user.ErrorMessage import ErrorMessage
from rest_framework.response import Response
from rest_framework.status import (HTTP_400_BAD_REQUEST,HTTP_200_OK,HTTP_404_NOT_FOUND,HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def login_user(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},
                        status=HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({'message':ErrorMessage.EXCEPTION_OCCURRED}, status=HTTP_500_INTERNAL_SERVER_ERROR)