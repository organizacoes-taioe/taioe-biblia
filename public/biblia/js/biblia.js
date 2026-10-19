/* Bíblia Taioé, no navegador:
   - a barra de cima: letra menor e maior, modo claro ou escuro, e as leituras;
   - as leituras: pontos de leitura com nome que acompanham o leitor (a posição muda conforme ele
     lê, e a leitura reabre no último ponto). Ficam só neste navegador, com o prefixo «biblia:»;
   - as notas: abrem coladas à linha da marca e somem com qualquer toque ou rolagem. Sem
     JavaScript, a marca da nota é um link para a lista de notas no fim do capítulo. */
(function () {
  'use strict';
  var d = document.documentElement;
  var BASE = '/biblia/';

  function ler(chave, padrao) {
    try { var v = localStorage.getItem(chave); return v === null ? padrao : JSON.parse(v); } catch (e) { return padrao; }
  }
  function guardar(chave, valor) {
    try { if (valor === null) localStorage.removeItem(chave); else localStorage.setItem(chave, JSON.stringify(valor)); } catch (e) { /* sem armazenamento */ }
  }
  function $(id) { return document.getElementById(id); }
  function el(tag, cls, texto) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (texto) e.textContent = texto;
    return e;
  }

  // ------------------------------------------------------------ letra e tema

  var fonte = Number(d.getAttribute('data-fonte') || 0);
  function mudarFonte(passo) {
    fonte = Math.max(-3, Math.min(5, fonte + passo));
    if (fonte) d.setAttribute('data-fonte', String(fonte)); else d.removeAttribute('data-fonte');
    try { localStorage.setItem('biblia:fonte', String(fonte)); } catch (e) { /* idem */ }
    $('letra-menor').disabled = fonte <= -3;
    $('letra-maior').disabled = fonte >= 5;
  }
  if ($('letra-menor')) {
    $('letra-menor').addEventListener('click', function () { mudarFonte(-1); });
    $('letra-maior').addEventListener('click', function () { mudarFonte(1); });
    mudarFonte(0);
  }
  function escuroAgora() {
    var t = d.getAttribute('data-tema');
    if (t) return t === 'escuro';
    return !!(window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
  }
  if ($('trocar-tema')) $('trocar-tema').addEventListener('click', function () {
    var novo = escuroAgora() ? 'claro' : 'escuro';
    d.setAttribute('data-tema', novo);
    try { localStorage.setItem('biblia:tema', novo); } catch (e) { /* idem */ }
  });

  // ------------------------------------------------------------ leituras

  // biblia:leituras = [{ id, nome, url, v, rotulo, quando }]; biblia:leitura-aberta = id;
  // biblia:ultimo = a última posição lida, com ou sem leitura aberta (onde a leitura nova começa).
  var leituras = ler('biblia:leituras', []);
  if (!Array.isArray(leituras)) leituras = [];
  var abertaId = ler('biblia:leitura-aberta', null);
  function aberta() {
    for (var i = 0; i < leituras.length; i++) if (leituras[i].id === abertaId) return leituras[i];
    return null;
  }
  if (abertaId && !aberta()) { abertaId = null; guardar('biblia:leitura-aberta', null); }
  function salvarLeituras() { guardar('biblia:leituras', leituras); }
  function onde(x) {
    if (!x || !x.url) return 'Sem posição ainda';
    return (x.rotulo || x.url) + (x.v ? ', v. ' + x.v : '');
  }
  function destino(x) {
    if (!x || !x.url || x.url.indexOf(BASE) !== 0) return BASE;
    return x.url + (x.v ? '#v' + String(x.v).replace(/[^0-9a-z]/gi, '') : '');
  }
  function abrirLeitura(x) {
    abertaId = x.id;
    guardar('biblia:leitura-aberta', x.id);
    location.href = destino(x);
  }
  function fecharLeitura() {
    abertaId = null;
    guardar('biblia:leitura-aberta', null);
    d.removeAttribute('data-leitura');
    fecharMenu();
    if (document.body.classList.contains('pag-leituras')) montarLeituras();
  }
  if (aberta()) d.setAttribute('data-leitura', ''); else d.removeAttribute('data-leitura');

  // O botão de cima: sem leitura aberta, leva à página das leituras; com uma aberta, abre o menu.
  var botao = $('botao-leituras'), menu = $('menu-leitura');
  function fecharMenu() { if (menu) { menu.hidden = true; botao.setAttribute('aria-expanded', 'false'); } }
  if (botao && menu) {
    botao.addEventListener('click', function (e) {
      var x = aberta();
      if (!x) return;
      e.preventDefault();
      if (!menu.hidden) { fecharMenu(); return; }
      $('menu-nome').textContent = x.nome;
      $('menu-pos').textContent = onde(x);
      menu.hidden = false;
      botao.setAttribute('aria-expanded', 'true');
    });
    $('fechar-leitura').addEventListener('click', fecharLeitura);
    document.addEventListener('click', function (e) {
      if (!menu.hidden && !menu.contains(e.target) && !botao.contains(e.target)) fecharMenu();
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') fecharMenu(); });
  }

  // Nas páginas de capítulo, a posição é o versículo no alto da tela (o que se está lendo).
  var cap = document.body.getAttribute('data-cap');
  if (cap) {
    var nums = Array.prototype.slice.call(document.querySelectorAll('.texto .num[id]'));
    var topo = document.querySelector('.topo');
    var relogio = null;
    var posicao = function () {
      // Até onde o salto para um versículo o deixa (scroll-padding-top), para a leitura reaberta
      // não recuar um versículo a cada vez.
      var folga = parseFloat(getComputedStyle(d).scrollPaddingTop) || 0;
      var limite = Math.max((topo ? topo.getBoundingClientRect().bottom : 0) + 12, folga + 8), v = null;
      if (window.scrollY > 40) {
        for (var i = 0; i < nums.length; i++) {
          if (nums[i].getBoundingClientRect().top <= limite) v = nums[i].textContent; else break;
        }
        if (v === null && nums.length) v = nums[0].textContent;
      }
      return { url: location.pathname, v: v, rotulo: cap, quando: Date.now() };
    };
    var registrar = function () {
      relogio = null;
      var p = posicao();
      guardar('biblia:ultimo', p);
      var x = aberta();
      if (x) { x.url = p.url; x.v = p.v; x.rotulo = p.rotulo; x.quando = p.quando; salvarLeituras(); }
    };
    var logo = function () { if (relogio) clearTimeout(relogio); relogio = setTimeout(registrar, 300); };
    window.addEventListener('scroll', logo, { passive: true });
    window.addEventListener('pagehide', function () { if (relogio) { clearTimeout(relogio); registrar(); } });
    setTimeout(registrar, 600);
  }

  // A página das leituras.
  function montarLeituras() {
    var w = $('leituras');
    w.innerHTML = '';
    if (!leituras.length) { w.appendChild(el('p', 'apagado', 'Nenhuma leitura ainda.')); }
    leituras.slice().sort(function (a, b) { return (b.quando || 0) - (a.quando || 0); }).forEach(function (x) {
      var item = el('div', 'leitura' + (x.id === abertaId ? ' aberta' : ''));
      var abrir = el('a', 'leitura-abrir');
      abrir.href = destino(x);
      abrir.appendChild(el('span', 'leitura-nome', x.nome));
      abrir.appendChild(el('span', 'leitura-onde', onde(x)));
      abrir.addEventListener('click', function (e) { e.preventDefault(); abrirLeitura(x); });
      item.appendChild(abrir);
      var acoes = el('div', 'leitura-acoes');
      if (x.id === abertaId) {
        acoes.appendChild(el('span', 'etiqueta', 'aberta'));
        var f = el('button', 'acao', 'Fechar'); f.type = 'button';
        f.addEventListener('click', fecharLeitura);
        acoes.appendChild(f);
      }
      var ren = el('button', 'acao', 'Renomear'); ren.type = 'button';
      ren.addEventListener('click', function () {
        var nome = window.prompt('Novo nome da leitura:', x.nome);
        if (nome === null) return;
        nome = nome.trim().slice(0, 60);
        if (!nome) return;
        x.nome = nome; salvarLeituras(); montarLeituras();
      });
      var apg = el('button', 'acao', 'Apagar'); apg.type = 'button';
      apg.addEventListener('click', function () {
        if (!window.confirm('Apagar a leitura «' + x.nome + '»?')) return;
        leituras = leituras.filter(function (y) { return y.id !== x.id; });
        salvarLeituras();
        if (x.id === abertaId) fecharLeitura(); else montarLeituras();
      });
      acoes.appendChild(ren); acoes.appendChild(apg);
      item.appendChild(acoes);
      w.appendChild(item);
    });
  }
  if (document.body.classList.contains('pag-leituras')) {
    var ultimo = ler('biblia:ultimo', null);
    $('nova-onde').textContent = ultimo && ultimo.url ? 'Começa em ' + onde(ultimo) + ', onde você estava.' : 'Começa no início da Bíblia.';
    $('nova-leitura').addEventListener('submit', function (e) {
      e.preventDefault();
      var nome = $('nome-leitura').value.trim().slice(0, 60);
      if (!nome) return;
      var x = { id: Date.now().toString(36) + Math.random().toString(36).slice(2, 6), nome: nome, quando: Date.now() };
      if (ultimo && ultimo.url) { x.url = ultimo.url; x.v = ultimo.v; x.rotulo = ultimo.rotulo; }
      leituras.push(x);
      salvarLeituras();
      abrirLeitura(x);
    });
    montarLeituras();
  }

  // ------------------------------------------------------------ notas

  var painel = $('nota-painel');
  if (!painel) return;
  var ref = $('nota-painel-ref'), texto = $('nota-painel-texto');
  var ativa = null, y0 = 0, largura0 = 0;

  function fechar(focar) {
    if (painel.hidden) return;
    painel.hidden = true;
    if (ativa) {
      ativa.classList.remove('ativa');
      if (focar) ativa.focus({ preventScroll: true });
      ativa = null;
    }
  }
  // O pé da linha em que está a marca: o retângulo do texto que cobre a altura da marca.
  function peDaLinha(marca) {
    var m = marca.getBoundingClientRect(), meio = (m.top + m.bottom) / 2, pe = 0;
    var bloco = marca.closest('.txt, .par') || marca.parentNode;
    var r = document.createRange();
    r.selectNodeContents(bloco);
    var rs = r.getClientRects();
    for (var i = 0; i < rs.length; i++) if (rs[i].top <= meio && rs[i].bottom >= meio && rs[i].bottom > pe) pe = rs[i].bottom;
    return pe || m.bottom + 6;
  }
  function posicionar(marca) {
    var folha = (marca.closest('.folha') || document.body).getBoundingClientRect();
    var margem = 8, alto = window.innerHeight;
    var barra = document.querySelector('.topo');
    var cima = barra ? Math.max(0, barra.getBoundingClientRect().bottom) : 0;
    var esq = Math.max(margem, folha.left - 12);
    var larg = Math.min(folha.width + 24, window.innerWidth - 2 * margem);
    painel.style.left = esq + 'px';
    painel.style.width = larg + 'px';
    painel.style.maxHeight = (alto - cima - 2 * margem) + 'px';
    var h = painel.offsetHeight;
    var y = peDaLinha(marca) + 4;
    if (y + h > alto - margem) y = alto - margem - h;   // não cabe: o pé da nota no pé da tela
    painel.style.top = Math.max(cima + margem, y) + 'px';
  }
  function abrir(marca) {
    var li = $('nota-' + marca.getAttribute('data-nota'));
    if (!li) return false;
    if (ativa === marca) { fechar(); return true; }
    if (ativa) ativa.classList.remove('ativa');
    ativa = marca;
    marca.classList.add('ativa');
    ref.textContent = 'Nota ' + marca.getAttribute('data-nota') + ' · ' + li.querySelector('.nota-v').textContent;
    texto.innerHTML = '';
    texto.appendChild(li.querySelector('.nota-texto').cloneNode(true));
    painel.hidden = false;
    posicionar(marca);
    y0 = window.scrollY; largura0 = window.innerWidth;
    return true;
  }

  // Qualquer toque fecha a nota (dentro dela também); tocar noutra marca abre a outra.
  document.addEventListener('click', function (e) {
    var marca = e.target.closest && e.target.closest('.nota-ref');
    if (marca) { if (abrir(marca)) e.preventDefault(); return; }
    fechar();
  });
  window.addEventListener('scroll', function () { if (!painel.hidden && Math.abs(window.scrollY - y0) > 3) fechar(); }, { passive: true });
  window.addEventListener('resize', function () { if (!painel.hidden && window.innerWidth !== largura0) fechar(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') fechar(true); });
})();
