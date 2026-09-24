/* Keep the editorial project order while filtering by research field. */
(function () {
  var nav = document.querySelector('.project-filters');
  var cards = Array.from(document.querySelectorAll('.project-grid [data-group]'));
  var count = document.querySelector('.project-count');
  if (!nav || !cards.length || !count) return;
  var links = Array.from(nav.querySelectorAll('[data-filter]'));
  var aliases = { 'all-projects': 'all', numerical: 'numerical', inverse: 'inverse', learning: 'learning', 'applied-projects': 'applied' };
  function apply(group) {
    var visible = 0;
    cards.forEach(function (card) {
      card.hidden = group !== 'all' && card.dataset.group !== group;
      if (!card.hidden) visible += 1;
    });
    links.forEach(function (link) {
      if (link.dataset.filter === group) link.setAttribute('aria-current', 'true');
      else link.removeAttribute('aria-current');
    });
    count.textContent = visible + (visible === 1 ? ' project' : ' projects');
  }
  function fromHash() {
    var id = window.location.hash.slice(1);
    apply(aliases[id] || 'all');
    // A direct project link must reveal the project even after a category filter.
    var target = document.getElementById(id);
    if (target && target.matches('[data-group]')) target.scrollIntoView();
  }
  nav.addEventListener('click', function (event) {
    var link = event.target.closest('[data-filter]');
    if (!link || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    apply(link.dataset.filter);
    history.pushState(null, '', link.getAttribute('href'));
  });
  window.addEventListener('hashchange', fromHash);
  window.addEventListener('popstate', fromHash);
  fromHash();
}());
