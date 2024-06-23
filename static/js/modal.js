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

function parseList(list) {
  list = list.replace(/['\[\]]/g, '')
  let parsed = list.split(',')
  parsed = parsed.filter((item) => {
    return item !== ''
  })
  let parsedList = []
  for (i in parsed) {
    parsedList.push(parsed[i].trim())
  }
  return parsedList
}

function modal(nombre, desc) {
  dialog.showModal()
  $('.modal-title').text(nombre)
  desc = parseList(desc)
  ingredients = parseList(ingredients)
  for (i in desc) {
    let body = document.createElement('li')
    body.textContent = desc[i]
    $('.modal-body').append(body)
  }
  for (i in ingredients) {
    let body = document.createElement('li')
    body.textContent = ingredients[i]
    $('.modal-ingredients').append(body)
  }
}

function unload() {
  dialog.close()
  $('.modal-body').empty();

}
