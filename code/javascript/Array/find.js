let arr=[1,3,5,7,7,9]

function shaixuan(num){
    return num==7;
}

// find 只筛选出一个,而 filter 筛选好多
// let v=arr.find(shaixuan)
//findIndex 输出 满足条件的索引
let v=arr.findIndex(shaixuan)

console.log(v)