/* Mobile Smile Care: Dental Hygiene — small enhancements.
   Every page works without this file; it adds the header border on scroll,
   menu closing, the phone action bar and in-page form sending. */
(function () {
  'use strict';
  var TO = 'mobilesmilecaredental@gmail.com';
  var PHONE = '(905) 941-7580';

  // Header hairline once the page scrolls; mobile action bar after the hero.
  var header = document.querySelector('.site-header');
  var bar = document.querySelector('.action-bar');
  var hero = document.querySelector('.hero, .page-head');
  function onScroll() {
    var y = window.scrollY || 0;
    if (header) header.classList.toggle('is-scrolled', y > 8);
    if (bar) {
      var limit = hero ? hero.offsetTop + hero.offsetHeight - 120 : 400;
      bar.classList.toggle('is-visible', y > limit);
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Close open <details> menus on outside click, Escape, or link choice.
  var menus = Array.prototype.slice.call(document.querySelectorAll('.navmenu, .menu-toggle'));
  function closeAll(except) {
    menus.forEach(function (m) { if (m !== except) m.removeAttribute('open'); });
  }
  document.addEventListener('click', function (e) {
    var inside = menus.filter(function (m) { return m.contains(e.target); })[0];
    closeAll(inside);
    if (inside && e.target.closest('a')) inside.removeAttribute('open');
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    var open = menus.filter(function (m) { return m.open; })[0];
    if (open) { open.removeAttribute('open'); var s = open.querySelector('summary'); if (s) s.focus(); }
  });
  var sheet = document.querySelector('.menu-toggle');
  if (sheet) sheet.addEventListener('toggle', function () {
    document.documentElement.style.overflow = sheet.open ? 'hidden' : '';
  });

  // Question form: Web3Forms when a key is set, otherwise the visitor's mail app.
  Array.prototype.forEach.call(document.querySelectorAll('form[data-form]'), function (form) {
    var status = form.querySelector('.form-status');
    var btn = form.querySelector('button[type="submit"]');
    function say(kind, text) {
      if (!status) return;
      status.className = 'form-status ' + (kind ? 'is-' + kind : '');
      status.textContent = text;
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.botcheck && form.botcheck.checked) return;
      var bad = null;
      Array.prototype.forEach.call(form.querySelectorAll('[required]'), function (el) {
        var empty = !String(el.value || '').trim();
        var wrongEmail = el.type === 'email' && !empty && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(el.value);
        el.setAttribute('aria-invalid', empty || wrongEmail ? 'true' : 'false');
        if ((empty || wrongEmail) && !bad) bad = { el: el, email: wrongEmail };
      });
      if (bad) {
        say('error', bad.email ? 'That email address doesn’t look right. Please check it.' : 'Please fill in your name, email and question.');
        bad.el.focus();
        return;
      }
      var data = {};
      Array.prototype.forEach.call(form.elements, function (el) {
        if (el.name && el.name !== 'botcheck') data[el.name] = el.value;
      });
      var body = 'Name: ' + data.name + '\nPhone: ' + (data.phone || 'not provided') + '\nEmail: ' + data.email +
        '\nVisit for: ' + (data.visit_for || '') + '\n\n' + data.message;
      var key = window.SMILE_CARE_FORM_KEY || '';

      if (!key) {
        window.location.href = 'mailto:' + TO + '?subject=' + encodeURIComponent(data.subject || 'Question') + '&body=' + encodeURIComponent(body);
        say('ok', 'Your email app should open with your message ready to send.');
        return;
      }
      btn.disabled = true;
      var label = btn.textContent;
      btn.textContent = 'Sending…';
      say('', '');
      fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({
          access_key: key, subject: data.subject || 'New question from mobilesmilecare.ca', from_name: 'Mobile Smile Care website',
          name: data.name, email: data.email, phone: data.phone, visit_for: data.visit_for, message: body, replyto: data.email
        })
      }).then(function (r) { return r.json().then(function (j) { if (!r.ok || j.success === false) throw new Error(); }); })
        .then(function () {
          form.reset();
          say('ok', 'Thank you. Your question is on its way, and Lisa will reply personally.');
          btn.textContent = 'Sent';
        })
        .catch(function () {
          btn.disabled = false;
          btn.textContent = label;
          say('error', 'Sorry, that didn’t send. Please call ' + PHONE + ' or email ' + TO + '.');
        });
    });
  });
})();
