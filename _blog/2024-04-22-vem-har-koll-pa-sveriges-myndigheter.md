---
title: "Vem har koll på Sveriges myndigheter?"
date: 2024-04-22 10:39:14 +00:00
lang: sv
ref:
author: "Pierre Mesure"
tags: ["open-data", "myndigheter", "sweden"]
excerpt: "För några veckor sedan gick Statskontoret ut med ett förvånande besked: de hade hittat 25 nya myndigheter som ingen verkade ha koll på."
image: /uploads/blog/vem-har-koll-pa-sveriges-myndigheter/01.png
medium_url: https://medium.com/civictechsweden/vem-har-koll-p%C3%A5-sveriges-myndigheter-dc8ca8e9dab7
medium_id: dc8ca8e9dab7
---

För några veckor sedan gick Statskontoret ut med ett förvånande besked: de hade hittat 25 nya myndigheter som ingen verkade ha koll på.

[Regeringens upptäckt: 25 okända myndigheter](https://www.expressen.se/nyheter/sverige/regeringens-upptackt--25-okanda-myndigheter/)

Denna anekdot ekar med ett problem som jag har brottats med i flera år i olika projekt. Om man vill analysera vad myndigheterna säger, vad de gör eller till exempel vad de spenderar måste man först ha koll på vilka de är och vad de heter. Men varje år kommer det nya myndigheter och andra läggs ner. Vissa byter namn, andra slås ihop.

Ett exempel som jag arbetar med just nu inom min roll på Ekonomistyrningsverkets datalabb är en dataanalys som vi gör av myndigheternas remissvar inom ett projekt som finansieras av ESO. Vi hämtar remissvar som PDF från [regeringen.se](http://regeringen.se/) men i den här datamängden finns även svar från kommuner, civilsamhälle, branschorganisationer och även myndigheter som har bytt namn eller upphört. Så hur hittar vi myndigheternas remissvar i dessa 40 000+ dokument?

Min naiva gissning när jag försökte för många år sedan var att det skulle vara så lätt som att ladda ner myndighetsregistret från SCB och matcha mot dessa namn. Men så enkelt är det inte. Här är några exempel på problem man stöter på:

- namnet “Jordbruksverket” får ingen träff i registret (myndigheten heter officiellt Statens jordbruksverk)
- Datainspektionen blev nyligen Integritetsskyddsmyndigheten men SCB:s register innehåller enbart aktuella namn
- Många organisationers namn innehåller stavfel, både i vår datamängd men även i myndighetsregistren.

Utöver det här är SCB:s myndighetsregister varken komplett eller uppdaterat. Så när jag läste artikeln var jag inte förvånad men det fick mig att vilja lära mig mer om problemet och utveckla en lösning som skulle göra situationen bättre.

### Var hittar man information om myndigheter?

Vi börjar med en kartläggning av de så kallade myndighetsregister och övriga listor som finns. Här är de jag har hittat:

- SCB:s [myndighetsregister](https://myndighetsregistret.scb.se/)
- Statskontorets [Fakta om statsförvaltningen](https://www.statskontoret.se/fokusomraden/fakta-om-statsforvaltningen/myndigheterna-under-regeringen/)
- ESV:s [register](https://www.esv.se/rapportering/myndighetsregistret/) över myndigheter som ingår i statens redovisningssystem samt [listan](https://www.esv.se/statsliggaren/) över myndigheter som har fått ett regleringsbrev
- Arbetsgivarverkets [medlemslista](https://www.arbetsgivarverket.se/statistik-och-analys/staten-i-siffror-anstallda-i-staten/staten-i-siffror-om-arbetsgivarverkets-medlemmar/)
- [Rättsdatabasen](https://beta.rkrattsbaser.gov.se/) som innehåller myndigheternas instruktioner
- Wikipedia och lillasyskonet [Wikidata](https://www.wikidata.org/)
- [Handlingar.se](http://handlingar.se/), en viktig tjänst som listar organisationer som omfattas av offentlighetsprincipen, inklusive statliga myndigheter

Alla dessa har sitt eget mål för att kartlägga den statliga förvaltningen och sitt eget perspektiv på problemet. Men vad händer om man hämtar data från alla dessa källor och slår dem ihop? Den potentiella nyttan är stor:

- Analysera myndigheter på ett smartare sätt utifrån de uppgifterna som kartläggs av olika organisationer
- Integrera dessa uppgifter i fler system tack vare ett standardiserat maskinläsbart format
- Identifiera myndigheter utifrån sina olika namn och förkortningar
- Upptäcka felen som finns i de ursprungliga källorna för att se till att kvaliteten ökar och att de olika registren blir mer konsekventa

### Myndighetsdata, allt på en och samma plats

Därför har jag startat projektet [Myndighetsdata](https://github.com/civictechsweden/myndighetsdata): myndigheternas nyckelinformation på en och samma plats. Datamängden innehåller information från alla listor ovan, inklusive nedlagda myndigheter, gamla och alternativa namn, och försöker att slå ihop informationen på ett automatiserat sätt.

![](/uploads/blog/vem-har-koll-pa-sveriges-myndigheter/01.png)

Här är ett exempel med Ekonomistyrningsverkets data sammanslaget:

```
{
  "name": "Ekonomistyrningsverket",
  "name_en": "National Financial Management Authority",
  "short_name": "ESV",
  "department": "Finansdepartementet",
  "org_nr": "202100-5026",
  "website": "www.esv.se",
  "phone": "086904300",
  "email": "registrator@esv.se",
  "cofog": 112,
  "cofog10": 1,
  "structure": "Enrådighet",
  "has_gd": true,
  "postal_address": "BOX 45316 104 30 STOCKHOLM",
  "office_address": "DROTTNINGGATAN 89 113 60 STOCKHOLM",
  "other_names": ["Potential other names..."],
  "sfs": [ "1998:417", ..., "2016:1023"],
  "wikidata": "Q7654780",
  "wikipedia": "https://sv.wikipedia.org/wiki/Ekonomistyrningsverket",
  "start": "1998-01-01",
  "employees": { "2024": 159, "2023": 136... },
  "women": { "2023": 95, "2022": 94... },
  "men": { "2023": 64, "2022": 63... },
}
```

Projektet går att ta del av här på [Github](https://github.com/civictechsweden/myndighetsdata). Datat innehåller maskinläsbara versioner av alla källor med standardiserade namn för de flesta fälten, vilket möjliggör jämförelser och analys. Det finns även en hopslagen lista som matchar samma myndigheter i alla register de förekommer i men den kan inte anses vara korrekt till den har granskats manuellt. Som jag berättar längre ner är data för smutsigt för att helt klassificeras automatiskt. Projektets källkod är såklart öppen och den kan återanvändas för att hämta data direkt från de olika källorna.

I slutändan är mitt mål inte att skapa ännu en lista utan att kunna jämföra, slå samman de som finns och lägga informationen på Wikidata så den kan användas ännu mer som pålitlig källa.

Nedan redovisar jag mer i detalj vad jag lärde mig från varje källa samt de olika bristerna jag upptäckte. Det kan vara viktigt för att förstå vad man kan skapa med uppgifterna.

### Anteckningar om de olika källorna

#### SCB:s myndighetsregister

![](/uploads/blog/vem-har-koll-pa-sveriges-myndigheter/02.png)

SCB har sedan 2007 ([SFS 2007:755](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forordning-2007755-om-det-allmanna_sfs-2007-755/)) i uppdrag att hålla ett myndighetsregister med grundläggande information. Som förordningen säger ska registret innehålla domstolar, affärsverk och utlandsmyndigheter men inte kommittéer eller särskilda utredare. Eftersom den skrevs 2007 fanns det bara instruktion om att göra registret “tillgängligt för allmänheten genom en publik webbplats”.

Det är lite oklart varför SCB, en av Sveriges största och bästa myndigheter på öppna data, som pumpar ut högkvalitativ statistik varje år, har valt att fullfölja uppdraget på en sådan miniminivå. Det bästa exemplet är att många myndigheters namn skrivs med VERSALER. Flera förvaltningsmyndigheter och nämnder som finns i andra listor saknas också men det är oklart om SCB har valt att inte inkludera dem eller bara glömt dem. Kvaliteten varierar mellan de olika kategorierna, vilket visar indirekt att vissa måste uppdateras mer manuellt än andra.

Värst är utlandsmyndigheterna där jag gissar att informationen kommer från UD när den kommer. Några exempel: “Svergies ambassad Santigao”, “Sveriges Ambassad Nur-Sultan” (Kazakstans huvudstad heter numera [Astana](https://sv.wikipedia.org/wiki/Astana) igen) men också Sveriges representation vid OSSE eller Svenska Dialoginstitutet för Mellanöstern och Nordafrika som verkar ha glömts helt (är de inte myndigheter?). Den säkraste källan är då UD:s webbplats men de publicerar ingen lista, bara informationssidor till utlandssvenskar. SCB publicerar också en fil med riksdagsmyndigheter (vilket efterfrågades ej i förordningen) men det är oklart varför den bara inkluderar 1 av de [9-10 nämnderna](https://www.riksdagen.se/sv/kontakt-och-besok/riksdagens-myndigheter-och-namnder/) som Riksdagen listar på sin webbsida.

Utöver kvaliteten är det också förvånande att SCB blockerar besökaren om man laddar ner för många filer. Det blir svårt att bygga en datainfrastruktur på det och det finns liten anledning att begränsa nedladdningen av 6 statiska filer ur ett tekniskt perspektiv. På webbsidan publicerar SCB även [en lista](https://myndighetsregistret.scb.se/Ar) över nedlagda och nya myndigheter för varje år sedan 2008. Tyvärr inte som strukturerad lista så jag måste [webbskrapa](https://en.wikipedia.org/wiki/Web_scraping) och rensa den innan jag slår ihop den med registret.

#### Statskontorets fakta om statsförvaltningen

![](/uploads/blog/vem-har-koll-pa-sveriges-myndigheter/03.png)

Statskontoret har i uppdrag att följa och beskriva den offentliga sektorns utveckling och publicerar i samband med sina kvalitativa rapporter en lista över myndigheter i en Excel-fil. Det är utan tvivel den mest pålitliga källan, inte minst för att myndigheten får riktade uppdrag som kompletterar den översiktliga bilden över statlig förvaltning. Det var under ett uppdrag att kartlägga nämndmyndigheter som 25 små nämnder hittades och blev tillagda till listan. Statskontoret är dessutom väldigt mån om att definiera vad de anser är en myndighet och vad som ingår i deras kartläggning: utlandsrepresentation och riksdagsmyndigheter exkluderas samt tillfälliga verksamheter.

Listan innehåller många uppgifter som måste ha samlats manuellt, såsom alternativa namn, förkortningar och ledningsform och den är så komplett och detaljerad att det skulle kunna liknas vid ett konstverk. Nackdelen med en manuell insamling är dock att det blir svårt att hålla den helt uppdaterad och felfri. Några mindre problem som jag kunde upptäcka är [en domstol som bytte namn 2022](https://www.domstol.se/nyheter/2022/11/hudiksvalls-tingsratt-blir-halsinglands-tingsratt2/) och [en myndighet som gjorde det 1977](https://sv.wikipedia.org/wiki/Universitetskanslers%C3%A4mbetet#Myndighetens_f%C3%B6reg%C3%A5ngare) (Statskontoret använder fortfarande den gamla stavningen utan “s”). Ett större problem är att listan inte har någon ambition att vara ett register och att uppgifterna inte är framtagna för att vara maskinläsbara. Filen har ingen permanent webbadress, ett tricks måste användas för att automatisera nedladdningen. Formatet och Excel-formler i vissa celler gör det svårt att extrahera informationen. I vissa fält förekommer det också kommentarer istället för värden.

#### Ekonomistyrningsverket

![](/uploads/blog/vem-har-koll-pa-sveriges-myndigheter/04.jpg)

ESV (OBS: min nuvarande arbetsgivare men detta inlägg är inget som myndigheten står bakom) har ganska bra koll på Sveriges myndigheter av olika anledningar:

- ESV sitter på statens redovisningssystem (HERMES) där en större del av myndigheterna rapporterar in,
- ESV samlar myndigheternas årsredovisningar,
- ESV förvaltar IT-systemet Statsliggaren där Regeringskansliet tar fram myndigheternas regleringsbrev.

Det kan framstå som förvirrande men dessa tre källor ger inte samma listor över myndigheter. Av den första skapas ESV:s myndighetsregister men det är inte fullständigt eftersom många myndigheter inte rapporterar i statens redovisningssystem. Det är inte heller varje myndighet som har en årsredovisning eller får ett regleringsbrev, de minsta nöjer sig med en instruktion.

Trots detta är ESV en intressant källa eftersom myndigheten publicerar mycket historiskt data, i vissa fall ända sedan 1999.

När det gäller datakvalitet finns det inte mycket att säga. Vissa fält innehåller konstigt data såsom “?” och eftersom myndigheterna själva anger sina uppgifter i systemet har flera glömt att hålla dem uppdaterade (t.ex. [bytte PRV engelskt namn 2020](https://www.altinget.se/nyttomnamn/0-myndighet-byter-namn) men har det gamla namnet kvar i HERMES). De två sista listorna måste webbskrapas från webbplatsen medan den första är tillgänglig som kalkylark.

#### Arbetsgivarverket

![](/uploads/blog/vem-har-koll-pa-sveriges-myndigheter/05.jpg)

Arbetsgivarverket är statens arbetsgivarorganisation och en myndighet i sig. De förvaltar en lista över sina medlemmar som både saknar vissa myndigheter och inkluderar andra organisationer. Trots detta är de en viktig källa kring HR-frågor. Deras öppna data är tyvärr mycket begränsat men det går att ladda ner en lista över medlemmar sedan 1996, vilket inkluderar många myndigheter som inte längre finns. Eftersom vissa medlemmar inte är myndigheter (t.ex. Svenska kyrkan som var medlem innan 2000) måste de tas bort från listan manuellt. Rent formatmässigt har de valt att erbjuda sin statistik med hjälp av Tableau för att kunna visualisera den. Det gör det omöjligt att automatiskt ladda ner data och filen är inte helt lätt att konvertera till strukturerat data.

#### Regeringskansliets rättsdatabaser

![](/uploads/blog/vem-har-koll-pa-sveriges-myndigheter/06.png)

Inte per se en lista över myndigheter men kanske den viktigaste källan eftersom den innehåller alla myndigheters instruktioner. Inte alla myndigheter har ett regleringsbrev eller en årsredovisning, men i princip alla har en instruktion. De allra flesta instruktionerna har ett väldigt tydligt namn “Förordning med instruktion för XXX” eller “Lag med instruktion för YYY” för riksdagsmyndigheter, vilket gör det väldigt enkelt att hitta de allra flesta myndigheterna ända sedan 1960-talet. Tyvärr delar vissa myndigheter en instruktion så det går t.ex. inte att veta hur många [lokala säkerhetsnämnder vid kärntekniska anläggningar](https://beta.rkrattsbaser.gov.se/sfs/item?bet=2007%3A1054) det finns utan att koppla det till en annan källa (som Statskontorets lista).

I övrigt är databasen av väldigt bra kvalitet, med några få undantag ([Formum för levande historia](https://beta.rkrattsbaser.gov.se/sfs/item?bet=2002%3A795)), och den nya beta-webbsidan som Regeringskansliet har skapat har ett väldigt bra API så det går att ladda ner hela svenska författningssamlingen väldigt lätt. API:t är privat och odokumenterat så det räcker kanske inte för att säga att Regeringskansliet helt har kommit igång med öppna data men det visar hur ett modernt [regeringen.se](http://regeringen.se/) kan se ut i framtiden.

#### Wikipedia och Wikidata

![](/uploads/blog/vem-har-koll-pa-sveriges-myndigheter/07.png)

Alla känner nog till Wikipedia men det är kanske färre som har hört talas om syskonprojektet Wikidata. Databasen innehåller mycket av Wikipedias information i ett strukturerat format (SPARQL), vilket gör det möjligt att hämta alla myndigheter och mycket metadata (om sådana finns). Tack vare projektets många volontärer och initiativ som [Govdirectory](https://www.wikidata.org/wiki/Wikidata:WikiProject_Govdirectory) och [Wikidata Riksdag](https://www.wikidata.org/wiki/Wikidata:WikiProject_Sweden/Swedish_Riksdag_documents) finns många svenska myndigheter på Wikidata, och mycket mer!

På sikt hoppas jag att mitt lilla projekt gör att vi kan samla ännu mer information där och hålla den uppdaterad.

**EDIT:** Efter att jag publicerade detta blogginlägg använde jag datat som samlades i projektet för att rensa och komplettera hundratals Wikidata-objekt och Wikipediasidor. Jag hoppas att det kan hjälpa fler i framtiden.

#### Handlingar.se

![](/uploads/blog/vem-har-koll-pa-sveriges-myndigheter/08.png)

Ännu en inofficiell källa är [handlingar.se](http://handlingar.se/), ett viktigt initiativ från Open Knowledge Sweden för att modernisera Sveriges offentlighetsprincip. Det är en plattform som gör det lätt att begära allmänna handlingar, kartlägga offentliga aktörers svar och publicera det som lämnas ut som öppna data. Elenor Weimar, Mattias Axell m.fl. gör ett grymt jobb med denna tjänst som bygger på öppen källkod och finns i [många länder i världen](http://alaveteli.org/deployments/), och en av deras insatser är en lista över organisationer som omfattas av offentlighetsprincipen, vilken de publicerar som öppna data (CSV). Listan innehåller mer än bara myndigheter men det går att filtrera på vissa kategorier.
