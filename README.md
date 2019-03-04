# webapi_base

Web API 共通ライブラリ

## Start Server
```bash
# htpasswd -sc ~/.htaccess novera-user
# pypi-server -vvv -p 80 -P ~/.htaccess --disable-fallback  /var/www/packages
```

## Upload Package
~/.pypirc
```bash
[distutils]
index-servers =
  internal

[internal]
repository: http://localhost:80
username: 
password: 
```

```bash
python setup.py sdist upload -r internal
```

## Install Package
```bash
pip install --trusted-host localhost --index-url http://localhost/simple/ webapi_base
```
