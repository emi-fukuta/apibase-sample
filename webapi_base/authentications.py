from rest_framework import authentication


class CommonAuthentication(authentication.TokenAuthentication):
  """
  共通認証処理
  トークンが無効でもエクセプションを発生させない
  """
  def authenticate_credentials(self, key):
    model = self.get_model()
    try:
      token = model.objects.select_related('user').get(key=key)
    except model.DoesNotExist:
      return None

    if not token.user.is_active:
      return None

    return token.user, token
