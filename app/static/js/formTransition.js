document.getElementById('register__next').addEventListener('click', function() {
  const step1 = document.getElementById('step1');
  const step2 = document.getElementById('step2');

  step1.classList.add('slide-out');
  step1.addEventListener('animationend', function() {
    step1.classList.add('hidden');
    step1.classList.remove('slide-out');
    step2.classList.remove('hidden');
    step2.classList.add('slide-in');
  }, { once: true });
});