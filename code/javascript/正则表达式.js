/*
 * @Descripttion: 正则表达式
 * @version:
 * @Author: hanyudeye
 * @Date: 2022-03-12 21:48:55
 * @LastEditTime: 2022-03-12 21:55:28
 */


let expression = /fuck/g;

let msg = "lorem you need to be fuck ,and fuck  you ";
let match = expression.exec(msg);

// 输出首次匹配的
console.log(match);
console.log(match[0]);

//这两者功能相同
console.log(match.index);
console.log(match['index']);