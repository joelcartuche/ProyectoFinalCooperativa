
//permite que solo se ingrese letras 
function soloLetras(e) {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toLowerCase();
    letras = " áéíóúabcdefghijklmnñopqrstuvwxyz";// letras que unicamente se pueden ingresar
    especiales = [8, 37, 39, 46];

    tecla_especial = false
    for (var i in especiales) {
        if (key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }

    if (letras.indexOf(tecla) == -1 && !tecla_especial)
        return false;
}

function limpia(elemento) { // en caso de que el usuario copie contenido y lo pege en el input sera borrado
    alert(elemento)
    var val = document.getElementById(elemento).value;
    var tam = val.length;
    for (i = 0; i < tam; i++) {
        if (!isNaN(val[i]))
            document.getElementById(elemento).value = '';
    }
}

function soloNumeros(e) {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toLowerCase();
    letras = " 0123456789";// unicamente numeros
    especiales = [8, 37, 39, 46];

    tecla_especial = false
    for (var i in especiales) {
        if (key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }

    if (letras.indexOf(tecla) == -1 && !tecla_especial)
        return false;
}

function decimales(e) {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toLowerCase();
    letras = " 0123456789";

    especiales = [8, 37, 39, 46];

    tecla_especial = false
    for (var i in especiales) {
        if (key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }    
    if (letras.indexOf(tecla) == -1 && !tecla_especial)
        return false;
}