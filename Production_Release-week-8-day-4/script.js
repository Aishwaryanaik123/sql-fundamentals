(() => {
  const form = document.querySelector('#issueForm');
  const input = document.querySelector('#issueInput');
  const list = document.querySelector('#issueList');
  const filter = document.querySelector('#filterSelect');
  const count = document.querySelector('#itemCount');
  const issueCount = document.querySelector('#issueCount');
  const statusMessage = document.querySelector('#statusMessage');
  let nextId = 1;
  let items = [];

  function render() {
    const visible = items.filter(item => filter.value === 'all' || (filter.value === 'done' ? item.done : !item.done));
    list.replaceChildren();
    if (!visible.length) {
      const empty = document.createElement('li');
      empty.className = 'empty';
      empty.textContent = items.length ? 'No items match this filter.' : 'No items yet. Add one above to test the feature.';
      list.append(empty);
    } else {
      visible.forEach(item => {
        const li = document.createElement('li');
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = item.done;
        checkbox.setAttribute('aria-label', `Mark ${item.text} completed`);
        checkbox.addEventListener('change', () => { item.done = checkbox.checked; render(); });
        const text = document.createElement('span');
        text.className = `issue-text${item.done ? ' done' : ''}`;
        text.textContent = item.text;
        const remove = document.createElement('button');
        remove.type = 'button';
        remove.className = 'small-btn delete-btn';
        remove.textContent = 'Remove';
        remove.addEventListener('click', () => { items = items.filter(x => x.id !== item.id); render(); });
        li.append(checkbox, text, remove);
        list.append(li);
      });
    }
    count.textContent = `${items.length} item${items.length === 1 ? '' : 's'}`;
    issueCount.textContent = String(items.filter(item => !item.done).length);
  }

  form.addEventListener('submit', event => {
    event.preventDefault();
    const text = input.value.trim();
    if (!text) { input.setCustomValidity('Please enter an item.'); input.reportValidity(); return; }
    input.setCustomValidity('');
    items.push({ id: nextId++, text, done: false });
    input.value = '';
    statusMessage.textContent = 'Item added successfully.';
    render();
  });
  input.addEventListener('input', () => input.setCustomValidity(''));
  filter.addEventListener('change', render);
  document.querySelector('#refreshBtn').addEventListener('click', () => {
    statusMessage.textContent = 'Demo checks completed: page scripts are running and the interface is responsive.';
  });
  render();
})();