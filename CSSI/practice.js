let button = document.querySelector("#buttonboy");
button.addEventListener("click", () => {
  console.log("I liked it!!");
});

let like_header = document.querySelector("#numoflikes");
let like_count = 0
button.addEventListener("click", () => {
  like_count++;
  like_header.innerHTML = like_count + " likes."
})

const randColor = () =>{
  like_header.style.color = "red";
}

like_header.addEventListener("click", randColor);
