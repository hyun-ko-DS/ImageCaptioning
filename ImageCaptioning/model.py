from transformers import pipeline

import time
from utils import *

pipe = pipeline("image-text-to-text", model="OpenGVLab/InternVL3_5-4B-HF", trust_remote_code=True)

def image_captioning(img_path, prompt):
    img_size = im_show(img_path)
    img_obj = Image.open(img_path)
    img_resized = resize_by_input(img_obj, img_size[0], img_size[1], 512)

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image", "url": img_resized},
                {"type": "text", "text": prompt}
            ]
        },
    ]

    t0 = time.time()
    output_txt = pipe(text=messages)
    clean_txt = extract_json(output_txt[0]["generated_text"][-1]["content"])
    print(f"Elapsed time: {time.time() - t0 :.2f}")
    return extract_json(clean_txt)