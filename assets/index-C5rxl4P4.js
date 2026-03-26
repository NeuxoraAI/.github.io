(function () {
  'use strict';

  const CONTACT_WHATSAPP_URL = 'https://wa.me/524622722089';
  const CONTACT_EMAIL = 'cmed.beta@gmail.com';
  const CONTACT_MAILTO_URL = `mailto:${CONTACT_EMAIL}`;
  const CONTACT_FORM_ENDPOINT =
    (typeof window !== 'undefined' && window.NEUXORA_FORM_ENDPOINT) ||
    'https://formspree.io/f/REEMPLAZAR_FORM_ID';
  const FORM_PROVIDER =
    (typeof window !== 'undefined' && window.NEUXORA_FORM_PROVIDER) ||
    'formspree';
  const BRIEFING_PLACEHOLDER_URL = 'https://neuxora.com/briefing.pdf';

  const copyBlocks = Object.freeze({
    hero: {
      kicker: 'León, Gto. · Squad IA',
      wordmark: 'NEUXORA',
      tagline: 'IA aplicada para operaciones críticas.',
      paragraph:
        'Diagnosticamos tu operación en 7 días, cruzamos datos sensibles y diseñamos software a medida con squads que se quedan hasta que funcione.',
      badges: ['Diagnóstico Línea A', 'IA aplicada + software a medida'],
      subpoints: [
        { label: 'Diagnóstico Línea A', value: '7 días' },
        { label: 'Tiempo de respuesta', value: '< 24 h' }
      ],
      primaryCta: 'Agendá tu diagnóstico',
      secondaryCta: 'Hablar con un squad'
    },
    presentacion: {
      title: 'No empezamos a programar hasta entender tu operación.',
      description:
        'Somos NEUXORA. Triangulamos estrategia, datos y desarrollo para marcas que están cansadas de los "pipelines mágicos". Escuchamos, auditamos y recién ahí diseñamos la solución con IA aplicada a tu operación real.',
      highlights: [
        {
          title: 'Diagnóstico profundo',
          body: 'Mapeamos procesos, datasets sensibles y stakeholders para detectar dónde la IA genera impacto inmediato.'
        },
        {
          title: 'Prototipos brutalmente honestos',
          body: 'Construimos MVP funcionales en semanas para validar tus hipótesis frente a usuarios reales antes del despliegue masivo.'
        },
        {
          title: 'Ciclo vivo',
          body: 'Operamos squads que mantienen, miden y evolucionan la solución junto con tu equipo interno sin desaparecer después del handoff.'
        }
      ],
      footnote: 'Si ya te dijeron que era imposible, dejá que lo intentemos nosotros.'
    },
    divisiones: {
      sectionLabel: 'Departamentos integrados',
      title: 'Contamos con cuatro departamentos completamente integrados.',
      subcopy:
        'Armamos squads cruzando medicina, IA, educación e investigación para mover agujas rápido y sin patear tu operación.',
      anchor: '#casos',
      ctaLabel: 'Ver capacidades',
      cards: [
        {
          slug: 'cmed',
          iconKey: 'iconCmed',
          title: 'C-MED área médica',
          summary: 'Clínicas conectadas, expediente vivo y automatización de flujos críticos.',
          badge: 'Salud'
        },
        {
          slug: 'ia-software',
          iconKey: 'iconAgencia',
          title: 'IA & Software a medida',
          summary: 'Arquitecturas híbridas, copilotos y plataformas listas para producción.',
          badge: 'IA aplicada'
        },
        {
          slug: 'educacion',
          iconKey: 'iconEducacion',
          title: 'Educación personalizada',
          summary: 'Sistemas adaptativos, tableros docentes y registros de desempeño.',
          badge: 'EdTech'
        },
        {
          slug: 'investigacion',
          iconKey: 'iconInvestigacion',
          title: 'Investigación aplicada',
          summary: 'Prototipos con universidades (VIDA-UG, Tec) listos para transferencia.',
          badge: 'I+D'
        }
      ]
    },
    metodo: {
      kicker: 'Método Línea A',
      headline: 'Método Línea A',
      description:
        'Nos metemos en tus procesos con un diagnóstico obsesivo, operamos con sprints visibles y quedamos al mando hasta que tu solución respire sola.',
      steps: [
        {
          title: 'Diagnóstico',
          description: 'Sesiones inmersivas para entender procesos, riesgos y datos. Entregamos mapa táctico.',
          duration: 'Semana 1'
        },
        {
          title: 'Cotización',
          description: 'Definimos alcance, MVP y milestones con costos claros y SLA aprobados.',
          duration: 'Semana 2'
        },
        {
          title: 'Desarrollo',
          description: 'Sprints quincenales, demos abiertas y ajustes sobre datos reales sin sorpresas.',
          duration: 'Semanas 3-8'
        },
        {
          title: 'Entrega',
          description: 'Implementación, capacitación y documentación viva para tu equipo.',
          duration: 'Semana 9'
        },
        {
          title: 'Mantenimiento',
          description: 'Monitoreo, soporte y evolución continua con respuesta <24h.',
          duration: 'Continuo'
        }
      ],
      cta: 'Solicitar diagnóstico',
      ctaBlock: {
        title: '¿Qué recibís en el diagnóstico Línea A?',
        description: 'Entregamos artefactos accionables para que decidas rápido sin humo.',
        deliverables: [
          'Mapa táctico de procesos, riesgos y owners',
          'Backlog priorizado con estimaciones y responsables',
          'Arquitectura IA + stack sugerido listo para aprobar',
          'Roadmap de despliegue y próximos 3 sprints'
        ],
        primaryCta: 'Reservar diagnóstico',
        secondaryCta: 'Descargar briefing',
        footnote: '7 días · NDA firmado · sin costo inicial'
      }
    },
    porque: {
      title: '¿Por qué NEUXORA?',
      subtitle: 'No somos consultores de slides; medimos impacto en horas de operación recuperadas.',
      bullets: [
        'Diagnóstico obsesivo basado en datos y usuarios reales.',
        'Arquitecturas IA operando en tu contexto regulatorio, no en laboratorios.',
        'Respuesta <24h y squads que se quedan para sostener lo que construyen.'
      ]
    },
    casos: {
      label: 'Resultados medibles',
      title: 'Vida UG · C-MED Investigación',
      description:
        'Co-diseñamos la app que captura medidas precisas para sillas de ruedas infantiles y elimina semanas de retrabajo en brigadas clínicas.',
      vidaUG: {
        kicker: 'Programa VIDA UG',
        headline: 'App de mediciones clínicas para niñas y niños con discapacidad motriz.',
        summary:
          'VIDA-UG necesitaba estandarizar mediciones en campo para fabricar sillas personalizadas sin perder trazabilidad regulatoria. Entramos con squads C-MED, IA aplicada y dev full-stack.',
        story: [
          {
            title: 'El reto',
            body: 'Las brigadas tomaban medidas en papel, con formatos distintos y datos incompletos que atrasaban entregas hasta por 3 semanas.'
          },
          {
            title: 'Cómo lo resolvimos',
            body: 'Construimos una app progresiva offline con checklist guiado, validaciones IA y cifrado para sincronizar datos seguros al centro C-MED.'
          },
          {
            title: 'Qué cambió',
            body: 'Los equipos capturan mediciones en 12 minutos, sincronizan en 2 y disparan órdenes automatizadas listas para auditoría clínica.'
          }
        ],
        metrics: [
          { value: '+37%', label: 'precisión en mediciones críticas' },
          { value: '5 a 2 días', label: 'entrega de sillas personalizadas' },
          { value: '100%', label: 'registros cifrados y auditables' }
        ],
        quote:
          'Cuando NEUXORA tomó el caso dejamos de perder semanas reconstruyendo medidas: ahora entregamos con rigor clínico.',
        quoteAuthor: 'María Rivera · Directora VIDA UG',
        ctas: {
          briefingLabel: 'Descargar briefing Vida UG',
          briefingHref: BRIEFING_PLACEHOLDER_URL,
          whatsappLabel: 'Hablar con C-MED'
        }
      }
    },
    contacto: {
      label: 'Contacto',
      headline: '¿Listo para destrabar tu proyecto imposible?',
      subcopy:
        'Te respondemos en menos de 24 horas con un plan de diagnóstico gratuito, entregables y riesgos claros.',
      helper:
        'El formulario vive en GitHub Pages y llega cifrado vía Formspree directo al squad.',
      phone: '+52 462 272 2089',
      phoneHref: 'tel:+524622722089',
      whatsapp: CONTACT_WHATSAPP_URL,
      email: CONTACT_EMAIL,
      emailHref: CONTACT_MAILTO_URL,
      horario: 'Lunes a Sábado · 09:00 - 20:00 h',
      whatsappCta: 'Hablar por WhatsApp',
      qrTitle: '¿Sin tiempo? Escaneá y escribinos por WhatsApp.',
      qrLabel: 'Escaneá el código para abrir WhatsApp.',
      infoLabels: {
        telefono: 'Teléfono',
        email: 'Email',
        horario: 'Horario'
      },
      directChannels: {
        title: 'Canales inmediatos',
        description: 'Respondemos en menos de 24h también por WhatsApp o correo directo.',
        emailCtaLabel: 'Enviar correo a C-MED'
      },
      form: {
        title: 'Mandanos tu brief',
        description:
          'Compartí el contexto, datasets sensibles y urgencia. Coordinamos el diagnóstico y NDA en horas.',
        helper:
          'Formspree procesa este formulario para GitHub Pages. Si migrás a Netlify, dejá activas las etiquetas data-netlify para que el backup funcione.',
        submitLabel: 'Enviar brief',
        success: 'Gracias por escribirnos. Te respondemos en menos de 24 horas.',
        error:
          'No pudimos enviar el formulario. Intentá nuevamente o escribinos a WhatsApp/correo.',
        configError:
          'Actualizá CONTACT_FORM_ENDPOINT con el ID real de Formspree antes de publicar.',
        sending: 'Enviando...'
      },
      formFields: {
        nombre: { label: 'Nombre completo', placeholder: 'Ej. Ana Torres' },
        email: { label: 'Email laboral', placeholder: 'nombre@empresa.com' },
        telefono: { label: 'Teléfono / WhatsApp', placeholder: '+52 462 000 0000' },
        sector: { label: 'Sector / Industria', placeholder: 'Seleccioná el frente principal' },
        mensaje: { label: 'Mensaje', placeholder: 'Contanos qué necesitás destrabar' }
      },
      sectores: ['Salud', 'Educación', 'Investigación', 'Retail', 'Startups'],
      emailCtaLabel: 'Enviar correo directo',
      privacyNote: 'Firmamos NDA antes de ver tus datos sensibles.'
    }
  });

  const processSteps = copyBlocks.metodo.steps;
  const divisionCards = copyBlocks.divisiones.cards;
  const vidaUGCase = copyBlocks.casos.vidaUG;
  const deliverables = copyBlocks.metodo.ctaBlock.deliverables;
  const sectorOptions = copyBlocks.contacto.sectores;
  const contactFormCopy = copyBlocks.contacto.form;
  const contactFormFields = copyBlocks.contacto.formFields;

  const assetsManifest = Object.freeze({
    logoHex: 'assets/logo-hex.svg',
    iconAgencia: 'assets/icon-agencia.svg',
    iconCmed: 'assets/icon-cmed.svg',
    iconEducacion: 'assets/icon-educacion.svg',
    iconInvestigacion: 'assets/icon-investigacion.svg',
    qrWhatsapp: 'assets/qr-whatsapp.svg'
  });

  function dataLayerSafePush(payload) {
    if (!payload || typeof payload !== 'object') {
      return;
    }

    try {
      if (Array.isArray(window.dataLayer)) {
        window.dataLayer.push(payload);
      } else {
        window.__nxDataLayerQueue = window.__nxDataLayerQueue || [];
        window.__nxDataLayerQueue.push(payload);
      }
    } catch (error) {
      console.error('[NEUXORA] dataLayerSafePush', error);
    }
  }

  function prefersReducedMotion() {
    return (
      window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches
    );
  }

  function smoothScrollToContact() {
    const contactSection = document.getElementById('contacto');
    if (!contactSection) {
      return;
    }

    contactSection.scrollIntoView({
      behavior: prefersReducedMotion() ? 'auto' : 'smooth',
      block: 'start'
    });
  }

  function openWhatsApp() {
    window.open(CONTACT_WHATSAPP_URL, '_blank', 'noopener,noreferrer');
  }

  function openBriefing() {
    window.open(BRIEFING_PLACEHOLDER_URL, '_blank', 'noopener,noreferrer');
  }

  function openEmail() {
    window.location.href = CONTACT_MAILTO_URL;
  }

  const CTA_BEHAVIORS = Object.freeze({
    diagnostico: smoothScrollToContact,
    whatsapp: openWhatsApp,
    briefing: openBriefing,
    'hero-primary': smoothScrollToContact,
    'hero-whatsapp': openWhatsApp,
    'case-briefing': openBriefing,
    'case-whatsapp': openWhatsApp,
    'contact-whatsapp': openWhatsApp,
    'contact-email': openEmail
  });

  const CTA_TARGETS = new Set(Object.keys(CTA_BEHAVIORS));

  function handleCTA(target, location) {
    if (!CTA_TARGETS.has(target)) {
      return;
    }

    const payload = {
      event: 'cta_click',
      location: location || 'hero',
      target
    };
    dataLayerSafePush(payload);

    const behavior = CTA_BEHAVIORS[target];
    if (typeof behavior === 'function') {
      behavior();
    }
  }

  function attachCTAHandlers() {
    document.querySelectorAll('[data-cta-target]').forEach((node) => {
      node.addEventListener('click', (event) => {
        const target = node.dataset.ctaTarget;
        const location = node.dataset.ctaLocation || 'hero';

        if (!CTA_TARGETS.has(target)) {
          return;
        }

        event.preventDefault();
        handleCTA(target, location);
      });
    });
  }

  function resolvePath(path) {
    return path.split('.').reduce((acc, segment) => {
      if (acc && Object.prototype.hasOwnProperty.call(acc, segment)) {
        return acc[segment];
      }
      return undefined;
    }, copyBlocks);
  }

  function hydrateCopy() {
    document.querySelectorAll('[data-copy-key]').forEach((node) => {
      const key = node.dataset.copyKey;
      if (!key) {
        return;
      }

      const value = resolvePath(key);
      const copyAttr = node.dataset.copyAttr;
      if (typeof value === 'string') {
        if (copyAttr) {
          node.setAttribute(copyAttr, value);
        } else if (node.dataset.copyType === 'html') {
          node.innerHTML = value;
        } else {
          node.textContent = value;
        }
      }
    });
  }

  function setAssetPlaceholders() {
    document.querySelectorAll('[data-asset-key]').forEach((node) => {
      const key = node.dataset.assetKey;
      if (key && assetsManifest[key]) {
        node.setAttribute('src', assetsManifest[key]);
      }
    });
  }

  function renderHeroWordmark() {
    const node = document.querySelector('[data-hero-wordmark]');
    const heading = document.querySelector('[data-hero-heading]');
    if (!node) {
      return;
    }

    const wordmark = copyBlocks.hero.wordmark || copyBlocks.hero.headline || '';
    node.setAttribute('aria-label', wordmark);
    if (heading) {
      heading.textContent = wordmark;
    }

    if (!wordmark) {
      node.textContent = '';
      return;
    }

    if (prefersReducedMotion()) {
      node.textContent = wordmark;
      node.dataset.motion = 'static';
      return;
    }

    node.dataset.motion = 'dynamic';
    node.innerHTML = '';
    [...wordmark].forEach((character, index) => {
      const span = document.createElement('span');
      span.textContent = character === ' ' ? '\u00A0' : character;
      span.className = 'hero-letter';
      span.style.setProperty('--letter-index', String(index));
      span.setAttribute('aria-hidden', 'true');
      node.appendChild(span);
    });
  }

  function renderDivisionCards() {
    const container = document.querySelector('[data-division-cards]');
    if (!container || !Array.isArray(divisionCards)) {
      return;
    }

    const fragment = document.createDocumentFragment();
    divisionCards.forEach((card, index) => {
      const article = document.createElement('article');
      article.className =
        'department-card rounded-3xl border border-white/10 bg-slate-900/70 p-6 shadow-nx-card transition duration-300 hover:border-cyan-400/40';
      article.setAttribute('data-card-slug', card.slug);

      const iconSrc = assetsManifest[card.iconKey] || '';
      article.innerHTML = `
        <div class="flex items-center justify-between text-xs uppercase tracking-[0.2em] text-slate-400">
          <span>${String(index + 1).padStart(2, '0')}</span>
          <span class="rounded-full border border-white/10 px-3 py-1 text-[11px] text-white/80">${card.badge}</span>
        </div>
        <div class="mt-5 flex items-center gap-3">
          <div class="rounded-2xl bg-white/5 p-3">
            <img src="${iconSrc}" alt="Icono ${card.title}" class="h-10 w-10" loading="lazy" />
          </div>
          <h3 class="text-lg font-semibold text-white">${card.title}</h3>
        </div>
        <p class="mt-4 text-sm text-slate-300">${card.summary}</p>
      `;

      const iconNode = article.querySelector('img');
      if (iconNode) {
        iconNode.dataset.assetKey = card.iconKey;
      }

      fragment.appendChild(article);
    });

    container.innerHTML = '';
    container.appendChild(fragment);
  }

  function renderWhyNeuxoraBullets() {
    const list = document.querySelector('[data-porque-list]');
    if (!list || !Array.isArray(copyBlocks.porque.bullets)) {
      return;
    }

    const fragment = document.createDocumentFragment();
    copyBlocks.porque.bullets.forEach((bullet) => {
      const item = document.createElement('li');
      item.className = 'flex items-start gap-3 text-base text-slate-200';
      item.innerHTML = `
        <span class="mt-2 h-2 w-2 flex-shrink-0 rounded-full bg-cyan-400"></span>
        <span>${bullet}</span>
      `;
      fragment.appendChild(item);
    });

    list.innerHTML = '';
    list.appendChild(fragment);
  }

  function renderProcessSteps() {
    const list = document.querySelector('[data-process-list]');
    if (!list || !Array.isArray(processSteps)) {
      return;
    }

    const fragment = document.createDocumentFragment();
    processSteps.forEach((step, index) => {
      const article = document.createElement('article');
      article.className =
        'process-step relative rounded-3xl border border-white/5 bg-slate-900/30 p-6 pl-10 transition-colors duration-300';
      article.dataset.processStep = 'true';
      article.dataset.stepIndex = String(index);
      if (index === 0) {
        article.classList.add('is-active');
      }

      article.innerHTML = `
        <div class="flex items-center justify-between text-xs uppercase tracking-[0.3em] text-slate-400">
          <span>${step.duration}</span>
          <span>${String(index + 1).padStart(2, '0')}</span>
        </div>
        <h3 class="mt-4 text-xl font-semibold text-white">${step.title}</h3>
        <p class="mt-3 text-sm text-slate-300">${step.description}</p>
      `;

      fragment.appendChild(article);
    });

    list.innerHTML = '';
    list.appendChild(fragment);
  }

  function renderDeliverablesList() {
    const list = document.querySelector('[data-deliverables-list]');
    if (!list || !Array.isArray(deliverables)) {
      return;
    }

    const fragment = document.createDocumentFragment();
    deliverables.forEach((deliverable) => {
      const item = document.createElement('li');
      item.className = 'flex items-start gap-3 text-sm text-slate-200';
      item.innerHTML = `
        <span class="mt-1 h-2 w-2 flex-shrink-0 rounded-full bg-cyan-400"></span>
        <span>${deliverable}</span>
      `;
      fragment.appendChild(item);
    });

    list.innerHTML = '';
    list.appendChild(fragment);
  }

  function renderVidaUGCase() {
    if (!vidaUGCase) {
      return;
    }

    const metricsContainer = document.querySelector('[data-case-metrics]');
    const storyContainer = document.querySelector('[data-case-story]');
    const briefingLink = document.querySelector('[data-case-briefing]');
    const whatsappLink = document.querySelector('[data-case-whatsapp]');

    if (metricsContainer && Array.isArray(vidaUGCase.metrics)) {
      const fragment = document.createDocumentFragment();
      vidaUGCase.metrics.forEach((metric) => {
        const item = document.createElement('div');
        item.className = 'rounded-3xl border border-white/10 bg-slate-900/70 p-4 shadow-nx-card';
        item.innerHTML = `
          <p class="text-3xl font-semibold text-white">${metric.value}</p>
          <p class="mt-2 text-sm text-slate-300">${metric.label}</p>
        `;
        fragment.appendChild(item);
      });
      metricsContainer.innerHTML = '';
      metricsContainer.appendChild(fragment);
    }

    if (storyContainer && Array.isArray(vidaUGCase.story)) {
      const fragment = document.createDocumentFragment();
      vidaUGCase.story.forEach((story) => {
        const card = document.createElement('article');
        card.className =
          'case-story-card rounded-3xl border border-white/10 bg-slate-900/60 p-5';
        card.innerHTML = `
          <p class="text-xs uppercase tracking-[0.3em] text-cyan-200">${story.title}</p>
          <p class="mt-2 text-sm text-slate-200">${story.body}</p>
        `;
        fragment.appendChild(card);
      });
      storyContainer.innerHTML = '';
      storyContainer.appendChild(fragment);
    }

    if (briefingLink && vidaUGCase.ctas?.briefingHref) {
      briefingLink.setAttribute('href', vidaUGCase.ctas.briefingHref);
    }

    if (whatsappLink) {
      whatsappLink.setAttribute('href', CONTACT_WHATSAPP_URL);
    }
  }

  function renderSectorOptions() {
    const select = document.querySelector('[data-sector-select]');
    if (!select || !Array.isArray(sectorOptions)) {
      return;
    }

    select.innerHTML = '';
    const placeholderOption = document.createElement('option');
    placeholderOption.value = '';
    placeholderOption.textContent = contactFormFields.sector.placeholder;
    placeholderOption.disabled = true;
    placeholderOption.selected = true;
    select.appendChild(placeholderOption);

    sectorOptions.forEach((sector) => {
      const option = document.createElement('option');
      option.value = sector;
      option.textContent = sector;
      select.appendChild(option);
    });
  }

  function renderDynamicSections() {
    renderHeroWordmark();
    renderDivisionCards();
    renderWhyNeuxoraBullets();
    renderProcessSteps();
    renderDeliverablesList();
    renderVidaUGCase();
    renderSectorOptions();
  }

  function initProcessTimeline() {
    const steps = document.querySelectorAll('[data-process-step]');
    if (!steps.length) {
      return;
    }

    const setActive = (target) => {
      steps.forEach((node) => {
        node.classList.toggle('is-active', node === target);
      });
    };

    setActive(steps[0]);

    if (!('IntersectionObserver' in window)) {
      return;
    }

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setActive(entry.target);
          }
        });
      },
      { threshold: 0.45, rootMargin: '-10% 0% -30% 0%' }
    );

    steps.forEach((step) => observer.observe(step));
  }

  const FORM_ENDPOINT_CONFIGURED =
    Boolean(CONTACT_FORM_ENDPOINT) &&
    !CONTACT_FORM_ENDPOINT.includes('REEMPLAZAR_FORM_ID');

  async function submitContactForm(event) {
    event.preventDefault();
    const form = event.currentTarget;
    const submitButton = form.querySelector('[data-form-submit]');
    const statusNode = form.querySelector('[data-form-status]');
    const honeypotField = form.querySelector('[data-honeypot]');

    if (!form || !submitButton) {
      return;
    }

    if (statusNode) {
      statusNode.textContent = contactFormCopy.sending;
      statusNode.dataset.state = 'pending';
    }

    submitButton.disabled = true;

    if (honeypotField && honeypotField.value) {
      submitButton.disabled = false;
      return;
    }

    if (!FORM_ENDPOINT_CONFIGURED) {
      if (statusNode) {
        statusNode.textContent =
          contactFormCopy.configError || contactFormCopy.error;
        statusNode.dataset.state = 'error';
      }
      submitButton.disabled = false;
      console.error('[NEUXORA] CONTACT_FORM_ENDPOINT is not configured');
      return;
    }

    const formData = new FormData(form);
    ['nombre', 'email', 'telefono', 'mensaje'].forEach((field) => {
      const fieldNode = form[field];
      if (fieldNode && typeof fieldNode.value === 'string') {
        formData.set(field, fieldNode.value.trim());
      }
    });
    formData.append('_provider', FORM_PROVIDER);
    formData.append('_origin', window.location.href);

    try {
      const response = await fetch(CONTACT_FORM_ENDPOINT, {
        method: 'POST',
        headers: { Accept: 'application/json' },
        body: formData
      });

      if (!response.ok) {
        throw new Error('CONTACT_FORM_FAILED');
      }

      form.reset();
      if (statusNode) {
        statusNode.textContent = contactFormCopy.success;
        statusNode.dataset.state = 'success';
      }
      dataLayerSafePush({
        event: 'contact_form_submit',
        status: 'success',
        provider: FORM_PROVIDER
      });
    } catch (error) {
      console.error('[NEUXORA] submitContactForm', error);
      if (statusNode) {
        statusNode.textContent = contactFormCopy.error;
        statusNode.dataset.state = 'error';
      }
      dataLayerSafePush({
        event: 'contact_form_submit',
        status: 'error',
        provider: FORM_PROVIDER
      });
    } finally {
      submitButton.disabled = false;
    }
  }

  function initContactForm() {
    const form = document.getElementById('contacto-form');
    if (!form) {
      return;
    }

    if (CONTACT_FORM_ENDPOINT) {
      form.setAttribute('action', CONTACT_FORM_ENDPOINT);
    }
    form.setAttribute('method', 'POST');
    form.dataset.formProvider = FORM_PROVIDER;
    const providerField = form.querySelector('[data-form-provider-field]');
    if (providerField) {
      providerField.value = FORM_PROVIDER;
    }

    form.addEventListener('submit', submitContactForm);
  }

  function init() {
    renderDynamicSections();
    hydrateCopy();
    setAssetPlaceholders();
    attachCTAHandlers();
    initProcessTimeline();
    initContactForm();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  window.NeuxoraSite = Object.assign({}, window.NeuxoraSite, {
    copyBlocks,
    assetsManifest,
    dataLayerSafePush,
    handleCTA,
    submitContactForm
  });
})();
