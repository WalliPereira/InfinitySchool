// Faça um programa que some todos os numero pares De 1 a 20 e retorne no terminal

let soma = 0

for (let num = 1; num <= 21; num++) {
    if (num % 2 === 0){
        soma += num
    }
}

console.log (`${soma}`)