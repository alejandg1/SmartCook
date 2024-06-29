let url = "https://proyecto_const_softw.railway.internal"
let ActualRecipe = {
  'Receta': "",
  'Instrucciones': "",
  'Ingredientes': ""
}
let nombre
let desc
let ingredients
let token = document.getElementById("token").value
document.getElementsByName('modal').forEach(function(e) {
  e.addEventListener('click', function() {
    nombre = e.getAttribute('data-name')
    desc = e.getAttribute('data-description')
    ingredients = e.getAttribute('data-ingredients')
    modal()
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

function modal() {
  $('.modal-ingredients').empty()
  dialog.showModal()
  $('.modal-title').text(nombre)
  if (nombre == "sin recetas disponibles") {
    $('#delete').hide()
    $('#pasos').hide()
    $('#ingredientes').hide()
    $('.modal-body').text("No hay recetas asociadas a este usuario")
  }
  else {
    desc = parseList(desc)
    ingredients = parseList(ingredients)
    for (i in desc) {
      if (desc[i] != '**') {
        let body = document.createElement('li')
        body.textContent = desc[i]
        $('.modal-body').append(body)
      }
    }
    ActualRecipe.Receta = nombre
    ActualRecipe.Instrucciones = desc.join(',')
    ActualRecipe.Ingredientes = ingredients.join(',')
    for (i in ingredients) {
      let body = document.createElement('li')
      body.textContent = ingredients[i]
      $('.modal-ingredients').append(body)
    }
  }
}

function unload() {
  dialog.close()
  $('.modal-body').empty();

}
let send, rm

try {
  send = document.getElementById('send')
  send.addEventListener('click', async () => {
    let resp = await fetch(url + "user/save/", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
        "X-csrftoken": token
      },
      body: JSON.stringify(ActualRecipe)
    })
    if (resp.ok) {
      dialog.close()
    }
    else {
      alert("No se ha podido guardar en el historial")
    }
  })
}
catch (e) {
  rm = document.getElementById('delete')
  rm.addEventListener('click', async () => {
    let resp = await fetch(url + "user/delete/", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
        "X-csrftoken": token
      },
      body: JSON.stringify({
        'nombre': nombre
      })
    })
    if (resp.ok) {
      window.location.reload()
    }
    else {
      alert("No se ha podido eliminar de tu historial")
    }
  })
}

