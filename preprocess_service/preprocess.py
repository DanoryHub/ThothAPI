import json
from PIL import Image

fields_template_mapping = {
    "BNTU_checkout": "./templates/BNTU_checkout/fields.json"
}

def read_json_template(path: str) -> dict:
    with open(path, "r+") as json_file:
        json_str = json_file.read()

    fields_dict = json.loads(json_str)["fields"]
    
    return fields_dict

def crop_image_template(img: Image, document_type: str):
    result = {}

    fields = read_json_template(fields_template_mapping[document_type])

    for field in fields:
        key = list(field.keys())[0]
        
        coordinates = field[key]
        left, top = coordinates["LeftUpper"]
        right_bias, bottom_bias = coordinates["Bias"]
        right = left + right_bias
        bottom = top + bottom_bias
        
        field_img = img.crop((left, top, right, bottom))
        
        result[key] = field_img
    
    return result


