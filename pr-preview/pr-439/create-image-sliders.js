document.getElementsByClassName("md-header__button")[0].title = "NOMAD"

//Script for writing creating image sliders in the docs

// Get all sliders on the page
const sliders = document.querySelectorAll(".image-slider");

sliders.forEach((slider, index) => {
    const images = slider.querySelectorAll("img");
    const prevButton = slider.querySelector(".nav-arrow.left");
    const nextButton = slider.querySelector(".nav-arrow.right");
    let currentImageIndex = 0;

    // Show the first image by default
    images[currentImageIndex].classList.add("active");

    // Add event listener for the 'Next' button
    nextButton.addEventListener("click", () => {
        images[currentImageIndex].classList.remove("active");
        currentImageIndex = (currentImageIndex + 1) % images.length; // Wrap around to the first image
        images[currentImageIndex].classList.add("active");
    });

    // Add event listener for the 'Prev' button
    prevButton.addEventListener("click", () => {
        images[currentImageIndex].classList.remove("active");
        currentImageIndex = (currentImageIndex - 1 + images.length) % images.length; // Wrap around to the last image
        images[currentImageIndex].classList.add("active");
    });
});