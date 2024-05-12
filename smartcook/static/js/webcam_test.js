

const showStream = idDevice => {
  navigator.mediaDevices.getUserMedia({
    video: {
      deviceId: idDevice,
    }
  },
    (streamObtenido) => {
      SelectDevice();
      $("#list").onchange = () => {
        if (stream) {
          stream.getTracks().forEach(function(track) {
            track.stop();
          });
        }
        showStream($("#list").value);
      }
      stream = streamObtenido;
      $video.srcObject = stream;
      $video.play();
    }, (error) => {
      console.log("error: ", error);
      $estado.innerHTML = "No se puede acceder a la cámara";
    });
}
