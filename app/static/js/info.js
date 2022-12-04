const arrow = document.querySelector("div.arrow");
const table = document.querySelector("table");
const hiddens = document.querySelectorAll(".hidden");

arrow.addEventListener("click", (event) => {
    console.log(table.style.width);
    if (table.style.width === "600px" || table.style.width === "") {
        table.style.width = "1000px";
    } else {
        table.style.width = "600px";
    }
    hiddens.forEach((element) => {
        element.classList.toggle("hidden");
        arrow.classList.toggle("left");
    });
});
