// Considere três notas (n1, n2, n3) e seus respectivos pesos (p1, p2, p3). Calcule a média ponderada das notas e atribua o resultado à variável "media".
// Após o cálculo, exiba a média ponderada no console.
let n1 = 2
let n2 = 4
let n3 = 7

let p1 = 5
let p2 = 8
let p3 = 3

let media = (n1 * p1 * n2 * p2 * n3 * p3)
let somaPeso = (5 + 8 + 3)
let mediaPonderada = media / somaPeso

console.log(mediaPonderada.toFixed(2))