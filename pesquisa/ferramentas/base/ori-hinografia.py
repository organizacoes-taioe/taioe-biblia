"""Pré-pesquisa: hinografia bizantina (São Cosme de Jerusalém, São Romano o Melodista) para Números.
Grava numeros/<ccc>/base/<autor>-<obra>.md.

Uso (da pasta biblia/):
    python -I -X utf8 pesquisa/ferramentas/base/ori-hinografia.py

O OCR grego da PG 98 e da *Analecta sacra* de Pitra no archive.org é ilegível; por isso o grego abaixo foi
transcrito à mão das imagens das páginas (archive.org, «/page/nNNN»), com o latim das próprias edições
(OCR conferido na imagem). Para refazer: baixar https://archive.org/download/<id>/page/n<NNN>.jpg e ler.
  - PG 98 (1860): id bim_early-english-books-1641-1700_1860_98; n232 = col. 461–462 (cânon do Natal);
    n253 = col. 503–504 (cânon da Exaltação da Cruz). Texto de Gallandi, *Bibliotheca veterum Patrum* XIII.
  - Pitra, *Analecta sacra* I (Paris 1876): id analectasacraspicilegiosolesmensipar; n103 = p. 3.
Busca que levou aos trechos: OCR latino (Balaam, virga, serpentem, Moyses) e, em Pitra, o grego «Βαλαάμ».
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ori_gregos_comum as O

SCRIPT = 'pesquisa/ferramentas/base/ori-hinografia.py'
PG98 = 'https://archive.org/details/bim_early-english-books-1641-1700_1860_98/page/n{}/mode/1up'
PITRA = 'https://archive.org/details/analectasacraspicilegiosolesmensipar/page/n{}/mode/1up'
COSME = 'São Cosme de Jerusalém, o Melodista (c. 675–c. 752), bispo de Maiúma, santo'
ROMANO = 'São Romano, o Melodista (c. 490–c. 556), diácono em Constantinopla, santo'

EXALT_ED = ('PG 98, 503–504 (Cosmae Hierosolymitani hymni, XII, «In exaltationem Crucis»; texto de Gallandi, com o latim). '
            'Grego transcrito da imagem da página (o OCR do archive.org é ilegível)')
EXALT_OBRA = ('Cânon da Exaltação da Santa Cruz (14 de setembro), «Σταυρὸν χαράξας Μωσῆς», cantado nas Matinas '
              'da festa (Menaion de setembro)')

ITENS = [
    dict(cap=17, arquivo='cosme-canon-exaltacao-cruz', titulo='São Cosme de Jerusalém, Cânon da Exaltação da Cruz',
         campos=[('Autor', COSME), ('Obra', EXALT_OBRA), ('Passagem', 'ode 3, irmo'), ('Edição', EXALT_ED),
                 ('Fonte', PG98.format(253)),
                 ('Cobre', 'Nm 17,16–26 (LXX 17,1–11): a vara de Aarão que floresce e escolhe o sacerdote, figura da cruz '
                  'que floresce para a Igreja antes estéril')],
         corpo='''Ode 3, irmo (PG 98, 503–504):

Ῥάβδος εἰς τύπον μυστηρίου παραλαμβάνεται· τῷ βλαστῷ γὰρ προκρίνει τὸν ἱερέα. Τῇ στερευούσῃ δὲ πρώην
Ἐκκλησίᾳ νῦν ἐξήνθησε ξύλον σταυροῦ, εἰς κράτος καὶ στερέωμα.

Latim da PG: Virga in typum mysterii assumitur: germine enim declarat sacerdotem. Sterili autem antea
Ecclesiae nunc effloruit lignum crucis in imperium et firmamentum.'''),
    dict(cap=20, arquivo='cosme-canon-exaltacao-cruz', titulo='São Cosme de Jerusalém, Cânon da Exaltação da Cruz',
         campos=[('Autor', COSME), ('Obra', EXALT_OBRA), ('Passagem', 'ode 3, tropário depois do irmo'), ('Edição', EXALT_ED),
                 ('Fonte', PG98.format(253)),
                 ('Cobre', 'alusão a Nm 20,10–11 (a rocha ferida dá água ao povo «rebelde», ἀπειθοῦντι; cf. Ex 17,6 e Dt 8,15, '
                  '«rocha ἀκρότομος»), lida como mistério da Igreja, que tem a cruz por força e firmeza')],
         corpo='''Ode 3, tropário (PG 98, 503–504):

Ὡς ἐπαφῆκε ῥαπιζομένη ὕδωρ ἀκρότομος ἀπειθοῦντι λαῷ καὶ σκληροκαρδίῳ, τῆς θεοκλήτου ἐδήλου Ἐκκλησίας τὸ
μυστήριον, ἧς ὁ σταυρὸς τὸ κράτος καὶ στερέωμα.

Latim da PG: Ubi emisit percussa aquam petra durissima immorigero populo et duri cordis, divinitus vocatae
indicavit Ecclesiae mysterium, cujus crux est imperium et firmamentum.'''),
    dict(cap=21, arquivo='cosme-canon-exaltacao-cruz', titulo='São Cosme de Jerusalém, Cânon da Exaltação da Cruz',
         campos=[('Autor', COSME), ('Obra', EXALT_OBRA), ('Passagem', 'ode 1, segundo tropário'), ('Edição', EXALT_ED),
                 ('Fonte', PG98.format(253)),
                 ('Cobre', 'Nm 21,8–9: a serpente de bronze posta na haste, remédio da mordida venenosa, presa ao lenho '
                  'em forma de cruz')],
         corpo='''Ode 1, tropário (PG 98, 503–504):

Ἀνέθηκε Μωϋσῆς ἐπὶ στήλης ἄκος, φθοροποιοῦ λυτήριον καὶ ἰοβόλου δήγματος· καὶ ξύλῳ τύπῳ σταυροῦ, τὸν πρὸς
γῆν συρόμενον ὄφιν προσέδησεν ἐγκάρσιον, ἐν τούτῳ θριαμβεύσας τὸ πῆμα. Διὸ Χριστῷ ᾄσωμεν τῷ Θεῷ ἡμῶν, ὅτι
δεδόξασται.

Latim da PG: Imposuit Moyses super conto remedium, corruptivi liberatorium et venefici morsus: et in ligno
figura crucis serpentem per terram se trahentem alligavit obliquum, in hoc triumphans noxam. Quare Christo
canamus Deo nostro, quoniam glorificatus est.'''),
    dict(cap=24, arquivo='cosme-canon-natal', titulo='São Cosme de Jerusalém, Cânon do Natal',
         campos=[('Autor', COSME),
                 ('Obra', 'Cânon do Natal do Senhor (25 de dezembro), «Χριστὸς γεννᾶται, δοξάσατε», cantado nas Matinas '
                  'da festa e, por seus irmos, desde a Apresentação (21/11)'),
                 ('Passagem', 'ode 4 (irmo «Ῥάβδος ἐκ τῆς ῥίζης Ἰεσσαί»), segundo tropário'),
                 ('Edição', 'PG 98, 461–464 (Cosmae Hierosolymitani hymni, I, «In Natale Domini»; texto de Gallandi, com o '
                  'latim e as variantes do Anthologium de Roma, 1738). Grego transcrito da imagem da página'),
                 ('Fonte', PG98.format(232)),
                 ('Cobre', 'Nm 24,17 («uma estrela sairá de Jacó»): os magos, «iniciados nas palavras do adivinho Balaão», '
                  'são as primícias dos gentios')],
         corpo='''Ode 4, tropário (PG 98, 461–462):

Τοῦ μάντεως πάλαι Βαλαὰμ τῶν λόγων μυητάς, σοφοὺς ἀστεροσκόπους χαρᾶς ἔπλησας, ἀστὴρ ἐκ τοῦ Ἰακὼβ
ἀνατείλας, Δέσποτα· ἐθνῶν ἀπαρχὴν εἰσαγομένους ἐδέξω δὲ προφανῶς. Δόξα τῇ δυνάμει σου, Κύριε.

Variante (nota f da PG, pelo Anthologium): em vez de «εἰσαγομένους ἐδέξω δὲ», «δῶρά σοι δεκτὰ προσκομίζοντας».

Latim da PG: Vatis quondam Balaam verbis imbutos sapientes astrorum inspectores gaudio replevisti, ceu stella
ex Jacob exortus, Domine: gentium primitias invehentes conspicue suscepisti. Gloria potentiae tuae, Domine.

Tropário anterior, da mesma ode (Gn 49,10, sem Números), para contexto: Ὃν πάλαι προεῖπεν Ἰακὼβ ἐθνῶν
ἀπεκδοχήν, Χριστέ, φυλῆς Ἰούδα ἐξανέτειλας…'''),
    dict(cap=24, arquivo='romano-kontakion-natal-1', titulo='São Romano, o Melodista, Kontákion do Natal I',
         campos=[('Autor', ROMANO),
                 ('Obra', 'Kontákion do Natal I, «Ἡ Παρθένος σήμερον τὸν ὑπερούσιον τίκτει» (o proêmio ainda se canta no '
                  'Natal bizantino)'),
                 ('Passagem', 'estrofe 6 (ς΄) na numeração de Pitra (os magos respondem à Virgem)'),
                 ('Edição', 'J.-B. Pitra, Analecta sacra spicilegio Solesmensi parata, t. I, Paris 1876, p. 3 (canticum I, '
                  '«De Christi Nativitate»), com tradução latina de Pitra; à margem, «Βαλαάμ Num. XXIV, 17». Grego transcrito '
                  'da imagem da página. Edições críticas modernas (Maas–Trypanis 1963; Grosdidier de Matons, SC 110) têm '
                  'direito: só como conferência'),
                 ('Fonte', PITRA.format(103)),
                 ('Cobre', 'Nm 24,17 (a estrela de Jacó, o oráculo de Balaão), explicado pelos magos: a estrela que apaga '
                  'os oráculos e agouros e é mais brilhante que a estrela visível, porque fez todos os astros')],
         corpo='''Estrofe ς΄ (Pitra I, p. 3):

Ἀκριβῶς γὰρ ἡμῖν
ὁ Βαλαὰμ παρέθετο
τῶν ῥημάτων τὸν νοῦν,
ὧνπερ προεμαντεύσατο,
εἰπὼν ὅτι μέλλει
ἀστὴρ ἀνατέλλειν,
ἀστὴρ σβεννύων
πάντα μαντεύματα
καὶ τὰ οἰωνίσματα·
ἀστὴρ ἐκλύων
παραβολὰς σοφῶν,
ῥήσεις τε αὐτῶν
καὶ τὰ αἰνίγματα·
ἀστὴρ ἀστέρος
τοῦ φαινομένου
ὑπερφαιδρότερος πολύ,
ὡς πάντων ἄστρων ποιητής·
περὶ οὗ προεγράφη
ἐκ τοῦ Ἰακὼβ ἀστράπτειν
παιδίον νέον, τὸν πρὸ αἰώνων Θεόν.

Latim de Pitra: Diligenter enim nobis Balaam proposuit oraculorum intellectum, quae ipse vaticinatus est,
dicens futurum esse ut stella exsurgat, stella quae omnia extinguat vaticinationes et omina; stella quae
dissolvat sophorum parabolas, eorumque sententias et aenigmata; stella hoc sidere quod emicat, eo splendidior,
quod scilicet cuncta condidit astra; de qua praedictum est, oriturum esse a Iacobo, ut fulgur, infantem
novum, Deum ante saecula.

Contexto (fim da estrofe ε΄, os magos à Virgem): … Ὅ τὸ ἄστρον ἰδόντες / συνήκαμεν, ὅτι ὤφθη / παιδίον
νέον, ὁ πρὸ αἰώνων Θεός.'''),
]


def main():
    for it in ITENS:
        campos = it['campos'] + [('Oriental', 'sim'), ('Língua', 'grc'), ('Baixado', f'{O.HOJE}, por {SCRIPT}')]
        p = O.gravar('numeros', it['cap'], it['arquivo'], it['titulo'], campos, it['corpo'])
        print('gravado', p)


if __name__ == '__main__':
    main()
