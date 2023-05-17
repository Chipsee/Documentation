import re
from typing import List
from bs4 import BeautifulSoup, Tag


def main(**kwargs: BeautifulSoup) -> None:
    """Finds matching thumbnails and create their PDF versions"""
    soup = kwargs["soup"]
    thumbnail_images = soup.find_all(
        "img", attrs={"class": re.compile(r"product-img|img-thumbnail")}
    )
    pdf_thumbnails: List[Tag] = []
    for img in thumbnail_images:
        pdf_figure = soup.new_tag("figure", attrs={"class": "align-center"})
        img_classes = [
            cls_ for cls_ in img.attrs["class"] if re.match(r"pdf-width-\d{1,3}", cls_)
        ]
        pdf_img: Tag = soup.new_tag(
            "img",
            attrs={
                "src": img["src"],
                "alt": img["alt"],
                "class": " ".join(img_classes),
            },
        )
        pdf_figcaption = soup.new_tag("figcaption", attrs={"style": "margin: 5px 0"})

        figcaption_text = soup.new_tag("p", attrs={"class": "caption_text"})
        figcaption_text.append(img["alt"])
        pdf_figcaption.append(figcaption_text)

        pdf_figure.append(pdf_img)
        pdf_figure.append(pdf_figcaption)

        pdf_thumbnails.append(pdf_figure)

    # Create a div containing new PDF thumbnails.
    pdf_div: Tag = soup.new_tag("div", attrs={"class": "product-images pdf-only"})
    for thumbnail in pdf_thumbnails:
        pdf_div.append(thumbnail)

    # Insert PDF Thumbnails after div#gallery
    html_thumbnails_node = soup.find("div", attrs={"id": "gallery"})
    if html_thumbnails_node:
        html_thumbnails_node.insert_after(pdf_div)


if __name__ == "__main__":
    main()
