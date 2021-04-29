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

## Local Development

```
$ functions-framework --target hello_get --debug
```
