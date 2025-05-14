document.querySelectorAll(".IG-picture").forEach(item => {
    item.addEventListener("click", function () {
        // Get the image source and overlay text
        let imageSrc = this.getAttribute("data-src");
        let title = this.querySelector(".overlay").textContent;

        // Set modal content
        document.getElementById("IGImage").src = imageSrc;
        document.getElementById("IGBoxTitle").textContent = title;
        document.getElementById("IGDescription").textContent = `This is the selected ${title.toLowerCase()} content.`; 
    });
});