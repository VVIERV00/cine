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
$("select").change(function(){
    var seleccionado = $("select").value;

    $("lista").children().each(function(){
        alert($(this));
        if (($(this).genero != seleccionado) && $(this).genero != "nulo"){
            $(this).hidden = true;
        }else{
            $(this).hidden = false;
        }
    })


    });
});

