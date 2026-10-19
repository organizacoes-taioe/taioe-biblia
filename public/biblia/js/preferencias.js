/* Bíblia Taioé: as escolhas do leitor, aplicadas antes de a página aparecer (este arquivo vem no
   <head>, sem defer, para não piscar). Tema: o do navegador até o leitor trocar; depois, o dele.
   Tamanho da letra: degraus de -3 a 5. Leitura aberta: o botão de cima já vem preenchido. */
(function () {
  'use strict';
  var d = document.documentElement;
  d.setAttribute('data-js', '');
  try {
    var t = localStorage.getItem('biblia:tema');
    if (t === 'claro' || t === 'escuro') d.setAttribute('data-tema', t);
    var f = localStorage.getItem('biblia:fonte');
    if (f && /^-?[0-9]$/.test(f) && f !== '0') d.setAttribute('data-fonte', f);
    if (localStorage.getItem('biblia:leitura-aberta')) d.setAttribute('data-leitura', '');
  } catch (e) { /* sem armazenamento: fica o padrão */ }
})();
