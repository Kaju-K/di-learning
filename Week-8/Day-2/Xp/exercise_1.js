// 1
// function funcOne() {
//     let a = 5;
//     if(a > 1) {
//         a = 3;
//     }
//     alert(`inside the funcOne function ${a}`);
// }

// funcOne()

// It will alert inside the funcOne function 3

// const a = 0;
// function funcTwo() {
//     a = 5;
// }

// function funcThree() {
//     alert(`inside the funcThree function ${a}`);
// }

// // #2.1 - run in the console:
// funcThree()
// funcTwo()
// funcThree()

// it will alert first "inside the funcThree function 0", then "inside the funcThree function 5"
// #2.2 What will happen if the variable is declared 
// with const instead of let ?
// it will alert first "inside the funcThree function 0", give an error in the console because you can't change const

//#3
// function funcFour() {
//     window.a = "hello";
// }


// function funcFive() {
//     alert(`inside the funcFive function ${a}`);
// }

// // #3.1 - run in the console:
// funcFour()
// funcFive()

// // it will alert "inside the funcFive function hello"

// #4
// let a = 1;

// function funcSix() {
//     let a = "test";
//     alert(`inside the funcSix function ${a}`);
// }


// // #4.1 - run in the console:
// funcSix()
// // it will alert "inside the funcSix function test"

// // #4.2 What will happen if the variable is declared 
// // with const instead of let ?

// // it will also alert "inside the funcSix function test"

//#5
// let a = 2;
// if (true) {
//     let a = 5;
//     alert(`in the if block ${a}`);
// }
// alert(`outside of the if block ${a}`);

// // #5.1 - run the code in the console
// // #5.2 What will happen if the variable is declared 
// // with const instead of let ?

// // both will alert first "in the if block 5" and then "outside of the if block 2"