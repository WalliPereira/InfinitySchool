// Escreva um programa em JavaScript que solicite ao usuário o nome, altura em centímetros e peso de uma pessoa.
// O programa deve calcular o índice de massa corporal (IMC) dessa pessoa, considerando a fórmula IMC = peso / (altura * altura), onde a altura deve ser convertida de centímetros para metros.

let nome  = prompt ("digite o seu nome:") 
        let alturaCentimentros  =  parseFloat(prompt("digite a sua altura em centimetros:"))
        let peso = parseFloat(prompt(" digite o seu peso em quilogramas:")) 
        let alturaMetros = alturaCentimentros / 100
        
        let imc = (peso /(alturaMetros * alturaMetros))

        function classificarIMC(imc) {
            if (imc < 16) {
            return "Baixo peso muito grave "
        } else if (imc >=16 && imc <= 16.99 ) {
            return "Baixo peso grave"
        } else if (imc >= 17 && imc <= 18.49) {
            return "Baixo peso"
        }else if (imc >= 18.5 && imc <= 24.99) {
            return "Peso normal"
        } else if (imc >= 25 && imc <= 29.99) { 
            return "Sobrepeso" 
        }else if  (imc >= 30 && imc <= 34.99) {
            return "Obesidade grau I" 
        }else if (imc >= 35 && imc <= 39.99) {
            return "Obesidade grau II"
        } else {
            return "Obesidade grau III"
         }
    }
    let classificacao = classificarIMC(imc);

console.log("Nome: " + nome);
console.log("IMC: " + imc.toFixed(2));
console.log("Classificação: " + classificacao);