import pymupdf


def extract_pdf_text(file_path):
    document = pymupdf.open(file_path)
    full_text = ""

    num_pages = len(document)

    for page in document:
        page_text = page.get_text()
        full_text += page_text + "\n"

    document.close()

    return full_text, num_pages

def render_pdf_page(pdf_path, page_number):

    output_image_path = f"data/page_{page_number}.png"

    with pymupdf.open(pdf_path) as document:

        page = document[page_number - 1]

        image = page.get_pixmap(
            matrix=pymupdf.Matrix(2, 2)
        )

        image.save(output_image_path)

    return output_image_path

def get_page_count(pdf_path):
    # Open the PDF
    with pymupdf.open(pdf_path) as document:
        # Determine the number of pages
        page_count = len(document)
    # Return that number
    return page_count

def render_pdf_pages(pdf_path, start_page, end_page):
    image_paths = []

    for page_number in range(start_page, end_page + 1):
        image_path = render_pdf_page(pdf_path, page_number)
        image_paths.append(image_path)

    return image_paths


