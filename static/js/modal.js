let nombre
let desc
let ingredients
let token = document.getElementById("token").value
let user = document.getElementById("user").value
document.getElementsByName('modal').forEach(function(e) {
  e.addEventListener('click', function() {
    nombre = e.getAttribute('data-name')
    desc = e.getAttribute('data-description')
    ingredients = e.getAttribute('data-ingredients')
    modal(nombre, desc)
  })
})

let dialog = document.querySelector('#modal')

function modal(nombre, desc) {
  dialog.showModal()
  $('.modal-title').text(nombre)
  let body = document.createElement('p')
  let ingred = document.createElement('p')
  for (let i = 0; i < ingredients.length; i++) {
    let ing = document.createElement('p')
    ing.textContent = ingredients[i]
    $('.modal-body').append(ing)
  }
  body.textContent = desc
  ingred.textContent = desc
  $('.modal-body').append(body)
}

function unload() {
  dialog.close()
  $('.modal-body').empty();

}
