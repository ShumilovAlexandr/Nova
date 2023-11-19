from django.core.exceptions import BadRequest
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import FileSerializer
from .upload_file import FileUpload


class FileView(APIView):
    serializer = FileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer(data=request.data)
        try:
            if serializer.is_valid():
                file = FileUpload(serializer.data["name"],
                                  serializer.data["data"])
                result = file.create_and_upload_file()
                return Response(result,
                                status=status.HTTP_201_CREATED)
        except BadRequest as e:
            return JsonResponse(e,
                                status.HTTP_400_BAD_REQUEST)

