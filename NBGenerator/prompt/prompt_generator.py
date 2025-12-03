__all__ = ["generate_prompt"]

def generate_prompt(hallucination_type):
    # 선택지 매핑 테이블
    options = {
        1: 'simply returned original image',
        2: 'pose',
        3: "facial identity",
        4: "outfit",
        5: "proportion",
        6: "background",
        7: "person",
        8: "perspective or depth",
        9: "object",   # unwanted objects
    }

    # 입력 문자열 → 정수 리스트 변환
    try:
        indices = [int(x.strip()) for x in hallucination_type.split(",")]
    except ValueError:
        raise ValueError("❌ 숫자만 입력해야 합니다. 예: 1,2")

    # --------------------------------------------
    # ✔ SPECIAL CASE: 입력이 1 또는 2만 포함된 경우
    # --------------------------------------------
    if set(indices).issubset({1, 2}):
        return (
            "Apply only the pose to the given image (Image 1). "
            "Do not apply or transfer any belongings, people, or visual elements from the keypoint image (Image 2) itself."
        )

    # --------------------------------------------
    # ✔ 나머지는 기존 로직 수행
    # --------------------------------------------

    # object 제거 여부 (9번 선택 시)
    remove_unwanted_object = 9 in indices

    # 1~8번은 일반 hallucination 항목으로 구성
    base_indices = [i for i in indices if i in range(1, 9)]  # -1, 0 제외
    hallucination_list = [options[i] for i in base_indices]

    # prompt-friendly string 변환
    if len(hallucination_list) == 0:
        hallucination_str = ""
    elif len(hallucination_list) == 1:
        hallucination_str = hallucination_list[0]
    else:
        hallucination_str = ", ".join(hallucination_list[:-1]) + " and " + hallucination_list[-1]

    # 기본 prompt 구성
    if hallucination_str:
        prompt = f"Pose Transfer: stirctly keep the pose of the person from Image 1, but substitute {hallucination_str} with those in Image 2."
    else:
        prompt = "Pose transfer: stictly keep the pose of the person from Image 1."

    # unwanted objects 제거 문구 추가
    if remove_unwanted_object:
        prompt += (
            " Do not include any unwanted objects or unknown from Image 2."
            " Only transfer the person and the selected attributes, not the surrounding objects."
        )

    return prompt