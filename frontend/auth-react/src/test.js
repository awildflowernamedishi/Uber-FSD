const arr = [1,2,3,4,5]

function test() {
    console.log('hello')
}
const test2 = test
test2()

const test3 = () =>  {
    console.log('hello from anonymous functions')
}
test3()