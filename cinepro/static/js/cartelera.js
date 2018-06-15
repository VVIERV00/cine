$(document).ready(function(){
/*$("select").onchange(function(){
    var seleccionado = $("select").value;
    var html = "<option>...</option>";
    list.each(function(
    alert(this):
        if (this.genero == seleccionado){
            html += "<option>";
            html += this.titulo;
            html += "</option>";
        }
    }));
    $("select").html(html);
});
*/
$("#select").change(function(){
    var seleccionado = $("#select").val();
   //alert("entra " + seleccionado);
    $("li").each(function(){
        //alert("este " + $(this).attr('genero'));
        if (seleccionado == "..."){
            //alert("booom");
            $(this).show();
        }else if (($(this).attr('genero') != seleccionado)){
            $(this).hide();
        }else{
            $(this).show();
        }
    })

});

$("#busquedaTexto").on('input',function(e){
    var seleccionado = $("#busquedaTexto").val();
    $("li").each(function(){
    //alert("ti " + $(this).attr('titulo')  + " di " + $(this).attr('director') + " selec " + seleccionado );
        if (seleccionado == ""){

            $(this).show();
        }else if ( ~($(this).attr('titulo').toLowerCase().indexOf(seleccionado.toLowerCase()))  ||  ~($(this).attr('director').toLowerCase().indexOf(seleccionado.toLowerCase()))) {
            $(this).show();
        }else{
            $(this).hide();
        }
    })
});
});

