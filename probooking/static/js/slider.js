
let slides = document.getElementsByClassName("slider-image");
slides[0].classList.add("current");
const current = document.getElementsByClassName("current");
let loopa = 0;
let slidelist = slides.length;
console.log(slidelist);
function next() {

  if (loopa == slidelist - 1) {
    slides[loopa].classList.remove("current");
    loopa = 0;
    slides[loopa].classList.add("current");
  } else {

    slides[loopa].classList.remove("current");
    loopa += 1;

    slides[loopa].classList.add("current");

  }
  console.log(loopa);

}

function prev() {
  console.log(loopa);
  if (loopa == 0) {
    slides[loopa].classList.remove("current");

    loopa = slidelist - 1;

    slides[loopa].classList.add("current");
  } else {
    slides[loopa].classList.remove("current");
    loopa -= 1;
    slides[loopa].classList.add("current");
  }


}

setInterval(function () {
  next();
}, 10000);
