$(document).ready(function(){
    $('.slider').slick({
        dots: true,
        infinite: true,
        speed: 500,
        cssEase: 'linear',
        autoplay: true,
        fade: true
    });
  });
// //   popup
// var btnAbrirPopup = document.getElementById('btn-abrir-popup'),
// 	overlay = document.getElementById('overlay'),
// 	popup = document.getElementById('popup'),
// 	btnCerrarPopup = document.getElementById('btn-cerrar-popup');

// btnAbrirPopup.addEventListener('click', function(){
// 	overlay.classList.add('active');
// 	popup.classList.add('active');
// });

// btnCerrarPopup.addEventListener('click', function(e){
// 	e.preventDefault();
// 	overlay.classList.remove('active');//"escondemos" el overlay con su popup
//   popup.classList.remove('active');
//   $('#userTxt').val(''); // dejamos en blanco los input de usuario y contraseña al cerrar el popup
//   $('#userPwd').val('');
// });
$('.slider').slick({
  dots: true,
  infinite: true,
  speed: 500,
  cssEase: 'linear',
  autoplay: true,
  fade: true
});
//opciones de galería lightbox
lightbox.option({
  'albumLabel':"",
  wrapAround: true
})