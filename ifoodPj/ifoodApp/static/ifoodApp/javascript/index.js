window.onload = function(){
    index();
}


function index(){
    var user = document.getElementById("username")
    var label = document.getElementById("error");
    if (label.textContent != ""){
        
        user.placeholder="";

    }
}
function remove(){
    var user = document.getElementById("username")
    var label = document.getElementById("error");
   
    if (label.style.display = "inline" ){
         console.log(label.textContent);
            label.style.display = "none";
            user.placeholder="Email";
    }
}