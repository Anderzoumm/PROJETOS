let x1= document.getElementById('x1');
let x2= document.getElementById('x2');
let opr= document.getElementById('opr');
let botao= document.getElementById('botao');
let resultado= document.getElementById('resp');
 
botao.addEventListener('click', calculo);

function calculo(){
    let valor1 = x1.value;
    let valor2 = x2.value;
    let operacao = opr.value;
    let res;
    if (opr.value == "Soma") {
        res = parseFloat(valor1) + parseFloat(valor2);
        }
    }