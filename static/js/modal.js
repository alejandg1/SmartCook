//NOTE: deshuso
document.getElementsByName('modal').forEach(function(e) {
  e.addEventListener('click', function() {
    var nombre = e.getAttribute('data-name')
    var desc = e.getAttribute('data-description')
    modal(nombre, desc)
  })
})

function modal(nombre, desc) {

  $('.modalcont').load('modal/?name=' + encodeURI(nombre) + '&desc=' + encodeURI(desc), function() {
  })
}



function unload() {
  $('.modalcont').empty()
}
