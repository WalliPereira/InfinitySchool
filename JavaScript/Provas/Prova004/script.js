// Sua tarefa é criar um módulo JavaScript que ofereça aos usuários a possibilidade de inserir um número inteiro positivo e, em resposta, calcular o fatorial desse número e também a sequência de Fibonacci até aquele número.

let numInt = parseInt(prompt("Digite um numero inteiro positivo:"))
let fatorial = 1
let fib1 = 0, fib2 = 2, next

// Calculo do numero Fatorial
if (numInt >=0) {
    for (let i = 1; i <= numInt; i++) {
        fatorial *= i
    }

console.log("Fatorial de" + numInt + " é: " + fatorial)

// Sequencia de Fibonacci

console.log("Sequencia de Fibonacci ate " + numInt + ":")
while (fib1 <= numInt) {
    console.log(fib1)

    next = fib1 +fib2
    fib1 = fib2
    fib2 = next
} 
} else {
    console.log("Por favor, insira um numero inteiro positivo")
}