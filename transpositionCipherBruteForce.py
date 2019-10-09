import math
from time import perf_counter


#test_message ciphertext = "Tleoolau  srrbu uerIn eP cm toeahnndentd e rtcLeetassebstd   aytnoodu  'My"
#test_message_extended: ciphertext = "Pwc hloiilFiewetarmo rhse.ntr sn  hea cHhi'nhheassxe. d; i  c  wocPaphauoiraeysuers   lriswladreeaen eddsddb      eshtettlhihnhioosetrmno  ioigkrArud. ereg  hsblhfTioay ahslt sce u aie htmbdsFeiose,raoro  ednersan   btncawterdhnihde  dta eFf hnitrowi nselenf  nln owtcothuhohw ira meom ttednsh hn .eole h lua wiIfryPimn s ot  i bvhwanpea in rfratoteosnhtevrk  hrieoaaero yisrouh rt rsia os lmnnniay,doidn   tsedoaf h  nnromsh dofetah m nrsiw ttetsath ee sheit,w e n  atrc alyoeit i r thskfttyeeeruo in or brtsmetu io dhtenmt-e yeeh  oelteacfs h sh  siD utctnotrhhagrhcein ooh eddgs cfiroeoalnem fmygaia p  dlrS,bbfoet eeuv .wcsl w aai shNludauoiksenb cie duohn a rbogP absl igl taieritisnreeon  ren aoten ttnh, the e coelt ua  yhmnihK eilsiru dismenAdko,mdrlen lebe  fira asonttolhr,a,flo, k   u aewtttan hhhefdaeeedt  r   ewtesoaraa ttt sshrh t keeehhn  erieotht m whasR,p ad.u rst  sbei lBsuvtiooititsnta oi ghnouni  snsgmbt l  pehwyniofeh inso owg srR hhaieuget b san'vldsz seeeiet r cadheyfin ex odsa pgre tsel da hrot ntoiohtdhuemeh etnymat  c  thFwefn era,rot es athFn hm ercteeb ehh  edn rwocecweafaehias ud tt ms lheaieso nfn hofirdookena fueagii ldrldnid  y  t aa oasstnrf  h de rdoP ploiuiceoyfleuasafdrrtili rien cbeodgsue s  tl wiaiutditntdyotyd.y nh,   be  hBiu.speunt ua t  Trih tbhpdehheer aeec inr  agsodwKuae  arst.atseee th m sBtenlo ee oifosnctn fitl ,i diid tmeocegsosnksi s   tvithtoiin iofnncos  egof ttd m hhh dpteeeteahim otteg.m ai h abibhtAnrlio t'ielua sndisnt g tedhm ays euhn  s sidwwtgks ieoae etruttmxhete oa  n aoctleosdthosf   ecs hsoik,oearre n fd daereen n alraadhiystn os  udtuetar hsdosetee   sh  iht-esttio  th s bsrrd myhaeide unedeattg  sshteFPtuee riir rmeenefsonrase rcrt auoheitrpsm oo .eeun o  nn.bfTl,d e ho eA weowrnte khsdaas ot kkto aeeerfwnvnne ede iesr nintuet mgsf hhm  feaaeaaextddtnrp  i dilhhat naeethlgi  eea nhnl niiaoydenndt es g  tc h tboiwisoe seso eeir mpnxvefea te atshi dchsinmeei ngos nodumeagneiern  rsntdttehte ohd  dw e ta.hs bhn oooyedTlmt   heehafse  enio fRryr aiu teligssh,orusii s ridntiweaegona,n   gs soop  t fnrhfhw  eiuehttvsl ohhe lR eens ud  teosisw lfsdtalf i ryo-sane,oemnoe tsostthitk  .ineesu sge tnH ,maadei .nre naderhtn dseedt tan haarttetndio  d o sP nnrmito eeehtcalrehoslrmius e,nluo  gdrfbs  e etan bconotuapdthrup  ensesn iedaoin  wwngtP  h.hinha eeoabNyrtvio rhetwcei a o nbnauagetnls esddkon.  if  tnn cBhogwauet hrtn iar  mftiPha  eiekhwde eee rm  noreodtuetui t  tdo,dR  n iutn fdsooao s trrniw o oahkuNtnanna stodpk  w on "
ciphertext = input("Enter transposition cipher text to decrypt: ")

key = math.ceil(len(ciphertext) / 2)


def dictionary():
    dictionary = open('dictionary.txt')
    dictionaryArray = []

    for word in dictionary.read().split('\n'):
        dictionaryArray.append(word)
    dictionary.close()
    return dictionaryArray

DICTIONARY = dictionary()
bestPlaintext = [0, 0,""]

def isEnglish(key, candidatePlaintext):

    totalNumberOfWords = len(candidatePlaintext.split())
    words = candidatePlaintext.split()
    counter = 0
    global bestPlaintext
    for word in words:

        if word.lower() in DICTIONARY:
            counter += 1

    if bestPlaintext[0] < counter / totalNumberOfWords:
        bestPlaintext[0] = counter / totalNumberOfWords
        bestPlaintext[1] = key
        bestPlaintext[2] = candidatePlaintext

def decrypt(key, ciphertext):

    numOfColumns = math.ceil(len(ciphertext) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfRows * numOfColumns) - len(ciphertext)
    plaintext = [''] * numOfColumns
    column = 0
    row = 0

    for character in ciphertext:
        plaintext[column] += character
        column += 1
        if (column > numOfColumns -1) or (column is numOfColumns -1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    candidatePlaintext = ''.join(plaintext)
    isEnglish(key, candidatePlaintext)
    return candidatePlaintext

numOfKeys = range(2, key + 1)
startTime = perf_counter()
for i in numOfKeys:
    decrypt(i, ciphertext)

print("Percentage of English Words: {}%".format(bestPlaintext[0] * 100))
print("Key:", bestPlaintext[1])
print("Message:\n", bestPlaintext[2])
endTime = perf_counter()
print("\n\n\nStart Time: ", startTime, " | End Tme: ", endTime, "\t| Elapsed Time: ", endTime - startTime)
