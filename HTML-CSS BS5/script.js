const produtosContainer = document.querySelector(".produtos")
const categoriasContainer = document.querySelector(".categorias")
const modal = document.querySelector("#modal")

let produtos = []

function abrirModal() {
    modal.style.display = 'flex'
}

function fecharModal() {
    modal.style.display = 'none'
}

async function captarProdutos() {
    try {
        const resposta = await fetch("http://localhost:80/products")
        const dados = await resposta.json()

        produtos = dados

        mostrarNaTela(dados)
    } catch (erro) {
        alert(erro.message)
    }  
}

function mostrarNaTela(arrayProdutos) {
    produtosContainer.innerHTML = '';

    arrayProdutos.forEach(produto => {
        produtosContainer.innerHTML += `
            <div class="produto">
                <img src="${produto.image}" />

                <h4>${produto.title}</h4>

                <div>
                    <p>R$ ${produto.price}</p>

                    <button>
                        <img src="https://cdn-icons-png.flaticon.com/512/126/126510.png" />
                    </button>
                </div>
            </div>
        `
    })
}

async function captarCategorias() {
    try {
        const resposta = await fetch("http://localhost:80/categories")
        const dados = await resposta.json()

        dados.forEach(categoria => {
            categoriasContainer.innerHTML += `
                <div>
                    <input oninput="filtrarPorCategoria()" name="categoria" type="checkbox" value="${categoria}" />
                    <label>${categoria}</label>
                </div>
            `
        })
    } catch (erro) {
        alert(erro.message)
    }  
}

function filtrarPorCategoria() {
    const inputsChecados = document.querySelectorAll("input[name=categoria]:checked")
    const filtros = []

    inputsChecados.forEach(input => filtros.push(input.value))

    let produtosFiltrados = produtos.filter(produtos => filtros.includes(produtos.category))

    mostrarNaTela(filtros.length > 0 ? produtosFiltrados : produtos)
   
}

captarCategorias()
captarProdutos()

/* 
    - http://localhost:80/categories
    - Captar a div de categorias
    - criar uma função para fazer a chamada de api nesta rota
    - Para cada Categoria crie um input checkbox com o value='category' e o nome da categoria
    - Quando o input for selecionado, filtre os produtos em cima da categoria
*/