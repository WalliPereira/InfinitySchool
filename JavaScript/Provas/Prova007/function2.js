
// Função para calcula a gorjeta com base no valor e qualidade do serviço
const calcularGorjeta = (valorTotal, qualidadeServico, callback) => {
    let percentual;

    switch (qualidadeServico) {
        case 'bom':
            percentual = 0.15; // 15% de gorjeta
            break;
        case 'regular':
            percentual = 0.10; // 10% de gorjeta
            break;
        case 'ruim':
            percentual = 0.05; // 5% de gorjeta
            break;
        default:
            percentual = 0;
    }

    const gorjeta = valorTotal * percentual;
    callback(gorjeta);
};

// Função para exibir o resultado
const exibirResultado = (gorjeta) => {
    const resultado = document.getElementById('resultado');
    resultado.textContent = `A gorjeta recomendada é: R$ ${gorjeta.toFixed(2)}`;
};

const calcularButton = document.getElementById('calcular');
calcularButton.addEventListener('click', () => {
    const valorTotal = parseFloat(document.getElementById('total').value);
    const qualidadeServico = document.getElementById('servico').value;

    if (!isNaN(valorTotal) && valorTotal > 0) {
        calcularGorjeta(valorTotal, qualidadeServico, exibirResultado);
    } else {
        alert('Por favor, insira um valor válido para a conta.');
    }
});
