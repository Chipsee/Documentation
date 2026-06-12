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
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
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

function getStaticBaseUrl() {
    const script = document.currentScript || document.querySelector('script[src*="/_static/js/material_custom.js"], script[src$="_static/js/material_custom.js"]');
    return new URL("../", script.src);
}

const staticBaseUrl = getStaticBaseUrl();
const docsBaseUrl = new URL("../", staticBaseUrl);
const threeDModelAliases = loadThreeDModelAliases();

function loadThreeDModelAliases() {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', new URL('3d_models/aliases.json', staticBaseUrl).href, false);
    xhr.send();
    return xhr.status == 200 ? JSON.parse(xhr.responseText) : {};
}

function resolveThreeDModelName(fbxName) {
    return threeDModelAliases[fbxName] || fbxName;
}

// A helper to test if FBX 3D file exists, otherwise will remove the HTML link element in another function
function fbxExists(fbxName) {
    let xhr = new XMLHttpRequest();
    xhr.open('HEAD', new URL(`3d_models/${resolveThreeDModelName(fbxName)}.fbx`, staticBaseUrl).href, false);
    xhr.send();
    return xhr.status == 200;
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
                const threeDUrl = new URL("ThreeD/three_d_model.html", docsBaseUrl);
                threeDUrl.searchParams.set("productModel", pcName);
                linkElem.href = threeDUrl.href;
            } else {
                // For the three links, remove the ones that do not have actual fbx files.
                linkElem.remove();
            }
        }

    });
}
addParamToThreeD();
