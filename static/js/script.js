document.addEventListener('DOMContentLoaded', () =>    {
    const menuToggle = document.querySelector('.menu-toggle');
    const mainNav = document.getElementById('mainNav');

    menuToggle.addEventListener('click', function() {
        mainNav.classList.toggle('active');
    });
});

if (menuToggle && mainNav) {
    menuToggle.addEventListener("click", () => {
    const isOpen = mainNav.classList.toggle("open");
   menuToggle.setAttribute("aria-expanded", isOpen? "true" : "false");
    });
}