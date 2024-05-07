let video = document.getElementById("divcam")
let canva = document.getElementById("canvas")

async function openCam() {
  let constr = {
    video: { width: 520, height: 420 },
    audio: false
  }
  try {
    let stream = await navigator.mediaDevices.getUserMedia(constr)
    video.srcObject = stream
    video.play()
  }
  catch (error) {
    console.log(error)
  }
}

function takephoto() {
}

document.addEventListener("DOMContentLoaded", async () => {
  try {
    openCam()
  }
  catch (e) {
    console.log(e)
  }
})
