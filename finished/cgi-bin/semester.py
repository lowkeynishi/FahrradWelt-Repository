#!/usr/bin/python3



class Fahrrad:

	def __init__(self, G_eingenschaften, Marke, model, rahmenmaterial, radgröße, gewicht, zulässiges_gesamtgewicht, geschlecht, preis, antrieb, kettenmodell, anzahl_gaenge, schaltungstyp, schaltwerk, umwerfer, kassette, kurbelgarniturbremstyp, bremse_vorne, bremse_hinten, bremsscheiben, gabel, federweg, lenker, sattel, sattelstütze, pedale, grips, beleuchtung):
		self.G_eingenschaften = G_eingenschaften
		self.Marke = Marke
		self.model = model
		self.rahmenmaterial = rahmenmaterial
		self.radgröße = radgröße
		self.gewicht = gewicht
		self.zulässiges_gesamtgewicht = zulässiges_gesamtgewicht
		self.geschlecht = geschlecht
		self.preis = preis
		self.antrieb = antrieb
		self.kettenmodell = kettenmodell
		self.anzahl_gaenge = anzahl_gaenge
		self.schaltungstyp = schaltungstyp
		self.schaltwerk = schaltwerk
		self.umwerfer = umwerfer
		self.kassette = kassette
		self.kurbelgarniturbremstyp = kurbelgarniturbremstyp
		self.bremse_vorne = bremse_vorne
		self.bremse_hinten = bremse_hinten
		self.bremsscheiben = bremsscheiben
		self.gabel = gabel
		self.federweg = federweg
		self.lenker = lenker
		self.sattel = sattel
		self.sattelstütze = sattelstütze
		self.pedale = pedale
		self.grips = grips
		self.beleuchtung = beleuchtung


 
