let nombre
let desc
let token = document.getElementById("token").value
let user = document.getElementById("user").value
document.getElementsByName('modal').forEach(function(e) {
  e.addEventListener('click', function() {
    nombre = e.getAttribute('data-name')
    desc = e.getAttribute('data-description')
    modal(nombre, desc)
  })
})

let dialog = document.querySelector('#modal')

function modal(nombre, desc) {
  dialog.showModal()
  $('.modal-title').text(nombre)
  let body = document.createElement('p')
  body.textContent = desc
  $('.modal-body').append(body)
}

function unload() {
  dialog.close()
  $('.modal-body').empty()
}
//
// let save = document.querySelector('#save')
// save.addEventListener('click', function() {
//   let histURL = 'http://localhost:8000/Hist/?user=' + user + ''
//   let resp = fetch(histURL, {
//     method: 'GET',
//     headers: {
//       'Content-Type': 'application/json',
//     }
//   })
//   if (!resp) {
//     let hist = {
//       user: user,
//     }
//     fetch('http://localhost:8000/Hist/', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json',
//         'cfrtoken': token
//       },
//       body: JSON.stringify(hist)
//     })
//   }
// })
//
