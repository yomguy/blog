Title: WTF le réseau en France ?!
Date: 2013-06-27 10:30
Category: WTF
Tags: WTF, réseau, France
Slug: wtf-le-reseau-en-france
Author: Guillaume Pellerin
Summary: Le networking en France

Comme je suis adèpte du networking dans les cafés en ce moment, je m'installe ce matin à la Vielleuse de Belleville à Paris. Cherchant un peu réseau, je tombe sur 3 os.

#FreeWifi

Je réussis à loader **une** page et puis plus rien... Il y a vraiment un problème avec ce système : 95% du temps, ça foire au bout de 5mn. Il va vraiment falloir dire la vérite sur la qualité des services Free qui, derrière des solutions technologiques autrefois solides et des tarifs alléchants, laisse vraiment à désirer aujourd'hui (SMS qui arrivent 3h après envoi, Youtube indisponible le soir, etc...).

#Noodo

Il y a une antenne ds le café installé par une obscure boîte "Noodo". Il faut un code que je demande au serveur. L'accès au web est conditionné par l'envoi d'un formulaire qui me demande même un mail. Je file ma junk adresse. Ouf, au bout de 10mn que je suis installé, j'ai enfin du réseau, mais pas pour longtemps:

> Vous avez atteint le temps limite de connexion. Vous ne pouvez pas vous connectez plus de 20 minutes  par jour dans cet établissement.

Je rêve assis ! C'est comme si une autoroute privée vous donnait un temps maximum pour effectuer un voyage au-délà duquel vous ne pourriez plus rouler.

#SFR

Je me rabas sur ma solution de secours : le partage de connexion en WiFi depuis mon phone Android. Heureusement, il est rooté et surtout hacké avec une ROM AOKP. Tous les FAI français bloquent ce type de partage - bien que les appareils et les OS comme Android le permettent - i.e. pour nous vendre des clés 3G à la con alors qu'on paie déjà une bande passante 3G avec les forfaits téléphoniques. Heureusement que les hackers sont là pour nous fournir des ROMs débridées !

J'ai donc enfin du réseau, mais notez que le pékin moyen avec une ROM salopée par sa FAI française n'aurait jamais pu faire ça... *MAIS*, car il y a toujours un *mais* dans ce p**** de pays... Je dois travailler sur mon projet [Telemeta](http://telemeta.org) et en particulier sur le site des [archives du CREM](http://archives.crem-cnrs.fr). Sauf que voilà, SFR a décidé de ne pas respecter la neutralité du net de sniffer toutes les requêtes web de ses usagers... Ainsi, à la place de du code HMTML/JavaScript - que je connais pour l'avoir codé - SFR renvoie une compression du code original en remplaçant tous les liens statiques par ceux d'un proxy 1.2.3.4, genre http://1.2.3.4/bmi-int-js/bmi.js?version=1346927152

La différence :

[https://gist.github.com/yomguy/5875132](https://gist.github.com/yomguy/5875132)

au lieu de :

[https://gist.github.com/yomguy/6263650](https://gist.github.com/yomguy/6263650)

En d'autres termes, tout le contenu désiré est lu par une machine distante qui vous la renvoie comme bon lui semble.
Résultat, gros bug du lecteur audio TimeSide dont j'ai besoin...

D'après quelques tests récents, ce filtrage n'a pas lieu lorsqu'on navigue directement depuis le smartphone, mais seulement en mode de connexion partagée ou lorqu'on utilise un clé 3G SFR. Ce GROS problème a été relaté et expliqué par reflets.info dans ces 3 posts : [1](http://reflets.info/sfr-modifie-le-source-html-des-pages-que-vous-visitez-en-3g/) [2](http://reflets.info/sfr-man-in-the-middle-oui-cest-particulierement-grave/) [3](http://reflets.info/sfr-nouveau-co-editeur-de-reflets-au-sens-de-la-lcen/)

#Moralité 

Il semble donc assez compliqué encore, dans les années 10 du XXIe siècle, de travailler convenablement en mode connecté et nomade en plein coeur de Paris. Les pouvoirs politiques ont beau faire mine de s'intéresser au développement et au financement de la société numérique, le cadre de l'exploitation des ressources semble complètement hors de contrôle.

Quelques propositions pour améliorer cet état de fait:

 1. Contrôller que les services vendus par les FAIs sont bien opérationnels, du moins selon un certain taux autour d'une localité.
 2. Interdire les limitations temporelles de connexion même sur un réseau privé, le volume de données étant un bien meilleur régulateur.
 3. Empêcher les FAIs de filtrer le contenu du web transmis sans accord préalable explicite avec ses clients.
