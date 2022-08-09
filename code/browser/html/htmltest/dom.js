window.onload=function(){
var els=document.getElementsByClassName("title");
var node=document.createTextNode("hello");
var node2=document.createTextNode("world");


for(let item of els){
console.log(item.getAttribute("class"))
}

}
