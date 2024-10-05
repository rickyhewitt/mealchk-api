# mealchk-cli
# providers/gcloud.py
# ricky@rickyhewitt.dev

from google.cloud import vision

# Provider must feature an image_to_string function
def image_to_string(img):
    print("Provider: gcloud")

    client = vision.ImageAnnotatorClient()

    with open(img, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)

    if "full_text_annotation" in response:
        print("Image analysis complete via gcloud: ")
        for page in response.full_text_annotation.pages:
            print("Confidence: ", page.confidence, "\n")
        print(response.full_text_annotation.text)
    else:
        print("Invalid image")

    return response.full_text_annotation.text