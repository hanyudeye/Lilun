console.log("hello")

// 引入模块，第一个参数必须数组

require(["demo/add"],function(addObj){
	var res=addObj.outAdd(10,20)
	alert(res)
	addObj.outShow()
})
