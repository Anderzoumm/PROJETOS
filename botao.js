let botao= document.querySelector('#botao');
let quebrado=false;
botao.addEventListener("mouseover", e=> {
    if (quebrado===false)
    botao.innerHTML = "DENTRO";
})
botao.addEventListener("mouseout", e=> {
    if (quebrado===false)
    botao.innerHTML = "FORA";
})
botao.addEventListener("click", e=> {
    botao.innerHTML = "GOZEI"
    quebrado=true;
})

/*  AO INVES DE FAZER AS FUNÇÕES SEPARADAS PODEMOS FAZER DENTRO DO EVENTLISTENER
botao.addEventListener("mouseout", fora);
function fora(){
    botao.style.backgroundColor = 'green';
}

DESSA FORMA

botao.addEventListener("mouseover", function(){
    botao.style.backgroundColor = 'green';
})
    */