Cube_nature = Fahrrad(
    G_eingenschaften="Das Cube Nature EXC ist ein vielseitiges Trekkingrad mit einer hochwertigen 22-Gang Kettenschaltung von Shimano Cues, einer leichten Aluminium Superlite Rahmenkonstruktion und einer SR Suntour Luftfedergabel mit Remote Lockout. Hydraulische Scheibenbremsen sorgen für zuverlässige Bremskraft bei jedem Wetter. Mit komfortablen Griffen, einem Natural Fit Sequence Sattel und 28 Zoll Schwalbe Land Cruiser Reifen eignet sich das Rad perfekt für Touren und den Alltag.",
    Marke="Cube",
    model="Nature EXC",
    rahmenmaterial="Aluminium Superlite, doppelt konifiziert",
    radgröße="28 Zoll",
    gewicht="13.1 kg",
    zulässiges_gesamtgewicht="115 kg",
    geschlecht="Herren",
    preis="1200€",
    antrieb="Kette",
    kettenmodell="KMC X10",
    anzahl_gaenge="22",
    schaltungstyp="Kettenschaltung",
    schaltwerk="Shimano Cues, 11-fach",
    umwerfer="Shimano Cues, Top-Swing, 31.8mm",
    kassette="Shimano Cues CS-LG400, 11-45T",
    kurbelgarniturbremstyp="Shimano Cues FC-U6010, Hollowtech II, 46/32 Zähne, mit Chainguard",
    bremse_vorne="Shimano BR-MT200, hydraulische Scheibenbremse",
    bremse_hinten="Shimano BR-MT200, hydraulische Scheibenbremse",
    bremsscheiben="160 mm / 160 mm",
    gabel="SR Suntour NCX E RL Air T, 63 mm, Remote Lockout",
    federweg="63 mm",
    lenker="Cube Comfort Trail Bar, 660 mm",
    sattel="Natural Fit Sequence",
    sattelstütze="Cube Performance Post, 27.2 mm",
    pedale="Acid PP Trekking",
    grips="Acid Travel",
    beleuchtung="Ohne Beleuchtung"
   
)
Trek_FX3_Disc = Fahrrad(
    G_eingenschaften="Das Trek FX 3 Disc ist ein vielseitiges Fitnessbike mit leichtem Aluminiumrahmen, vibrationsdämpfender Carbon-Gabel und zuverlässiger 18-Gang Shimano-Schaltung. Hydraulische Scheibenbremsen sorgen für starke Bremsleistung bei jedem Wetter. Es ist ideal für Fitness, Pendeln oder alltägliche Fahrten. Mit ergonomischen Griffen, sportlichem Bontrager-Sattel und 700x32c Reifen ist es auf Komfort und Effizienz ausgelegt.",
    Marke="Trek",
    model="FX 3 Disc",
    rahmenmaterial="Alpha Gold Aluminium",
    radgröße="28 Zoll",
    gewicht="ca. 11.6 kg",
    zulässiges_gesamtgewicht="136 kg", 
    geschlecht="Herren",
    preis="ca. 899 €", 
    antrieb="Kette",
    kettenmodell="Shimano HG53",
    anzahl_gaenge="18",
    schaltungstyp="Kettenschaltung",
    schaltwerk="Shimano Sora, 9-fach",
    umwerfer="Shimano Sora, 2-fach",
    kassette="Shimano HG200, 11–34 Zähne",
    kurbelgarniturbremstyp="Shimano Sora, 46/30 Zähne",
    bremse_vorne="Shimano MT201, hydraulische Scheibenbremse",
    bremse_hinten="Shimano MT201, hydraulische Scheibenbremse",
    bremsscheiben="160 mm / 160 mm",
    gabel="FX Carbon-Gabel mit Gewindeeinsätzen für Zubehör",
    federweg="keine Federung",
    lenker="Bontrager Aluminium Fitness, 660 mm",
    sattel="Bontrager H1",
    sattelstütze="Bontrager Aluminium, 27.2 mm",
    pedale="Wellgo Plattformpedale",
    grips="Bontrager Satellite IsoZone",
    beleuchtung="Ohne Beleuchtung"

)
Liv_Alight_3 = Fahrrad(
    G_eingenschaften="Das Liv Alight 3 ist ein leichtes, elegantes Damen-Fitnessbike mit komfortabler Geometrie für Stadt- und Freizeitfahrten. Es verfügt über einen Aluminiumrahmen, eine 3x7-Gang Shimano-Kettenschaltung und zuverlässige V-Bremsen. Der flache Lenker sorgt für eine aufrechte Sitzposition und Kontrolle im Alltag. Ideal für Pendlerinnen und Freizeitsportlerinnen.",
    Marke="Liv",
    model="Alight 3",
    rahmenmaterial="Aluminium",
    radgröße="28 Zoll",
    gewicht="ca. 11.4 kg",
    zulässiges_gesamtgewicht="ca. 125 kg",
    geschlecht="Damen",
    preis="ca. 549 €",
    antrieb="Kette",
    kettenmodell="KMC Z7",
    anzahl_gaenge="21",
    schaltungstyp="Kettenschaltung",
    schaltwerk="Shimano Tourney, 7-fach",
    umwerfer="Shimano Tourney, 3-fach",
    kassette="Shimano MF-TZ500, 14-34 Zähne",
    kurbelgarniturbremstyp="Forged alloy, 28/38/48 Zähne",
    bremse_vorne="Tektro V-Brake",
    bremse_hinten="Tektro V-Brake",
    bremsscheiben="Nicht vorhanden (V-Brakes)",
    gabel="Stahlgabel",
    federweg="keine Federung",
    lenker="Giant Sport, 31.8 mm",
    sattel="Liv Sport Comfort",
    sattelstütze="Giant D-Fuse, Aluminium, 27.2 mm",
    pedale="Platform Pedale, Kunststoff",
    grips="Liv Ergo Griffe",
    beleuchtung="Ohne Beleuchtung"

)
Cube_Access_WS = Fahrrad(
    G_eingenschaften="Das Cube Access WS ist ein robustes und vielseitiges Damen-Mountainbike mit Aluminiumrahmen, komfortabler Geometrie und einer zuverlässigen 2x8 Shimano-Schaltung. Die SR Suntour Federgabel sorgt für Komfort auf unebenen Strecken. Hydraulische Scheibenbremsen bieten Sicherheit bei jeder Witterung. Ideal für Einsteigerinnen im Gelände oder für sportliche Ausflüge.",
    Marke="Cube",
    model="Access WS",
    rahmenmaterial="Aluminium Lite",
    radgröße="27.5 oder 29 Zoll (je nach Rahmengröße)",
    gewicht="ca. 14.5 kg",
    zulässiges_gesamtgewicht="115 kg",
    geschlecht="Damen",
    preis="ca. 599 €",
    antrieb="Kette",
    kettenmodell="KMC Z8",
    anzahl_gaenge="16",
    schaltungstyp="Kettenschaltung",
    schaltwerk="Shimano Altus, 8-fach",
    umwerfer="Shimano Tourney, 2-fach",
    kassette="Shimano HG200, 12-32 Zähne",
    kurbelgarniturbremstyp="Shimano FC-M315, 36/22 Zähne",
    bremse_vorne="Tektro HD-M275, hydraulische Scheibenbremse",
    bremse_hinten="Tektro HD-M275, hydraulische Scheibenbremse",
    bremsscheiben="160 mm / 160 mm",
    gabel="SR Suntour XCT Disc, 100 mm Federweg",
    federweg="100 mm",
    lenker="Cube Rise Trail Bar, 680 mm",
    sattel="Cube Natural Fit Venec Lite WS",
    sattelstütze="Cube Performance Post, 27.2 mm",
    pedale="Cube PP MTB",
    grips="Cube Performance Griffe",
    beleuchtung="Ohne Beleuchtung"

)
Woom_3 = Fahrrad(
    G_eingenschaften="Das Woom 3 ist ein ultraleichtes, ergonomisch gestaltetes 16-Zoll-Kinderfahrrad für Kinder im Alter von ca. 4 bis 6 Jahren. Es fördert das Gleichgewicht und die Fahrtechnik mit kindgerechter Geometrie, niedrigem Gewicht und leichtgängigen Komponenten. Ideal für das sichere Erlernen des Radfahrens.",
    Marke="Woom",
    model="3",
    rahmenmaterial="Aluminium 6061",
    radgröße="16 Zoll",
    gewicht="5.4 kg",
    zulässiges_gesamtgewicht="ca. 60 kg",
    geschlecht="Kinder",
    preis="ca. 449 €",
    antrieb="Kette",
    kettenmodell="KMC C410",
    anzahl_gaenge="1",
    schaltungstyp="keine Schaltung (Singlespeed)",
    schaltwerk="nicht vorhanden",
    umwerfer="nicht vorhanden",
    kassette="18 Zähne (freilaufend)",
    kurbelgarniturbremstyp="Woom Kurbelgarnitur, 25 Zähne",
    bremse_vorne="V-Brake mit ergonomischem Bremshebel",
    bremse_hinten="V-Brake mit ergonomischem Bremshebel",
    bremsscheiben="Keine (V-Brakes)",
    gabel="Starrgabel, Aluminium",
    federweg="keine Federung",
    lenker="Woom Alu-Lenker, kindgerecht gebogen",
    sattel="Woom Sattel, ergonomisch für Kinder",
    sattelstütze="Aluminium, 250 mm, 25.4 mm Durchmesser",
    pedale="Kindgerechte Kunststoffpedale mit Reflektoren",
    grips="Woom Ergogriffe",
    beleuchtung="Keine (optional nachrüstbar)"
)
Puky_zl_18 = Fahrrad(
    G_eingenschaften="Das Puky ZL 18 ist ein robustes, stabiles und kindgerechtes 18-Zoll-Kinderfahrrad für Kinder ab etwa 5 Jahren. Es ist mit Rücktrittbremse, Felgenbremsen, Schutzblechen, Gepäckträger und kompletter Sicherheitsausstattung ausgestattet. Perfekt für den Einstieg in den Straßenverkehr.",
    Marke="Puky",
    model="ZL 18",
    rahmenmaterial="Aluminium",
    radgröße="18 Zoll",
    gewicht="ca. 10.2 kg",
    zulässiges_gesamtgewicht="ca. 60–65 kg",
    geschlecht="Kinder",
    preis="ca. 279 €",
    antrieb="Kette",
    kettenmodell="KMC Standard",
    anzahl_gaenge="1",
    schaltungstyp="keine Schaltung (Singlespeed)",
    schaltwerk="nicht vorhanden",
    umwerfer="nicht vorhanden",
    kassette="18 Zähne (freilaufend mit Rücktritt)",
    kurbelgarniturbremstyp="Puky Standardkurbel, ca. 28 Zähne",
    bremse_vorne="V-Brake (Felgenbremse)",
    bremse_hinten="Rücktrittbremse",
    bremsscheiben="Keine (Felgen- und Rücktrittbremse)",
    gabel="Starrgabel, Stahl",
    federweg="keine Federung",
    lenker="Kindgerechter Lenker mit Sicherheitsgriffen",
    sattel="Kindersattel, gepolstert",
    sattelstütze="Stahl, ca. 25.4 mm",
    pedale="Kindgerechte rutschfeste Kunststoffpedale",
    grips="Sicherheitslenkergriffe",
    beleuchtung="Dynamo-Lichtanlage vorne und hinten mit Standlichtfunktion"
)





