from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.models import Token


@api_view(['POST'])
@permission_classes([])
def signup(request):
    data = {'data': '', 'status': ''}
    user_serialized = UserSerializer(data=request.data)
    if user_serialized.is_valid():
        user_serialized.save()
        data['data'] = {'user': {'email': user_serialized.data.get('email'),
                                 'user': user_serialized.data.get('username'),
                                 'mobile': user_serialized.data.get('mobile'),
                                 'profile_image': user_serialized.data.get('profile_image')
                                 },
                        'token': Token.objects.get(user__username=user_serialized.data.get('username')).key,
                        'massage': 'Created'}
        data['status'] = status.HTTP_201_CREATED
    else:
        data['data'] = user_serialized.errors
        data['status'] = status.HTTP_400_BAD_REQUEST
    return Response(**data)

@api_view(['POST'])
@permission_classes([])
def logout(request):
    try:
        request.user.auth_token.delete()
    except (AttributeError, ObjectDoesNotExist):
        pass
    return Response({'massage':'Success'},status=status.HTTP_204_NO_CONTENT)