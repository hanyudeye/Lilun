$(function () {
  $(".title").css("background-color", "red");

  $(".content").css("font-size", "45px");

  $(".hide").hide();

  $(".show").click(function (e) {
    e.preventDefault();
    $(".hide").toggle();
  });

  //   $("li").remove(".choose");
  $("li").parent("ul").css("border", "1px solid red");

  //   $("[name=doc]").load("http://phpapi.bb/test.php");

  let name = "wm";
  let age = 35;

  let serialize;
  $("#serialize").click(function (e) {
    serialize = $("form").serialize();
    console.log(serialize);
    $.ajax({
      type: "get",
      url: "http://phpapi.bb/test.php",
      data: serialize,
      dataType: "json",
      success: function (response) {
        console.log(response);
        if (response.status == "ok") $("[name=doc]").val(response.name);
      },
    });
  });

  
});
