let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}


const toolbar_sale = document.querySelector(".toolbar_sale");

window.addEventListener("scroll", function () {
  let scrollHeight = window.scrollY;
  console.log("scroll" , toolbar_sale);
  if (scrollHeight >= 550) {
    console.log("scroll height" , scrollHeight)
    console.log("ele" , toolbar_sale)

    toolbar_sale.style.position = "fixed";
    toolbar_sale.style.top = "100px";
    toolbar_sale.style.width = "31%";

    toolbar_sale.style.left = "0";
     // Đặt vị trí sticky bên trái
      // Đặt margin top là 300px
  } else {
    // Nếu không cuộn đủ 600px, hủy bỏ kiểu sticky và margin
    toolbar_sale.style.position = "static";
    toolbar_sale.style.marginTop = "0";
    toolbar_sale.style.width = "100%";
  }
});

var jsonPath = "assets/json/sale.json";

document.addEventListener("DOMContentLoaded", function() {


  fetch(jsonPath)
      .then(response => response.json())
      .then(data => {
          var saleContainer = document.getElementById("saleContainer");

          data.forEach(item => {
              var card = document.createElement("div");
              card.classList.add("card");

              var image = document.createElement("div");
              image.classList.add("image");
              var imgElement = document.createElement("img");
              imgElement.src = item.image;
              image.appendChild(imgElement);

              var title = document.createElement("div");
              title.classList.add("title");
              var titleElement = document.createElement("h1");
              titleElement.textContent = item.title;
              title.appendChild(titleElement);

              var des = document.createElement("div");
              des.classList.add("des");
              var pElement = document.createElement("p");
              pElement.textContent = item.content;
              var button = document.createElement("button");
              button.textContent = "Xem thêm";
              des.appendChild(pElement);
              des.appendChild(button);

              card.appendChild(image);
              card.appendChild(title);
              card.appendChild(des);

              saleContainer.appendChild(card);
          });
      })
      .catch(error => console.error("Error fetching JSON:", error));
});


var Filter = function(type){
fetch(jsonPath)
    .then(response => response.json())
    .then(data => {
        var objectList = createObjectsFromJson(data);
        console.log(objectList); // In danh sách các đối tượng ra để kiểm tra trong console
    objectList = objectList.filter(o => o.type== type)
    var saleContainer = document.getElementById("saleContainer")
    saleContainer.innerHTML = "";
    for (var i = 0; i < objectList.length; i++)
    {
      var item = document.createElement("div");
      item.innerHTML = `
              <div class="image">
                  <img src="${objectList[i].image}">
              </div>
              <div class="title">
                  <h1>${objectList[i].title}</h1>
              </div>
              <div class="des">
                  <p>${objectList[i].content}</p>
                  <button>Xem thêm</button>
              </div>
      `;
item.classList.add("card")
        saleContainer.appendChild(item)
    }


  })
    .catch(error => console.error("Error fetching JSON:", error));



function createObjectsFromJson(data) {
    var objectList = [];

    data.forEach(function(item) {
        var newObject = {...item}
        objectList.push(newObject);
    });

    return objectList;
}
}













