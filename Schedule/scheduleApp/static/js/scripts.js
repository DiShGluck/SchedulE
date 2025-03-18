document.addEventListener('DOMContentLoaded', function () {
    function setupFilters() {
      const form = document.getElementById('filter-form');
      if (!form) return;
  
      const groupSelect = form.querySelector('select[name="group"]');
      const daySelect = form.querySelector('select[name="day"]');
  
      if (groupSelect) {
        groupSelect.addEventListener('change', function () {
          form.submit();
        });
      }
  
      if (daySelect) {
        daySelect.addEventListener('change', function () {
          form.submit();
        });
      }
    }
  
    function setupClickableRows() {
      const rows = document.querySelectorAll('.clickable-row');
      rows.forEach(row => {
        row.addEventListener('click', function () {
          window.location.href = this.dataset.href;
        });
      });
    }
    function setupHoverEffects() {
        const rows = document.querySelectorAll('.clickable-row');
        rows.forEach(row => {
          row.addEventListener('mouseover', function () {
            this.classList.add('shadow-lg'); 
          });
          row.addEventListener('mouseout', function () {
            this.classList.remove('shadow-lg');
          });
        });
      }
    setupFilters();
    setupClickableRows();
    setupHoverEffects();
  });