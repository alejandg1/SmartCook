let video = document.getElementById("divcam")
let canvas = document.getElementById("canvas")
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
        if (type === "videoinput") {
          videoDevices.push(device);
        }
      });
      if (videoDevices.length > 0) {
        videoDevices.forEach(dispositivo => {
          const option = document.createElement('option');
          option.value = dispositivo.deviceId;
          option.text = dispositivo.label;
          $("#list").appendChild(option);
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
    let stream = await navigator.mediaDevices.getUserMedia()
    video.srcObject = stream
    video.play()
  }
  catch (error) {
    console.log(error)
  }
}

function takephoto() {
  const context = canvas.getContext('2d');
  if (video.paused || video.ended) {
    console.error("Can't capture image, video is not playing");
    return;
  }
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  context.drawImage(video, 0, 0);
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

$("#list").onchange = () => {
  openCam($("#list").value)
}
