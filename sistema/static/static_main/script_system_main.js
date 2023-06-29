function show_sub_menus(){
  const toggleBtn = document.getElementById('toggle-btn');
  const sidebar = document.getElementById('sidebar');

  toggleBtn.addEventListener('change', function() {
      if (toggleBtn.checked) {
          sidebar.classList.add('open');
      } else {
          sidebar.classList.remove('open');
      }
  });
}