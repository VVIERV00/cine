$(document).ready(function(){
    $("#botonComentar").click(function(){

        var id = $(this).attr('id');
        alert("Hola" + $("#idPeliculaa"));
        var comentario = $(this).attr('textoComentario').val();

        alert(id + " " + comentario);
    });

    $(".sesion").click(function(){
                alert("sesion");

        var sesion = $(this).attr("id");
        var pelicula = $("#idPeliculaa").attr('valor');
        var urlX = '/sesion/'+sesion+'/' + pelicula;
        alert(urlX);
        $.ajax({

            type: 'POST',
            url: urlX,
            data: {
                'fecha': sesion,
                'pelicula' : pelicula
            },
            dataType: 'json',
            success: function (salas) { //hay que hacer json.decode?
                alert("EXITO");

                html = "";
                for (sala in salas){
                    html+="<a class='sala' sesion='" +sesion + "' >"; //meto el numero de filas? mejor no
                    html+=sala;
                    html+="</a>";
                }

                $("#salas").html(html);
            }
      });


    });

    $("#botonReserva").click(function(){ //fecha pelicula sala
        var urlX =  window.location.pathname + "/reservar";
        var seleccionados = $("#salas input");
        var lista = [];
        var indice = 0;
        seleccionados.each(function(){

            if($(this).is(":checked")){
                lista
                lista[indice] = "1";
            }else{
                lista[indice] = "0";
            }
            indice++;
        });
        for (; indice<300; indice++){
            lista[indice] = "0";
        }

        $.ajax({

            type: 'POST',
            url: urlX,
            data: {
                'ocupacion': lista,
            },
            dataType: 'json',
            success: function (resultado) { //hay que hacer json.decode?
                alert("EXITO");


                $("#confirmacion").html(resultado.responseText);
            }
        });

    });



     $(".sala").click(function(){
         alert("sala");

        var sala = $(this).val();
        var sesion = $(this).attr("sesion");
        var pelicula = $("#idPeliculaa");

      $.ajax({
        url: '/sesion/'+ sesion +'/'+pelicula+ '/' + sala,
        data: {
          'pelicula' : pelicula,
          'sesion': sesion,
          'sala' : sala
        },
        dataType: 'json',
        success: function (sala) { //hay que hacer json.decode?
            html = "";
            for (var i = 0; i<sala.filas; i++){

                for (var j = 0; j<sala.columnas; j++){

                    if (sala.ocupacion[j+i*sala.columnas] == 0){
                        html+="<input type='checkbox' numero='0' ></input>";
                    }else{
                        html+="<input type='checkbox' numero='1' checked ></input>";
                    }
                }

               html+= "</br>";

            }

            $("#butacas").html(html);
        }
      });

    });


       $("#trigger").click();

});


    function cargar(){
        alert("se llama")
        var array = $("#arraySecreto").attr("valor");
        alert(array)
        $("#X input").each(function(index, element){

            if (array[index] == "1"){
                $(element).prop('checked', true);

            }
        })
    }