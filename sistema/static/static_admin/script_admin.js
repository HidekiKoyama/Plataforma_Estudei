function showConfirmation() {
    if (confirm('Tem certeza de que deseja deletar o cadastro?')) {
      document.getElementById('delete-cad').submit();
    }
}   