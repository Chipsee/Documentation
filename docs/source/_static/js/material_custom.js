const content_parent = document.getElementById("product");
var imgs = document.getElementsByClassName("product-img");
var imgs_list = new Array();

for ( var i = 0; i < imgs.length; i++ ) {
    var img_tag = imgs[i];
    imgs_list.push([img_tag.getAttribute("alt"), img_tag.getAttribute("src")]);
}


function pr_indicators() {
    var indicator = "<div class='carousel-indicators'>";
    for ( var i = 0; i < imgs.length; i++ ) {
        if (i==0){
            indicator += `<button type="button" class="active" style="background-color:#EF3D30" aria-current="true" data-bs-target="#carouselExample" data-bs-slide-to=${i} aria-label="Slide ${i + 1}"></button>`;
        }else{
            indicator += `<button type="button" style="background-color:#EF3D30" data-bs-target="#carouselExample" data-bs-slide-to=${i} aria-label="Slide ${i + 1}"></button>`;
        }
    }
    indicator += "</div>";
    return indicator
}

function pr_inner(pr_items) {
    var inner = "<div class='carousel-inner'>";
    for ( var i = 0; i < imgs.length; i++ ) {
        var pr_item = pr_items[i];
        if (i==0){
            inner += `<div class="carousel-item active"><img src="${pr_item[1]}" class="d-block img-fluid" alt="${pr_item[0]}">
      <div class="carousel-caption d-none d-md-block">
        <h5 style="color: #fff!important; text-shadow: 2px 2px 7px #000;">${pr_item[0]}</h5>
      </div></div>`;
        }else{
            inner += `<div class="carousel-item"><img src="${pr_item[1]}" class="d-block img-fluid" alt="${pr_item[0]}">
      <div class="carousel-caption d-none d-md-block">
        <h5 style="color: #fff!important; text-shadow: 2px 2px 7px #000;">${pr_item[0]}</h5>
      </div></div>`;
        }
    }
    inner += "</div>";
    return inner
}

function pr_carousel(indicators, inner) {
    var pr_carousel = "<div id='carouselExample' class='carousel slide' data-bs-ride='carousel' style='padding-bottom: 30px;'>";
    pr_carousel += indicators;
    pr_carousel += inner;
    var btns = `<button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" style="background-image: url(data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23EF3D30'%3e%3cpath d='M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z'/%3e%3c/svg%3e)" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
    <span class="carousel-control-next-icon" style="background-image: url(data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23EF3D30'%3e%3cpath d='M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z'/%3e%3c/svg%3e)" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button></div>`;
    pr_carousel += btns;
    return pr_carousel
}

function pr_modal(carousel) {
    var pr_modal = `<div class="modal-dialog" role="document"><div class="modal-content"><div class="modal-header" style="padding: 0 1rem;background-color: #2D445E;"><button type="button" class="close" data-bs-dismiss="modal" aria-label="Close"><span aria-hidden="true" style="font-size: 1.5rem;color:#fff;">&times;</span></button></div><div class="modal-body">${carousel}</div></div></div>`;
    return pr_modal
}
function thumbnails(pr_items) {
    var tb_row = "";
    for ( var i = 0; i < imgs.length; i++ ) {
        var pr_item = pr_items[i];
        tb_row += `<div class="col-12 col-sm-6 col-lg-3 gy-2"><img class="img-thumbnail mx-auto d-block" style="height: 150px;width: 200px;" src="${pr_item[1]}" alt="${pr_item[0]}" data-bs-target="#carouselExample" data-bs-slide-to="${i}"></div>`;
    }
    return tb_row
}

var listItems = document.querySelectorAll("#product img.product-img");
var listItem = listItems[listItems.length - 1];
var footer = document.querySelector("footer.md-footer");

const newModal = pr_modal(pr_carousel(pr_indicators(), pr_inner(imgs_list)));
const newThumbnail = thumbnails(imgs_list);

const ModalNode = document.createElement('div');
ModalNode.setAttribute('class', 'modal fade');
ModalNode.setAttribute('id', 'imageModal');
ModalNode.setAttribute('tabindex', '-1');
ModalNode.setAttribute('role', 'dialog');
ModalNode.setAttribute('aria-hidden', 'true');
ModalNode.innerHTML = newModal;

const ThumbnailNode = document.createElement('div');
ThumbnailNode.setAttribute('class', 'row');
ThumbnailNode.setAttribute('id', 'gallery');
ThumbnailNode.setAttribute('data-bs-toggle', 'modal');
ThumbnailNode.setAttribute('data-bs-target', '#imageModal');
ThumbnailNode.innerHTML = newThumbnail;


function insertAfter(newNode, existingNode) {
    existingNode.parentNode.insertBefore(newNode, existingNode.nextElementSibling);
}
// Insert modal after footer
insertAfter(ModalNode, footer);
// Insert thumbnail
insertAfter(ThumbnailNode, listItem);


listItems.forEach(element => {
    element.remove()
});

