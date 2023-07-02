function showConfirmation() {
    if (confirm('Tem certeza de que deseja deletar o cadastro?')) {
      document.getElementById('delete-cad').submit();
    }
    else{
      show_mensage();
    }
}   

function show_mensage(){
  const message = document.getElementById('message');
  function exibirMensagem(texto, tempo) {
    message.textContent = texto;
    message.style.display = 'block';
  
    setTimeout(function() {
      message.style.display = 'none';
    }, tempo);
  }
  // Exemplo de uso:
  exibirMensagem('Esta é uma mensagem de exemplo.', 3000); // A mensagem será exibida por 3 segundos (3000 ms)
}
