let numUs = parseFloat(window.prompt("Digite um valor inicial"))
let numUs2 = parseFloat(window.prompt("Digite um valor final"))
let ordem = window.prompt("DIgite a ordem").toLowerCase()


if (ordem === 'crescente' ) {
    for (i = numUs; i <= numUs2; i += 1) {
        console.log(i)
    }
} else if (ordem === 'descrecente') {
    for (i = numUs; i >= numUs2; i -= 1) {
        console.log(i)
    }
}