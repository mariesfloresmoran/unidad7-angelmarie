const url = 'http://localhost:8000/transactions/service/';

const container =document.querySelector(".row");

async function getpagos(){
    const response =await fetch(url);
    const data =await  response.json();
    console.log(data);
    data.results.forEach((pays) => {
        container.innerHTML += renderPay(pays);
    });
}
getpagos();

function renderPay(pays){
    // console.log("pays", pays)
    return `
    <div class="col col-lg-11">
        <div class=" alert alert-success" role="alert">
          <span class="material-symbols-outlined float-start me-2">
            payments
            </span>            
          <b id="service">${pays.name}</b> 
          <span class="float-center">
            <b id="payment_date" class="ms-5" >${pays.fecha_pago}</b>
          </span>
          <span class="float-end">
            <span class="material-symbols-outlined float-start ">
              attach_money
              </span>
              <span id="amount">${pays.monto}</span>
          <div class="col-md-6">
    
          </div>
    
        </div>
    `;
}

