/* Bíblia Taioé: a nota abre num painel no pé da tela, sem tirar o leitor do lugar.
   Sem JavaScript, a marca da nota é um link para a lista de notas no fim do capítulo. */
(function () {
  'use strict';
  var painel = document.getElementById('nota-painel');
  if (!painel) return;
  var ref = document.getElementById('nota-painel-ref');
  var texto = document.getElementById('nota-painel-texto');
  var ativa = null;

  function fechar() {
    painel.hidden = true;
    if (ativa) { ativa.classList.remove('ativa'); ativa.focus(); ativa = null; }
  }
  function abrir(marca) {
    var li = document.getElementById('nota-' + marca.getAttribute('data-nota'));
    if (!li) return false;
    if (ativa === marca) { fechar(); return true; }
    if (ativa) ativa.classList.remove('ativa');
    ativa = marca;
    marca.classList.add('ativa');
    ref.textContent = 'Nota ' + marca.getAttribute('data-nota') + ' · ' + li.querySelector('.nota-v').textContent;
    texto.innerHTML = '';
    texto.appendChild(li.querySelector('.nota-texto').cloneNode(true));
    painel.hidden = false;
    return true;
  }

  document.addEventListener('click', function (e) {
    var marca = e.target.closest && e.target.closest('.nota-ref');
    if (marca) { if (abrir(marca)) e.preventDefault(); return; }
    if (!painel.hidden && !painel.contains(e.target)) fechar();
  });
  document.getElementById('nota-fechar').addEventListener('click', fechar);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !painel.hidden) fechar(); });
})();
