import fitz
import pdfplumber

# 表格提取
with pdfplumber.open("") as f:
    page = f.pages[0]
    table = page.extract_table()
    for row in table:
        row = list(filter(lambda x: x is not None, row))
        print(row)

# 圖片提取
doc = fitz.open("")
for page in doc:
    tupleImages = page.get_images()
    for xref in tupleImages:
        xref = xref[0]
        img = doc.extract_image(xref)
        image_filename = f"{xref}.{img['ext']}"
        with open(image_filename, 'wb') as f:
            f.write(img["image"])
