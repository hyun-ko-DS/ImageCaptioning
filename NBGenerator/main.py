import argparse
from prompt.prompt_generator import *
from generate.generate import generate_nanobanana

def main():
    parser = argparse.ArgumentParser(description='NBGenerator: Qwen-Image-Edit Hallucination Fix Module')
    parser.add_argument('--qwen_result', type=str, required=True, help='Path to the 1st result image from qwen_image_edit')
    parser.add_argument('--img_original', type=str, required=True, help='Path to the original image')
    parser.add_argument('--img_rendered', type=str, required=True, help='Path to the rendered keypoint image')
    parser.add_argument('--hallucination_type', type=str, required=True, help='Hallucination type numbers (comma-separated, e.g., "1,2" or "2,4")')
    
    args = parser.parse_args()
    
    qwen_image = args.qwen_result
    original_image = args.img_original
    rendered_image = args.img_rendered
    hallucination_type = args.hallucination_type
    
    # hallucination_type 파싱: "1,2" -> [1, 2]
    try:
        indices = [int(x.strip()) for x in hallucination_type.split(",")]
    except ValueError:
        raise ValueError("❌ hallucination_type은 숫자만 입력해야 합니다. 예: 1,2")
    
    # hallucination_type이 1 또는 2를 포함하면 rendered_image, 그 외에는 original_image 사용
    if any(idx in [1, 2] for idx in indices):
        ref_image = rendered_image
    else:
        ref_image = original_image
    
    prompt = generate_prompt(hallucination_type)
    print(prompt)
    prefix = "result"
    generate_nanobanana(qwen_image = qwen_image, ref_image = ref_image, prefix = prefix, prompt = prompt)

if __name__ == "__main__":
    main()


''' 
argument 세부 설명
--qwen_result: 1차 생성 이미지 경로
--img_original: 원본 이미지 경로
--img_rendered: 렌더링된 키포인트 이미지 경로
--hallucination_type: 할루시네이션 유형 번호 (쉼표로 구분, 예: "1,2" 또는 "2,4")
'''
# python main.py --qwen_result ../test_data/qwen_001.png --img_original ../test_data/ref_full_001.jpg --img_rendered ../test_data/ref_full_001_overlay.png --hallucination_type "5"
# python main.py --qwen_result ../test_data/qwen_002.png --img_original ../test_data/ref_full_002.png --img_rendered ../test_data/ref_full_002_overlay.png --hallucination_type "1"
# python main.py --qwen_result ../test_data/qwen_003.png --img_original ../test_data/ref_full_003.jpg --img_rendered ../test_data/ref_full_003_overlay.png --hallucination_type "8"
# python main.py --qwen_result ../test_data/qwen_004.png --img_original ../test_data/ref_full_004.jpg --img_rendered ../test_data/ref_full_004_overlay.png --hallucination_type "1"
