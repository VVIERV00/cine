$(document).ready(function(){

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
    /*var form = $('<form action="' + urlX + '" method="post">' +
      '<input type="text" name="api_url" value="' + Return_URL + '" />' +
        '</form>');
    $('body').append(form);*/
    $("#botonReserva").click(function(){ //fecha pelicula sala
        var urlX =  window.location.pathname + "/reservar";
        var seleccionados = $(':checkbox')
        var lista = [];
        var indice = 0;

        seleccionados.each(function(){
            if($(this).is(":checked")){
                lista[indice] = "1";
            }else{
                lista[indice] = "0";
            }
            indice++;
        });
        for (; indice<300; indice++){
            lista[indice] = "0";
        }


        /*$.extend({
         redirectPost: function(location, args){
            var form = '';
            $.each( args, function( key, value ) {
                value = value.split('"').join('\"')
                form += '<input type="hidden" name="'+key+'" value="'+value+'">';
            });
               $('<form action="' + location + '" method="POST">' + form + '</form>').appendTo($(document.body)).submit();
        }
        });*/

         post(urlX, {'ocupacion': lista}, "POST");
       /* $.ajax({

            type: 'POST',
            url: urlX,
            data: {
                'ocupacion': lista,
            },
            dataType: 'json',
            success: function (resultado) { //hay que hacer json.decode?
                $("#confirmacion").html(resultado.responseText);
            }
        });*/

        //alert("Su reserva se ha efectuado con éxito");

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
        var array = $("#arraySecreto").attr("valor");
        $("#X input").each(function(index, element){

            if (array[index] == "1"){
                $(element).prop('checked', true);

            }
        })
    }

    function post(path, params, method) {
    method = method || "post"; // Set method to post by default if not specified.

    // The rest of this code assumes you are not using a library.
    // It can be made less wordy if you use one.
    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);

    for(var key in params) {
        if(params.hasOwnProperty(key)) {
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", params[key]);

            form.appendChild(hiddenField);
        }
    }

    document.body.appendChild(form);
    form.submit();
}