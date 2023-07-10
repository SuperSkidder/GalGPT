import base64
import io
from PIL import Image
import requests
import time

url = ""


def generate(prompt, negative):
    payload = {

        "prompt": prompt,
        "negative_prompt": negative,
        "steps": 25,
        "seed": -1,
        "width": 512,
        "height": 512,
        "restore_faces": 'false',
        "override_settings": {
            "sd_model_checkpoint": "majicMIX.safetensors[e4a30e4607]"
            # "sd_model_checkpoint": "cetus.safetensors [876b4c7ba5]"
        },
        "sampler_index": "DPM++ SDE Karras"
    }

    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
    r = response.json()

    for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(',', 1)[0])))
        image.save('out/output' + str(time.time()) + '.png')
        print("已生成图片:" + prompt)
