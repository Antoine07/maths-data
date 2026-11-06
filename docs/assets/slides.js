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
  current = indexFromHash();
  setMode(reading);
})();
