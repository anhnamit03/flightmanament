function addClickEvenntToCardTickets(){
    var checked_card = document.querySelectorAll(".card_ticket");

checked_card.forEach(function (cardTicket) {
    cardTicket.addEventListener("click", function (event) {
        let choose1 = false;
        let choose2 = false;

        var show = cardTicket.querySelector('.price_1');
        var show2 = cardTicket.querySelector('.price_2');
        var detailTicket = cardTicket.querySelector('.itinerary-part-offer');
        var detailTicket2 = cardTicket.querySelector('.itinerary-part-offer.second');
        var icon = show.querySelector('.fa-solid');
        var icon2 = show2.querySelector('.fa-solid');

        show.addEventListener('click', function () {
            if (choose2) {
                detailTicket2.style.display = 'none';
                icon2.classList.remove('fa-chevron-up');
                icon2.classList.add('fa-chevron-down');
                choose2 = false;
            }


            if (detailTicket.style.display === 'none' || detailTicket.style.display === '') {
                detailTicket.style.display = 'flex';
                icon.classList.remove('fa-chevron-down');
                icon.classList.add('fa-chevron-up');
                choose1 = true;
            } else {
                detailTicket.style.display = 'none';
                icon.classList.remove('fa-chevron-up');
                icon.classList.add('fa-chevron-down');
                choose1 = false;
            }
        });


        show2.addEventListener('click', function () {
            if (choose1) {
                detailTicket.style.display = 'none';
                icon.classList.remove('fa-chevron-up');
                icon.classList.add('fa-chevron-down');
                choose1 = false;
            }
            if (detailTicket2.style.display === 'none' || detailTicket.style.display === '') {
                detailTicket2.style.display = 'flex';
                icon2.classList.remove('fa-chevron-down');
                icon2.classList.add('fa-chevron-up');
                choose2 = true;
            } else {
                detailTicket2.style.display = 'none';
                icon2.classList.remove('fa-chevron-up');
                icon2.classList.add('fa-chevron-down');
                choose2 = false
            }
        });
    });
});

}



document.addEventListener('DOMContentLoaded', function () {
    let choose1 = false;
    let choose2 = false;

    var show = document.querySelector('.price_1');
    var show2 = document.querySelector('.price_2');
    var detailTicket = document.querySelector('.itinerary-part-offer');
    var detailTicket2 = document.querySelector('.itinerary-part-offer.second');
    var icon = show.querySelector('.fa-solid');
    var icon2 = show2.querySelector('.fa-solid');
    show.addEventListener('click', function () {
        if (choose2) {
            detailTicket2.style.display = 'none';
            icon2.classList.remove('fa-chevron-up');
            icon2.classList.add('fa-chevron-down');
            choose2 = false;
        }


        if (detailTicket.style.display === 'none' || detailTicket.style.display === '') {
            detailTicket.style.display = 'flex';
            icon.classList.remove('fa-chevron-down');
            icon.classList.add('fa-chevron-up');
            choose1 = true;
        } else {
            detailTicket.style.display = 'none';
            icon.classList.remove('fa-chevron-up');
            icon.classList.add('fa-chevron-down');
            choose1 = false;
        }
    });
    show2.addEventListener('click', function () {
        if (choose1) {
            detailTicket.style.display = 'none';
            icon.classList.remove('fa-chevron-up');
            icon.classList.add('fa-chevron-down');
            choose1 = false;
        }
        if (detailTicket2.style.display === 'none' || detailTicket.style.display === '') {
            detailTicket2.style.display = 'flex';
            icon2.classList.remove('fa-chevron-down');
            icon2.classList.add('fa-chevron-up');
            choose2 = true;
        } else {
            detailTicket2.style.display = 'none';
            icon2.classList.remove('fa-chevron-up');
            icon2.classList.add('fa-chevron-down');
            choose2 = false
        }
    });
});
document.addEventListener('DOMContentLoaded', function () {
    var show12 = document.querySelector('.input_group.hanhkhach');
    var detailTicket = document.querySelector('.list-customer');

    var choose1 = false;
    var choose2 = false;

    show12.addEventListener('click', function (event) {
        event.stopPropagation(); // Ngăn chặn sự kiện click ngoại tuyến (bấm vào show12 không ẩn detailTicket)

        if (choose2) {
            var detailTicket2 = document.querySelector('.itinerary-part-offer.second');
            var icon2 = document.querySelector('.show-button i.fa-chevron-up');
            detailTicket2.style.display = 'none';
            icon2.classList.remove('fa-chevron-up');
            icon2.classList.add('fa-chevron-down');
            choose2 = false;
        }

        if (detailTicket.style.display === 'none' || detailTicket.style.display === '') {
            detailTicket.style.display = 'block';
            choose1 = true;
        } else {
            detailTicket.style.display = 'none';
            choose1 = false;
        }
    });

    // Lắng nghe sự kiện click toàn cục
    document.addEventListener('click', function (event) {
        if (!show12.contains(event.target) && !detailTicket.contains(event.target)) {
            detailTicket.style.display = 'none';
            choose1 = false;
        }
    });

    // Ngăn chặn sự kiện click trong detailTicket lan ra ngoài
    detailTicket.addEventListener('click', function (event) {
        event.stopPropagation();
    });
});








