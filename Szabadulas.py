nev = input('Mi a neved?: ')
end = False
bef = 0
kulcs = False
hiba = 0

print('És most egy kis kompetencia teszt.')
komp = int(input('5+5?: '))
if komp != 10:
    print('Bocs, de buta embereket nem tesztelek ennél tovább.')

    end = True
else:

    print(f'''
    Na, akkor kedves {nev}, most elmagyarázom a dolgokat itt.

    Ha bár úgy érzeheted magad mintha szabad lennél, valojában nagyobb kalitkába nem is lehetnél bezárva.
    Szóval vázolom mi lesz a dolgod. Kérdéseket teszek fel és minden helyes válaszért cserébe közelebb
    jutsz a szabadságodhozz. Helytelen válaszokért peddig feljebb visszek egy számlálott. Ha ez a szám túl
    magas a kalandunk végére, akkor csak szimplán megölek.
    Ja és helytelen válaszoknál nem engedlek tovább... bocsi

    Eddig még érthető remélem. Na de hogy csavarjunk a csavaron...
    Lesznek válaszok ami se nem jó, se nem rosszak.
    Tételezük hogy ezzek ilyen morális kérdések.
    Minden ilyen után más és más kérdést kapsz.

    Egyenlöre ennyi. Jó szorakozást!
    ''')

    input('Mond ha kezdhejük... ')
    print('Remek!')
    while end == False:
        tovabb = False
        while tovabb == False:
            print('1.Kérdés: Mi az iskola neve:')
            print("a. Petrik Lajos Két Tanítási Nyelvű Technikum\nb. Petrik Lajos Négy Tanítási Nyelvű Technikum\nc. Petrik László Két Tanítási Nyelvű Technikum\nd. Petrik Lajos Két Tanítási Nyelvű Szakgimnázium")

            valasz = input()
            valasz = valasz.strip().lower()
            match valasz:
                case "a":
                    print('Jó... ez könnyü volt.')
                    tovabb = True
                case "b":
                    print('Szerintem tanulj meg olvasni.')
                    hiba +=1
                case "c":
                    print('Hát ez nagyon gyatya.')
                    hiba += 1
                case "d":
                    print('Ez kicsit gáz bratyesz.')
                    hiba +=1
                case _:
                    print('Ez még opcio se volt.')
                    hiba +=1

        tovabb = False
        while tovabb == False:
            print('2.Kérdés: Volt egy könyvem aminek a címe Egri valami volt... Nem tudod véletlenül?:')
            print("a. Egri csaták\nb. Egri maffiák\nc. Egri csillagok\nd. Egri Hold")

            valasz = input()
            valasz = valasz.strip().lower()
            match valasz:
                case "a":
                    print('Nah.. valami más volt.')
                    hiba +=1
                case "b":
                    print('Biztos nagy sikert ért vona el, de nem ez kellet nekem.')
                    hiba +=1
                case "c":
                    print('Ja, tényleg... na mindegy.')
                    tovabb = True
                case "d":
                    print('Ilyen hülyeséget... várjá... nem, nem jó.')
                    hiba +=1
                case _:
                    print('a,b,c,d válaszok vannak öcsipók.')
                    hiba +=1

        tovabb = False
        ut = 0
        while tovabb == False:
            print('3.Kérdés: Teljes kiörlésü kenyér vagy fehér kenyér:')
            print("a. Teljes kiörlésü\nb. Fehér")

            valasz = input()
            valasz = valasz.strip().lower()
            match valasz:
                case "a":
                    print('Na most ezért elitélek...')
                    ut = 1
                    tovabb = True
                case "b":
                    print('Figyelek ám')
                    ut = 2
                    tovabb = True
                case _:
                    print('Csak két opció volt most. Két darab...')
                    hiba +=1
            
        tovabb = False
        if ut == 1:
            while tovabb == False:
                print('4.Kérdés:Na ez jó lesz: Éjjel-nappal jár, de mégis egy helyben áll. Micsoda ez?:')
                print("a. Áram\nb. Emberi test\nc. Filmtekercs\nd. Óra")

                valasz = input()
                valasz = valasz.strip().lower()
                match valasz:
                    case "a":
                        print('Szerintem átvezetem rajtad mingyárt.')
                        hiba +=1
                    case "b":
                        print('Most elárultad hogy egy lusta disznó vagy... vagy csak kiváncsi.')
                        hiba +=1
                    case "c":
                        print('Hmm... nem, bár nem hibáztatlak.')
                        hiba +=1
                    case "d":
                        print('Gondolhatam vona hogy nem vagy ekkora sügér.')
                        tovabb = True
                    case _:
                        print('Fel ne ad már... Ki fog engemet szorakoztatni?')
                        hiba +=1

            
            tovabb = False
            while tovabb == False:
                print('5.Kérdés: Egy elektromos vonat észak felé halad. Merre száll a füstje?')
                print("a. Észak felé\nb. Amere többen vannak\nc. Amere fúj a szél\nd. Ennyire hülyének nézzel?")

                valasz = input()
                valasz = valasz.strip().lower()
                match valasz:
                    case "a":
                        print('A füst biztos tudja, merre kell mennie, de most nem.')
                        hiba += 1
                    case "b":
                        print('Bár úgytünhet, de a fizika nem így müködik.')
                        hiba += 1
                    case "c":
                        print('Remélem az arcodba fúj a szél ezzek a mondatok után.')
                        hiba += 1
                    case "d":
                        print('Igen.. enyire.')
                        tovabb = True
                    case _:
                        print('Remélem tudod hogy minden ilyenért felmegy a számláló.')
                        hiba += 1

            tovabb = False
            while tovabb == False:
                print('6.Kérdés: Hány hónapban van legalább 28 nap?')
                print("a. 12\nb. 2\nc. 6\nd. 1")

                valasz = input()
                valasz = valasz.strip().lower()
                match valasz:
                    case "a":
                        print('Oké... nem foglak hűlyébnek nézzni mint amenyire kellene...')
                        tovabb = True
                    case "b":
                        print('Valahogy ez a legrosszabb válasz amit adhatál volna.')
                        hiba += 1
                    case "c":
                        print('*Siroksz XD*.')
                        hiba += 1
                    case "d":
                        print('.... tényleg?')
                        hiba += 1
                    case _:
                        print(' A B C D ! NEM OLYAN NEHÉZ!')
                        hiba += 1

            tovabb = False
            while tovabb == False:
                print('Utolsó kérdés.... Most van esélyed kimenekülnöd, de látom hogy éhes vagy... ahogy ez a gyermek is\nÉhesen nem tudsz sokáig túléni, ahogy a fiu sem..\nSzóval itt a nagy kérdés:Megeszed a fiut és elmenekülsz.. vagy feláldozod magad.. és a fiu nem csak kimenekül, de még jól is lakik.')
                print("A választás a te kezedbe van.")
                print("a. Feláldozod a gyermeket\nb. Feláldozod magadat.")

                valasz = input()
                valasz = valasz.strip().lower()
                match valasz:
                    case "a":
                        print('Hmm.. Akkor fogyaszunk...')
                        tovabb = True
                        bef = 1
                    case "b":
                        print('Milyen önfeláldozó vagy... Kérlek kövess...')
                        tovabb = True
                        bef = 2

            
        if ut == 2:
            #be kell fejezni bratyesz
            while tovabb == False and ut == 2:
                print('4.Kérdés:Hmm... Ki volt a 15.-íg Amerikai elnök?:')
                print("a. George Washington\nb. Andrew Jackson\nc. James Buchanan\nd. Theodore Roosevelt")

                valasz = input()
                valasz = valasz.strip().lower()
                match valasz:
                    case "a":
                        print('Nem... Ö volt az első... asszem.... ')
                        hiba +=1
                    case "b":
                        print('7. elnök, de már közelitünk.')
                        hiba +=1
                    case "c":
                        print('Meg googliztat, tudom ám :-) ')
                        tovabb = True
                    case "d":
                        print('Tedy hogy a jó é.... Khm.. bocsánat. Amúgy rossz válasz.')
                        hiba +=1
                    case _:
                        print('Gatya?')
                        hiba +=1

            
            tovabb = False
            while tovabb == False:
                print('8.Kérdés: Mi következik a számsorban? 1, 1, 2, 3, 5, 8, 13, ?')
                print("a. 18\nb. 20\nc. 21\nd. 26")

                valasz = input()
                valasz = valasz.strip().lower()
                match valasz:
                    case "a":
                        print('Menni fog, eskü nem szivatlak.')
                        hiba += 1
                    case "b":
                        print('Sorozatos fájdalmat érzek rajtad.')
                        hiba += 1
                    case "c":
                        print('Csak remélni tudom hogy nem csak random válaszolsz')
                        tovabb = True
                    case "d":
                        print('26.... 26... valami más lesz.')
                        hiba += 1
                    case _:
                        print('a,b,c,d válaszok vannak öcsipók.')
                        hiba += 1

            tovabb = False
            while tovabb == False:
                print('6.Kérdés: Ha egy kakas tojást tojik egy háztető tetején, melyik oldalra esik le?')
                print("a. Balra\nb. Jobbra\nc. Fejel fel, vagy lefele van a kakas?\nd. Egyikre sem.")

                valasz = input()
                valasz = valasz.strip().lower()
                match valasz:
                    case "a":
                        print('Vagy balkezes vagy... vagy bal****.')
                        hiba += 1
                    case "b":
                        print('Jobbra a második ajtó lesz a fogyatékos rendelő.')
                        hiba += 1
                    case "c":
                        print('Nagyesélyel ugyanúgy ahogy te landoltál gyereként a földre...')
                        hiba += 1
                    case "d":
                        print('Ha tojna akkor bajba lennénk.')
                        tovabb = True
                    case _:
                        print('Nincs rántotta tojás nélkül...')
                        hiba += 1

            tovabb = False
            while tovabb == False:
                print('Oké.. öszinte leszek... innen nincs hagyományos kijút, de van választási lehetöséged...\nVan egy amuleten.. egy "jó barátom" adta... ha összetöröd élve kijutsz innen, de bele tudsz örülni.\nVagy feladthatód magad az isteneknek és része lehetsz valami nagy dolognak.')
                print('Kérlek válasz...')
                print("a. Élet\nb. Halál")

                valasz = input()
                valasz = valasz.strip().lower()
                match valasz:
                    case "a":
                        print('Szóval így döntötél.... Isten legyen kegyelmező veled...')
                        tovabb = True
                        bef = 3
                    case "b":
                        print('Élet túl nehéz volt számodra... vagy csak elég volt ebből a játékból')
                        tovabb = True
                        bef = 4
        end = True


