(function () {
  "use strict";

  var root = document.documentElement;

  try {
    var year = document.getElementById("year");
    if (year) year.textContent = new Date().getFullYear();
  } catch (error) {
    // The date is optional; navigation and content must keep working.
  }

  try {
    var nav = document.getElementById("nav");
    if (nav) {
      var navScrolled = null;
      var scrollFrame = null;
      var updateNav = function () {
        scrollFrame = null;
        var nextScrolled = window.scrollY > 16;
        if (nextScrolled !== navScrolled) {
          nav.classList.toggle("scrolled", nextScrolled);
          navScrolled = nextScrolled;
        }
      };
      var requestNavUpdate = function () {
        if (scrollFrame === null) scrollFrame = window.requestAnimationFrame(updateNav);
      };
      updateNav();
      window.addEventListener("scroll", requestNavUpdate, { passive: true });
    }

    var toggle = document.querySelector(".nav-toggle");
    var menu = document.getElementById("mobile-menu");
    if (toggle && menu) {
      var main = document.querySelector("main");
      var footer = document.querySelector("footer");
      var menuLinks = Array.prototype.slice.call(menu.querySelectorAll("a"));
      var breakpoint = window.matchMedia("(min-width: 901px)");
      var menuOpen = false;
      var setBackgroundInert = function (inert) {
        [main, footer].forEach(function (element) {
          if (element && "inert" in element) element.inert = inert;
        });
      };
      var setOpen = function (open, restoreFocus) {
        menuOpen = open;
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
        toggle.setAttribute("aria-label", open ? "Cerrar menú" : "Abrir menú");
        menu.setAttribute("data-open", open ? "true" : "false");
        menu.setAttribute("aria-hidden", open ? "false" : "true");
        document.body.classList.toggle("mobile-menu-open", open);
        setBackgroundInert(open);
        if (open && menuLinks.length) menuLinks[0].focus();
        if (!open && restoreFocus) toggle.focus();
      };
      var handleMenuKeydown = function (event) {
        if (!menuOpen) return;
        if (event.key === "Escape") {
          event.preventDefault();
          setOpen(false, true);
          return;
        }
        if (event.key !== "Tab") return;

        var focusable = [toggle].concat(menuLinks);
        var first = focusable[0];
        var last = focusable[focusable.length - 1];
        if (event.shiftKey && document.activeElement === first) {
          event.preventDefault();
          last.focus();
        } else if (!event.shiftKey && document.activeElement === last) {
          event.preventDefault();
          first.focus();
        }
      };
      var handleBreakpoint = function (event) {
        if (event.matches && menuOpen) setOpen(false, true);
      };

      toggle.addEventListener("click", function () { setOpen(!menuOpen, menuOpen); });
      document.addEventListener("keydown", handleMenuKeydown);
      menuLinks.forEach(function (link) {
        link.addEventListener("click", function () { setOpen(false, false); });
      });
      if (typeof breakpoint.addEventListener === "function") {
        breakpoint.addEventListener("change", handleBreakpoint);
      } else if (typeof breakpoint.addListener === "function") {
        breakpoint.addListener(handleBreakpoint);
      }

      root.classList.add("nav-enhanced");
      setOpen(false, false);
    }
  } catch (error) {
    root.classList.remove("nav-enhanced");
    document.body.classList.remove("mobile-menu-open");
  }

  try {
    var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
    var observer = null;
    var revealTargets = Array.prototype.slice.call(document.querySelectorAll(".reveal, .dark-section"));
    var showAllMotionContent = function () {
      root.classList.remove("motion-pending", "motion-ready");
      revealTargets.forEach(function (element) {
        element.classList.add(element.classList.contains("dark-section") ? "motion-dark-visible" : "visible");
      });
      if (observer) {
        observer.disconnect();
        observer = null;
      }
    };
    var initializeMotion = function () {
      if (reducedMotion.matches || !("IntersectionObserver" in window)) {
        showAllMotionContent();
        return;
      }

      observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add(entry.target.classList.contains("dark-section") ? "motion-dark-visible" : "visible");
          observer.unobserve(entry.target);
        });
      }, { threshold: 0.08 });
      revealTargets.forEach(function (element) { observer.observe(element); });
      root.classList.add("motion-pending");
      window.requestAnimationFrame(function () {
        root.classList.add("motion-ready");
      });
    };
    var handleMotionPreference = function (event) {
      if (event.matches) showAllMotionContent();
    };

    if (typeof reducedMotion.addEventListener === "function") {
      reducedMotion.addEventListener("change", handleMotionPreference);
    } else if (typeof reducedMotion.addListener === "function") {
      reducedMotion.addListener(handleMotionPreference);
    }
    initializeMotion();
  } catch (error) {
    root.classList.remove("motion-pending", "motion-ready");
  }
})();
