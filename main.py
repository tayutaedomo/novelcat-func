def hello_get(request):
    return 'Hello World!'


def predict_category(request):
    fields = {}
    for key, value in request.form.to_dict().items():
        fields[key] = value
        print('Processed field: %s %s' % (key, value))

    size = 0
    files = request.files.to_dict()
    for file_name, file in files.items():
        data = file.read()
        size = len(data)
        print('Processed file size: %s' % size)
        print(data)

    return 'OK'
