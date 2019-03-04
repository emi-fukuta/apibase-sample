import urllib3


class HTTP:

  def __init__(self):
    self.connection = urllib3.PoolManager()

  def release_connection_pool(self):
    return self.connection.clear()

  def request(self, method, url, headers=None, body=None, fields=None):

    try:
      if fields:
        return self.connection.request(method, url, headers=headers, fields=fields)

      return self.connection.request(method, url, headers=headers, body=body)

    except Exception as e:
      raise e
