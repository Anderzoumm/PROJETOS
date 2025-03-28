const mens = "Hello, World!";      
let nome = "Ander";
console.log(mens);
console.log ("Olá, " + nome + "!"); 

/* PRINCIPAIS COMANDOS EM JS*/
let paragrafo= document.querySelector('p');
/* AQUI EU CRIEI UMA VARIAVEL CHAMADA PARAGRAFO
E NELA EU ATRIBUI UM ELEMENTO HTML QUE EU QUERO SELECIONAR
COM O COMANDO QUERYSELECTOR*/
 paragrafo.addEventListener("mouseover", atualizaNome);
/* AQUI EU ADICIONEI UM EVENTO DE CLIQUE NO PARAGRAFO
E QUANDO O USUARIO PASSAR NO PARAGRAFO, O EVENTO
ATUALIZANOME SERÁ CHAMADO*/
paragrafo.addEventListener("mouseout", atualizaNome2);
function atualizaNome(){
    paragrafo.textContent = "DENTRO"
}
function atualizaNome2(){
    paragrafo.textContent = "FORA"
}