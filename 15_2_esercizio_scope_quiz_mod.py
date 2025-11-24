# Facciamo un gioco a quiz sfruttando lo scope delle variabili.

# Abbiamo un dict di domande con soluzioni. 
import random



def quiz(topic, numero_domande):
    if topic=="storia": n=random.randint(0,29)
    if topic == "geografia":n=random.randint(30,59)
    if topic == "cinema":n=random.randint(60,89)
    elif topic == "random":n=random.randint(0,89)

    global dict_domande
    dict_domande = list(dict_domande.items())[n:n+numero_domande]

    punteggio = 0 # è dentro a una funzione, quindi non potrà essere global, perché
    # questa funzione potrei passarla ai miei colleghi, che la utilizzano in 
    # altri ambienti. Quindi l'unica comunicazione che questa funzione ha con
    # l'esterno è la lista di domande con risposte che viene caricata.
    # punteggio sarà quindi vista come nonlocal dalle eventuali funzioni interne
    # alla funzione "madre" quiz.
    print("Benvenuto nel gioco a Quiz! Rispondi 1 per True o 0 per False.")

    def fai_domanda(domanda,risposta_corretta):
        nonlocal punteggio
        risposta = bool(int(input(domanda)))
        if risposta == risposta_corretta:
            punteggio += 1
            print("Risposta Giusta!")
        else: print("Risposta Sbagliata")
        
    for d,r in dict_domande:
        fai_domanda(d,r)
    
    print(f"Il punteggio totale è: {punteggio} su {numero_domande}")



