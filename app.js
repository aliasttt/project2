function hello(){
    alert("this is miguels website")}


document.addEventListener("DOMContentLoaded",function(){

   document.querySelector("form").onsubmit =  function() {

    const gholi = document.querySelector("#name").value;
    alert(`Welcome to this website ${gholi}!`);}
 
   });
