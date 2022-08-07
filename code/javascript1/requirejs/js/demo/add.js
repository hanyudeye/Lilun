//定义模块
// 遵从AMD规范

define(function () {
  function add(x, y) {
    return x + y;
  }

  function show() {
    console.log("hello,world");
  }

  //对外暴露
  return {
    outAdd: add,
    outShow: show,
  };
});
