function drawImage(canvas, img, width, height) {
  let context = canvas.getContext("2d");
  canvas.width = width;
  canvas.height = height;
  context.drawImage(img, 0, 0, canvas.width, canvas.height);
}

let canvas = document.getElementById("canvas");
let input = document.getElementById("id_image");

input.addEventListener("change", () => {
  let file = input.files[0];
  let reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onload = () => {
    let img = new Image();
    img.src = reader.result;
    img.onload = () => {
      drawImage(canvas, img, 250, 250);
      canvas.classList.remove("hidden");
    };
  };
});
