require('dotenv').config()
let url = process.env.URL

function drawImage(canvas, img, width, height) {
  let context = canvas.getContext("2d");
  canvas.width = width;
  canvas.height = height;
  context.drawImage(img, 0, 0, canvas.width, canvas.height);
}

document.addEventListener("DOMContentLoaded", () => {
  let videoDiv = document.getElementById("divcam")
  let canvas = document.getElementById("canvas")
  let token = document.getElementById("token").value
  let img = undefined
  navigator.mediaDevices.getUserMedia({
    video: {
      width: 520,
      height: 420
    },
    audio: false,
  })
    .then(stream => {
      videoDiv.srcObject = stream
      videoDiv.play()
    })
    .catch(error => {
      console.log(error)
    })

  document.getElementById("take").addEventListener("click", () => {
    videoDiv.pause();
    drawImage(canvas, videoDiv, videoDiv.videoWidth, videoDiv.videoHeight);
    let foto = canvas.toDataURL('media/image.png');
    videoDiv.play();
    img = foto
  })
  document.getElementById("savePht").addEventListener("click", async () => {
    if (img === undefined || img === "") {
      alert("No se ha tomado la foto")
      return
    }
    let Image = canvas.toDataURL('image/png').split(',')[1];
    let form = new FormData()
    form.append("image", Image)
    let resp = await fetch(url + "img/", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
        "X-csrftoken": token
      },
      body: JSON.stringify(Image)
    })
    if (resp.ok) {
      window.location.href = url + "recognition/"
    }
    else {
      alert("No se ha podido guardar la imagen")
    }
  })
})
