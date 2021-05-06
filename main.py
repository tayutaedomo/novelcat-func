# import base64
from io import BytesIO
from PIL import Image


def hello_get(request):
    return 'Hello World!'


# model = None


def predict_category(request):
    local = {
        'predicted': False
    }

    fields = {}
    for key, value in request.form.to_dict().items():
        fields[key] = value
        print('Processed field: %s %s' % (key, value))

    content = None
    size = 0

    files = request.files.to_dict()
    for file_name, file in files.items():
        content = file.read()
        size = len(content)
        print('Processed file size: %s' % size)
        # print(content)

    # global model
    # if not model:
    #     model = load_model('etc/model/category-2.h5', compile=False)

    if content:
        # local['file_base64'] = str(base64.b64encode(content), 'utf-8')

        img = Image.open(BytesIO(content)).convert('RGB')
        print('img', img)
        # img_resize = img.resize((229, 229))
        # img_np = np.asarray(img_resize) / 255.0
        # img_reshape = img_np.reshape(1, 229, 229, 3)

    # x = img_reshape
    # y = np.argmax(model.predict(x))
    # y_proba = model.predict_proba(x)
    # y_proba = np.round((y_proba[0] * 100), 5)

    return 'OK'
