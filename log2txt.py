import xml.etree.cElementTree as ET   #Modul für den XML-Parser

count = 0 #Zähler für den Statistikblock 0 = Schreiben, 1 = Lesen


def write_mit_umbruch(text, umbruch = 84):
    '''
    Funktion bricht den 'text' nach 'umbruch' Zeichen um
    '''

    anzahl_zeilen = int(len(text) / umbruch)+1 #prüft auf wieviele Zeilen umgebruchen werden muss
    n = 0
    for i in range(anzahl_zeilen):
        datei.write(text[n:n+umbruch] + '\n') #Schiebt den String in Stücken durch  
        n += umbruch


with open('Bandlog.txt', 'w', encoding='utf-8') as datei: #Öffnen der Datei
    tree = ET.parse('Log.xml') #Parsen in ein Dictionary
    root = tree.getroot() 
    datei.write(3 * "\t" + "Protokoll der Sicherung auf LTO-Magnetband \n\n") #Überschrift setzen

    #Durchackern und bedingt Ausgeben der Elemente
    for child in root:
        if child.attrib['id'] == '1':
            text = child.attrib['policy'] + " gestartet auf " + child.attrib['Machine'] + "\nmit " + root.attrib['product'] + " Version: " \
            + root.attrib['version'] + " Build: "+ root.attrib['build']+"\n"
            datei.write(text + '\n')


        #Der Statistikblock muss erst noch am | als Liste aufgesplittet werden.
        if 'Statistiken' in child.attrib['message']:
            datei.write("Statistik:\n")
            statistik = child.attrib['message'].split("|")

            for item in statistik:
                #Die folgende Abfrage von count un find könnte man zusammenfassen, aber so ist sie besser nachzuvollziehen
                #sie soll unterscheiden, ob es sich um den nullten = Schreib- oder den ersten = Leseblock handelt
                if (count == 0):
                    if (item.find("Schreib") != -1 or item.find("geschrieb") != -1):
                        datei.write("\t" + item.lstrip() + '\n' )   #Schmeißt dabei noch das erste Zeichen raus und rückt ein  


                if (count == 1):
                    if (item.find("Lese") != -1 or item.find("geles") != -1):
                        datei.write("\t" + item.lstrip() + '\n' )   #Schmeißt dabei noch das erste Zeichen raus und rückt ein  


            count += 1  # Zeigt an, dass der erste (schreib) Statistikblock durch ist  
            datei.write("\n")
            continue # Abbrechen der Bearbeitung, damit das item nicht in die nächten if's rutscht

        if 'Komprimierung' in child.attrib['message']:
            found = child.attrib['message'].find('Zu')    #Hackt die kryptische Meldung nach dem gesicherten Pfad ab
            write_mit_umbruch(child.attrib['message'][:found] + '\n')


        else:   #alle anderen Zeilen Umgebrochen ausgeben
            write_mit_umbruch(child.attrib['message'])


    datei.close() # wird ja durch with automatisch geschlossen, aber Vorsicht ist die Mutter der Porzellankiste 
