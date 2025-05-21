from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import AuthorSerializer, BookSerializer
from .models import Book, Author

# Create your views here.
class BookNoParameters(APIView):
    def get(self, request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        book = request.data
        serializer = BookSerializer(data=book)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class BookWithParameters(APIView):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        serializer = BookSerializer(Book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        book_to_update = Book.objects.get(id=id)
        serialize = BookSerializer(book_to_update, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, id):
        book_to_delete = Book.objects.get(id=id)
        book_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthorNoParameters(APIView):
    def get(self, request):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        author = request.data
        serializer = AuthorSerializer(data=author)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class AuthorWithParameters(APIView):
    def get(self, request, id):
        author = Author.objects.get(id=id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        author_to_update = Author.objects.get(id=id)
        serializer = AuthorSerializer(author_to_update, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        author_to_delete = Author.objects.get(id=id)
        author_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)