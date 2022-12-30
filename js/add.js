const boton = document.querySelector("#boton");
const input = document.querySelectorAll("#duedateforyment");
const monto = document.querySelectorAll("amount");
const select = document.querySelector("#service");

boton.onclick = async function (event) {
  event.preventDefault();

  const body = {
    "name": select.value,
    "paymentDate":input,
    "amount":monto,

  };

  
  try {
    await fetch("http://127.0.0.1:8000/service", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    Swal.fire({
      text: "Pago Agregado",
      icon: "success",
    });
  } catch (error) {
    Swal.fire({
      text: error,
      icon: "error",
    });
  }
};
