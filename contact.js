const contactDialog = document.getElementById('contact-dialog');
if (contactDialog && typeof contactDialog.showModal === 'function') {
  document.querySelectorAll('[data-contact], a[href="mailto:info@alisio28.com"]').forEach((link) => {
    if (link.closest('.email-options')) return;
    link.setAttribute('aria-haspopup', 'dialog');
    link.setAttribute('aria-controls', 'contact-dialog');
    link.addEventListener('click', (event) => {
      event.preventDefault();
      contactDialog.showModal();
    });
  });
  contactDialog.addEventListener('click', (event) => {
    if (event.target !== contactDialog) return;
    const bounds = contactDialog.getBoundingClientRect();
    if (event.clientX < bounds.left || event.clientX > bounds.right ||
        event.clientY < bounds.top || event.clientY > bounds.bottom) {
      contactDialog.close();
    }
  });
}
