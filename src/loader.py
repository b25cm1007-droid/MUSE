import os

def get_image_paths(folder_path):
    images = []
    for file in os.listdir(folder_path):
        if file.lower().endswith((".jpg", ".png", ".jpeg")):
            images.append(os.path.join(folder_path, file))
    return images


def load_all_images():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    ai_folder = os.path.join(BASE_DIR, "data", "ai_images")
    artist_folder = os.path.join(BASE_DIR, "data", "artist_images")

    ai_images = get_image_paths(ai_folder)
    artist_images = get_image_paths(artist_folder)

    return ai_images, artist_images