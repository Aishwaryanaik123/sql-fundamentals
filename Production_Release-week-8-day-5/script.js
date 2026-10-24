(() => {
  const runButton = document.getElementById('runCheck');
  const result = document.getElementById('checkResult');
  const count = document.getElementById('checksCount');
  runButton.addEventListener('click', () => {
    const checks = [
      ['Page title exists', Boolean(document.title.trim())],
      ['Main heading exists', Boolean(document.querySelector('h1'))],
      ['Stylesheet loaded', [...document.styleSheets].some(sheet => {
        try { return sheet.href && sheet.href.endsWith('style.css'); } catch (_) { return false; }
      })],
      ['JavaScript running', true],
      ['Viewport meta configured', Boolean(document.querySelector('meta[name="viewport"]'))]
    ];
    const passed = checks.filter(([, ok]) => ok).length;
    count.textContent = `${passed}/${checks.length} passed`;
    result.textContent = `${passed} of ${checks.length} client-side checks passed. This does not test a live server or backend.`;
    result.dataset.status = passed === checks.length ? 'pass' : 'warning';
  });
})();
