$(function(){

let title= $("div").filter(".title").attr("class")

$("input").change(
    function(){
        console.log($(this).val())
    }
)

$.get(
"http://localhost:3000/items",
"",
function(data){
    console.log(data)
},
"json"
);


})