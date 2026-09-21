/* Progressive enhancement: all navigation links remain usable without JavaScript. */
(function () {
  var button = document.querySelector('.nav-hamburger');
  var links = document.querySelector('.nav-links');
  if (!button || !links) return;
  document.documentElement.classList.add('js-nav');
  button.hidden = false;
  var narrow = window.matchMedia('(max-width: 1023px)');

  function setOpen(open, restoreFocus) {
    links.classList.toggle('open', open);
    button.setAttribute('aria-expanded', String(open));
    button.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
    if (restoreFocus) button.focus();
  }
  button.addEventListener('click', function () {
    var open = button.getAttribute('aria-expanded') !== 'true';
    setOpen(open, false);
    if (open) links.querySelector('a').focus();
  });
  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && button.getAttribute('aria-expanded') === 'true') {
      setOpen(false, true);
    }
  });
  document.addEventListener('click', function (event) {
    if (!links.contains(event.target) && !button.contains(event.target)) setOpen(false, false);
  });
  document.addEventListener('focusin', function (event) {
    if (!links.contains(event.target) && !button.contains(event.target)) setOpen(false, false);
  });
  links.addEventListener('click', function (event) {
    if (event.target.closest('a') && narrow.matches) setOpen(false, false);
  });
  narrow.addEventListener('change', function () {
    setOpen(false, narrow.matches && links.contains(document.activeElement));
  });
}());
