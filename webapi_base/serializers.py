from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


class CommonAuthTokenSerializer(serializers.Serializer):
  """
  トークン認証シリアライザ
  """
  email    = serializers.CharField(label=_("email"))
  password = serializers.CharField(
      label=_("password"),
      style={'input_type': 'password'},
      trim_whitespace=False
  )

  def validate(self, attrs):
    email    = attrs.get('email')
    password = attrs.get('password')

    if email and password:
      user = authenticate(request=self.context.get('request'),
                          email=email, password=password)

      # The authenticate call simply returns None for is_active=False
      # users. (Assuming the default ModelBackend authentication
      # backend.)
      if not user:
        msg = _('Unable to log in with provided credentials.')
        raise serializers.ValidationError(msg, code='authorization')
    else:
      msg = _('Must include "username" and "password".')
      raise serializers.ValidationError(msg, code='authorization')

    attrs['user'] = user
    return attrs
