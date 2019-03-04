from django.db import models


class MySQLCharField(models.Field):

  def __init__(self, *args, **kwargs):
    if kwargs.get('max_length'):
      self.max_length = kwargs.get('max_length')
    super(MySQLCharField, self).__init__(*args, **kwargs)

  def db_type(self, connection):
    if connection.settings_dict['ENGINE'] == 'django.db.backends.mysql':
      return 'char(%s)' % self.max_length
    else:
      return 'varchar'
