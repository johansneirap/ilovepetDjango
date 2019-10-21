jQuery.validator.addMethod("rutValido", function (value, element) {
  if (Fn.validaRut(value)) {
      return true;
  } else {
      return false;
  };
}, "Rut No Valido");

$(function() {
      $("#formulario_registro").validate({
        rules: {
          email: {
            required: true,
            email: true
          },
          pass: "required",
          pass2: {
            required: true,
            equalTo: "#pass"
          },
          bday: {
            required: true
          },
          rut: {
            rutValido: true
          }
        },
        messages: {
          email: {
            required: 'Ingresa tu correo electrónico',
            email: 'Formato de correo no válido'
          },
          pass: {
            required: 'Ingresa una contraseña',
          },
          pass2: {
            required: 'Reingresa la contraseña',
            equalTo: 'Las contraseñas ingresadas no coinciden'
          },
          bday: {
            required: 'Ingresa una fecha',
            max: 'Debe ser mayor de edad'
          },
          rut: {
            required: "Ingresa tu rut"
          },
          nombre: {
            required: "Ingresa tu nombre"
          },
          nro: {
            required: "Ingresa tu número de contacto"
          },
          cel: {
            required: "Ingresa tu celular"
          },
          terminos: {
            required: "Debes aceptar los terminos"
          }
        }
      });
    });

    //seteo fecha maxima como hoy
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1;
    var yyyy = today.getFullYear()-18;
     if(dd<10){
            dd='0'+dd
        } 
        if(mm<10){
            mm='0'+mm
        } 
    today = yyyy+'-'+mm+'-'+dd;
    document.getElementById("bday").setAttribute("max", today);
    
    $("#rut").on({
      "focus": function(event) {
        $(event.target).select();
      },
      "keyup": function(event) {
        $(event.target).val(function(index, value) {
          return value.replace(/[^k|K|\d]/g, "")
            .replace(/([0-9])(k|K|[0-9]{1})$/, '$1-$2')
            .replace(/\B(?=(\d{3})+(?!\d)\.?)/g, ".");
        });
      }
    });

    var Fn = {
        validaRut : function (rutInput) {
            rutInput = rutInput.replace(".", "");
            rutInput = rutInput.replace(".", "");
            var tmp     = rutInput.split('-');
            var digv    = tmp[1]; 
            var rut     = tmp[0];
            if ( digv == 'K' ) digv = 'k' ;
            return (Fn.dv(rut) == digv );
        },
        dv : function(rut){
          var rutStr = rut.toString();
          var multiplo = 2;
          var suma = 0;
          var dv=0;
        	for(i=0;i<rutStr.length;i++){
            suma += (Math.floor(rut/10**i)%10)*multiplo;
            multiplo++;
            if(multiplo==8) multiplo = 2;
          }
          dv = 11-(suma%11);
          if(dv==10) dv="k";
          if(dv==11) dv=0;
          return dv;
        }
    }
    $("#cel").on({
      "focus": function(event) {
        $(event.target).select();
      },
      "keyup": function(event) {
        $(event.target).val(function(index, value) {
          return value.replace(/[^-|+|\d]/g, "");
        });
      }
    });
    $("#nombre").on({
      "focus": function(event) {
        $(event.target).select();
      },
      "keyup": function(event) {
        $(event.target).val(function(index, value) {
          return value.replace(/[^a-zA-Z]/g, "");
        });
      }
    });