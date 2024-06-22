function drawImage(canvas, img, width, height) {
  let context = canvas.getContext("2d");
  canvas.width = width;
  canvas.height = height;
  context.drawImage(img, 0, 0, canvas.width, canvas.height);
}

canvas = document.getElementById("canvas")
imput = document.getElementById("id_image")

imput.addEventListener("change", () => {
  let file = imput.files[0]
  let reader = new FileReader()
  reader.readAsDataURL(file)
  reader.onload = () => {
    let img = new Image()
    img.src = reader.result
    img.onload = () => {
      drawImage(canvas, img, 400, 300)
    }
  }
})

