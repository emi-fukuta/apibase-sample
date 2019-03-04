from rest_framework import viewsets, exceptions

from .views import CommonAPIView


class CommonViewSet(viewsets.ViewSet, CommonAPIView):
  """
  共通ビューセット
  """
  pass


class CommonModelViewSet(viewsets.ModelViewSet, CommonAPIView):
  """
  共通モデルビューセット
  """
  pass
