(function () {
  'use strict';

  var toggle = document.querySelector('.nav-toggle');
  var menu = document.getElementById('mobile-menu');
  if (!toggle || !menu) return;

  var body = document.body;
  var links = menu.querySelectorAll('.mobile-menu-link');

  function setOpen(open) {
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    menu.setAttribute('data-open', open ? 'true' : 'false');
    menu.setAttribute('aria-hidden', open ? 'false' : 'true');
    body.classList.toggle('mobile-menu-open', open);
  }

  toggle.addEventListener('click', function () {
    var isOpen = toggle.getAttribute('aria-expanded') === 'true';
    setOpen(!isOpen);
  });

  document.addEventListener('keydown', function (ev) {
    if (ev.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      setOpen(false);
      toggle.focus();
    }
  });

  links.forEach(function (link) {
    link.addEventListener('click', function () { setOpen(false); });
  });

  var mq = window.matchMedia('(min-width: 769px)');
  mq.addEventListener('change', function (ev) {
    if (ev.matches) setOpen(false);
  });

  setOpen(false);
})();
