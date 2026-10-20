"""Grava as pistas e as ausências do grupo «orientais gregos não clássicos» (ascetas, Máximo, bizantinos,
hinografia) em <livro>/<ccc>/base/_pistas-orientais-gregos.md e _ausentes-orientais-gregos.md.

Uso (da pasta biblia/):
    python -I -X utf8 pesquisa/ferramentas/base/ori-pistas-gregos.py

As pistas vêm de ori-buscar-gregos.py (n-gramas dos versículos) sobre os textos do khazarzar e do OCR latino
da PG 97–98 e de Pitra; ficaram como pista porque (a) a edição tem direito (Berthold 1973; Fatouros 1992;
SC; Chrestou), (b) o grego do OCR é ilegível, ou (c) é só citação, com pouca leitura do versículo.
Para achar o lugar num texto: rodar ori-buscar-gregos.py no arquivo e procurar o versículo na saída.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ori_gregos_comum as O

K = 'https://khazarzar.skeptik.net/pgm/PG_Migne/'
MAC64 = K + 'Macarius%20of%20Egypt_PG%2034/Sermones%2064.pdf'
MAC7 = K + 'Macarius%20of%20Egypt_PG%2034/Homiliae%207.pdf'
MAC28 = K + 'Macarius%20of%20Egypt_PG%2034/Sermo%2028%20recensio%20brevior.pdf'
MAC50 = K + 'Macarius%20of%20Egypt_PG%2034/Homiliae%20spirituales%2050.pdf'
MAXA = K + 'Maximus%20Confessor_PG%2090-91/'
TEOD = K + 'Theodorus%20Studita_PG%2099/Epistulae.pdf'
SIM_C = K + 'Symeonis%20Junioris_PG%20120/Catechesae.pdf'
SIM_T = K + 'Symeonis%20Junioris_PG%20120/Theologica.pdf'
PAL2 = K + 'Gregorius%20Palamas%20Thessalonicensis%20Metropolita_PG%20150-151/tomos%202.pdf'
PG97 = 'https://archive.org/details/bim_early-english-books-1641-1700_1860_97'
PG98 = 'https://archive.org/details/bim_early-english-books-1641-1700_1860_98'
PITRA = 'https://archive.org/details/analectasacraspicilegiosolesmensipar'

MAC_B = ('São Macário (Pseudo-Macário), Sermones 64 (coleção B), ed. Berthold, GCS 1973 (edição com direito: só '
         'citação curta; não está na PG)')
SIM = 'São Simeão, o Novo Teólogo'
SIM_ED = 'texto digital da ed. grega do khazarzar (segue as edições modernas, SC 96–129 etc.: citação curta)'
PAL = 'Gregório Palamas (escritor eclesiástico bizantino, posterior a 1054), Tríades em defesa dos hesicastas'
PAL_ED = 'ed. Chrestou, t. 2 (Tessalônica 1966; edição com direito); PG 150–151 tem só parte'
TEO = 'São Teodoro Estudita, Cartas (ed. Fatouros, CFHB 31, 1992: edição com direito)'

PISTAS = {
    ('2corintios', 3): [
        f'{MAC_B}, logos 58, §§ 1–2: comentário corrido de 2Cor 3,7–18 (o véu é a treva do pecado de Adão, tirada '
        f'pela luz do Espírito; «rosto descoberto» é o da alma; a glória de Moisés passava porque estava no corpo) e '
        f'4,6. O melhor achado do grupo para 2Cor 3, mas a edição tem direito. {MAC64}',
        f'{MAC_B}, outros logoi: 2Cor 3,18 citado e explicado em vários logoi (busca: «ανακεκαλυμμενω προσωπω»). {MAC64}',
        f'{PAL}, Tríade I, 3 (sobre a luz): 2Cor 3,18 e 4,6 lidos como a luz divina vista pelos santos ({PAL_ED}). {PAL2}',
        f'São Máximo, Capita theologica II, 77 (PG 90, 1161): «de glória em glória» (2Cor 3,18) como progresso da '
        f'alma; texto gravado em salmos/042/base/maximo-capitulos-teologicos.md. {MAXA}PG_91AGI.pdf',
    ],
    ('2corintios', 4): [
        f'{MAC_B}, logos 58, § 2: 2Cor 4,6 («Deus que disse: das trevas brilhe a luz»): a iluminação da graça não é só '
        f'conhecimento, mas luz que habita na alma. {MAC64}',
        f'São Macário, Sermo 28 (recensio brevior): 2Cor 4,6–7 e 3,18 juntos, o tesouro no vaso de barro = o Espírito '
        f'na alma (edição moderna; conferir qual). {MAC28}',
        f'São Macário, Homilias espirituais (duas passagens) citam 2Cor 4,7 («tesouro em vasos de barro»), sem comentar muito. {MAC50}',
        f'{SIM}, Catequeses (duas passagens) e Discursos teológicos e éticos I: 2Cor 4,6–7 lidos como a luz de Cristo '
        f'que habita o coração ({SIM_ED}). {SIM_C} ; {SIM_T}',
        f'{PAL}, Tríade I, 2 e I, 3, e o tratado contra as proposições de Barlaão: 2Cor 4,6 e 4,7 em favor da luz incriada vista no coração ({PAL_ED}). {PAL2}',
        f'São Máximo, Liber asceticus §§ 25–26 (PG 90): cita 2Cor 4,8–11 como retrato do Apóstolo que ama '
        f'(só citação). {MAXA}PG_91AGI.pdf',
    ],
    ('2corintios', 5): [
        f'{MAC_B}: 2Cor 5,1–4 explicado num logos paralelo à Homilia espiritual 5 (gravada em base/macario-homilias-espirituais.md). {MAC64}',
        f'São Máximo, Capita theologica (centúria II): 2Cor 5,16 («se conhecemos Cristo segundo a carne…») num capítulo '
        f'próprio (conferir: busca «εγνωκαμεν κατα σαρκα»). {MAXA}PG_91AGI.pdf',
        f'São Máximo, Cartas (PG 91): 2Cor 5,20 («somos embaixadores de Cristo») citado numa carta (só citação). {MAXA}PG_91A_7.pdf',
        f'{SIM}, Discursos teológicos e éticos, discurso V: 2Cor 5,17 («nova criatura») contra quem diz ter o Espírito sem '
        f'senti-lo ({SIM_ED}). {SIM_T}',
        f'{SIM}, Capítulos gnósticos e teológicos: 2Cor 5,14 («o amor de Cristo nos constrange») ({SIM_ED}). {SIM_T}',
    ],
    ('2corintios', 6): [
        f'{TEO}: 2Cor 6,3–10 («como moribundos, e eis que vivemos; tristes, mas sempre alegres») em cartas de consolo '
        f'aos monges perseguidos na crise iconoclasta (várias cartas). {TEOD}',
        f'São Macário, Homiliae 7 (coleção HA, ed. Marriott 1918): 2Cor 6,4–5 em lista longa. {MAC7}',
        f'{SIM}, Discursos teológicos e éticos XI: 2Cor 6,10 («como nada tendo, e tudo possuindo») ({SIM_ED}). {SIM_T}',
    ],
    ('2corintios', 7): [
        f'{MAC_B}: 2Cor 6,16–7,1 («tendo estas promessas, purifiquemo-nos») explicado. {MAC64}',
        f'{TEO}: 2Cor 7,1 em exortações aos monges (duas cartas). {TEOD}',
    ],
    ('salmos', 37): [
        f'{MAC_B}: Sl 36(37),5 LXX («revela ao Senhor o teu caminho») citado e aplicado. {MAC64}',
    ],
    ('salmos', 38): [
        f'{SIM}, Ações de graças (Εὐχαριστίαι, no fim das Catequeses): cita em sequência Sl 37(38),4–9 LXX como oração '
        f'do penitente ({SIM_ED}). {SIM_C}',
    ],
    ('salmos', 39): [
        f'São Máximo, Quaestiones ad Thalassium 49 (PG 90; coluna não conferida): Sl 38(39),2–3 LXX («quando o pecador se pôs diante '
        f'de mim, emudeci») lido como o silêncio na guerra dos pensamentos; texto da PG no khazarzar (PD), curto. {MAXA}PG_91A_2.pdf',
    ],
    ('salmos', 40): [
        f'São Máximo, Disputatio Bizyae (PG 90): Sl 39(40),7–9 LXX como prova da vontade humana de Cristo '
        f'(argumento dogmático, não exegese). {MAXA}PG_91A_8.pdf',
    ],
    ('salmos', 42): [
        f'{TEO}: Sl 41(42),2 («como a corça anseia») desenvolvido numa carta. {TEOD}',
        f'São Macário, Homilias espirituais 25: Sl 41(42),4 («as lágrimas foram o meu pão») sobre as lágrimas. {MAC50}',
        f'{SIM}, Capítulos práticos e teológicos: Sl 41(42),6.12 («por que estás triste, ó minha alma?») ({SIM_ED}). {SIM_T}',
        f'São Máximo, Ambigua a João (PG 91, 1073): Sl 41(42),3 entre as provas de que a alma ainda não repousa em Deus. {MAXA}PG_91A_3.pdf',
    ],
    ('salmos', 45): [
        f'{TEO}: Sl 44(45),11–12 («ouve, filha… o rei desejará a tua beleza») numa carta a uma monja. {TEOD}',
        f'{SIM}, Discursos teológicos e éticos I: Sl 44(45),10.16 («a rainha à tua direita») ({SIM_ED}). {SIM_T}',
        f'São Máximo, carta (PG 91): Sl 44(45),5 («avança, prospera e reina») aplicado a um bispo. {MAXA}PG_91A_7.pdf',
    ],
    ('salmos', 47): [
        f'{TEO}: Sl 46(47),2 («povos, batei palmas») numa carta. {TEOD}',
        f'Escólios a Dionísio (PG 4, atribuídos a Máximo; boa parte é de João de Citópolis): Sl 46(47),6.9 '
        f'(«subiu Deus entre aclamações»). Autoria incerta. {MAXA}PG_91A_5.pdf',
    ],
    ('salmos', 49): [
        f'{SIM}, Catequeses: Sl 48(49),13.21 («o homem na honra não compreendeu, comparou-se aos animais») em duas '
        f'catequeses ({SIM_ED}). {SIM_C}',
        f'{TEO}: Sl 48(49),2 («ouvi isto, todos os povos») numa carta. {TEOD}',
        f'São Macário, Homilias espirituais 16, fim: Sl 48(49),13 sobre a nobreza esquecida da alma (só citação). {MAC50}',
    ],
    ('salmos', 50): [
        f'São Máximo, Quaestiones ad Thalassium 62 (PG 90): Sl 49(50),16 («ao pecador disse Deus: por que recitas os '
        f'meus preceitos?») aplicado a quem ensina sem viver. {MAXA}PG_91A_2.pdf',
        f'{SIM}, Catequeses e Cartas: Sl 49(50),16–17 contra quem ensina sem praticar ({SIM_ED}). {SIM_C}',
    ],
    ('numeros', 17): [
        f'Santo André de Creta, Homilias I e IV sobre a Natividade de Maria (PG 97, c. 809–810 e 865–866): «vara de '
        f'Aarão sempre verde» e «Alegra-te, vara de Aarão», títulos da Virgem (Nm 17,23); o grego do OCR é ilegível '
        f'(usar a imagem da página). {PG97}',
        f'Santo André de Creta (?), homilia mariana da PG 97 (Dormição?; coluna a conferir): a arca com «a vara de Aarão que '
        f'floresceu» (Hb 9,4). {PG97}',
        f'PG 97, teotokion de um cânon depois do Cânon de Lázaro (latim: «Moysis quidem virga, nec non virga Aaronis»): '
        f'conferir autor e texto na imagem. {PG97}',
    ],
    ('numeros', 21): [
        f'PG 98 (obra de São Germano de Constantinopla?, latim: «serpentis aerei in cruce suspensio»): a serpente de '
        f'bronze e os «exércitos de serpentes venenosas» do deserto; conferir autor e coluna (OCR, linha ~18553). {PG98}',
    ],
    ('numeros', 22): [
        f'São Romano (atribuído), kontákion dos santos Cosme e Damião (Pitra, Analecta sacra I, n.º XXVII): a jumenta '
        f'de Balaão que fala (Nm 22,28–30) comparada ao animal que fala num milagre dos santos; grego do OCR razoável. {PITRA}',
    ],
    ('numeros', 24): [
        f'Pitra, Analecta sacra I, n.º XXIX «De Nativitate», estrofe νβ΄ (p. 232 aprox.; imagem n332): «Μάντεως χρησμοὶ '
        f'Βαλαὰμ ἀποπληροῦνται» — os magos persas cumprem os oráculos de Balaão; autor a conferir (Romano ou outro melodista). {PITRA}',
    ],
    ('numeros', 25): [
        f'São Germano de Constantinopla, De vitae termino (PG 98; coluna não conferida): Fineias e Zambri como '
        f'argumento sobre o termo da vida (só exemplo). {PG98}',
    ],
}

AUS = ('Santo André de Creta, Grande Cânon (PG 97, 1329–1385): conferido no latim de Combefis (OCR do archive.org) — '
       'de Números só traz os cap. 12, 14 e 16 (Datã e Abirão, ode 6); nada de Coré e dos incensórios, da vara de Aarão, '
       'de Meribá, da serpente de bronze, de Balaão nem de Fineias. ' + PG97)


def main():
    for (livro, cap), linhas in PISTAS.items():
        for l in linhas:
            O.linha_lista(livro, cap, 'pistas', l)
    for cap in range(17, 26):
        O.linha_lista('numeros', cap, 'ausentes', AUS)
    print('ok')


if __name__ == '__main__':
    main()
