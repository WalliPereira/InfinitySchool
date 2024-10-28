const metroInput = document.getElementById('metro');
const unidadeDestinoInput = document.getElementById('unidadeDestino');
const converterButton = document.getElementById('converter');
const resultadoDiv = document.getElementById('resultado');

converterButton.addEventListener('click', (e) => {
    e.preventDefault();
    const valorMetro = parseFloat(metroInput.value);
    const unidadeDestino = unidadeDestinoInput.value;
    const resultado = converterMetro(unidadeDestino, valorMetro);
    resultadoDiv.textContent = `Resultado : ${resultado}`;
});

function converterMetro(unidadeDestino, valorMetro) {
    switch (unidadeDestino) {
        case 'Jarda':
            return valorMetro * 1.094;
        case 'Pé':
            return valorMetro * 3.281;
        case 'Polegada':
            return valorMetro * 39.37;
        case 'Milha':
            return valorMetro * 0.000621;
        default:
            return 'Unidade de medida inválida';
    }
}