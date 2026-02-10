const emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
function cad(){
    const fill = document.getElementById("fill");
    if (fill.style.display = "block" ){
            fill.style.display = "none";
            
    }
}
function passError(){
    var passError = document.getElementById("pass_count");
    passError.style.display = "none";
}
function pass(){
    var pass = document.getElementById("id_password").value;
    if (pass.length < 8) {
        document.getElementById("pass").style.display = "block";
    } else {
        document.getElementById("pass").style.display = "none";
    }
}
function emailValidate(){
    if(!emailRegex.test(cadEmail.value)){
        
  
}