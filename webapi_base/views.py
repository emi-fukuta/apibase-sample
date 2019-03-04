from django.conf import settings
from rest_framework import views, exceptions

from .serializers import CommonAuthTokenSerializer


class CommonAPIView(views.APIView):
  """
  共通APIビュー
  """
  def permission_denied(self, request, message=None):
    """
    開発環境以外は認証エラーも含めて存在なしエラーを返却する
    """
    # ローカル・開発環境はデフォルトのエラーを返却する
    if settings.ENV in ['local', 'development']:
      if request.authenticators and not request.successful_authenticator:
        raise exceptions.NotAuthenticated()
      raise exceptions.PermissionDenied(detail=message)

    # STG・本番環境はすべて404エラーを返却する
    raise exceptions.NotFound(detail=message)


class CommonObtainAuthToken(CommonAPIView):
  """
  共通認証トークン取得ビュー
  """
  serializer_class = CommonAuthTokenSerializer
