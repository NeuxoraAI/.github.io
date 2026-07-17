(function () {
  "use strict";

  var nav = document.getElementById("nav");
  var toggle = document.querySelector(".nav-toggle");
  var menu = document.getElementById("mobile-menu");
  var year = document.getElementById("year");

  if (year) year.textContent = new Date().getFullYear();

  if (nav) {
    var updateNav = function () {
      nav.classList.toggle("scrolled", window.scrollY > 16);
    };
    updateNav();
    window.addEventListener("scroll", updateNav, { passive: true });
  }

  if (toggle && menu) {
    var setOpen = function (open) {
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Cerrar menú" : "Abrir menú");
      menu.setAttribute("data-open", open ? "true" : "false");
      menu.setAttribute("aria-hidden", open ? "false" : "true");
      document.body.classList.toggle("mobile-menu-open", open);
    };

    toggle.addEventListener("click", function () {
      setOpen(toggle.getAttribute("aria-expanded") !== "true");
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        setOpen(false);
        toggle.focus();
      }
    });
    menu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () { setOpen(false); });
    });
    window.matchMedia("(min-width: 901px)").addEventListener("change", function (event) {
      if (event.matches) setOpen(false);
    });
  }

  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08 });
    reveals.forEach(function (element) { observer.observe(element); });
  } else {
    reveals.forEach(function (element) { element.classList.add("visible"); });
  }
})();
