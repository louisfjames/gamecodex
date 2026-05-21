document.addEventListener('DOMContentLoaded', function () {
  const removeModal = document.getElementById('removeEntryModal');
  if (!removeModal) return;

  removeModal.addEventListener('show.bs.modal', function (event) {
    const button = event.relatedTarget;
    const entryUrl = button.getAttribute('data-entry-url');
    const form = removeModal.querySelector('#removeEntryForm');
    form.action = entryUrl;
  });
});