var today = new Date();
var formattedToday = today.toISOString().split("T")[0]; // Lấy ngày hôm nay dưới định dạng yyyy-MM-dd

var goDateInput = document.getElementById("go_date");


goDateInput.setAttribute("min", formattedToday); // Đặt ngày tối thiểu cho ngày đi là ngày hôm nay






var minusButton_nomal = document.querySelector("#minus_button_nomal");
var plusButton_nomal = document.querySelector("#plus_button_nomal");
var minusButton_child = document.querySelector("#minus_button_child");
var plusButton_child = document.querySelector("#plus_button_child");
var minusButton_baby = document.querySelector("#minus_button_baby");
var plusButton_baby = document.querySelector("#plus_button_baby");
var quantityPassengerInput = document.getElementById("quantity_passenger");
var quantitychild = document.getElementById("quantity_child");
var quantitynomal = document.getElementById("quantity_nomal");
var quantitybaby = document.getElementById("quantity_baby");
var passenger_child = 0;
var passenger_nomal = 0;
var passenger_baby = 0;

function updatePassengerQuantity() {
    quantityPassengerInput.textContent = passenger_nomal + passenger_child + " Hành khách";
    quantitynomal.textContent = passenger_nomal;
    quantitychild.textContent = passenger_child;
    quantitybaby.textContent = passenger_baby;
}

minusButton_nomal.addEventListener("click", function () {
    if (passenger_nomal > 1) {
        passenger_nomal--;
        updatePassengerQuantity();
    }
});

plusButton_nomal.addEventListener("click", function () {
    if (passenger_nomal + passenger_child < 9) {
        passenger_nomal++;
        updatePassengerQuantity();
    }
});

minusButton_child.addEventListener("click", function () {
    if (passenger_child > 0) {
        passenger_child--;
        updatePassengerQuantity();
    }
});

plusButton_child.addEventListener("click", function () {
    if (passenger_child < 2 && passenger_nomal + passenger_child < 9) {
        passenger_child++;
        updatePassengerQuantity();
    }
});

minusButton_baby.addEventListener("click", function () {
    if (passenger_baby > 0) {
        passenger_baby--;
        updatePassengerQuantity();
    }
});

plusButton_baby.addEventListener("click", function () {
    if (passenger_baby < 2) {
        passenger_baby++;
        updatePassengerQuantity();
    }
});




var fromDateShow = document.querySelector('#destination');
var toDateShow = document.querySelector('#departure');
var placeArray = [];

fetch('assets/json/place.json')
    .then(response => response.json())
    .then(data => {
        data.forEach(item => {
            const value = Object.values(item)[0];
            placeArray.push(value);
        });

        var fromDateOptions = '<option></option>';
        placeArray.forEach((place) => {
            fromDateOptions += `<option>${place}</option>`;
        });
        fromDateShow.innerHTML = fromDateOptions;

        fromDateShow.addEventListener("change", function () {
            var selectedValue = this.value;

            var newArray = placeArray.filter(function (place) {
                return place !== selectedValue;
            });

            var toDateOptions = '<option></option>';
            newArray.forEach((place) => {
                toDateOptions += `<option>${place}</option>`;
            });
            toDateShow.innerHTML = toDateOptions;
        });
    })
    .catch(error => {
        console.error('Error fetching JSON:', error);
    });
