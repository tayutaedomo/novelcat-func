# import base64
from io import BytesIO
from PIL import Image
import numpy as np
import json
from tensorflow.keras.models import load_model


def hello_get(request):
    return 'Hello World!'


model = None


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

    global model
    if not model:
        model = load_model('etc/model/category.h5', compile=False)

    if content:
        img = Image.open(BytesIO(content)).convert('RGB')
        img_resize = img.resize((229, 229))
        img_np = np.asarray(img_resize) / 255.0
        img_reshape = img_np.reshape(1, 229, 229, 3)

        x = img_reshape
        y = np.argmax(model.predict(x))
        y_proba = model.predict_proba(x)
        y_proba = np.round((y_proba[0] * 100), 5)
        local['predicted'] = True
        local['y'] = y.astype(np.int32)
        local['y_proba'] = y_proba

    return json.dumps(local, cls=MyJsonEncoder), 200, {'Content-Type': 'application/json'}


class MyJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        # elif isinstance(obj, np.floating):
        #     return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyJsonEncoder, self).default(obj)
