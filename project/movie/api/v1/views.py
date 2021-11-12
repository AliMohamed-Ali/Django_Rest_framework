from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from movie.models import Movie
from .serializer import MovieSerializer


@api_view(['GET'])
def hello(request):
    data = {'massage': ' hello from api '}
    return Response(data=data)


@api_view(['GET'])
def movie_list(request):
    movie = Movie.objects.all()
    serializer_movie = MovieSerializer(instance=movie, many=True)
    return Response(data=serializer_movie.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def movie_create(request):
    serializer_movie = MovieSerializer(data=request.data)
    if serializer_movie.is_valid():
        serializer_movie.save()
        data = {
            'massage': 'Success',
            'data': {'id': serializer_movie.data.get('id')}
        }
        return Response(data=data, status=status.HTTP_201_CREATED)
    return Response(data=serializer_movie.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def movie_detail(request, pk):
    movie = Movie.objects.filter(pk=pk)
    if movie.exists():
        print(movie)
        movie = movie.first()
        print(movie)

    else:
        return Response(data={"massage": "failed Movies Doesn't exist "}, status=status.HTTP_400_BAD_REQUEST)
    serializer_movie = MovieSerializer(instance=movie)
    return Response(data=serializer_movie.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def movie_delete(request, pk):
    response = {}
    try:
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        response['data'] = {'massage': 'Successfully Deleted Movie '}
        response['status'] = status.HTTP_200_OK
    except Exception as e:
        response['data'] = {'massage': 'Error While Deleting Movie {} '.format(str(e))}
        response['status'] = status.HTTP_400_BAD_REQUEST
    print('Response ->', response)
    return Response(**response)


@api_view(['PUT', 'PATCH'])
def movie_update(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Exception as e:
        return Response(data={'massage': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        serializer_movie = MovieSerializer(instance=movie, data=request.data)
    elif request.method == 'PATCH':
        serializer_movie = MovieSerializer(instance=movie, data=request.data, partial=True)

    if serializer_movie.is_valid():
        serializer_movie.save()
        return Response(data=serializer_movie.data, status=status.HTTP_200_OK)
    return Response(data=serializer_movie.errors, status=status.HTTP_400_BAD_REQUEST)
