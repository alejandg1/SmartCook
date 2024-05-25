let video = document.getElementById("divcam")
let canvas = document.getElementById("canvas")
let id = document.getElementById("ID").className
const GetDevice = () => navigator
  .mediaDevices
  .enumerateDevices();

function ClearSelect() {
  $("#list").empty()
}

const SelectDevice = () => {
  ClearSelect();
  GetDevice()
    .then(devices => {
      const videoDevices = [];
      devices.forEach(device => {
        const type = device.kind;
        console.log(device)
        if (type === "videoinput") {
          videoDevices.push(device);
        }
      });
      if (videoDevices.length > 0) {
        let cam = 0
        videoDevices.forEach(dispositivo => {
          cam = cam + 1
          const option = document.createElement('option');
          option.value = dispositivo.deviceId;
          option.text = "camara " + cam + ": " + dispositivo.kind;
          console.log(dispositivo)
          $("#list").append(option);
        });
      }
    });
}

async function openCam(IDdev) {
  let constr = {
    video: { width: 520, height: 420 },
    audio: false,
    device: IDdev

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
  video.pause();
  let contexto = canvas.getContext("2d");
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  contexto.drawImage(video, 0, 0, canvas.width, canvas.height);

  let foto = canvas.toDataURL('../media/png/user_' + id + Date.now() + '.png');

  video.play();

  return foto;
}

document.addEventListener("DOMContentLoaded", async () => {
  try {
    SelectDevice()
    openCam($("#list").value)
    navigator.mediaDevices.enumerateDevices()
  }
  catch (e) {
    console.log(e)
  }
})

document.getElementById("list").addEventListener("change", () => {
  console.log($("#list").value)
  openCam($("#list").value)
}
)
