/* Header */
window.addEventListener("scroll", function () {
    var header = document.querySelector("header");
    header.classList.toggle("sticky", window.scrollY > 10);
});

/* Scroll And Hide */
function reveal() {
    var reveals = document.querySelectorAll(".reveal");
    for (var i = 0; i < reveals.length; i++) {
        var windowHeight = window.innerHeight;
        var revealtop = reveals[i].getBoundingClientRect().top;
        var revealpoin = 150;

        if (revealtop < windowHeight - revealpoin) {
            reveals[i].classList.add('active');
        }
        else {
            reveals[i].classList.remove('active');
        }
    }
}

window.addEventListener('scroll', reveal);

/* Progress Bar */
const progressBar = document.getElementById("progressBar");
window.addEventListener("scroll", function () {
    let progress = Math.ceil(
        (window.pageYOffset /
            (document.body.scrollHeight - window.innerHeight)) *
        100
    );
    progressBar.style = `width: ${progress}%`;
});

/* Back To Top */
const backToTopButton = document.querySelector("#back-to-top");
if (backToTopButton != null) {
    window.addEventListener("scroll", function scrollFunction() {
        if (window.pageYOffset > 300) {
            if (!backToTopButton.classList.contains("fadeInRight")) {
                backToTopButton.classList.remove("fadeOutRight");
                backToTopButton.classList.add("fadeInRight");
                backToTopButton.style.display = "flex";
            }
        } else {
            if (backToTopButton.classList.contains("fadeInRight")) {
                backToTopButton.classList.remove("fadeInRight");
                backToTopButton.classList.add("fadeOutRight");
                setTimeout(function () {
                    backToTopButton.style.display = "none";
                }, 250);
            }
        }
    });
    backToTopButton.addEventListener("click", function backToTop() {
        window.scrollTo(0, 0);
    });
}

/* Choose  */
const btns_booking = document.querySelectorAll(".booking_nav span");
btns_booking.forEach(function (btn_booking) {
    btn_booking.addEventListener("click", function () {
        document.querySelector(".booking_nav .active").classList.remove("active");
        btn_booking.classList.add("active");
    })
})

/* Responsive Menu Bar */
const menu = document.querySelector(".menu");
const menuBtn = document.querySelector(".menu_btn");
const closeBtn = document.querySelector(".close_btn");

menuBtn.addEventListener("click", () => {
    menu.classList.add("active");
})

closeBtn.addEventListener("click", () => {
    menu.classList.remove("active");
})

/* Hide Password*/
const pwShowHide = document.querySelectorAll(".eye-icon");
pwShowHide.forEach(eyeIcon => {
    eyeIcon.addEventListener("click", () => {
        let pwFields = eyeIcon.parentElement.parentElement.querySelectorAll(".password");

        pwFields.forEach(password => {
            if (password.type === "password") {
                password.type = "text";
                eyeIcon.classList.replace("bx-hide", "bx-show");
                return;
            }
            password.type = "password";
            eyeIcon.classList.replace("bx-show", "bx-hide");
        })

    })
})

/* Open Modal Login */
const lgBtn = document.querySelector(".js_login");
const modal = document.querySelector(".js_modal");
const formLogin = document.querySelector(".form_login");
lgBtn.addEventListener("click", function (e) {
    e.preventDefault();
    modal.classList.add("open");
});

/* Close Modal Login */
modal.addEventListener("click", function (event) {
    modal.classList.remove("open");
});

formLogin.addEventListener("click", function (event) {
    event.stopPropagation();
});
//scroll-ticket
// const toolbar_sale = document.querySelector(".book-ticket");

// window.addEventListener("scroll", function () {
//   let scrollHeight = window.scrollY;
//   console.log("scroll" , toolbar_sale);
//   if (scrollHeight >= 550) {
//     console.log("scroll height" , scrollHeight)
//     console.log("ele" , toolbar_sale)

//     toolbar_sale.style.position = "fixed";
//     toolbar_sale.style.top = "100px";
//     toolbar_sale.style.width = "31%";

//     toolbar_sale.style.left = "0";
//      // Đặt vị trí sticky bên trái
//       // Đặt margin top là 300px
//   } else {
//     // Nếu không cuộn đủ 600px, hủy bỏ kiểu sticky và margin
//     toolbar_sale.style.position = "static";
//     toolbar_sale.style.marginTop = "0";
//     toolbar_sale.style.width = "100%";
//   }
// });

