$(document).ready(function(){
    $("#botonComentar").click(function(){

        var id = $(this).attr('idPelicula');
        alert("Hola" + id);
        var comentario = $(this).attr('textoComentario').val();

        alert(id + " " + comentario);
    });

});