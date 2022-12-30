const newS = document.querySelector("#NewServiceName");
const prefix = document.querySelector("#prefix");
const logo = document.querySelector("#logo");
const buton = document.querySelector("#addbutton");

buton.onclick = async function (event) {
  event.preventDefault();

  const body = {
    "name": newS.value,
    "prefix":prefix.value,
    "logo":logo.value,

  };

  
  try {
    await fetch("http://127.0.0.1:8000/transactions/service", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    Swal.fire({
      text: "Servicio Agregado",
      icon: "success",
    });
  } catch (error) {
    Swal.fire({
      text: error,
      icon: "error",
    });
  }
};
