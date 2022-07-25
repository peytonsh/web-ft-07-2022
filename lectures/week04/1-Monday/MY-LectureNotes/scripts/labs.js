

let firstName= 'peyton'
let lastName= 'shelley'

// console.log(firstName + '   ' + lastName)

// let greeting = `My name is ${firstName} ${lastName}`

// console.log(greeting)


// let a = 4
// let b = 5

// let sum = a + b

// console.log(`the sume of a & b is ${sum}`)

// firstName.length
// lastName.length

// console.log(firstName.length + lastName.length)

// let name = firstName + " " + lastName;

// let result = name.indexof(lastName)

// console.log(result);



// let num1 = 5
// let num2 = 3

// if (num1 > num2){
//     console.log(`${num1} is greater than ${num2}`)
// }
// else if(num1 < num2){
//     console.log(`${num1} is less than ${num2}`)
// }
// else {
//     console.log(`${num1} is equal to ${num2}`)
// }



// let month =6;

// switch (month){
//     case 1:
//     case 3:
//     case 5:
//     case 7:
//     case 8:
//     case 10:
//     case 12: 
//         console.log('This month has 31 days')
//         break;

//     case 4:
//     case 6:
//     case 9:
//     case 11: 
//         console.log('This month has 30 days')
//         break;

//     case 2:
//         console.log('this month has 28 days')
//         break;
    
//     default:
//         console.log(
//         'unknown month')
//         break;
//         }




// let num=1;
// while(num<21){
//     if(num%2==0){
//         console.log(num);
//     }
//     num ++;
// }


// for(num=1;num<= 20; num++){
//     if(num%2==0){
//         console.log(num)
//     }
// }


// for(num=1; num<=30; num++) {
//     if(num%3 ==0 && num%5 != 0){
//         console.log(`${num} + fizz`)
//     }else if(num%5==0 && num%3!=0){
//         console.log(`${num} + buzz`)
//     }else if(num%15==0){
//         console.log(`${num} + fizz + buzz`)
//     }else{
//         console.log(num)
//     }
// }



// for loop solution #1

var str1 = "javascript".split("");


for (var i = 1; i < str1.length; i+=2) {
     str1[i] = "z";
}
console.log( str1.join("") );

// for loop solution #2

let str1 = "javascript";

strArr = str1.split('');

for (k = 0; k < strArr.length; k++){
    if ((k+1) % 2 == 0){
        strArr[k] = "Z"
    }
}
str1 = strArr.join('')

console.log(str1)


//  while loop solution
let str1 = "javascript";
arr = str1.split('')
console.log(arr)
let count = 0
while (count <= arr.length){
    if (count %2 != 0){
        arr[count] = 'Z'
    }
    count += 1
}
console.log(arr.join(''))


// Example output:
// jZvZsZrZpZ OR each letter on a new line
// HINT: You can use  if((i+1) % 2 == 0) to check for even indexes