match bef:
    case 0:
        print("A butaságod elüzött mindenkitt, ezért egyedül maradtál egy cellában és szép lassan elrohadtál.")
    case 1:
        if(hiba > 5):
            print("Elfogyasztodtad a gyermeket, de közel sem adodt annyi energiát hogy hosszútávon túl élj.\nTalán itt annyira nem rossz ha tudsz még embereket idecsalogatni")
            input('Tovább...  ')
            print("Évek telnek el és csak gyülnek az áldozataid száma, hírneved késöbb a halálodat okoza....")
            print("------------")
            print("End 1. Éhes Király balladája")
        else:
            print("Elfogyasztodtad a gyermeket, megbánás vesz téged körül, de amit megtetél már nem lehet visszacsinálni...")
            input('Tovább...  ')
            print("Sikerült kiérned egy partra. Egy csonakot lopsz magadnak és elszöksz erről az átkozot szigetről...")
            print("------------")
            print("End 2. Szabadság megfizethető áron...")
    case 2:
        if(hiba > 5):
            print("Egy mély álomba kerülsz, pár perc múlva felébretsz, lábaid lemorzsolodva és be vannak kötve valamilyen ruhadaraba...")
            input('Tovább...  ')
            print("'Áh látom felébredtél.... sajnos nem tudtunk egy huzamban elfogyasztani téged, szóval félrerakunt és holnap befejezünk...'\n'Addigis vigyáz magadra... szeretnénk téged még frissen elfogasztatni'")
            print("------------")
            print("End 3. Minden jó cselekedetnek megvan a saját büntetése...")
        else:
            print("Egy mély álomba kerülsz.... soha töbet nem kelsz fel.... \nMár csak abba reménykedhetsz hogy ezzel tudtál eleget segiteni a gyermeknek.")
            print("------------")
            print("End 4. Utolsó vacsora...")

    ## Bfejezendő
    case 3:
        if(hiba > 5):
            print("befejezendő befejezés")
        else:
            print("befejezendő befejezés")
    case 4:
        if(hiba > 5):
            print("befejezendő befejezés")
        else:
            print("befejezendő befejezés")
    case _:
        print("Valahol kiestél a szabaduló szobából... és nem fog tudni visszajuttni.")


