# Fontes modernas para 2Cor 2 (grupo «modernos»): só o que é novo

Complementa `../001/fontes-modernos.md` (ler antes). Pesquisa de 2026-10-18.

## 1. Varredura dos Papas: a referência vem partida por etiquetas

- No vatican.va a sigla vem em itálico: `(<i>2 Cor</i> 2,15)`. Um filtro rápido sobre o HTML **bruto**
  com `2\s*Cor\s*2\s*,` não casa nada. Filtrar o bruto por uma palavra solta (`Cor`, `lacrime`,
  `Troade`) e só então limpar as etiquetas e aplicar o regex de verdade. Assim a varredura dos ~7.100
  documentos do cache (Francisco, Bento XVI e João Paulo II, Leão XIV) leva ~12 min. Script:
  `mod2/papas3.py` no scratchpad desta conversa.
- O cache da conversa de Nm 14 (`…/639cd05d-…/scratchpad/dl/`) tem homilias, audiências, Angelus e
  Santa Marta, mas **não os discursos** (*speeches*): os discursos aos bispos *ad limina*, aos
  seminaristas e às sociedades bíblicas só apareceram pelo Clerus (abaixo). Para o próximo capítulo,
  vale baixar também os índices `…/<papa>/<língua>/speeches/<AAAA>.index.html`.
- Endereços de discursos de João Paulo II: em 2000 o mês vira trimestre
  (`…/john-paul-ii/it/speeches/2000/apr-jun/documents/hf_jp-ii_spe_20000520_santa-rita.html`); em 1999 a
  data do nome vem invertida (`hf_jp-ii_spe_20111999_ad-limina-german.html` = 20/11/1999). Os índices
  mensais (`…/speeches/1999/november.index.html`) às vezes voltam vazios pelo `curl`: achar pelo WebSearch.

## 2. Clerus: as páginas de citações das perícopes de 2Cor 2

- `https://www.clerus.org/bibliaclerusonline/en/9asp0jn.htm` (2Cor 1,12–2,4), `…/9ahynmb.htm` (2,5-11),
  `…/9asskkb.htm` (2,12-17). O link de cada entrada (`cwg.htm#ze`) leva a uma página com dezenas de
  documentos; a âncora nem sempre cai no lugar certo: **procurar «2Co 2» na página inteira**.
  Script: `mod2/clerus2.py` (baixa as páginas em paralelo e mostra o contexto de cada «2Co 2,x»).
- O Clerus deu o que a varredura não dá: discursos (JP2 aos bispos alemães, 20/11/1999, com 2,4; aos
  bispos do Malawi, 05/05/1989, com 2,15-16; aos seminaristas de Guadalajara, 30/01/1979, com 2,14; às
  Sociedades Bíblicas Unidas, 16/03/1995; Bento XVI aos bispos novos, 22/09/2008, com 2,17), *Vita
  consecrata* 105 e o Denzinger (DS 235, Bonifácio I, *Manet beatum*, 422, com 2,10-11; DS 602,
  Niceia II, com 2,17).
- O Denzinger latino do Clerus (`dva.htm` ≈ DS 100, `dvc.htm` ≈ DS 211–235, `dvt.htm` = DS 1492…)
  traz os textos abreviados («...»): o DS 235 latino **não** tem a citação de 2Cor 2,10-11, que só
  aparece na tradução inglesa (Deferrari). O texto inteiro está em PL 20 (cartas de Bonifácio I).
- **Missal de 2002 no Clerus**: `…/en/gle.htm` = Quinta-feira Santa, Missa do Crisma (pp. 290–297).
  As páginas `glj`–`glq` não são o santoral.

## 3. Documentos antigos do Magistério (latim, vatican.va)

Baixados e varridos para 2Cor 2 (Leão XIII a Paulo VI): *Haerent animo* (Pio X, 1908), *Ad catholici
sacerdotii* (Pio XI, 1935), *Menti nostrae* (Pio XII, 1950), *Mystici Corporis*, *Mediator Dei*,
*Sacerdotii nostri primordia* (João XXIII), *Ecclesiam suam*, *Paenitemini*, *Indulgentiarum doctrina*,
*Sacerdotalis caelibatus*, *Evangelica testificatio* (Paulo VI), *Divinum illud munus*, *Fin dal
principio*, *Depuis le jour* (Leão XIII); do Vaticano II em latim: LG, DV, SC, GS, PO, OT, PC, CD, AA,
AG, UR. Endereços: `https://www.vatican.va/content/<papa>/la/<encyclicals|apost_exhortations|apost_constitutions>/documents/hf_<sigla>_<tipo>_<data>_<título>.html`
(Pio X: `hf_p-x_exh_19080804_haerent-animo`; Pio XII: `hf_p-xii_exh_19500923_menti-nostrae`); Vaticano II:
`…/archive/hist_councils/ii_vatican_council/documents/vat-ii_<tipo>_<data>_<título>_lt.html`.
Rendeu só «bonus odor Christi» (Pio X, Pio XI, Pio XII). *Indulgentiarum doctrina* não cita 2Cor 2,10.

## 4. Santos

- **Francisco de Sales**: o *Index scripturaire* (t. XXVII, PDF p. 289) só tem, para 2Cor 2, o v. 15:
  «XXIV, 189; XXV, 45». Os PDFs dos t. III (*Introduction*) e XXV (*Opuscules* IV) não estavam no
  cache: `https://www.donboscosanto.eu/francesco_di_sales/03-Oeuvres%20de%20S.%20Francois%20de%20Sales-Tome%20III-Introduction%20a%20la%20vie%20devote-web.pdf`
  e `…/25-Oeuvres%20de%20S.%20Francois%20de%20Sales-Tome%20XXV-Vol.4-Opuscules-web.pdf` (baixados em
  `fs/` no scratchpad desta conversa).
- **Santo Afonso**: na concordância, as palavras que acham 2Cor 2 são `absorbeatur`, `donavi`,
  `adulterantes` e `triumphat`. `circumveniamur`, `abundantiori`, `obiurgatio`, `donastis` não existem;
  `odor` dá só citações alheias.
- **Newman**: procurar «2 Cor. ii.» e as frases da King James: «savour of death unto death», «sweet
  savour of Christ», «Who is sufficient for these things», «I had no rest in my spirit».
- **Vianney** (*Sermons*, `dl/vianney/v.txt`), **João da Cruz** e **Teresa** (DCO, `dl/es/`): nada sobre
  2Cor 2 (Teresa e João da Cruz falam dos «ardides» do demônio sem citar 2,11).
- **São Josemaria**: o escriva.org não responde a busca pelo WebFetch (a página de resultados vem vazia).

## 5. Liturgia

- **Lecionário de 1970, comuns, Missas rituais, votivas e por diversas necessidades** (OLM 701–927),
  quadro completo num arquivo só: `https://1981.catholic-resources.org/Lectionary/1970USL-Commons.htm`
  (os endereços `1970USL-Ritual.htm` etc. não existem).
- **Quadro das epístolas dos domingos e festas**: `https://catholic-resources.org/Lectionary/Overview-Epistles.htm`.
- **Grafia dos nomes de Paulo no Brasil** («Trôade», «Macedônia»): At 16,1-10 no sábado da 5ª semana
  da Páscoa (Vatican News, 24/05/2025).
