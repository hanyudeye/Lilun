const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const { window } = new JSDOM(`<!DOCTYPE html>`);
const $ = require('jQuery')(window);
// console.log($)  // 查看 jquery 是否能够执行


var arr = [2, 3, 45];
var arr1 = { 0: 3, 1: 4, 2: 3, length: 3 };

// arr.forEach(element => {

// });

$.each(arr1, function (index, value) {

    console.log(index + " >>> " + value)

})