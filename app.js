function hello(){
    alert("this is miguels website")}

//document.querySelector("#name")
/*function ali() {
    
    alert(`welcome to this website ${x}!`)
    

}
const x = document.querySelector("form").value ;

x.onsubmit = ali();*/
document.addEventListener("DOMContentLoaded",function(){

   document.querySelector("form").onsubmit =  function() {

    const gholi = document.querySelector("#name").value;
    alert(`Welcome to this website ${gholi}!`);}
 
   });
