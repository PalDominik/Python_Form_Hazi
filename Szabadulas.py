nev = input('Mi a neved?: ')
end = False
kulcs = False
hiba = 0

print('És most egy kis kompetencia teszt.')
komp = input('5+5?: ')
if komp != 10:
    print('Bocs, de buta embereket nem tesztelek ennél tovább.')
    bef = 1
    end = True
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
        print("a. Petrik Lajos Két Tanítási Nyelvű Technikum\nb.Petrik Lajos Négy Tanítási Nyelvű Technikum\nc.Petrik László Két Tanítási Nyelvű Technikum\nd.Petrik Lajos Két Tanítási Nyelvű Szakgimnázium")

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

    while tovabb == False and ut == 1:
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