/// lấy ticket
var listTicket;
fetch('assets/json/ticket.json')
    .then(response => response.json())
    .then(data => {
        listTicket = data;


    })
    .catch(error => {
        console.error('Error fetching JSON:', error);
    });


var listTicket1;
fetch('assets/json/time_fly.json')
    .then(response => response.json())
    .then(data => {
        listTicket1 = data;


    })
    .catch(error => {

        console.error('Error fetching JSON:', error);
    });


document.getElementById("search").addEventListener("click", function () {
    var selectedFromDate = fromDateShow.value;
    var selectedToDate = toDateShow.value;
    var chooseDateInput = document.getElementById("choose_date");
    if (selectedFromDate == "" || selectedToDate==""||chooseDateInput=="") {
        alert("Vui lòng nhập đầy đủ thông tin")
    }
    else{
    fetch("assets/json/place.json")
        .then(response => response.json())
        .then(data => {
            var objectList = createObjectsFromJson(data);
            console.log(objectList, selectedFromDate, selectedToDate);

            // lấy mã
            var correspondingCodeFrom = null;
            var correspondingCodeTO = null;

            for (var i = 0; i < objectList.length; i++) {
                var cityData = objectList[i];
                var cityValue = Object.values(cityData)[0];

                console.log(cityData, cityValue);
                if (cityValue === selectedFromDate) {
                    correspondingCodeFrom = Object.keys(cityData)[0];
                    console.log(correspondingCodeFrom);

                }
                if (cityValue === selectedToDate) {
                    correspondingCodeTO = Object.keys(cityData)[0];
                }
            }
            // lấy danh sách

            var time_fly;
            for (var i = 0; i < listTicket1.length; i++) {
                if ((listTicket1[i].place_1 === correspondingCodeFrom && listTicket1[i].place_2 === correspondingCodeTO) ||
                    (listTicket1[i].place_1 === correspondingCodeTO && listTicket1[i].place_2 === correspondingCodeFrom)) {
                    time_fly = listTicket1[i].time;
                    console.log("sdssss")
                    console.log(typeof listTicket1[i].time, listTicket1[i].time)
                    break;

                }
            }
            function set_time(value) {
                if (value <= 24) {
                    return value;
                }
                else {
                    return value - 24;
                }
            }
            console.log(time_fly);

            var listItemTicket = [];
            for (var i = 0; i < listTicket.length; i++) {
                if (
                    (listTicket[i].destination === correspondingCodeFrom && listTicket[i].departure === correspondingCodeTO)) {
                    listItemTicket.push(listTicket[i]);
                }
            }


           var add_item_for_card =  (a) =>{
            var cardTicketElement = document.querySelector('.card_tickets')
            cardTicketElement.innerHTML = "";
            for (var i = 0; i < a.length; i++) {
                var item = document.createElement("div");
                item.innerHTML = `


                <div class="group-content">
                    <div class="card-content">
                        <div class=" from">
                            <h3 class="time_from">${a[i].start} h</h3>
                            <h4 class="sign_from">${correspondingCodeFrom}</h4>
                        </div>

                        <div class=" center">
                            <i class="fa-solid fa-plane"></i>
                            <h5 class="time_all">${time_fly}h</h5>
                        </div>

                        <div class=" to">
                            <h3 class="time_to">${set_time(parseFloat(a[i].start) + time_fly)} h</h3>
                            <h4 class="sign_to">${correspondingCodeTO}</h4>
                        </div>
                    </div>


                    <div class=" prices">
                        <div class="price_1">
                            <a href="#">${a[i].price} VNĐ</a>
                            <i class="fa-solid fa-chevron-down"></i>


                        </div>

                        <div class="price_2">
                            <a href="#">${parseInt(a[i].price) * 3} VNĐ</a>
                            <i class="fa-solid fa-chevron-down"></i>
                        </div>
                    </div>
                </div>

                <div class="itinerary-part-offer">
                    <div class="offer-branch">
                        <div class="content-header">
                            <h1>Phổ thông siêu tiết kiệm</h1>
                        </div>
                        <div class="show-ticket">
                            <h1>Hết vé</h1>
                        </div>
                        <div class="extand-ticket">
                            <ul>
                                <li>
                                    <i class="fa-solid fa-check" style="color: #018de5;"></i>
                                    Hành lý xách tay: Không quá 12kg
                                </li>
                                <li>
                                    <i class="fa-solid fa-xmark" style="color: crimson;"></i>
                                    Không bao gồm hành lý ký gửi
                                </li>
                                <li>
                                    <i class="fa-solid fa-dollar-sign" style="color: #018de5;"></i>
                                    Thay đổi mất phí
                                </li>
                                <li>
                                    <i class="fa-solid fa-xmark" style="color: crimson;"></i>
                                    Không được phép đổi chuyến tại sân bay
                                </li>
                                <li>
                                    <i class="fa-solid fa-dollar-sign" style="color: #018de5;"></i>
                                    Hoàn/hủy vé mất phí
                                </li>
                                <li>
                                    <i class="fa-regular fa-paper-plane" style="color: #0d65fd;"></i>
                                    Tích lũy 10% số dặm
                                </li>
                                <li>
                                    <a href="#">XEM CHI TIẾT</a>
                                </li>

                            </ul>
                        </div>
                    </div>
                    <div class="offer-branch">
                        <div class="content-header">
                            <h1>Phổ thông siêu tiết kiệm</h1>
                        </div>
                        <div class="show-ticket">
                            <h1>Hết vé</h1>
                        </div>
                        <div class="extand-ticket">
                            <ul>
                                <li>
                                    <i class="fa-solid fa-check" style="color: #018de5;"></i>
                                    Hành lý xách tay: Không quá 12kg
                                </li>
                                <li>
                                    <i class="fa-solid fa-xmark" style="color: crimson;"></i>
                                    Không bao gồm hành lý ký gửi
                                </li>
                                <li>
                                    <i class="fa-solid fa-dollar-sign" style="color: #018de5;"></i>
                                    Thay đổi mất phí
                                </li>
                                <li>
                                    <i class="fa-solid fa-xmark" style="color: crimson;"></i>
                                    Không được phép đổi chuyến tại sân bay
                                </li>
                                <li>
                                    <i class="fa-solid fa-dollar-sign" style="color: #018de5;"></i>
                                    Hoàn/hủy vé mất phí
                                </li>
                                <li>
                                    <i class="fa-regular fa-paper-plane" style="color: #0d65fd;"></i>
                                    Tích lũy 10% số dặm
                                </li>
                                <li>
                                    <a href="#">XEM CHI TIẾT</a>
                                </li>

                            </ul>
                        </div>
                    </div>
                    <div class="offer-branch">
                        <div class="content-header">
                            <h1>Phổ thông siêu tiết kiệm</h1>
                        </div>
                        <div class="show-ticket">
                            <h1>Hết vé</h1>
                        </div>
                        <div class="extand-ticket">
                            <ul>
                                <li>
                                    <i class="fa-solid fa-check" style="color: #018de5;"></i>
                                    Hành lý xách tay: Không quá 12kg
                                </li>
                                <li>
                                    <i class="fa-solid fa-xmark" style="color: crimson;"></i>
                                    Không bao gồm hành lý ký gửi
                                </li>
                                <li>
                                    <i class="fa-solid fa-dollar-sign" style="color: #018de5;"></i>
                                    Thay đổi mất phí
                                </li>
                                <li>
                                    <i class="fa-solid fa-xmark" style="color: crimson;"></i>
                                    Không được phép đổi chuyến tại sân bay
                                </li>
                                <li>
                                    <i class="fa-solid fa-dollar-sign" style="color: #018de5;"></i>
                                    Hoàn/hủy vé mất phí
                                </li>
                                <li>
                                    <i class="fa-regular fa-paper-plane" style="color: #0d65fd;"></i>
                                    Tích lũy 10% số dặm
                                </li>
                                <li>
                                    <a href="#">XEM CHI TIẾT</a>
                                </li>

                            </ul>
                        </div>
                    </div>
                    <div class="offer-branch">
                        <div class="content-header">
                            <h1>Phổ thông siêu tiết kiệm</h1>
                        </div>
                        <div class="show-ticket">
                            <h1>Hết vé</h1>
                        </div>
                        <div class="extand-ticket">
                            <ul>
                                <li>
                                    <i class="fa-solid fa-check" style="color: #018de5;"></i>
                                    Hành lý xách tay: Không quá 12kg
                                </li>
                                <li>
                                    <i class="fa-solid fa-xmark" style="color: crimson;"></i>
                                    Không bao gồm hành lý ký gửi
                                </li>
                                <li>
                                    <i class="fa-solid fa-dollar-sign" style="color: #018de5;"></i>
                                    Thay đổi mất phí
                                </li>
                                <li>
                                    <i class="fa-solid fa-xmark" style="color: crimson;"></i>
                                    Không được phép đổi chuyến tại sân bay
                                </li>
                                <li>
                                    <i class="fa-solid fa-dollar-sign" style="color: #018de5;"></i>
                                    Hoàn/hủy vé mất phí
                                </li>
                                <li>
                                    <i class="fa-regular fa-paper-plane" style="color: #0d65fd;"></i>
                                    Tích lũy 10% số dặm
                                </li>
                                <li>
                                    <a href="#">XEM CHI TIẾT</a>
                                </li>

                            </ul>
                        </div>
                    </div>
                </div>
                <div class="itinerary-part-offer second">

                    <div class="offer-branch">
                        <div class="content-header">
                            <h1>Phổ thông siêu tiết kiệm</h1>
                        </div>
                        <div class="show-ticket">
                            <h1>Hết vé</h1>
                        </div>
                        <div class="extand-ticket">
                            <ul>
                                <li>
                                    <i class="fa-solid fa-check" style="color: #018de5;"></i>
                                    Hành lý xách tay: Không quá 12kg
                                </li>
                                <li>
                                    <i class="fa-solid fa-xmark" style="color: crimson;"></i>
                                    Không bao gồm hành lý ký gửi
                                </li>
                                <li>
                                    <i class="fa-solid fa-dollar-sign" style="color: #018de5;"></i>
                                    Thay đổi mất phí
                                </li>
                                <li>
                                    <i class="fa-solid fa-xmark" style="color: crimson;"></i>
                                    Không được phép đổi chuyến tại sân bay
                                </li>
                                <li>
                                    <i class="fa-solid fa-dollar-sign" style="color: #018de5;"></i>
                                    Hoàn/hủy vé mất phí
                                </li>
                                <li>
                                    <i class="fa-regular fa-paper-plane" style="color: #0d65fd;"></i>
                                    Tích lũy 10% số dặm
                                </li>
                                <li>
                                    <a href="#">XEM CHI TIẾT</a>
                                </li>

                            </ul>
                        </div>
                    </div>
                    <div class="offer-branch">
                        <div class="content-header">
                            <h1>Phổ thông siêu tiết kiệm</h1>
                        </div>
                        <div class="show-ticket">
                            <h1>Hết vé</h1>
                        </div>
                        <div class="extand-ticket">
                            <ul>
                                <li>
                                    <i class="fa-solid fa-check" style="color: #018de5;"></i>
                                    Hành lý xách tay: Không quá 12kg
                                </li>
                                <li>
                                    <i class="fa-solid fa-xmark" style="color: crimson;"></i>
                                    Không bao gồm hành lý ký gửi
                                </li>
                                <li>
                                    <i class="fa-solid fa-dollar-sign" style="color: #018de5;"></i>
                                    Thay đổi mất phí
                                </li>
                                <li>
                                    <i class="fa-solid fa-xmark" style="color: crimson;"></i>
                                    Không được phép đổi chuyến tại sân bay
                                </li>
                                <li>
                                    <i class="fa-solid fa-dollar-sign" style="color: #018de5;"></i>
                                    Hoàn/hủy vé mất phí
                                </li>
                                <li>
                                    <i class="fa-regular fa-paper-plane" style="color: #0d65fd;"></i>
                                    Tích lũy 10% số dặm
                                </li>
                                <li>
                                    <a href="#">XEM CHI TIẾT</a>
                                </li>

                            </ul>
                        </div>
                    </div>
                </div>

      `;
                item.classList.add("card_ticket")
                cardTicketElement.appendChild(item)
            }
           }
           add_item_for_card(listItemTicket);
        })
        .catch(error => console.error("Error fetching JSON:", error));
    function createObjectsFromJson(data) {
        var objectList = [];

        data.forEach(function (item) {
            var newObject = { ...item }
            objectList.push(newObject);
        });
        return objectList;
    }
     }
})

addClickEvenntToCardTickets()


