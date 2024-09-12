// Solicita ao usuário que digite um número e armazena na variável
let numero = prompt("Digite um número para ver sua tabuada:");

// Converte o valor de entrada para um número inteiro
numero = parseInt(numero);

// Verifica se o valor inserido pelo usuário é um número válido
if (!isNaN(numero)) {
    console.log(`Tabuada de ${numero}:`);
    // Loop de 1 a 10 para calcular e exibir os múltiplos do número inserido
    for (let i = 1; i <= 10; i++) {
        console.log(`${numero} x ${i} = ${numero * i}`);
    }
} else {
    console.log("Por favor, insira um número válido.");
}
