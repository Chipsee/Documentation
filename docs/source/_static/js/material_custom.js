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
            inner += `<div class="carousel-item active"><h6 style="color:#444444!important;text-align:center;" class="fs-5">${pr_item[0]}</h6><img src="${pr_item[1]}" class="d-block img-fluid" alt="${pr_item[0]}"></div>`;
        }else{
            inner += `<div class="carousel-item"><h6 style="color:#444444!important;text-align:center;" class="fs-5">${pr_item[0]}</h6><img src="${pr_item[1]}" class="d-block img-fluid" alt="${pr_item[0]}"></div>`;
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
function thumbnails() {
    for ( var i = 0; i < imgs.length; i++ ) {
        let img_thumbnail = imgs[i];
        img_thumbnail.setAttribute('data-bs-target', '#carouselExample');
        img_thumbnail.setAttribute('data-bs-slide-to', `${i}`);
        // img_thumbnail.style.width = "200px";
        // img_thumbnail.style.height = "140px";
        img_thumbnail.classList.add('pdf-width-70', 'img-fluid');
        img_thumbnail.parentNode.classList.add('h-100', 'd-flex', 'align-items-center', 'justify-content-center');
    }
}

// Update thumbnails
thumbnails();

var footer = document.querySelector("footer.md-footer");
const newModal = pr_modal(pr_carousel(pr_indicators(), pr_inner(imgs_list)));

const ModalNode = document.createElement('div');
ModalNode.setAttribute('class', 'modal fade');
ModalNode.setAttribute('id', 'imageModal');
ModalNode.setAttribute('tabindex', '-1');
ModalNode.setAttribute('role', 'dialog');
ModalNode.setAttribute('aria-hidden', 'true');
ModalNode.innerHTML = newModal;


function insertAfter(newNode, existingNode) {
    existingNode.parentNode.insertBefore(newNode, existingNode.nextElementSibling);
}
// Insert modal after footer
insertAfter(ModalNode, footer);

// Sidebar menu
const sidebar_menu = document.querySelector(".md-sidebar.md-sidebar--secondary");
const sidebar_item = document.querySelector(".md-nav.md-nav--secondary > .md-nav__list > li.md-nav__item");

if (sidebar_item != null){
    sidebar_menu.style.backgroundColor = "#f4f7f7";
}

// A helper to test if FBX 3D file exists, otherwise will remove the HTML link element in another function
function fbxExists(fbxName) {
    let xhr = new XMLHttpRequest();
    xhr.open('HEAD', `/_static/3d_models/${fbxName}.fbx`, false);
    xhr.send();
    return xhr.status != 404;
}

// Add query param to let 3D js know what product it needs to display, open 3D page.
function addParamToThreeD() {
    const productPN = document.querySelector("#d-model>p");

    if (!productPN) {
        return;
    }
    
    ["epc", "ppc", "aio"].forEach((pcType) => {
        const linkElem = document.getElementById(`3d-link-${pcType}`);
        if (!productPN.textContent.includes(pcType.toUpperCase())) {
            // Avoid AIO mistaken as PPC.
            linkElem.remove();
            return;
        }
        if (linkElem) {
            const pcName = `${pcType.toUpperCase()}-${productPN.textContent.split(' ')[0].split('-').slice(1, ).join('-')}`;
            if (fbxExists(pcName)) {
                linkElem.href += `?productModel=${pcName}`;
            } else {
                // For the three links, remove the ones that do not have actual fbx files.
                linkElem.remove();
            }
        }

    });
}
addParamToThreeD();


