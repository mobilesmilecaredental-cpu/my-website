/* Smile Care — interactive behaviour for the static site.
   The pages are complete HTML on their own; everything here is enhancement. */
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var calm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- mobile menu ---------- */
  function menuPanel() { return $('[data-state="menuOpen"]'); }
  function setMenu(open) {
    var p = menuPanel();
    if (p) p.style.display = open ? 'block' : 'none';
  }
  document.addEventListener('click', function (e) {
    var t = e.target.closest ? e.target.closest('[data-h]') : null;
    if (!t) return;
    var h = t.getAttribute('data-h');
    if (h === 'toggleMenu') {
      e.preventDefault();
      var p = menuPanel();
      setMenu(!p || p.style.display === 'none');
    } else if (h === 'closeMenu') {
      setMenu(false);
    } else if (h === 'f.toggle') {
      e.preventDefault();
      toggleFaq(t);
    } else if (h === 'onCopy') {
      e.preventDefault();
      copyBody(t);
    }
  });

  /* ---------- FAQ accordion ---------- */
  function toggleFaq(btn) {
    var card = btn.parentElement;
    var panel = $('[data-panel]', card);
    if (!panel) return;
    var open = panel.style.display !== 'none';
    $$('[data-panel]').forEach(function (p) {
      if (p !== panel) { p.style.display = 'none'; setSign(p.parentElement, '+'); }
    });
    panel.style.display = open ? 'none' : 'block';
    setSign(card, open ? '+' : '\u2013');
  }
  function setSign(card, ch) {
    var b = $('[data-h="f.toggle"]', card);
    if (!b) return;
    var spans = b.querySelectorAll('span');
    if (spans.length) spans[spans.length - 1].textContent = ch;
  }

  /* ---------- FAQ search ---------- */
  var search = $('[data-h="onFaqSearch"]');
  if (search) {
    search.addEventListener('input', function () {
      var q = search.value.trim().toLowerCase();
      var cards = $$('[data-h="f.toggle"]').map(function (b) { return b.parentElement; });
      var shown = 0;
      cards.forEach(function (card) {
        var hit = !q || card.textContent.toLowerCase().indexOf(q) !== -1;
        card.style.display = hit ? '' : 'none';
        if (hit) shown++;
      });
      var empty = $('[data-state="noFaqMatches"]');
      if (empty) empty.style.display = shown ? 'none' : 'block';
    });
  }

  /* ---------- forms ---------- */
  var EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  var TO = 'mobilesmilecaredental@gmail.com';

  function labelFor(el) {
    var wrap = el.parentElement;
    var lab = wrap && wrap.querySelector('label');
    if (lab) return lab.textContent.replace(/\*/g, '').trim();
    return el.getAttribute('data-field') || 'Field';
  }

  function collect(form) {
    return $$('[data-field]', form).map(function (el) {
      return { el: el, key: el.getAttribute('data-field'), label: labelFor(el), value: (el.value || '').trim(), required: el.hasAttribute('required') };
    });
  }

  function subjectFor(form, fields) {
    var kind = form.getAttribute('data-h') || '';
    var get = function (k) { var f = fields.filter(function (x) { return x.key === k; })[0]; return f ? f.value : ''; };
    if (kind.indexOf('Fam') !== -1) return 'Family visit request: ' + get('parent');
    if (get('facility')) return 'Care home inquiry: ' + get('facility');
    return 'Website inquiry: ' + (get('subject') || 'general');
  }

  function panelIn(form, names) {
    var scope = form.closest('section') || document;
    for (var i = 0; i < names.length; i++) {
      var p = scope.querySelector('[data-state="' + names[i] + '"]');
      if (p) return p;
    }
    return null;
  }

  $$('form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var fields = collect(form);
      var errPanel = panelIn(form, ['sendError', 'famError']);
      var okPanel = panelIn(form, ['submitted', 'famDone']);
      var handoff = panelIn(form, ['handoff', 'famHandoff']);

      var missing = fields.some(function (f) { return f.required && !f.value; });
      var emailField = fields.filter(function (f) { return f.key === 'email'; })[0];
      var badEmail = emailField && !EMAIL.test(emailField.value);
      if (missing || badEmail) {
        if (errPanel) {
          errPanel.textContent = missing
            ? 'Please fill in the required fields so we know how to help.'
            : 'That email address doesn\u2019t look right. Please double-check it.';
          errPanel.style.display = 'block';
        }
        return;
      }
      if (errPanel) errPanel.style.display = 'none';

      var subject = subjectFor(form, fields);
      var body = fields.map(function (f) { return f.label + ': ' + (f.value || 'not provided'); }).join('\n');
      var key = window.SMILE_CARE_FORM_KEY || '';
      var btn = form.querySelector('button[type="submit"]');

      if (key) {
        var payload = { access_key: key, subject: subject, message: body, from_name: 'Smile Care website' };
        fields.forEach(function (f) { payload[f.key] = f.value; });
        if (emailField) payload._replyto = emailField.value;
        if (btn) { btn.disabled = true; btn.dataset.label = btn.textContent; btn.textContent = 'Sending\u2026'; }
        fetch('https://api.web3forms.com/submit', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify(payload)
        }).then(function (r) {
          if (!r.ok) throw new Error('bad status');
          form.style.display = 'none';
          if (okPanel) okPanel.style.display = 'block';
        }).catch(function () {
          if (btn) { btn.disabled = false; btn.textContent = btn.dataset.label || 'Send'; }
          if (errPanel) {
            errPanel.textContent = 'Something went wrong sending that. Please call (905) 941-7580 or email directly.';
            errPanel.style.display = 'block';
          }
        });
        return;
      }

      // No key configured: hand off to the visitor's mail app.
      var mailto = 'mailto:' + TO + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      try {
        var a = document.createElement('a');
        a.href = mailto; a.style.display = 'none';
        document.body.appendChild(a); a.click(); a.remove();
      } catch (err) {}
      if (handoff) {
        var gmail = handoff.querySelector('a[href]');
        if (gmail) gmail.href = 'https://mail.google.com/mail/?view=cm&fs=1&to=' + encodeURIComponent(TO) +
          '&su=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
        handoff.setAttribute('data-body', body);
        form.style.display = 'none';
        handoff.style.display = 'block';
      } else if (okPanel) {
        form.style.display = 'none';
        okPanel.style.display = 'block';
      }
    });
  });

  function copyBody(btn) {
    var panel = btn.closest('[data-state]');
    var text = (panel && panel.getAttribute('data-body')) || TO;
    var done = function () { btn.textContent = 'Copied'; setTimeout(function () { btn.textContent = 'Copy message'; }, 1800); };
    if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function () {});
    else done();
  }

  /* ---------- scroll reveals ---------- */
  function initReveals() {
    if (typeof IntersectionObserver === 'undefined') return;
    // Never hide content in a context that may not run observers at all.
    if (document.visibilityState === 'hidden') return;
    var dist = calm ? 8 : 24;
    var anims = [];
    var delivered = false;
    var io = new IntersectionObserver(function (entries) {
      delivered = true;
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        if (en.target.__rv) en.target.__rv.play();
        io.unobserve(en.target);
      });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.05 });

    var prep = function (el, delay) {
      if (!el || el.nodeType !== 1 || el.__rv) return;
      var cs = getComputedStyle(el);
      if (cs.position === 'absolute' || cs.position === 'fixed') return;
      var r = el.getBoundingClientRect();
      var vh = window.innerHeight || document.documentElement.clientHeight;
      if (r.height === 0 || r.top < vh * 0.92) return;
      if (!el.animate) return;
      var anim = el.animate([
        { opacity: 0, transform: 'translateY(' + dist + 'px)' },
        { opacity: 1, transform: 'none' }
      ], { duration: 750, delay: delay, easing: 'cubic-bezier(.22,.7,.3,1)', fill: 'both' });
      anim.pause(); anim.currentTime = 0;
      anim.onfinish = function () { try { anim.cancel(); } catch (e) {} };
      el.__rv = anim; anims.push(anim); io.observe(el);
    };
    var isList = function (el) {
      return el.children.length >= 3 && /grid-template-columns|flex-direction:column/.test(el.getAttribute('style') || '');
    };
    $$('section, footer').forEach(function (sec) {
      Array.prototype.forEach.call(sec.children, function (wrap) {
        if (wrap.nodeType !== 1) return;
        var cs = getComputedStyle(wrap);
        if (cs.position === 'absolute' || cs.position === 'fixed') return;
        if (isList(wrap)) {
          Array.prototype.forEach.call(wrap.children, function (c, i) { prep(c, Math.min(i, 8) * 80); });
          return;
        }
        var kids = Array.prototype.slice.call(wrap.children);
        var lists = kids.filter(isList);
        if (!lists.length) { prep(wrap, 0); return; }
        var d = 0;
        kids.forEach(function (k) {
          if (lists.indexOf(k) === -1) { prep(k, d); d += 60; return; }
          Array.prototype.forEach.call(k.children, function (c, i) { prep(c, d + Math.min(i, 8) * 70); });
          d += 90;
        });
      });
    });
    var revealAll = function () { anims.forEach(function (a) { try { a.finish(); } catch (e) {} }); };
    // If the observer never reports back, show everything rather than leaving
    // content stranded at opacity 0.
    setTimeout(function () { if (!delivered) revealAll(); }, 800);
    // Second net: anything paused while inside the viewport gets finished.
    var sweep = function () {
      var vh = window.innerHeight || document.documentElement.clientHeight;
      anims.forEach(function (a) {
        if (a.playState !== 'paused') return;
        var el = a.effect && a.effect.target;
        if (!el) return;
        var r = el.getBoundingClientRect();
        if (r.bottom > 0 && r.top < vh) { try { a.finish(); } catch (e) {} }
      });
    };
    window.addEventListener('scroll', sweep, { passive: true });
    setTimeout(sweep, 1500);
    document.addEventListener('visibilitychange', function () { if (document.visibilityState === 'hidden') revealAll(); });
    window.addEventListener('beforeprint', revealAll);
    window.addEventListener('pagehide', revealAll);
  }

  /* ---------- parallax ---------- */
  function initParallax() {
    var k = calm ? 0.45 : 1;
    var targets = [];
    var add = function (el, amp) { if (el && el.nodeType === 1 && el.animate) targets.push({ el: el, amp: amp * k }); };
    var hero = document.getElementById('top');
    if (hero) Array.prototype.forEach.call(hero.children, function (ch) {
      if (getComputedStyle(ch).position === 'absolute') add(ch, 26);
    });
    add($('img[src*="logo-wordmark"]'), 10);
    add($('img[src*="qr-book"]'), 8);
    $$('section div').forEach(function (d) {
      var gc = getComputedStyle(d).gridTemplateColumns;
      if (gc && gc.indexOf('64px') === 0 && d.firstElementChild) add(d.firstElementChild, 7);
    });
    if (!targets.length) return;
    targets.forEach(function (t) {
      t.anim = t.el.animate(
        [{ transform: 'translateY(' + (-t.amp) + 'px)' }, { transform: 'translateY(' + t.amp + 'px)' }],
        { duration: 1000, fill: 'both', composite: 'add', easing: 'linear' }
      );
      t.anim.pause(); t.anim.currentTime = 500;
    });
    var ticking = false;
    var update = function () {
      ticking = false;
      var vh = window.innerHeight || document.documentElement.clientHeight;
      targets.forEach(function (t) {
        var r = t.el.getBoundingClientRect();
        if (r.bottom < -200 || r.top > vh + 200) return;
        var p = Math.max(-1, Math.min(1, (r.top + r.height / 2 - vh / 2) / vh));
        try { t.anim.currentTime = (p + 1) / 2 * 1000; } catch (e) {}
      });
    };
    var onScroll = function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } };
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });
    update();
  }

  /* ---------- sparkle cursor ---------- */
  function initSparkles() {
    if (!document.body.animate && !Element.prototype.animate) return;
    var layer = document.createElement('div');
    layer.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:9999;overflow:hidden';
    document.body.appendChild(layer);
    var colors = ['#FFFFFF', '#FFF8ED', '#FBEEDC'];
    var star = function (c) {
      return 'url("data:image/svg+xml,' + encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 0c1 9 3 11 12 12-9 1-11 3-12 12-1-9-3-11-12-12 9-1 11-3 12-12z" fill="' + c + '"/></svg>') + '")';
    };
    var emit = function (x, y, scale, delay) {
      var spread = 10 + 12 * scale;
      var px = x + (Math.random() * spread - spread / 2);
      var py = y + (Math.random() * spread - spread / 2);
      var col = colors[(Math.random() * colors.length) | 0];

      var glow = document.createElement('div');
      var gsize = (12 + Math.random() * 12) * scale;
      glow.style.cssText = 'position:absolute;left:' + px + 'px;top:' + py + 'px;width:' + gsize + 'px;height:' + gsize +
        'px;border-radius:50%;background:radial-gradient(circle, rgba(255,252,245,.4) 0%, rgba(214,184,132,.13) 40%, transparent 70%);transform:translate(-50%,-50%);opacity:0;will-change:transform,opacity';
      layer.appendChild(glow);
      var ganim = glow.animate([
        { opacity: 0, transform: 'translate(-50%,-50%) scale(.4)' },
        { opacity: 0.22 * scale, transform: 'translate(-50%,-50%) scale(1)', offset: 0.3 },
        { opacity: 0, transform: 'translate(-50%,-50%) scale(1.5)' }
      ], { duration: 950 + Math.random() * 450, delay: delay, easing: 'ease-out', fill: 'backwards' });
      ganim.onfinish = function () { glow.remove(); };

      var el = document.createElement('div');
      var size = (5 + Math.random() * 6) * scale;
      el.style.cssText = 'position:absolute;left:' + px + 'px;top:' + py + 'px;width:' + size + 'px;height:' + size +
        'px;background-image:' + star(col) + ';background-size:contain;background-repeat:no-repeat;filter:drop-shadow(0 0 2px rgba(255,255,255,.8)) drop-shadow(0 0 5px rgba(212,180,128,.3));opacity:0;will-change:transform,opacity';
      layer.appendChild(el);
      var rot = Math.random() * 80 - 40, drift = Math.random() * 14 - 7, peak = 0.62 * scale;
      var frames = calm ? [
        { opacity: 0, transform: 'translate(-50%,-50%) scale(.7)' },
        { opacity: 0.55 * scale, transform: 'translate(-50%,-50%) scale(1)', offset: 0.35 },
        { opacity: 0, transform: 'translate(-50%,-50%) scale(.8)' }
      ] : [
        { opacity: 0, transform: 'translate(-50%,-50%) scale(.2) rotate(0deg)' },
        { opacity: peak, transform: 'translate(-50%,-50%) scale(1) rotate(' + rot + 'deg)', offset: 0.3 },
        { opacity: 0, transform: 'translate(calc(-50% + ' + drift + 'px),calc(-50% + 14px)) scale(.25) rotate(' + (rot * 2) + 'deg)' }
      ];
      var anim = el.animate(frames, { duration: 900 + Math.random() * 400, delay: delay, easing: 'cubic-bezier(.25,.6,.4,1)', fill: 'backwards' });
      anim.onfinish = function () { el.remove(); };
    };
    var last = 0, lx = null, ly = null, run = 0;
    window.addEventListener('mousemove', function (e) {
      var now = performance.now();
      if (now - last > 300) run = 0;
      if (now - last < 55) return;
      if (lx !== null && run > 0 && Math.hypot(e.clientX - lx, e.clientY - ly) < 14) return;
      last = now; lx = e.clientX; ly = e.clientY;
      var count = run === 0 ? 3 : run === 1 ? 2 : 1;
      var scale = run === 0 ? 1.15 : run === 1 ? 1 : 0.85;
      for (var i = 0; i < count; i++) emit(e.clientX, e.clientY, scale, i * 55);
      run++;
    }, { passive: true });
  }

  /* ---------- nav active state ---------- */
  function initNavSpy() {
    if (typeof IntersectionObserver === 'undefined') return;
    var sections = $$('section[id]');
    if (!sections.length) return;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var id = en.target.id;
        $$('.nav-lnk, .nav-mlnk').forEach(function (a) {
          var href = a.getAttribute('href') || '';
          a.classList.toggle('on', href === '#' + id);
        });
      });
    }, { rootMargin: '-45% 0px -45% 0px' });
    sections.forEach(function (s) { io.observe(s); });
  }

  function start() {
    try { initReveals(); } catch (e) {}
    try { initParallax(); } catch (e) {}
    try { if (!calm) initSparkles(); } catch (e) {}
    try { initNavSpy(); } catch (e) {}
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
