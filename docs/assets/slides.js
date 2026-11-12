(() => {
  'use strict';
  const articles = [...document.querySelectorAll('#slides > article')];
  const links = [...document.querySelectorAll('[data-slide-link]')];
  if (!articles.length) return;
  const byId = id => document.getElementById(id);
  const previous = byId('previous');
  const next = byId('next');
  const progress = byId('progress');
  const outline = byId('outline');
  let current = 0;
  let reading = document.body.classList.contains('reading-mode');
  let observer;
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function indexFromHash() {
    const hash = decodeURIComponent(location.hash.slice(1));
    if (/^\d+$/.test(hash)) return Math.min(articles.length - 1, Math.max(0, Number(hash) - 1));
    const target = document.getElementById(hash);
    const index = articles.findIndex(article => article.contains(target));
    return index < 0 ? 0 : index;
  }
  function updateProgress() {
    const number = current + 1;
    byId('position').textContent = `Slide ${number} sur ${articles.length}`;
    byId('page-number').textContent = `${String(number).padStart(2, '0')} / ${articles.length}`;
    byId('progress-label').textContent = `${Math.round(100 * number / articles.length)} %`;
    progress.value = number;
    previous.disabled = current === 0;
    next.disabled = current === articles.length - 1;
    links.forEach((link, i) => i === current ? link.setAttribute('aria-current', 'step') : link.removeAttribute('aria-current'));
    const active = links[current];
    if (active && outline.getBoundingClientRect().width && !reading) {
      const list = active.parentElement;
      if (active.offsetTop < list.scrollTop || active.offsetTop + active.offsetHeight > list.scrollTop + list.clientHeight) list.scrollTop = active.offsetTop - list.clientHeight / 2;
    }
  }
  function select(index, { hash = true, scroll = false, focus = false } = {}) {
    current = Math.min(articles.length - 1, Math.max(0, index));
    articles.forEach((article, i) => { article.hidden = !reading && i !== current; });
    if (hash) history.replaceState(null, '', `#${current + 1}`);
    updateProgress();
    if (scroll) articles[current].scrollIntoView({ behavior: reduceMotion ? 'instant' : 'smooth', block: 'start' });
    if (focus) {
      const article = articles[current];
      article.tabIndex = -1;
      article.focus({ preventScroll: true });
    }
  }
  function setMode(value) {
    reading = value;
    document.body.classList.toggle('reading-mode', reading);
    byId('mode-slides').setAttribute('aria-pressed', String(!reading));
    byId('mode-reading').setAttribute('aria-pressed', String(reading));
    select(current);
    observer?.disconnect();
    if (reading && 'IntersectionObserver' in window) {
      observer = new IntersectionObserver(entries => {
        const visible = entries.filter(entry => entry.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
        if (visible) { current = articles.indexOf(visible.target); updateProgress(); }
      }, { rootMargin: '-8% 0px -45% 0px', threshold: [0, .1, .5] });
      articles.forEach(article => observer.observe(article));
    }
  }
  previous.addEventListener('click', () => select(current - 1, { focus: true }));
  next.addEventListener('click', () => select(current + 1, { focus: true }));
  links.forEach((link, i) => link.addEventListener('click', event => {
    event.preventDefault();
    select(i, { scroll: reading, focus: true });
    outline.classList.remove('is-open');
    byId('toggle-outline').setAttribute('aria-expanded', 'false');
  }));
  document.querySelectorAll('.prose a[href^="#"]').forEach(link => link.addEventListener('click', event => {
    const target = document.getElementById(decodeURIComponent(link.hash.slice(1)));
    const index = articles.findIndex(article => article.contains(target));
    if (index >= 0) { event.preventDefault(); select(index, { scroll: reading, focus: true }); }
  }));
  byId('mode-slides').addEventListener('click', () => setMode(false));
  byId('mode-reading').addEventListener('click', () => setMode(true));
  byId('toggle-outline').addEventListener('click', event => {
    const open = outline.classList.toggle('is-open');
    event.currentTarget.setAttribute('aria-expanded', String(open));
  });
  async function toggleFullscreen() {
    try {
      if (document.fullscreenElement) await document.exitFullscreen();
      else if (document.body.requestFullscreen) await document.body.requestFullscreen();
    } catch { /* Browser may refuse fullscreen outside a direct user action. */ }
  }
  if (!document.fullscreenEnabled) byId('fullscreen').hidden = true;
  byId('fullscreen').addEventListener('click', toggleFullscreen);
  document.addEventListener('keydown', event => {
    if (event.altKey || event.ctrlKey || event.metaKey || event.target.closest('input, textarea, select, summary, details, pre, [contenteditable="true"]')) return;
    if (!reading && ['ArrowRight', 'ArrowLeft', 'Home', 'End'].includes(event.key)) {
      event.preventDefault();
      select(event.key === 'Home' ? 0 : event.key === 'End' ? articles.length - 1 : current + (event.key === 'ArrowRight' ? 1 : -1), { focus: true });
    }
    if (event.key.toLowerCase() === 'f' && !event.target.closest('button, a')) { event.preventDefault(); toggleFullscreen(); }
  });
  window.addEventListener('hashchange', () => select(indexFromHash(), { hash: false, scroll: reading }));
  byId('print').addEventListener('click', () => window.print());
  let printDetails = [];
  window.addEventListener('beforeprint', () => {
    printDetails = [...document.querySelectorAll('details')].filter(detail => !detail.open);
    printDetails.forEach(detail => { detail.open = true; });
  });
  window.addEventListener('afterprint', () => { printDetails.forEach(detail => { detail.open = false; }); });
  function fallbackImage(img) {
    if (img.classList.contains('image-unavailable')) return;
    img.classList.add('image-unavailable');
    const fallback = document.createElement('a');
    fallback.className = 'image-fallback';
    fallback.href = img.src;
    fallback.target = '_blank';
    fallback.rel = 'noopener';
    fallback.textContent = `${img.alt && img.alt !== 'Image' ? img.alt : 'Illustration du cours'} — ouvrir la source ↗`;
    img.insertAdjacentElement('afterend', fallback);
  }
  document.querySelectorAll('.prose img').forEach(img => {
    img.addEventListener('error', () => fallbackImage(img));
    if (img.complete && img.naturalWidth === 0) fallbackImage(img);
  });
  const svgNS = 'http://www.w3.org/2000/svg';
  const formatFr = (value, digits = 2) => value.toFixed(digits).replace('.', ',').replace('-', '−');
  document.querySelectorAll('[data-wave-demo]').forEach(root => {
    const period = root.querySelector('[data-wave-period]');
    const phase = root.querySelector('[data-wave-phase]');
    const toggle = root.querySelector('[data-wave-toggle]');
    const path = root.querySelector('[data-wave-path]');
    const hand = root.querySelector('[data-wave-hand]');
    const circlePoint = root.querySelector('[data-wave-circle-point]');
    const graphPoint = root.querySelector('[data-wave-graph-point]');
    const cursor = root.querySelector('[data-wave-cursor]');
    const readout = root.querySelector('[data-wave-readout]');
    const periodLabel = root.querySelector('[data-wave-period-label]');
    const phaseLabel = root.querySelector('[data-wave-phase-label]');
    let time = 0;
    let running = false;
    let frame = 0;
    let lastFrame = 0;
    const plot = { left: 270, top: 86, width: 680, middle: 166, amplitude: 80 };
    function render() {
      const p = Number(period.value);
      const phaseDegrees = Number(phase.value);
      const phaseRadians = phaseDegrees * Math.PI / 180;
      const wave = t => Math.sin(2 * Math.PI * t / p + phaseRadians);
      const angle = 2 * Math.PI * time / p + phaseRadians;
      const cx = 125, cy = 166, radius = 78;
      const px = cx + radius * Math.cos(angle);
      const py = cy - radius * Math.sin(angle);
      hand.setAttribute('x2', px.toFixed(2));
      hand.setAttribute('y2', py.toFixed(2));
      circlePoint.setAttribute('cx', px.toFixed(2));
      circlePoint.setAttribute('cy', py.toFixed(2));
      const points = Array.from({ length: 241 }, (_, i) => {
        const t = 48 * i / 240;
        const x = plot.left + plot.width * t / 48;
        const y = plot.middle - plot.amplitude * wave(t);
        return `${i ? 'L' : 'M'}${x.toFixed(2)},${y.toFixed(2)}`;
      }).join(' ');
      path.setAttribute('d', points);
      const currentX = plot.left + plot.width * (time % 48) / 48;
      const currentY = plot.middle - plot.amplitude * wave(time);
      graphPoint.setAttribute('cx', currentX.toFixed(2));
      graphPoint.setAttribute('cy', currentY.toFixed(2));
      cursor.setAttribute('x1', currentX.toFixed(2));
      cursor.setAttribute('x2', currentX.toFixed(2));
      periodLabel.textContent = `${p} h`;
      phaseLabel.textContent = `${phaseDegrees}°`;
      readout.textContent = `Temps : ${formatFr(time, 1)} h · phase : ${formatFr(angle * 180 / Math.PI, 0)}° · sinusoïde : ${formatFr(wave(time))}`;
    }
    function stop() {
      running = false;
      lastFrame = 0;
      cancelAnimationFrame(frame);
      toggle.textContent = '▶ Démarrer';
      toggle.setAttribute('aria-pressed', 'false');
    }
    function tick(now) {
      if (!running) return;
      if (lastFrame) time = (time + (now - lastFrame) * 0.003) % 48;
      lastFrame = now;
      render();
      frame = requestAnimationFrame(tick);
    }
    period.addEventListener('input', render);
    phase.addEventListener('input', render);
    toggle.addEventListener('click', () => {
      if (running) return stop();
      running = true;
      toggle.textContent = 'Ⅱ Pause';
      toggle.setAttribute('aria-pressed', 'true');
      frame = requestAnimationFrame(tick);
    });
    root.querySelector('[data-wave-reset]').addEventListener('click', () => { stop(); time = 0; render(); });
    if ('IntersectionObserver' in window) new IntersectionObserver(entries => {
      if (!entries[0].isIntersecting) stop();
    }).observe(root);
    render();
  });
  document.querySelectorAll('[data-clock-demo]').forEach(root => {
    const slider = root.querySelector('[data-clock-hour]');
    const toggle = root.querySelector('[data-clock-toggle]');
    const hand = root.querySelector('[data-clock-hand]');
    const point = root.querySelector('[data-clock-point]');
    const label = root.querySelector('[data-clock-hour-label]');
    const readout = root.querySelector('[data-clock-readout]');
    const cosine = root.querySelector('[data-clock-cos]');
    const sine = root.querySelector('[data-clock-sin]');
    let hour = Number(slider.value);
    let running = false;
    let frame = 0;
    let lastFrame = 0;
    function render() {
      const shownHour = ((hour % 24) + 24) % 24;
      const angle = 2 * Math.PI * shownHour / 24;
      const c = Math.cos(angle), s = Math.sin(angle);
      const x = 230 + 104 * c;
      const y = 170 - 104 * s;
      hand.setAttribute('x2', x.toFixed(2));
      hand.setAttribute('y2', y.toFixed(2));
      point.setAttribute('cx', x.toFixed(2));
      point.setAttribute('cy', y.toFixed(2));
      label.textContent = `${formatFr(shownHour, 2)} h`;
      cosine.textContent = formatFr(c, 3);
      sine.textContent = formatFr(s, 3);
      const distance = Math.hypot(c - 1, s);
      readout.textContent = `Encodage : (${formatFr(c, 3)} ; ${formatFr(s, 3)}) · distance à minuit : ${formatFr(distance, 3)}`;
    }
    function stop() {
      running = false;
      lastFrame = 0;
      cancelAnimationFrame(frame);
      toggle.textContent = '▶ Faire avancer l’heure';
      toggle.setAttribute('aria-pressed', 'false');
    }
    function tick(now) {
      if (!running) return;
      if (lastFrame) {
        hour = (hour + (now - lastFrame) * 0.002) % 24;
        slider.value = String(hour);
      }
      lastFrame = now;
      render();
      frame = requestAnimationFrame(tick);
    }
    slider.addEventListener('input', () => { hour = Number(slider.value); render(); });
    toggle.addEventListener('click', () => {
      if (running) return stop();
      running = true;
      toggle.textContent = 'Ⅱ Pause';
      toggle.setAttribute('aria-pressed', 'true');
      frame = requestAnimationFrame(tick);
    });
    root.querySelector('[data-clock-reset]').addEventListener('click', () => { stop(); hour = 23; slider.value = '23'; render(); });
    if ('IntersectionObserver' in window) new IntersectionObserver(entries => {
      if (!entries[0].isIntersecting) stop();
    }).observe(root);
    render();
  });
  current = indexFromHash();
  setMode(reading);
})();
