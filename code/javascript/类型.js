//对象的创建的 ： 方式1 
var person = {
  name: "阿明",
  age: 36,
  toString:function(){
      console.log(" 我是一个 person")
  }
};
person.toString();
console.log(person);

//方法2 
var people=new Object();
people.name="名歌";
people.age=33;
console.log(people);

console.log(typeof 123);
console.log(typeof "123");
console.log(typeof true)
console.log(typeof Array("hello"));
console.log(typeof person);
console.log(typeof people);

let nums=[1,9,7,2];
nums.push(3);
nums.shift();  //头部pop出
nums.pop();  //尾部pop ，等效于 unshift
console.log(nums);
console.log(nums.sort());
console.log(nums.reverse());

