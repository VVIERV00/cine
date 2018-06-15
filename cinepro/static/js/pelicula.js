$(document).ready(function(){
    $("#botonComentar").click(function(){
        $.ajax({
        url : "comentario/crear", // the endpoint
        type : "POST", // http method
        data : { comentario : $('#textoComentario').val(), idPelicula : $('#idPelicula').val()}, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#textoComentario').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            //$('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
              //  " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }

        });

    });




});