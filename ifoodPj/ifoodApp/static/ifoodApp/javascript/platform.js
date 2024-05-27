function show(aside){
    aside.style.display = "block"

}
function add(){
    if (add_remove.value <20){
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
function remove(){
    if (add_remove.value > 0){
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