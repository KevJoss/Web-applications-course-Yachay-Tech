const $boton = $("#color-toggle");
const $hero = $(".hero");

const colorPalette = [
    "#EDE9FE",
    "#E0D7FF",
    "#F3E8FF",
    "#E8F4FD",
    "#E0F2FE",
    "#F0FDF4",
    "#ECFDF5",
    "#FFF0F6",
    "#FDE8F0",
    "#FEF3C7",
    "#fcfcfd",
];

function changeColor() {
    const randomIndex = Math.floor(Math.random() * colorPalette.length);
    const selectedColor = colorPalette[randomIndex];

    $hero.css("background-color", selectedColor);
}

$boton.on("click", changeColor);

// IMAGE MODAL

$(document).ready(function () {
    const $modal = $("#image-modal");
    const $trigger = $("#profile-img-trigger");
    const $closeBtn = $("#modal-close-btn");

    function openModal() {
        $modal.removeAttr("hidden");
        setTimeout(() => $modal.addClass("modal-visible"), 10);
        $closeBtn.focus();
    }

    function closeModal() {
        $modal.removeClass("modal-visible");
        $modal.one("transitionend", () => $modal.attr("hidden", true));
    }

    // Open when clicking the profile photo
    $trigger.on("click", openModal);

    // Close when clicking the × button
    $closeBtn.on("click", closeModal);

});