dict_domande = {
"Nome della cavalla di Garibaldi era Marsala?\n": True, #inizio storia
"Napoleone ha vinto a Waterloo?\n": False,
"La Rivoluzione Francese iniziò nel 1789?\n": True,
"Il Colosseo si trova a Firenze?\n": False,
"Cristoforo Colombo scoprì l'America nel 1492?\n": True,
"L'Impero Romano cadde nel 476 d.C.?\n": True,
"La Prima Guerra Mondiale iniziò nel 1939?\n": False,
"Leonardo da Vinci dipinse la Gioconda?\n": True,
"La Magna Carta fu firmata in Inghilterra?\n": True,
"La caduta di Costantinopoli avvenne nel 1453?\n": True,
"Il Rinascimento ebbe inizio in Spagna?\n": False,
"Giulio Cesare fu assassinato nel Senato romano?\n": True,
"La Guerra dei Cent'anni durò 116 anni?\n": True,
"L'Unità d'Italia fu completata nel 1871?\n": True,
"Napoleone era francese?\n": True,
"Il Muro di Berlino cadde nel 1989?\n": True,
"La Rivoluzione Russa avvenne nel 1917?\n": True,
"L'Impero Ottomano era guidato da un Sultano?\n": True,
"La Dichiarazione d'Indipendenza americana fu firmata nel 1776?\n": True,
"Hitler era un generale durante la Prima Guerra Mondiale?\n": False,
"La carta stampata fu inventata da Gutemberg?\n": True,
"La civiltà egizia utilizzava i geroglifici?\n": True,
"La guerra di Troia è un evento storico confermato?\n": False,
"La battaglia di Hastings avvenne nel 1066?\n": True,
"Marco Polo raggiunse la Cina nel XIII secolo?\n": True,
"La rivoluzione industriale iniziò in Inghilterra?\n": True,
"L'Impero Bizantino era la continuazione dell'Impero Romano d'Oriente?\n": True,
"La peste nera colpì l'Europa nel XIV secolo?\n": True,
"Giovanna d'Arco fu bruciata sul rogo?\n": True,
"La Costituzione degli Stati Uniti è la più antica carta costituzionale ancora in vigore?\n": True,
"Capitale dell'Equador è Buenos Aires?\n": False, # Inizio geografia
"Capitale dell'Uruguay è Montevideo?\n": True, 
"Il fiume Nilo attraversa il Brasile?\n": False,
"La capitale del Giappone è Tokyo?\n": True,
"L'Australia è un continente?\n": True,
"Roma è la capitale della Spagna?\n": False,
"Il deserto del Sahara si trova in Africa?\n": True,
"La capitale del Canada è Toronto?\n": False,
"Il Monte Everest è la montagna più alta del mondo?\n": True,
"L'Islanda si trova nell'Oceano Indiano?\n": False,
"La capitale della Turchia è Ankara?\n": True,
"Il Lago Victoria è il lago più grande del mondo?\n": False,
"La capitale del Messico è Città del Messico?\n": True,
"La Russia è il paese più esteso del mondo?\n": True,
"Il fiume Mississippi scorre in Europa?\n": False,
"La capitale dell'India è Nuova Delhi?\n": True,
"Il Monte Kilimangiaro si trova in Asia?\n": False,
"La capitale della Francia è Parigi?\n": True,
"L'Africa è un continente?\n": True,
"Il Mar Mediterraneo bagna le coste dell'Italia?\n": True,
"La capitale della Germania è Berlino?\n": True,
"Il Sahara è un fiume?\n": False,
"La capitale dell'Egitto è Il Cairo?\n": True,
"L'Argentina si trova in America del Sud?\n": True,
"La capitale della Cina è Shanghai?\n": False,
"Il fiume Danubio attraversa più di dieci paesi?\n": True,
"La capitale del Regno Unito è Londra?\n": True,
"Il Lago Baikal si trova in Russia?\n": True,
"La capitale della Norvegia è Oslo?\n": True,
"Il deserto di Gobi si trova in Africa?\n": False,
"Il personaggio di Darth Vader appare nei film di 'Harry Potter'?\n": False,
"Il film 'Il Padrino' è stato diretto da Francis Ford Coppola?\n": True,
"Wolverine è stato interpretato da Hugh Jackman?\n": True,
"Il film 'Titanic' è stato diretto da Steven Spielberg?\n": False,
"Leonardo DiCaprio ha vinto un Oscar per 'The Revenant'?\n": True,
"Il personaggio di Forrest Gump è stato interpretato da Tom Hanks?\n": True,
"'Il Signore degli Anelli' è una trilogia cinematografica?\n": True,
"Il film 'Inception' è uscito nel 2010?\n": True,
"Marilyn Monroe ha recitato in 'Colazione da Tiffany'?\n": False,
"Alfred Hitchcock è noto per i suoi film horror?\n": False,
"Il film 'Avatar' è stato diretto da James Cameron?\n": True,
"Brad Pitt ha interpretato il personaggio di Tyler Durden in 'Fight Club'?\n": True,
"Il premio Oscar viene assegnato ogni quattro anni?\n": False,
"Audrey Hepburn ha interpretato il ruolo di Holly Golightly in 'Colazione da Tiffany'?\n": True,
"Il film 'Gladiatore' è ambientato nell'antica Roma?\n": True,
"Quentin Tarantino ha diretto il film 'Pulp Fiction'?\n": True,
"Meryl Streep ha vinto più di 3 premi Oscar nella sua carriera?\n": False,
"Il film 'Jurassic Park' è basato su un romanzo di Michael Crichton?\n": True,
"Il personaggio di Jack Sparrow è interpretato da Johnny Depp?\n": True,
"Il film 'Matrix' è del 1999?\n": True,
"Charlie Chaplin è famoso per i suoi film muti?\n": True,
"Il film 'La La Land' ha vinto l'Oscar per il miglior film nel 2017?\n": False,
"Tom Cruise ha recitato nella serie di film 'Mission: Impossible'?\n": True,
"Il regista Federico Fellini era italiano?\n": True,
"Natalie Portman ha interpretato Padmé Amidala in 'Star Wars'?\n": True,
"Sylvester Stallone ha interpretato Rocky Balboa?\n": True,
"Il film 'E.T. l'extra-terrestre' è stato diretto da Steven Spielberg?\n": True,
"Morgan Freeman ha doppiato Mufasa nel film 'Il Re Leone'?\n": True,
"Il film 'Avatar' è ambientato sul pianeta Pandora?\n": True,
"La saga di 'Harry Potter' è composta da 8 film?\n": True,
}

#print(dict_domande.items())
# I dictionary sono ordinati, nel senso delle chiavi, cioè l'ordine nel
# quale sono inserite le coppie viene mantenuto.

quante_domande = int(input("Benvenuto nel programma Pursuit AB digita il numero delle domande\n"))
tipo_domande = int(input("e digita 1 per storia, 2 per geografia, 3 per cinema e 4 per misto\n"))

if tipo_domande == 1:
    tipo = "storia"
if tipo_domande == 2:
    tipo = "geografia"
if tipo_domande == 3:
    tipo = "cinema"
elif tipo_domande == 4:
    tipo = "random" 

quiz(tipo, quante_domande)