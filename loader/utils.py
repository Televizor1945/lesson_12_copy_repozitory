import json

from exceptions import WrongImgType

UPLOAD_FOLDER = "uploads/images"
POST_PATH = "posts.json"

def save_uploaded_image(picture):
    filename = picture.filename

    picture.save()

def save_picture(picture):
    allowed_type = ["jpg", "png", "gif", "jpeg"]
    picture_type = picture.filename.split(".")[-1]
    if picture_type not in ["jpg", "png", "gif", "jpeg"]:
        raise WrongImgType(f"Неверный формат файла! Допустим только {', '.join(allowed_type)}!")
    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
    picture.save(picture_path)
    return picture_path

def add_post(post_list, post):
    post_list.append(post)
    with open(POST_PATH, "w", encoding="utf-8") as file:
        json.dump(post_list, file)