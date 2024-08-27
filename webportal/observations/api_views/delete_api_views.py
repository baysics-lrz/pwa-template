from rest_framework.generics import DestroyAPIView
from rest_framework.exceptions import PermissionDenied
from observations.serializers import *
from observations.models import Category1, Category2, Category3, Category4


class DeleteCategory1(DestroyAPIView):
    queryset = Category1.objects.all()
    serializer_class = Category1Serializer

    # overwriting the destroy-method
    def perform_destroy(self, instance):
        # performing the deleting only if the user in the instance is the one sending the request
        if self.request.user != instance.user:
            raise PermissionDenied('You can not delete entries of other users!')
        else:
            instance.delete()


class DeleteCategory2(DestroyAPIView):
    queryset = Category2.objects.all()
    serializer_class = Category2Serializer

    # overwriting the destroy-method
    def perform_destroy(self, instance):
        # performing the deleting only if the user in the instance is the one sending the request
        if self.request.user != instance.user:
            raise PermissionDenied('You can not delete entries of other users!')
        else:
            instance.delete()


class DeleteCategory3(DestroyAPIView):
    queryset = Category3.objects.all()
    serializer_class = Category3Serializer

    # overwriting the destroy-method
    def perform_destroy(self, instance):
        # performing the deleting only if the user in the instance is the one sending the request
        if self.request.user != instance.user:
            raise PermissionDenied('You can not delete entries of other users!')
        else:
            instance.delete()


class DeleteCategory4(DestroyAPIView):
    queryset = Category4.objects.all()
    serializer_class = Category4Serializer

    # overwriting the destroy-method
    def perform_destroy(self, instance):
        # performing the deleting only if the user in the instance is the one sending the request
        if self.request.user != instance.user:
            raise PermissionDenied('You can not delete entries of other users!')
        else:
            instance.delete()



