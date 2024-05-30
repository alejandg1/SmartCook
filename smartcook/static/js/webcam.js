document.addEventListener("DOMContentLoaded", () => {
  let videoDiv = document.getElementById("divcam")
  let canvas = document.getElementById("canvas")
  let userID = document.getElementById("user").value
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
    let contexto = canvas.getContext("2d");
    canvas.width = videoDiv.videoWidth;
    canvas.height = videoDiv.videoHeight;
    contexto.drawImage(videoDiv, 0, 0, canvas.width, canvas.height);
    let foto = canvas.toDataURL('../media/png/' + userID + '.png');
    videoDiv.play();
    img = foto
  })
  document.getElementById("savePht").addEventListener("click", async () => {
    // let url = "http://localhost:8000/img/"
    let url = "https://qpqcn6vw-8000.use2.devtunnels.ms/img/"
    if (img === undefined) {
      alert("No se ha tomado la foto")
      return
    }
    console.log(img)
    let resp = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": token
      },
      body: JSON.stringify({
        image: img,
        user: userID
      })

    })
    let data = await resp.json()
    console.log(data)
  })
})
