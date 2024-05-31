import easyocr


class OCRService:
    def __init__(self):
        self.reader = easyocr.Reader(['en'])

    def get_doc_content(self, images_list: list) -> list:
        content_list = []
        for image in images_list:
            image_content = self.reader.readtext(image)
            content_list.append(image_content)
        return content_list
