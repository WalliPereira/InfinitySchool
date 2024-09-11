

let n1 = parseFloat(window.prompt("Digite um numero"))
let n2 = parseFloat(window.prompt("Digite outro numero"))
let n3 = 0

let s = n1 + n2 

for (let soma = n1 + n2; soma <= 15; soma++) {
    n3 = n1 + n2 
    s += " " + n3
    n1 = n2 
    n2 = n3

    console.log(n3)
}
console.log(n3)