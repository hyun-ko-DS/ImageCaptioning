from utils import *
from prompt import *
from model import image_captioning

from transformer import pipe
import argparse

def main():
    parser = argparse.ArgumentParser(description='ImageCaptioning Module')
    parser.add_argument('--img_path', type=str, required=True)
    parser.add_argument('--type', type=str, required=True)
    args = parser.parse_args()
    
    img_path = args.img_path
    type = args.type

    if type == "img_org":
        prompt = prompt_img_org
    elif type == "nano_org":
        prompt = prompt_nano_org
    elif type == "nano_rendered":
        prompt = prompt_nano_rendered
    else:
        raise ValueError("Invalid type")

    result = pipe(prompt, img_path)
if __name__ == "__main__":
    main()