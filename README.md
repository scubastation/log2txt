# log2txt
Umformatierung des Bandlogs

Bei der Acronis-Bandsicherung wird das Protokoll als Log.xml ausgegeben.
Um es der Dokumentation hinzuzufügen, formatiert das Programm diese in 
eine Textdatei um.

Die Datei muss im gleichen Verzeichnis, in dem die Log.xlm liegt ausgeführt werden.
Unter Windows kann die .exe verwendet werden. Einige Virenscanner liefern eine fehlerhafte Meldung!
Wenn man die Log.xml im Explorer mit der Maus auf die .Exe zieht schlagen die Scanner nicht Alarm - strange. 
Ansonsten einfach: python log2txt.py von der Konsole
Ergebnis ist eine Datei namens Bandlog.txt

Interessant ist die Funktion für den Zeilenumbruch.
