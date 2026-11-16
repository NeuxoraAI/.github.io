// @ts-check
(function () {
  "use strict";

  var root = document.documentElement;
  root.classList.add("js-enhanced");

  function setYear() {
    var yearEl = document.getElementById("year");
    if (yearEl) {
      yearEl.textContent = String(new Date().getFullYear());
    }
  }

  /**
   * Orbiting particle galaxy in the hero: a tilted ring of colored dashes that reacts to the pointer.
   */
  function initAntigravityCanvas() {
    var canvas = /** @type {HTMLCanvasElement | null} */ (
      document.querySelector("[data-antigravity-canvas]")
    );
    if (!canvas || !canvas.getContext) return;

    var ctx = canvas.getContext("2d");
    if (!ctx) return;

    var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
    var hero = canvas.closest(".hero") || document.body;
    var focus = hero.querySelector(".hero-centered, .hero-header-split, .narrow");
    var width = 0;
    var height = 0;
    var cx = 0;
    var cy = 0;
    var rx = 0;
    var ry = 0;
    var rafId = null;
    var isVisible = true;
    var pointer = { x: 0, y: 0, active: false };

    // Spectrum stays fixed in space; particles change color as they orbit through it.
    var PALETTE = [
      [91, 108, 255],
      [150, 95, 235],
      [217, 119, 87],
      [232, 168, 74],
      [47, 165, 140],
    ];
    var SHADES = 30;
    var shades = [];
    for (var s = 0; s < SHADES; s++) {
      var pos = (s / SHADES) * PALETTE.length;
      var from = PALETTE[Math.floor(pos) % PALETTE.length];
      var to = PALETTE[(Math.floor(pos) + 1) % PALETTE.length];
      var mix = pos - Math.floor(pos);
      shades.push(
        "rgb(" +
          Math.round(from[0] + (to[0] - from[0]) * mix) + "," +
          Math.round(from[1] + (to[1] - from[1]) * mix) + "," +
          Math.round(from[2] + (to[2] - from[2]) * mix) + ")"
      );
    }

    var TILT = -0.2;
    var cosT = Math.cos(TILT);
    var sinT = Math.sin(TILT);
    var TWO_PI = Math.PI * 2;

    /**
     * @typedef {{ a: number, rf: number, w: number, z: number, phase: number, ox: number, oy: number }} Particle
     */
    /** @type {Particle[]} */
    var particles = [];

    var seedParticles = function () {
      var count = width < 700 ? 150 : 420;
      particles = [];
      for (var i = 0; i < count; i++) {
        // Sum of randoms clusters particles around the ring and leaves the center clear for text.
        var rf = 0.62 + (Math.random() + Math.random() + Math.random()) * 0.26;
        particles.push({
          a: Math.random() * TWO_PI,
          rf: rf,
          w: 0.05 / (rf * Math.sqrt(rf)),
          z: 0.35 + Math.random() * 0.65,
          phase: Math.random() * TWO_PI,
          ox: 0,
          oy: 0,
        });
      }
    };

    var resize = function () {
      var rect = canvas.getBoundingClientRect();
      if (!rect.width || !rect.height) return;
      var dpr = Math.min(window.devicePixelRatio || 1, 2);
      var wasMobile = width < 700;
      width = rect.width;
      height = rect.height;
      canvas.width = Math.round(width * dpr);
      canvas.height = Math.round(height * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.lineCap = "round";

      var focusRect = focus ? focus.getBoundingClientRect() : null;
      cx = width / 2;
      cy = focusRect ? focusRect.top - rect.top + focusRect.height / 2 : height * 0.42;
      rx = Math.min(width * 0.47, 700);
      ry = Math.max(rx * 0.55, focusRect ? focusRect.height * 0.62 : 0);

      if (!particles.length || wasMobile !== width < 700) seedParticles();
    };

    var render = function (time) {
      ctx.clearRect(0, 0, width, height);
      var t = time * 0.001;

      for (var i = 0; i < particles.length; i++) {
        var p = particles[i];
        var angle = p.a + t * p.w;
        var breathe = p.rf * (1 + 0.035 * Math.sin(t * 0.5 + p.phase));
        var ex = Math.cos(angle) * rx * breathe;
        var ey = Math.sin(angle) * ry * breathe;
        var x = cx + ex * cosT - ey * sinT + p.ox;
        var y = cy + ex * sinT + ey * cosT + p.oy;

        if (pointer.active) {
          var dx = x - pointer.x;
          var dy = y - pointer.y;
          var distSq = dx * dx + dy * dy;
          if (distSq < 32400 && distSq > 1) {
            var dist = Math.sqrt(distSq);
            var force = (1 - dist / 180) * 2.2 * p.z;
            p.ox += (dx / dist) * force;
            p.oy += (dy / dist) * force;
          }
        }
        p.ox *= 0.94;
        p.oy *= 0.94;

        if (x < -20 || x > width + 20 || y < -20 || y > height + 20) continue;

        // Dash follows the orbit tangent.
        var tx = -Math.sin(angle) * rx;
        var ty = Math.cos(angle) * ry;
        var tLen = Math.sqrt(tx * tx + ty * ty) || 1;
        var half = (1.5 + p.z * 3.5) / tLen;
        var hx = (tx * cosT - ty * sinT) * half;
        var hy = (tx * sinT + ty * cosT) * half;

        var norm = (((angle % TWO_PI) + TWO_PI) % TWO_PI) / TWO_PI;
        ctx.strokeStyle = shades[Math.floor(norm * SHADES) % SHADES];
        ctx.globalAlpha = (0.22 + 0.5 * p.z) * (0.7 + 0.3 * Math.sin(t * 1.6 + p.phase));
        ctx.lineWidth = 1 + p.z * 1.3;
        ctx.beginPath();
        ctx.moveTo(x - hx, y - hy);
        ctx.lineTo(x + hx, y + hy);
        ctx.stroke();
      }
      ctx.globalAlpha = 1;
    };

    var step = function (time) {
      rafId = null;
      if (!isVisible || reducedMotion.matches) return;
      render(time);
      rafId = window.requestAnimationFrame(step);
    };

    var startLoop = function () {
      if (rafId === null && isVisible && !reducedMotion.matches) {
        rafId = window.requestAnimationFrame(step);
      }
    };

    var stopLoop = function () {
      if (rafId !== null) {
        window.cancelAnimationFrame(rafId);
        rafId = null;
      }
    };

    hero.addEventListener(
      "pointermove",
      function (event) {
        var rect = canvas.getBoundingClientRect();
        pointer.x = event.clientX - rect.left;
        pointer.y = event.clientY - rect.top;
        pointer.active = true;
      },
      { passive: true }
    );

    hero.addEventListener(
      "pointerleave",
      function () {
        pointer.active = false;
      },
      { passive: true }
    );

    if ("IntersectionObserver" in window) {
      var visObserver = new IntersectionObserver(
        function (entries) {
          isVisible = Boolean(entries[0] && entries[0].isIntersecting);
          if (isVisible) startLoop();
          else stopLoop();
        },
        { threshold: 0.01 }
      );
      visObserver.observe(hero);
    }

    if (typeof reducedMotion.addEventListener === "function") {
      reducedMotion.addEventListener("change", function (event) {
        if (event.matches) {
          stopLoop();
          render(0);
        } else {
          startLoop();
        }
      });
    }

    window.addEventListener(
      "resize",
      function () {
        resize();
        if (reducedMotion.matches) render(0);
      },
      { passive: true }
    );
    resize();
    // Reduced motion still gets the galaxy, as one still frame.
    if (reducedMotion.matches) render(0);
    else startLoop();
  }

  /**
   * Split hero headlines into words so CSS can reveal them one by one.
   * Screen readers keep the full sentence through aria-label.
   */
  function initWordReveal() {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    document.querySelectorAll(".hero-title, .page-title, .statement-text").forEach(function (title) {
      var words = title.textContent.trim().split(/\s+/);
      title.setAttribute("aria-label", words.join(" "));
      title.textContent = "";
      words.forEach(function (word, index) {
        var span = document.createElement("span");
        span.className = "word";
        span.setAttribute("aria-hidden", "true");
        span.style.setProperty("--word-index", String(index));
        span.textContent = word;
        title.appendChild(span);
        title.appendChild(document.createTextNode(" "));
      });
      title.classList.add("word-reveal");
    });
  }

  /**
   * Native <dialog> overlays: contact modal, photo lightbox, copy-to-clipboard and back-to-top.
   * Without JS (or without <dialog>) the contact links stay plain mailto links.
   */
  function initOverlays() {
    var contact = document.getElementById("contact-dialog");
    var lightbox = document.getElementById("lightbox");
    var supported = contact && typeof contact.showModal === "function";

    if (supported) {
      var mailLink = contact.querySelector("[data-contact-mail]");
      document
        .querySelectorAll('.nav-cta, .mobile-menu-link[href^="mailto:"], .hero .btn-primary[href^="mailto:"]')
        .forEach(function (trigger) {
          trigger.addEventListener("click", function (event) {
            event.preventDefault();
            // Keep the subject line of whichever button was pressed.
            if (mailLink) mailLink.href = trigger.getAttribute("href");
            contact.showModal();
          });
        });

      var lightboxImg = lightbox && lightbox.querySelector("[data-lightbox-img]");
      var lightboxCaption = lightbox && lightbox.querySelector("[data-lightbox-caption]");
      document.querySelectorAll("figure img").forEach(function (img) {
        if (!lightboxImg || img === lightboxImg) return;
        var open = function () {
          var caption = img.closest("figure").querySelector("figcaption");
          lightboxImg.src = img.currentSrc || img.src;
          lightboxImg.alt = img.alt;
          lightboxCaption.textContent = caption ? caption.textContent : img.alt;
          lightbox.showModal();
        };
        img.tabIndex = 0;
        img.setAttribute("role", "button");
        img.classList.add("is-zoomable");
        img.addEventListener("click", open);
        img.addEventListener("keydown", function (event) {
          if (event.key === "Enter" || event.key === " ") {
            event.preventDefault();
            open();
          }
        });
      });

      [contact, lightbox].forEach(function (dialog) {
        if (!dialog) return;
        // A click on the backdrop lands on the dialog element itself.
        dialog.addEventListener("click", function (event) {
          if (event.target === dialog) dialog.close();
        });
      });
    }

    document.querySelectorAll("[data-copy]").forEach(function (button) {
      var label = button.querySelector("[data-copy-label]");
      var original = label ? label.textContent : "";
      button.addEventListener("click", function () {
        if (!navigator.clipboard) return;
        navigator.clipboard.writeText(button.getAttribute("data-copy")).then(function () {
          if (!label) return;
          label.textContent = "Correo copiado";
          window.setTimeout(function () {
            label.textContent = original;
          }, 2000);
        });
      });
    });

    var toTop = document.querySelector(".to-top");
    if (toTop) {
      var syncToTop = function () {
        toTop.classList.toggle("is-visible", window.scrollY > 700);
      };
      window.addEventListener("scroll", syncToTop, { passive: true });
      syncToTop();
    }
  }

  /**
   * Morphing active pill indicator for showcase tabs, service verticals, filters & metrics.
   */
  function initSlidingPills() {
    var groups = Array.prototype.slice.call(document.querySelectorAll("[data-sliding-tabs]"));
    if (!groups.length) return;

    /** @param {Element} container */
    var syncGroup = function (container) {
      var indicator = /** @type {HTMLElement | null} */ (
        container.querySelector(":scope > .sliding-pill-indicator")
      );
      if (!indicator) return;
      var activeBtn = /** @type {HTMLElement | null} */ (
        container.querySelector('[aria-selected="true"], [aria-pressed="true"]')
      );
      if (!activeBtn) {
        indicator.classList.remove("is-ready");
        return;
      }
      var left = activeBtn.offsetLeft;
      var top = activeBtn.offsetTop;
      var w = activeBtn.offsetWidth;
      var h = activeBtn.offsetHeight;
      if (!w || !h) return;

      indicator.style.width = w + "px";
      indicator.style.height = h + "px";
      indicator.style.transform = "translate3d(" + left + "px, " + top + "px, 0)";
      indicator.classList.add("is-ready");
    };

    groups.forEach(function (container) {
      var indicator = document.createElement("span");
      indicator.className = "sliding-pill-indicator";
      indicator.setAttribute("aria-hidden", "true");
      container.classList.add("has-sliding-pill");
      container.insertBefore(indicator, container.firstChild);

      container.addEventListener("pill:sync", function () {
        window.requestAnimationFrame(function () {
          syncGroup(container);
        });
      });

      window.requestAnimationFrame(function () {
        syncGroup(container);
      });
    });

    var syncAll = function () {
      groups.forEach(syncGroup);
    };

    window.addEventListener("resize", syncAll, { passive: true });
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(syncAll);
    }
  }

  /**
   * Pointer-tracked soft radial highlight on surface and process cards.
   */
  function initCardSpotlight() {
    var cards = Array.prototype.slice.call(document.querySelectorAll("[data-spotlight-card]"));
    if (!cards.length) return;

    var finePointer = window.matchMedia("(pointer: fine)");
    if (!finePointer.matches) return;

    cards.forEach(function (node) {
      if (!(node instanceof HTMLElement)) return;
      var card = node;
      var framePending = false;
      var nextX = 0;
      var nextY = 0;

      card.addEventListener(
        "pointermove",
        function (event) {
          var rect = card.getBoundingClientRect();
          nextX = event.clientX - rect.left;
          nextY = event.clientY - rect.top;
          if (framePending) return;
          framePending = true;
          window.requestAnimationFrame(function () {
            framePending = false;
            card.style.setProperty("--spot-x", nextX.toFixed(1) + "px");
            card.style.setProperty("--spot-y", nextY.toFixed(1) + "px");
          });
        },
        { passive: true }
      );
    });
  }

  /**
   * Animate benchmark bar widths from 0% to their target percentage.
   * @param {ParentNode | undefined} scope
   */
  function animateMetricBars(scope) {
    var rootEl = scope || document;
    var bars = Array.prototype.slice.call(rootEl.querySelectorAll(".metric-fill"));
    if (!bars.length) return;

    var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
    if (reducedMotion.matches) return;

    bars.forEach(function (node) {
      if (!(node instanceof HTMLElement)) return;
      var bar = node;
      var target = bar.getAttribute("data-target-width");
      if (!target) {
        target = bar.style.width || "0%";
        bar.setAttribute("data-target-width", target);
      }
      bar.style.width = "0%";
      window.requestAnimationFrame(function () {
        window.requestAnimationFrame(function () {
          bar.style.width = target || "0%";
        });
      });
    });
  }

  /** @param {Element | null} element */
  function triggerEnterAnimation(element) {
    if (!(element instanceof HTMLElement)) return;
    element.classList.remove("panel-entering");
    void element.offsetWidth;
    element.classList.add("panel-entering");
  }

  function initScrollNav() {
    var nav = document.getElementById("nav");
    if (!nav) return;

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
      if (scrollFrame === null) {
        scrollFrame = window.requestAnimationFrame(updateNav);
      }
    };

    updateNav();
    window.addEventListener("scroll", requestNavUpdate, { passive: true });
  }

  function initMobileMenu() {
    var toggle = document.querySelector(".nav-toggle");
    var menu = document.getElementById("mobile-menu");
    if (!toggle || !menu) return;

    var main = document.querySelector("main");
    var footer = document.querySelector("footer");
    var menuLinks = Array.prototype.slice.call(menu.querySelectorAll("a"));
    var breakpoint = window.matchMedia("(min-width: 901px)");
    var menuOpen = false;

    var setBackgroundInert = function (inert) {
      [main, footer].forEach(function (element) {
        if (element && "inert" in element) {
          element.inert = inert;
        }
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

    var handleKeydown = function (event) {
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
      if (event.matches && menuOpen) {
        setOpen(false, true);
      }
    };

    toggle.addEventListener("click", function () {
      setOpen(!menuOpen, menuOpen);
    });
    document.addEventListener("keydown", handleKeydown);
    menuLinks.forEach(function (link) {
      link.addEventListener("click", function () {
        setOpen(false, false);
      });
    });

    if (typeof breakpoint.addEventListener === "function") {
      breakpoint.addEventListener("change", handleBreakpoint);
    } else if (typeof breakpoint.addListener === "function") {
      breakpoint.addListener(handleBreakpoint);
    }

    root.classList.add("nav-enhanced");
    setOpen(false, false);
  }

  function initScrollReveal() {
    var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
    var observer = null;
    var revealTargets = Array.prototype.slice.call(document.querySelectorAll(".reveal"));
    if (!revealTargets.length) return;

    revealTargets.forEach(function (container) {
      var children = Array.prototype.slice.call(container.children);
      children.forEach(function (child, idx) {
        child.style.setProperty("--stagger-i", String(Math.min(idx, 6)));
      });
    });

    var showAll = function () {
      root.classList.remove("motion-pending", "motion-ready");
      revealTargets.forEach(function (element) {
        element.classList.add("visible");
      });
      if (observer) {
        observer.disconnect();
        observer = null;
      }
    };

    if (reducedMotion.matches || !("IntersectionObserver" in window)) {
      showAll();
      return;
    }

    observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("visible");
          animateMetricBars(entry.target);
          observer.unobserve(entry.target);
        });
      },
      { threshold: 0.08 }
    );

    revealTargets.forEach(function (element) {
      observer.observe(element);
    });
    root.classList.add("motion-pending");
    window.requestAnimationFrame(function () {
      root.classList.add("motion-ready");
    });

    if (typeof reducedMotion.addEventListener === "function") {
      reducedMotion.addEventListener("change", function (event) {
        if (event.matches) showAll();
      });
    }
  }

  function initTabGroup(tabSelector, panelSelector, tabAttr, panelAttr) {
    var tabs = Array.prototype.slice.call(document.querySelectorAll(tabSelector));
    var panels = Array.prototype.slice.call(document.querySelectorAll(panelSelector));
    if (!tabs.length || !panels.length) return;

    var activate = function (targetId, moveFocus, isUserAction) {
      tabs.forEach(function (tab) {
        var isSelected = tab.getAttribute(tabAttr) === targetId;
        tab.setAttribute("aria-selected", isSelected ? "true" : "false");
        tab.setAttribute("tabindex", isSelected ? "0" : "-1");
        if (isSelected && moveFocus) {
          tab.focus();
        }
      });

      panels.forEach(function (panel) {
        var shouldShow = panel.getAttribute(panelAttr) === targetId;
        var wasHidden = panel.hidden;
        panel.hidden = !shouldShow;
        if (shouldShow && (isUserAction || wasHidden)) {
          triggerEnterAnimation(panel);
          animateMetricBars(panel);
        }
      });

      var tabList = tabs[0].closest("[data-sliding-tabs]");
      if (tabList) {
        tabList.dispatchEvent(new CustomEvent("pill:sync"));
      }
    };

    tabs.forEach(function (tab, index) {
      tab.addEventListener("click", function () {
        activate(tab.getAttribute(tabAttr), false, true);
      });

      tab.addEventListener("keydown", function (event) {
        var nextIndex = null;
        if (event.key === "ArrowRight" || event.key === "ArrowDown") {
          nextIndex = (index + 1) % tabs.length;
        } else if (event.key === "ArrowLeft" || event.key === "ArrowUp") {
          nextIndex = (index - 1 + tabs.length) % tabs.length;
        } else if (event.key === "Home") {
          nextIndex = 0;
        } else if (event.key === "End") {
          nextIndex = tabs.length - 1;
        }
        if (nextIndex === null) return;
        event.preventDefault();
        activate(tabs[nextIndex].getAttribute(tabAttr), true, true);
      });
    });

    var initial = tabs.find(function (t) {
      return t.getAttribute("aria-selected") === "true";
    }) || tabs[0];
    activate(initial.getAttribute(tabAttr), false, false);
  }

  function initTerminalReplay() {
    var replayBtn = document.querySelector("[data-terminal-replay]");
    var terminalContainer = document.querySelector("[data-terminal-stream]");
    if (!replayBtn || !terminalContainer) return;

    var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
    var timers = [];

    var clearTimers = function () {
      timers.forEach(function (id) {
        window.clearTimeout(id);
      });
      timers = [];
    };

    var runStream = function () {
      clearTimers();
      var lines = Array.prototype.slice.call(terminalContainer.querySelectorAll(".term-line"));
      if (!lines.length) return;

      if (reducedMotion.matches) {
        lines.forEach(function (line) {
          line.classList.remove("is-hidden");
        });
        return;
      }

      lines.forEach(function (line) {
        line.classList.add("is-hidden");
      });

      lines.forEach(function (line, idx) {
        var timer = window.setTimeout(function () {
          line.classList.remove("is-hidden");
        }, idx * 140);
        timers.push(timer);
      });
    };

    replayBtn.addEventListener("click", function () {
      var medscanTab = document.querySelector('[data-workbench-tab="medscan"]');
      if (medscanTab && medscanTab.getAttribute("aria-selected") !== "true") {
        medscanTab.click();
      }
      runStream();
    });
  }

  function initArchInspectors() {
    var containers = Array.prototype.slice.call(document.querySelectorAll("[data-arch-inspector]"));
    containers.forEach(function (container) {
      var nodes = Array.prototype.slice.call(container.querySelectorAll("[data-arch-node]"));
      var readout = container.querySelector("[data-arch-detail]");
      if (!nodes.length || !readout) return;

      var selectNode = function (node, animate) {
        nodes.forEach(function (item) {
          var active = item === node;
          item.classList.toggle("is-active", active);
          item.setAttribute("aria-pressed", active ? "true" : "false");
        });
        var title = node.getAttribute("data-node-title") || node.textContent;
        var desc = node.getAttribute("data-node-desc") || "";
        readout.innerHTML = "";
        var strong = document.createElement("strong");
        strong.textContent = title + ": ";
        readout.appendChild(strong);
        readout.appendChild(document.createTextNode(desc));
        if (animate) triggerEnterAnimation(readout);
      };

      nodes.forEach(function (node) {
        node.addEventListener("click", function () {
          selectNode(node, true);
        });
      });

      var initial = nodes.find(function (n) {
        return n.classList.contains("is-active");
      }) || nodes[0];
      selectNode(initial, false);
    });
  }

  function initFilters() {
    var groups = Array.prototype.slice.call(document.querySelectorAll("[data-filter-group]"));
    groups.forEach(function (group) {
      var buttons = Array.prototype.slice.call(group.querySelectorAll("[data-filter]"));
      var items = Array.prototype.slice.call(group.querySelectorAll("[data-filter-item]"));
      if (!buttons.length || !items.length) return;

      var applyFilter = function (category) {
        group.classList.toggle("is-filtered", category !== "all");
        buttons.forEach(function (btn) {
          btn.setAttribute("aria-pressed", btn.getAttribute("data-filter") === category ? "true" : "false");
        });

        items.forEach(function (item) {
          if (category === "all") {
            item.hidden = false;
            triggerEnterAnimation(item);
            return;
          }
          var raw = item.getAttribute("data-categories") || "";
          var categories = raw.split(/\s+/).filter(Boolean);
          var show = categories.indexOf(category) !== -1;
          item.hidden = !show;
          if (show) triggerEnterAnimation(item);
        });

        var filterBar = group.querySelector("[data-sliding-tabs]");
        if (filterBar) {
          filterBar.dispatchEvent(new CustomEvent("pill:sync"));
        }
      };

      buttons.forEach(function (btn) {
        btn.addEventListener("click", function () {
          applyFilter(btn.getAttribute("data-filter"));
        });
      });
    });
  }

  try {
    setYear();
    initWordReveal();
    initAntigravityCanvas();
    // SMIL ignores the reduced-motion media query, so freeze orbit illustrations by hand.
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      document.querySelectorAll("svg.orbit-art").forEach(function (svg) {
        if (svg.pauseAnimations) svg.pauseAnimations();
      });
    }
    initSlidingPills();
    initCardSpotlight();
    initScrollNav();
    initMobileMenu();
    initOverlays();
    initScrollReveal();
    initTabGroup("[data-workbench-tab]", "[data-workbench-panel]", "data-workbench-tab", "data-workbench-panel");
    initTabGroup("[data-service-tab]", "[data-service-panel]", "data-service-tab", "data-service-panel");
    initTabGroup("[data-metric-tab]", "[data-metric-panel]", "data-metric-tab", "data-metric-panel");
    initTerminalReplay();
    initArchInspectors();
    initFilters();
  } catch (error) {
    root.classList.remove("nav-enhanced", "motion-pending", "motion-ready");
    document.body.classList.remove("mobile-menu-open");
  }
})();
