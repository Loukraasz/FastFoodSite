function checkPassword() {
    var password = document.getElementById("pass").value;
    var confirmPassword = document.getElementById("conf_pass").value;
    if(password != confirmPassword) {
        document.getElementById("checkP").style.display = "block";
         form.addEventListener("submit", function(event) {
            event.preventDefault();
        });
        return false;
    }else{
        document.getElementById("checkP").style.display = "none";
        return true;
    }
}
function wPass(){
    document.getElementById("w_pass").style.display = "none";
}
function togglePass() {
    var img = document.getElementById("toggle");
     if (img.src.includes("hidden_pass.jpg")) {
        img.src = img.dataset.view;
    } else {
        img.src = img.dataset.hidden;
    }
    var pass = document.getElementById("pass");
    var confPass = document.getElementById("conf_pass");
    if (pass.type === "password") {
        pass.type = "text";
    } else {
        pass.type = "password";
    }
    if (confPass.type === "password") {
        confPass.type = "text";
    } else {
        confPass.type = "password";
    }
}
