function show(aside){
    aside.style.display = "block";
    
    }
function hideAside(event){
    if (aside.style.display == "block"){
        falseSubmit(event);
        aside.style.display = "none";
    }
}

function falseSubmit(event){
    event.preventDefault();
}
function add(event){
    if (add_remove.value <20){
        falseSubmit(event);
        add_remove.value ++;
        let x = document.getElementById("total");
        const p = document.getElementById("price").innerText;
        p_format = parseFloat(p);
        x_format = parseFloat(x.value);
        x_format += p_format
        format = x_format.toFixed(2);
        x.value = format
    }
}
function remove(event){
    if (add_remove.value > 0){
        falseSubmit(event);
        add_remove.value --;
        let x = document.getElementById("total");
        const p = document.getElementById("price").innerText;
        p_format = parseFloat(p);
        x_format = parseFloat(x.value);
        x_format -= p_format
        format = x_format.toFixed(2);
        x.value = format
    }
    
}