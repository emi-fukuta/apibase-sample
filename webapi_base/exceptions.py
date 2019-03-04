from rest_framework.views import exception_handler


def common_exception_handler(exc, context):
  """
  共通エクセプションハンドラ
  エラー詳細情報のキーを'detail'ではなく'error'にする
  """
  response = exception_handler(exc, context)

  # キーをdetailからerrorに置き換える
  if response and response.data and response.data.get('detail'):
    response.data['error'] = response.data.pop('detail')

  return response
