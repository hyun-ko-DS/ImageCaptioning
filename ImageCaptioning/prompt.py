prompt_img_org = """
Describe this image in a strict JSON format:
{
"sex": man / woman / male baby / female baby
"object": "nothing" if no object belonging to the person, "{object in body parts}" if the person has an object e.g. "a pencil on the person's right hand",
"outfit": an outfit type with color,
"background": a short description of the person's surrounding backgrounds in a phrase
}
"""

prompt_nano_org = """
Describe this image in a strict JSON format:
{
"sex": man / woman / male baby / female baby
"background": a short description of the person's surrounding backgrounds
}
"""

prompt_nano_rendered = """
Describe this rendered image in a strict JSON format:
{
"sex": man / woman / male baby / female baby
"pose": a detailed description of bing the person's pose
"background": a short description of the person's surrounding backgrounds
}
"""