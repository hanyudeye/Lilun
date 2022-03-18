layui.use("form", function () {
  var form = layui.form;

  //各种基于事件的操作，下面会有进一步介绍
  form.on("input(test)", function (data) {
    console.log(data);
  });

  form.on("checkbox(test2)", function (data) {
    console.log(data);
  });

  form.on("select(aihao)", function (data) {
    console.log(data);
  });
});
