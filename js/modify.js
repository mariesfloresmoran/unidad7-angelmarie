const newS = document.querySelector("#UpdateSer");
const prefix = document.querySelector("#Uprefix");
const logo = document.querySelector("#Ulogo");
const buton = document.querySelector("#modifybutton");


window.onload = async function setData(){
    try {
        const response = await fetch(`http://localhost:8000/transactions/service/${id}/`);
        const data = await response.json();
        newS.value = data.newS;
        prefix.value = data.prefix;
        logo.value = data.logo;
        } catch (error) {
            console.log(error);
        }
  }


buton.onclick = async function (event) {
  event.preventDefault();

  const body = {
    "name": newS.value,
    "prefix":prefix.value,
    "logo":logo.value,

  };

    
  try {
    await fetch("http://127.0.0.1:8000/transactions/service", {
      method: "PUT",
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
