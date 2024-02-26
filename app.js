function hello(){
    alert("this is miguels website")}


 

function ali() {
    const x = document.querySelector("#submit").value ;
    alert(`welcome to this website ${x}`)
    

}

document.querySelector("form").onsubmit = ali()