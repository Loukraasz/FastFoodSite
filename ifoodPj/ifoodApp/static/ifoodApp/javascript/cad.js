const emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

window.onload = function(){
    pass();
    email();
}


function pass(){
    var pass = document.getElementById("id_password");
    var label = document.getElementById("pass_count");
    if (label.textContent != ""){
        pass.placeholder="";

    }
}
function email(){
    var email = document.getElementById("id_email");
    var label = document.getElementById("email");
    if (label.textContent != ""){
        email.value="";
        email.placeholder="";

    }
}
function remove(la,inp,pla){
    var user = document.getElementById(inp)
    var label = document.getElementById(la);
    if (label.style.display = "inline" ){
         console.log(label.textContent);
            label.style.display = "none";
            user.placeholder=pla;
    }
}

function cad(){
    const fill = document.getElementById("fill");
    if (fill.style.display = "block" ){
            fill.style.display = "none";
            
    }
} 
function passwordCheck(){
    var pass = document.getElementById("id_password").value;
    if (pass.length < 8) {
        document.getElementById("pass").style.display = "block";
    } else {
        document.getElementById("pass").style.display = "none";
    }
}
function emailValidate(){
    var cadEmail = document.getElementById("id_email");
    if(!emailRegex.test(cadEmail.value)){
        form.addEventListener("submit", function(event){
            event.preventDefault();
        });
  
    }
  
}
function togglePass() {
    var img = document.getElementById("toggle");
     if (img.src.includes("hidden_pass.jpg")) {
        img.src = img.dataset.view;
    } else {
        img.src = img.dataset.hidden;
    }
    var pass = document.getElementById("id_password");
    if (pass.type === "password") {
        pass.type = "text";
    } else {
        pass.type = "password";
    }
}