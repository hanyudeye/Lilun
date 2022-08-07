let arr = [1, 3, 6, 9];
//是否奇数
function is_jishu(num) {
  return !(num % 2 == 0);
}

//数组筛选器
console.log(arr.filter(is_jishu));
