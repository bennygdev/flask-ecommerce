const savedIcon = document.querySelector('.saved');

savedIcon.addEventListener('mouseover', () => {
  savedIcon.classList.remove('fa-regular');
  savedIcon.classList.add('fa-solid');
});

savedIcon.addEventListener('mouseout', () => {
  savedIcon.classList.remove('fa-solid');
  savedIcon.classList.add('fa-regular');
});

// scroll to stick navbar
document.addEventListener("DOMContentLoaded", () => {
  const navbar = document.querySelector('.main__navbar');
  const navbarHeight = navbar.offsetHeight;

  let isSticky = false;
  let lastScrollTop = 0;

  window.addEventListener("scroll", () => {
    let scrollTop = window.scrollY;

    if (scrollTop > lastScrollTop) {
      // Scroll down
      if (scrollTop > navbarHeight && !isSticky) {
        navbar.classList.add("sticky");
        isSticky = true;
      }
    } else {
      // Scroll up
      if (scrollTop <= navbarHeight && isSticky) {
        
        navbar.classList.remove("sticky");
        isSticky = false;
      }
    }

    lastScrollTop = scrollTop;
  })
})