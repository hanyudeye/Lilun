// 检查 unicode 的 a ，unicode 码是 61; 

r=/\u{61}/ug;

// console.log(r.test('ababab'));

var r = /\d/;
// 注意看，返回值是一个数组，除了匹配到的元素之外，还有一个 index 属性
console.log(r.exec('123')); // ["1", index: 0, input: "123"]