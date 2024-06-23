function drawImage(canvas, img, width, height) {
  let context = canvas.getContext("2d");
  canvas.width = width;
  canvas.height = height;
  context.drawImage(img, 0, 0, canvas.width, canvas.height);
}
document.addEventListener("DOMContentLoaded", () => {
  let img = document.getElementById("img").value
  let canvas = document.getElementById("canvas")
  let imgElement = new Image()
  imgElement.src = img
  imgElement.onload = () => {
    drawImage(canvas, imgElement, 300, 200)
  }
})
