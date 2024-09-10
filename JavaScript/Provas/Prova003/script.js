// O programa deve solicitar ao professor o número total de estudantes na turma e, em seguida, pedir que ele insira as notas de cada aluno individualmente. 
// pós receber todas as notas, o programa deverá calcular a média da turma e identificar a maior e a menor nota obtida.

let alunos = window.Number(prompt("Quantidade de alunos"))
let soma = 0 
let maiorNota = -Infinity
let menorNota = Infinity
let controlador = 1

while (controlador <= alunos ) {
    let nota = window.parseFloat(prompt(`Digite a nota do aluno ${controlador}º`))
    soma += nota

    if (nota > maiorNota) {
        maiorNota = nota
    } 
    
    if (nota < menorNota) {
        menorNota = nota
    }

    controlador++
}

let mediaDaTurma = soma / alunos

document.writeln(`A media da turma é: ${mediaDaTurma.toFixed(2)}`);
document.writeln(`, A maior nota da turma é: ${maiorNota}`);
document.writeln(`, A menor nota da turma é: ${menorNota}`);