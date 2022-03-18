var canvas = document.getElementById("test-shape-canvas");

ctx = canvas.getContext("2d");

ctx.clearRect(0, 0, 200, 200);
ctx.fillStyle = '#dddddd'; // 设置颜色
ctx.fillRect(10, 10, 130, 130); // 把(10,10)位置大小为130x130的矩形涂色
