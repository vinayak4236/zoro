console.log("hello there")
let inputbox;
document.getElementById("btn").onclick = function(){
    console.log("button pressed")
    inputbox = document.getElementById("input").value 
    console.log(inputbox)
    //document.getElementById("headline").innerHTML = "you have entered some value";//
    document.getElementById("headline").innerHTML = inputbox;
}