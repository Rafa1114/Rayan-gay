function adicionarItem(){

let nome = document.getElementById("nomeItem").value;
let quantidade = document.getElementById("quantidadeItem").value;

let estoque = JSON.parse(localStorage.getItem("estoque")) || [];

estoque.push({
nome: nome,
quantidade: quantidade
});

localStorage.setItem("estoque", JSON.stringify(estoque));

alert("Item adicionado!");

}

let tabela = document.getElementById("tabela");

if(tabela){

let estoque = JSON.parse(localStorage.getItem("estoque")) || [];

estoque.forEach((item, index) => {

let linha = tabela.insertRow();

let col1 = linha.insertCell(0);
let col2 = linha.insertCell(1);
let col3 = linha.insertCell(2);

col1.innerText = item.nome;
col2.innerText = item.quantidade;

col3.innerHTML = `<button onclick="removerItem(${index})">Remover</button>`;

});

}

let nome = document.getElementById("nomeItem").value;
let quantidade = document.getElementById("quantidadeItem").value

function removerItem(index){

let estoque = JSON.parse(localStorage.getItem("estoque")) || [];

estoque.splice(index, 1);

localStorage.setItem("estoque", JSON.stringify(estoque));

location.reload();

}
// Mostrar/ocultar senha
function toggleSenha() {
    const senhaInput = document.getElementById("senha");

    if (senhaInput.type === "password") {
        senhaInput.type = "text";
    } else {
        senhaInput.type = "password";
    }
}

// Verificar login
function verificarLogin() {
    const usuarioDigitado = document.getElementById("login").value;
    const senhaDigitada = document.getElementById("senha").value;

    if (
        (usuarioDigitado === "vinicius" && senhaDigitada === "1234") ||
        (usuarioDigitado === "admin" && senhaDigitada === "4321")
    ) {
        alert("Login realizado com sucesso!");
        window.location.href = "/usuarios";
    } else {
        alert("Usuário ou senha incorretos!");
    }
}