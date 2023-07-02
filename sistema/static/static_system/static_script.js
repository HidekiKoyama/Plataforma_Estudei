var searchInput = document.getElementById('search-input');
var userTable = document.getElementById('user-table');
var rows = userTable.getElementsByTagName('tr');

searchInput.addEventListener('input', function() {
  var filter = searchInput.value.toLowerCase();

  for (var i = 1; i < rows.length; i++) { // Começa do 1 para ignorar o cabeçalho
    var userCell = rows[i].getElementsByTagName('td')[0]; // Índice 2 representa a coluna "Usuário"

    if (userCell) {
      var userValue = userCell.textContent || userCell.innerText;

      if (userValue.toLowerCase().indexOf(filter) > -1) {
        rows[i].style.display = '';
      } else {
        rows[i].style.display = 'none';
      }
    }
  }
});
