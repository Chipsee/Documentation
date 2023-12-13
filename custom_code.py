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
                "class": " ".join(img_classes) + " pdf-product-img",
            },
        )
        pdf_figcaption = soup.new_tag("figcaption", attrs={"style": "margin: 5px 0"})

        figcaption_text = soup.new_tag("p", attrs={"class": "caption"})
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


    # Setting the product image on the cover page
    if len(thumbnail_images) > 0:
        front_view_img = thumbnail_images[0]["src"]
        prod_img_tag = soup.find("div", attrs={"id": "cover_product_img_area"})
        prod_img_tag["style"] = f"background-image: url('{front_view_img}');"

    remove_toc_number(soup)
    remove_href_of_image(soup)

def remove_toc_number(soup):
    """
    By default, the table of content numbering links like this:
    1. PPC-CM4-050
      1.1. Product Overview
      ...
      1.6. Connectivity 11
        1.6.1. RS232/RS485/CAN
      ...
      1.14. Disclaimer
      
    This method removes the "1." at the start of each link like this:
    PPC-CM4-050
      1. Product Overview
      ...
      6. Connectivity 11
        6.1. RS232/RS485/CAN
      ...
      14. Disclaimer
    """
    toc = soup.find("article", {"id": "doc-toc"})
    all_a_with_num = toc.find_all('a', attrs={'data-numbering' : True})
    for a_with_num in all_a_with_num:
        a_with_num['data-numbering'] = a_with_num['data-numbering'][2:]

def remove_href_of_image(soup):
    """
    By default, in PDF, images have a hyperlink to go to the docs.chipsee.com, because the HTML is:
    <a class="reference internal" href="https://docs.chipsee.com/_images/x.jpg">
      <img alt="power_img" class="align-middle" src="file:...///.../_images/CS10600RA4070P-D-Power.jpg" 
      style="width: 720px;"/>
    </a>
    
    This method removes the `<a class= href= ></a>` and 
    keeps `<img alt= class= src= style= />` such that images in PDF are not clickable.
    
    Becomes: 
    <img alt="power_img" class="align-middle" src="file:...///.../_images/CS10600RA4070P-D-Power.jpg" 
    style="width: 720px;"/>
    """
    img_anchors = soup.find_all('a', href=re.compile('docs.chipsee.com\/_images'))
    for img_anchor in img_anchors:
        img_anchor.replaceWithChildren()

if __name__ == "__main__":
    main()
