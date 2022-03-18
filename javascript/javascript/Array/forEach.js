// forEach 为数组的元素执行操作而非筛选

let arr=[1,3,5,8]
let copy=[]
//执行乘方
function pow(n){
    return n*n;
}

arr.forEach(function(item){
    copy.push(item*item)
})
console.log(copy)