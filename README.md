# novelcat-func

Function of Novel category predict with GCF

## Setup

```
$ git git@github.com:tayutaedomo/novelcat-func.git
$ cd novelcat-func
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

### Lint and Formatter

```
$ pip install flake8
$ pip install autopep8
```

settings.json for Visual Studio Code

```
{
  "editor.formatOnSave": true,
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true,
    "python.linting.flake8Args": [
    "--ignore=E111, E114, E402, E501"
  ],
  "python.linting.lintOnSave": true,
  "python.formatting.provider": "autopep8",
    "python.formatting.autopep8Args": [
    "--indent-size=2",
    "--ignore E402"
  ]
}
```

### Download .h5

```
$ cd novelcat-func
$ curl -L -o "etc/model/category_v1.0.0.h5" "https://www.dropbox.com/s/obhtl90tw3xqt36/category_v1.0.0.h5?dl=0"
$ mv etc/model/category_v1.0.0.h5 etc/model/category.h5
```

## Local Development

```
$ cd novelcat-func
$ functions-framework --target hello_get --debug
```

## Deploy to Cloud Functions

```
$ cd novelcat-func
$ gcloud functions deploy predict_category --region asia-northeast1 --runtime python37 --memory 1024MB --timeout 120 --trigger-http --allow-unauthenticated
```
