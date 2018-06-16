$(document).ready(function(){
    $("#botonComentar").click(function(){

        var id = $(this).attr('id');
        alert("Hola" + $("#idPeliculaa"));
        var comentario = $(this).attr('textoComentario').val();

        alert(id + " " + comentario);
    });

    $(".sesion").click(function(){
        var sesion = $(this).parent().attr("id");
        var pelicula = $("#idPeliculaa");
      $.ajax({
        url: '/sesion/fecha/pelicula',
        data: {
          'fecha': sesion,
          'pelicula' : pelicula
        },
        dataType: 'json',
        success: function (salas) { #hay que hacer json.decode?
            html = "";
            for (sala in salas){
                html+="<li sesion='" +sesion + "'   ><a class='sala'></a>"; //meto el numero de filas? mejor no
                html+=sala;
                html+="</li>";
            }

            $("#salas").html(html);
        }
      });

    });

     $(".sala").click(function(){
        var sala = $(this).parent().val();
        var sesion = $(this).parent().attr("sesion");
        var pelicula = $("#idPeliculaa");

      $.ajax({
        url: '/sesion/fecha/pelicula/sala',
        data: {
          'pelicula' : pelicula,
          'sesion': sesion,
          'sala' : sala
        },
        dataType: 'json',
        success: function (sala) { #hay que hacer json.decode?
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
});