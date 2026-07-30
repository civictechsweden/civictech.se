---
title: "Almedalsdata, öppna data om världens största politiska festival"
date: 2021-08-03 17:42:41 +00:00
lang: sv
ref: almedalsdata
author: "Pierre Mesure"
tags: ["sweden", "democracy", "open-data", "civictech", "almedalen"]
excerpt: "För de som inte vet är Almedalsveckan en politisk festival som äger rum varje år under julis första vecka i Visby, en mysig stad på Gotland."
image:
medium_url: https://medium.com/civictechsweden/almedalsdata-%C3%B6ppna-data-om-v%C3%A4rldens-st%C3%B6rsta-politiska-festival-760a46ed3b3c
medium_id: 760a46ed3b3c
---

[English version](/blog/almedalsdata-diving-into-the-data-of-the-worlds-biggest-political-festival-en/)

För de som inte vet är **Almedalsveckan** en politisk festival som äger rum varje år under julis första vecka i Visby, en mysig stad på Gotland. Det initierades för cirka 50 år sedan av dåvarande utbildningsminister Olof Palme och har nu vuxit till att bli vad jag tror är världens största politiska festival. Tusentals event, tiotusentals deltagare och nästan alla viktiga svenska politiker och ekonomiska intressen!

![](https://cdn-images-1.medium.com/max/1024/1*HK8uBoJMxHsmRjSC2IzDCQ.jpeg)
*Annie Lööf håller sitt partiledartal i Almedalen den 4 juli 2018 (CC-BY 4.0 Pierre Mesure)*

Sedan jag kom till Sverige har jag varit fascinerad av Almedalsveckan. Jag var där varje år fram till pandemin och det blev snabbt en del av mina svenska somrar. Jag kan nog säga att det hjälpte mig mycket att förstå det svenska samhället, det politiska systemet och en del landets kultur. Jag minns fortfarande hur förvånad jag var 2017 när jag först deltog. Jag kunde knappt svenska men lyckades redan prata med två ministrar och några riksdagsledamöter (inte säkert att de förstod mig 😁).

Småningom fick jag även se festivalens mörkare sidor, vilken plats lobbying och pengar har nu tagit och hur underrepresenterade vissa grupper blir i denna arena. Men även om det har kommit kritik om den här besvärliga trenden har jag ännu inte hittat någon ambitiös utforskning om lobbying under festivalen (helt möjligt att jag missade det, skicka gärna dina bok/artikeltips!).

### Festivalprogrammet

![](https://cdn-images-1.medium.com/max/1024/1*3g8quSm_6pLAU3kycwxFkA.jpeg)
*Program från 2017 och 2018 (CC-BY 4.0 Pierre Mesure)*

Ett föremål som alltid fascinerat mig är det tjocka **programmet** som en får när en lämnar båten och kommer in i Visby centrum för första gången. En lång lista över alla event (fast bara de offentliga event, skulle jag senare förstå) som jag religiöst bläddrade i för att göra min egen lista.

Skulle detta program kunna vara ett bra utgångsmaterial för att förstå **vilka intressen som har kommit och försvunnit i den offentliga debatten?** För att **utvärdera det ökande inflytandet av privata intressen i svensk politik?**

Även om själva boken är brett distribuerad och webbplatsen är offentlig var alla dessa frågor svåra att svara på. Som vanligt i Sverige finns det strukturerat data av riktigt bra kvalitet men att göra det tillgänglig som **öppna data** är inte naturligt för organisatörerna… Därför bestämde jag att titta närmare på det och idag presenterar jag…

### Almedalsdata

**Almedalsdata** är ett litet **civic tech** projekt som jag har jobbat med under min fritid. Det första steget var att hitta så många program som möjligt online. Det andra var att skriva ett litet skript för att hämta data och konvertera det till ett strukturerat format.

Resultatet finns tillgängligt på Github [här](https://github.com/civictechsweden/almedalsdata).

#### Vilka data finns tillgängliga?

Just nu har jag lyckats samla **alla event från 2009 tills idag**.

För varje event finns det de följande fälten: titel, arrangör, talare, beskrivning, datum, adress, kategori och några andra metadata.

Jag kommer förmodligen lägga till åren 2003 till 2008 men jag hittade bara listor utan mycket information om dem. Inget tidigare än 2003. Hör av dig om du känner till källor som jag inte hittat!

#### Vad finns i data?

Mycket, men jag har inte hunnit gräva än. Denna datamängd kan till exempel användas för att spåra vissa politikers karriärer. Kolla Nooshi Dadgostar:

- 2016: [Bostadspolitisk talesperson, (V)](https://program.almedalsveckan.info/event/user-view/42157)
- 2018: [Vice ordförande, Vänsterpartiet](https://program.almedalsveckan.info/event/user-view/51842)
- 2021: [Partiledare, Vänsterpartiet](https://program.almedalsveckan.info/event/user-view/60998)

På samma sätt kan det också hjälpa till att identifiera några svängdörrar:

- 2016: [sektionschef för Center för e-samhället, SKL](https://program.almedalsveckan.info/event/user-view/42241)
- 2018: [CDO of Sweden](https://program.almedalsveckan.info/event/user-view/50206)
- 2019: [Förbundsdirektör, IT&Telekomföretagen](https://program.almedalsveckan.info/event/user-view/59563)

För tillfället har jag bara samlat några intressanta statistik, till exempel antalet event per år:

![](https://cdn-images-1.medium.com/max/1024/1*q5ha6veqX5dl-sQy3J5yQw.png)
*Antal event per år (CC-BY 4.0 Pierre Mesure)*

Efter en stabil tillväxt under de senaste tio åren, som kulminerade på festivalens 50-årsjubileum (också ett valår), ställdes in Almedalsveckan helt 2020 innan den kom tillbaka i en mycket mindre skala 2021.

Här finns de 10 mest aktiva arrangörerna och de 10 mest populära ämnena:

![](https://cdn-images-1.medium.com/max/1024/1*ubKEwkEh3D__rjw2oEAAbw.png)
*Antal event per arrangör och per ämne, topp 10 (CC-BY 4.0 Pierre Mesure)*

Och till slut informationen du behövde mest idag!? Andelen event som erbjöd mat, sedan 2011!

![](https://cdn-images-1.medium.com/max/1024/1*n8kR41tGuISEuluGKt4mNw.png)
*Andel event som erbjuder mat per år (CC-BY 4.0 Pierre Mesure)*

Andelen event som låser människor med gratis frukost/fika verkar minska sedan början av 2010-talet. Den första pandemi-Almedalsveckan når en djup botten med endast 4 event 2021.

![](https://cdn-images-1.medium.com/max/1024/1*eI6TqmjSaUuxJze3oJ3rNw.jpeg)
*Wraps som snart ska ätas, Almedalsveckan 2017 (CC-BY 4.0 Pierre Mesure)*

### Nu är det din tur!

Vad kommer du hitta i den här datamängden? Du får gärna [utforska](https://flatgithub.com/civictechsweden/almedalsdata?filename=summary.csv) och [återanvända](https://github.com/civictechsweden/almedalsdata)! Vänligen nämn projektet om du gör det! Och tveka inte att bidra om du kan hitta mer data!
