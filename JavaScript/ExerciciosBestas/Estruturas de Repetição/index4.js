// Definir se um numero é par ou não

var numero = parseFloat(window.prompt("Digite um numero"))

var verificacao = function (numero) {
    if (numero % 2 === 0) {
        return `${numero} e par` ;
    } else {
        return `${numero} e impar` ;
    }
}

console.log(verificacao(numero))
