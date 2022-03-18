layui.use("upload", function () {
  var $ = layui.jquery,
    upload = layui.upload;

  upload.render({
    elem: "#test5",
    url: "https://httpbin.org/post", //改成您自己的上传接口
    accept: "video", //视频
    done: function (res) {
      layer.msg("上传成功");
      console.log(res);
    },
  });
});
