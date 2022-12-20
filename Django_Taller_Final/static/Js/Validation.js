function Val_Number()
{
    var number = document.getElementById("telefono").value;
    var msj = document.getElementById("msj-telefono");

    if(number != ""){
        if(number.length == 9)
        {
            msj.innerHTML= '';
            return true
        }
        else
        {
            msj.innerHTML = 'El formato no es valido.'
            return false
        }
    }
    else
    {
        return false
    }

}