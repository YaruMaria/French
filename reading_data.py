# reading_data.py
# Капитанская дочка - А.С. Пушкин
# Глава I: LE SERGENT AUX GARDES (Сержант гвардии)
# Разбита на 4 части для удобства чтения

READINGS = {
    "captains_daughter": {
        "title": "La Fille du capitaine - Alexandre Pouchkine",
        "subtitle": "Chapitre I: Le sergent aux gardes",
        "total_parts": 8,
        "parts": {
            1: {
                "title": "Partie 1/4: Mon père, mon enfance et Savéliitch",
                "text": """
<p><strong>Chapitre I. LE SERGENT AUX GARDES.</strong></p>

<p>Mon père, André Pétrovitch Grineff, après avoir servi dans sa jeunesse sous le comte Munich, avait quitté l'état militaire en 17.. avec le grade de premier major. Depuis ce temps, il avait constamment habité sa terre du gouvernement de Simbirsk, où il épousa Mlle Avdotia, fille d'un pauvre gentilhomme du voisinage.</p>

<p>Des neuf enfants issus de cette union, je survécus seul; tous mes frères et sœurs moururent en bas âge.</p>

<p>J'avais été inscrit comme sergent dans le régiment Séménofski par la faveur du major de la garde, le prince B..., notre proche parent. Je fus censé être en congé jusqu'à la fin de mon éducation.</p>

<p>Alors on nous élevait autrement qu'aujourd'hui. Dès l'âge de cinq ans je fus confié au piqueur Savéliitch, que sa sobriété avait rendu digne de devenir mon menin.</p>

<p>Grâce à ses soins, vers l'âge de douze ans je savais lire et écrire, et pouvais apprécier avec certitude les qualités d'un lévrier de chasse.</p>

<p>À cette époque, pour achever de m'instruire, mon père prit à gages un Français, M. Beaupré, qu'on fit venir de Moscou avec la provision annuelle de vin et d'huile de Provence.</p>

<p>Son arrivée déplut fort à Savéliitch.</p>

<p>« Il semble, grâce à Dieu, murmurait-il, que l'enfant était lavé, peigné et nourri. Où avait-on besoin de dépenser de l'argent et de louer un moussié, comme s'il n'y avait pas assez de domestiques dans la maison ? »</p>

<p>Beaupré, dans sa patrie, avait été coiffeur, puis soldat en Prusse, puis il était venu en Russie pour être outchitel, sans trop savoir la signification de ce mot.</p>

<p>C'était un bon garçon, mais étonnamment distrait et étourdi.</p>

<p>Il n'était pas, suivant son expression, ennemi de la bouteille, c'est-à-dire, pour parler à la russe, qu'il aimait à boire.</p>

<p>Mais, comme on ne présentait chez nous le vin qu'à table, et encore par petits verres, et que, de plus, dans ces occasions, on passait l'outchitel, mon Beaupré s'habitua bien vite à l'eau-de-vie russe, et finit même par la préférer à tous les vins de son pays, comme bien plus stomachique.</p>

<p>Nous devînmes de grands amis, et quoique, d'après le contrat, il se fût engagé à m'apprendre le français, l'allemand et toutes les sciences, il aima mieux apprendre de moi à babiller le russe tant bien que mal.</p>

<p>Chacun de nous s'occupait de ses affaires; notre amitié était inaltérable, et je ne désirais pas d'autre mentor. Mais le destin nous sépara bientôt, et ce fut à la suite d'un événement que je vais raconter.</p>
""",
                "questions": [
                    {"id": 1, "type": "quiz", "question": "Quel grade mon père avait-il quand il a quitté l'armée?",
                     "options": ["Capitaine", "Premier major", "Colonel", "Sergent"], "correct": "Premier major"},
                    {"id": 2, "type": "quiz", "question": "À quel âge Pierre a-t-il été confié à Savéliitch?",
                     "options": ["À trois ans", "À cinq ans", "À sept ans", "À dix ans"], "correct": "À cinq ans"},
                    {"id": 3, "type": "quiz", "question": "Que savait faire Pierre à douze ans?",
                     "options": ["Jouer du piano", "Lire et écrire", "Dessiner", "Danser"],
                     "correct": "Lire et écrire"},
                    {"id": 4, "type": "quiz", "question": "Qui était Beaupré dans sa patrie?",
                     "options": ["Professeur", "Coiffeur", "Soldat", "Marchand"], "correct": "Coiffeur"},
                    {"id": 5, "type": "quiz", "question": "Pourquoi Savéliitch n'aimait-il pas Beaupré?",
                     "options": ["Il était trop sévère", "On dépensait de l'argent pour rien",
                                 "Il ne parlait pas russe", "Il était paresseux"],
                     "correct": "On dépensait de l'argent pour rien"}
                ]
            },

            2: {
                "title": "Partie 2/4: L'incident avec Beaupré",
                "text": """
<p><strong>Chapitre I. LE SERGENT AUX GARDES (suite).</strong></p>

<p>Quelqu'un raconte en riant à ma mère que Beaupré s'enivrait constamment. Ma mère n'aimait pas à plaisanter sur ce chapitre; elle se plaignit à son tour à mon père, lequel, en homme expéditif, manda aussitôt cette canaille de Français. On lui répondit humblement que le moussié me donnait une leçon. Mon père accourut dans ma chambre. Beaupré dormait sur son lit du sommeil de l'innocence. De mon côté, j'étais livré à une occupation très intéressante.</p>

<p>On m'avait fait venir de Moscou une carte de géographie, qui pendait contre le mur sans qu'on s'en servît, et qui me tentait depuis longtemps par la largeur et la solidité de son papier. J'avais décidé d'en faire un cerf-volant, et, profitant du sommeil de Beaupré, je m'étais mis à l'ouvrage.</p>

<p>Mon père entra dans l'instant même où j'attachais une queue au cap de Bonne-Espérance. À la vue de mes travaux géographiques, il me secoua rudement par l'oreille, s'élança près du lit de Beaupré, et, l'éveillant sans précaution, il commença à l'accabler de reproches. Dans son trouble, Beaupré voulut vainement se lever; le pauvre outchitel était ivre mort. Mon père le souleva par le collet de son habit, le jeta hors de la chambre et le chassa le même jour, à la joie inexprimable de Savéliitch.</p>

<p>C'est ainsi que se termina mon éducation.</p>

<p>Je vivais en fils de famille, m'amusant à faire tourbillonner les pigeons sur les toits et jouant au cheval fondu avec les jeunes garçons de la cour. J'arrivai ainsi jusqu'au delà de seize ans. Mais à cet âge ma vie subit un grand changement.</p>
""",
                "questions": [
                    {"id": 1, "type": "quiz",
                     "question": "Que faisait Pierre quand son père est entré dans sa chambre?",
                     "options": ["Il lisait un livre", "Il fabriquait un cerf-volant", "Il dormait",
                                 "Il écrivait une lettre"], "correct": "Il fabriquait un cerf-volant"},
                    {"id": 2, "type": "quiz", "question": "Qu'a fait le père de Beaupré?",
                     "options": ["Il lui a donné de l'argent", "Il l'a chassé de la maison", "Il l'a promu",
                                 "Il l'a envoyé à Moscou"], "correct": "Il l'a chassé de la maison"},
                    {"id": 3, "type": "quiz", "question": "Pourquoi Savéliitch était-il joyeux?",
                     "options": ["Il aimait Beaupré", "Il était content que Beaupré soit chassé", "Il a reçu un cadeau",
                                 "Il a eu une promotion"], "correct": "Il était content que Beaupré soit chassé"},
                    {"id": 4, "type": "quiz", "question": "Que faisait Pierre après le départ de Beaupré?",
                     "options": ["Il étudiait beaucoup", "Il s'amusait avec les garçons de la cour", "Il travaillait",
                                 "Il lisait des livres"], "correct": "Il s'amusait avec les garçons de la cour"}
                ]
            },

            3: {
                "title": "Partie 3/4: La décision du père",
                "text": """
<p><strong>Chapitre I. LE SERGENT AUX GARDES (suite).</strong></p>

<p>Un jour d'automne, ma mère préparait dans son salon des confitures au miel, et moi, tout en me léchant les lèvres, je regardais le bouillonnement de la liqueur. Mon père, assis près de la fenêtre, venait d'ouvrir l'Almanach de la cour, qu'il recevait chaque année. Ce livre exerçait sur lui une grande influence; il ne le lisait qu'avec une extrême attention, et cette lecture avait le don de lui remuer prodigieusement la bile.</p>

<p>Ma mère, qui savait par coeur ses habitudes et ses bizarreries, tâchait de cacher si bien le malheureux livre, que des mois entiers se passaient sans que l'Almanach de la cour lui tombât sous les yeux. En revanche, quand il lui arrivait de le trouver, il ne le lâchait plus durant des heures entières.</p>

<p>Ainsi donc mon père lisait l'Almanach de la cour en haussant fréquemment les épaules et en murmurant à demi-voix: « Général!... il a été sergent dans ma compagnie. Chevalier des ordres de la Russie!... y a-t-il si longtemps que nous...? » Finalement mon père lança l'Almanach loin de lui sur le sofa et resta plongé dans une méditation profonde, ce qui ne présageait jamais rien de bon.</p>

<p>« Avdotia Vassiliéva, dit-il brusquement en s'adressant à ma mère, quel âge a Pétroucha? »</p>

<p>— Sa dix-septième petite année vient de commencer, répondit ma mère. Pétroucha est né la même année que notre tante Nastasia Garasimovna a perdu un oeil, et que...</p>

<p>— Bien, bien, reprit mon père; il est temps de le mettre au service. »</p>

<p>La pensée d'une séparation prochaine fit sur ma mère une telle impression qu'elle laissa tomber sa cuiller dans sa casserole, et des larmes coulèrent de ses yeux. Quant à moi, il est difficile d'exprimer la joie qui me saisit. L'idée du service se confondait dans ma tête avec celle de la liberté et des plaisirs qu'offre la ville de Saint-Pétersbourg. Je me voyais déjà officier de la garde, ce qui, dans mon opinion, était le comble de la félicité humaine.</p>
""",
                "questions": [
                    {"id": 1, "type": "quiz", "question": "Que lisait mon père?",
                     "options": ["Un roman", "L'Almanach de la cour", "Une lettre", "Un journal"],
                     "correct": "L'Almanach de la cour"},
                    {"id": 2, "type": "quiz", "question": "Quel âge avait Pierre?",
                     "options": ["15 ans", "16 ans", "17 ans", "18 ans"], "correct": "17 ans"},
                    {"id": 3, "type": "quiz", "question": "Qu'a décidé le père?",
                     "options": ["Envoyer Pierre à l'école", "Mettre Pierre au service militaire",
                                 "Envoyer Pierre à Moscou", "Marier Pierre"],
                     "correct": "Mettre Pierre au service militaire"},
                    {"id": 4, "type": "quiz", "question": "Comment Pierre a-t-il réagi à cette nouvelle?",
                     "options": ["Il était triste", "Il était joyeux", "Il avait peur", "Il était indifférent"],
                     "correct": "Il était joyeux"},
                    {"id": 5, "type": "quiz", "question": "Où Pierre voulait-il servir?",
                     "options": ["À l'armée", "Dans la marine", "Dans la garde à Saint-Pétersbourg",
                                 "Dans l'administration"], "correct": "Dans la garde à Saint-Pétersbourg"}
                ]
            },

            4: {
                "title": "Partie 4/4: Le départ et Zourine",
                "text": """
<p><strong>Chapitre I. LE SERGENT AUX GARDES (fin).</strong></p>

<p>Mon père n'aimait ni à changer ses plans, ni à en remettre l'exécution. Le jour de mon départ fut à l'instant fixé. La veille, mon père m'annonça qu'il allait me donner une lettre pour mon chef futur, et me demanda du papier et des plumes.</p>

<p>« Eh bien! quoi? » dit-il. « Pétroucha n'ira pas à Pétersbourg. Qu'y apprendrait-il? à dépenser de l'argent et à faire des folies. Non, qu'il serve à l'armée, qu'il flaire la poudre, qu'il devienne un soldat et non pas un fainéant de la garde, qu'il use les courroies de son sac. »</p>

<p>Il termina sa lettre, la mit avec mon brevet sous le même couvert, ôta ses lunettes, m'appela et me dit: « Cette lettre est adressée à André Karlovitch R..., mon vieux camarade et ami. Tu vas à Orenbourg pour servir sous ses ordres. »</p>

<p>Toutes mes brillantes espérances étaient donc évanouies. Au lieu de la vie gaie et animée de Pétersbourg, c'était l'ennui qui m'attendait dans une contrée lointaine et sauvage. Le lendemain matin, une kibitka de voyage fut amenée devant le perron. Mes parents me donnèrent leur bénédiction.</p>

<p>J'arrivai dans la nuit à Simbirsk, où je devais rester vingt-quatre heures. Ennuyé de regarder par les fenêtres sur une ruelle sale, je me mis à errer par les chambres de l'auberge. J'entrai dans la pièce du billard et j'y trouvai un grand monsieur d'une quarantaine d'années, Ivan Ivanovitch Zourine, chef d'escadron dans les hussards.</p>

<p>Zourine m'invita à dîner, me proposa de m'apprendre à jouer au billard, puis de jouer de l'argent. Je consentis. Nous continuâmes à jouer. Zourine me déclara que j'avais perdu cent roubles. Le lendemain, je m'éveillai avec un grand mal de tête, et reçus un billet de Zourine me demandant de lui envoyer les cent roubles perdus. Je commandai à Savéliitch de remettre cent roubles. Je partis de Simbirsk avec une conscience inquiète et des remords silencieux.</p>
""",
                "questions": [
                    {"id": 1, "type": "quiz", "question": "Où le père a-t-il envoyé Pierre servir?",
                     "options": ["À Saint-Pétersbourg", "À Moscou", "À Orenbourg", "À Simbirsk"],
                     "correct": "À Orenbourg"},
                    {"id": 2, "type": "quiz", "question": "Qui Pierre a-t-il rencontré à Simbirsk?",
                     "options": ["Un vieil ami", "Un officier nommé Zourine", "Son cousin", "Un professeur"],
                     "correct": "Un officier nommé Zourine"},
                    {"id": 3, "type": "quiz", "question": "Combien d'argent Pierre a-t-il perdu au billard?",
                     "options": ["50 roubles", "100 roubles", "200 roubles", "500 roubles"], "correct": "100 roubles"},
                    {"id": 4, "type": "quiz", "question": "Comment Pierre se sentait-il en quittant Simbirsk?",
                     "options": ["Heureux", "Fier", "Avec des remords", "Indifférent"], "correct": "Avec des remords"}
                ]
            },
            5: {
                "title": "Chapitre II (Partie 1/4): Les remords de Pierre",
                "text": """
<p><strong>Chapitre II. LE GUIDE.</strong></p>

<p>Mes réflexions pendant le voyage n'étaient pas très agréables. D'après la valeur de l'argent à cette époque, ma perte était de quelque importance. Je ne pouvais m'empêcher de convenir avec moi-même que ma conduite à l'auberge de Simbirsk avait été des plus sottes, et je me sentais coupable envers Savéliitch. Tout cela me tourmentait.</p>

<p>Le vieillard se tenait assis, dans un silence morne, sur le devant du traîneau, en détournant la tête et en faisant entendre de loin en loin une toux de mauvaise humeur. J'avais fermement résolu de faire ma paix avec lui; mais je ne savais par où commencer.</p>

<p>Enfin je lui dis: "Voyons, voyons, Savéliitch, finissons-en, faisons la paix. Je reconnais moi-même que je suis fautif. J'ai fait hier des bêtises et je t'ai offensé sans raison. Je te promets d'être plus sage à l'avenir et de te mieux écouter. Voyons, ne te fâche plus, faisons la paix."</p>

<p>— Ah! mon père Piôtr Andréitch, me répondit-il avec un profond soupir, je suis fâché contre moi-même, c'est moi qui ai tort par tous les bouts. Comment ai-je pu te laisser seul dans l'auberge? Mais que faire? Le diable s'en est mêlé. L'idée m'est venue d'aller voir la femme du diacre qui est ma commère, et voilà, comme dit le proverbe: j'ai quitté la maison et suis tombé dans la prison. Quel malheur! quel malheur! Comment reparaitre aux yeux de mes maîtres? Que diront-ils quand ils sauront que leur enfant est buveur et joueur?"</p>

<p>Pour consoler le pauvre Savéliitch, je lui donnai ma parole qu'à l'avenir je ne disposerais pas d'un seul kopek sans son consentement. Il se calma peu à peu, ce qui ne l'empêcha point cependant de grommeler encore de temps en temps en branlant la tête: "Cent roubles! c'est facile à dire".</p>
""",
                "questions": [
                    {"id": 1, "type": "quiz", "question": "Pourquoi Pierre se sentait-il coupable?",
                     "options": ["Il avait perdu de l'argent", "Il avait insulté Savéliitch",
                                 "Il avait menti à ses parents", "Il avait fui la maison"],
                     "correct": "Il avait perdu de l'argent"},
                    {"id": 2, "type": "quiz", "question": "Que promet Pierre à Savéliitch?",
                     "options": ["De ne plus jouer", "De ne pas dépenser d'argent sans son accord", "De devenir sage",
                                 "De l'écouter toujours"], "correct": "De ne pas dépenser d'argent sans son accord"},
                    {"id": 3, "type": "quiz", "question": "Comment Savéliitch appelait-il Pierre?",
                     "options": ["Mon fils", "Mon petit père", "Mon seigneur", "Mon ami"], "correct": "Mon petit père"}
                ]
            },

            6: {
                "title": "Chapitre II (Partie 2/4): Le bourane (tempête de neige)",
                "text": """
<p>J'approchais du lieu de ma destination. Autour de moi s'étendait un désert triste et sauvage, entrecoupé de petites collines et de ravins profonds. Tout était couvert de neige. Le soleil se couchait. Ma kibitka suivait l'étroit chemin, ou plutôt la trace qu'avaient laissée les traîneaux de paysans.</p>

<p>Tout à coup mon cocher jeta les yeux de côté, et s'adressant à moi: "Seigneur, dit-il en ôtant son bonnet, n'ordonnes-tu pas de retourner en arrière?</p>

<p>— Pourquoi cela?</p>

<p>— Le temps n'est pas sûr. Il fait déjà un petit vent. Vois-tu comme il roule la neige du dessus?</p>

<p>— Eh bien! qu'est-ce que cela fait?</p>

<p>— Et vois-tu ce qu'il y a là-bas? (Le cocher montrait avec son fouet le côté de l'orient.)</p>

<p>— Je ne vois rien de plus que la steppe blanche et le ciel serein.</p>

<p>— Là, là, regarde... ce petit nuage."</p>

<p>J'aperçus, en effet, sur l'horizon un petit nuage blanc que j'avais pris d'abord pour une colline éloignée. Mon cocher m'expliqua que ce petit nuage présageait un bourane (tempête de neige).</p>

<p>J'avais ouï parler des chasse-neige de ces contrées, et je savais qu'ils engloutissent quelquefois des caravanes entières. Savéliitch, d'accord avec le cocher, me conseillait de revenir sur nos pas. Mais le vent ne me parut pas fort; j'avais l'espérance d'arriver à temps au prochain relais: j'ordonnai donc de redoubler de vitesse.</p>

<p>Le cocher mit ses chevaux au galop; mais il regardait sans cesse du côté de l'orient. Cependant le vent soufflait de plus en plus fort. Le petit nuage devint bientôt une grande nuée blanche qui s'élevait lourdement, croissait, s'étendait, et qui finit par envahir le ciel tout entier. Une neige fine commença à tomber et tout à coup se précipita à gros flocons. Le vent se mit à siffler, à hurler. C'était un chasse-neige.</p>

<p>En un instant le ciel sombre se confondit avec la mer de neige que le vent soulevait de terre. Tout disparut. "Malheur à nous, seigneur! s'écria le cocher; c'est un bourane."</p>
""",
                "questions": [
                    {"id": 1, "type": "quiz", "question": "Qu'est-ce qu'un 'bourane'?",
                     "options": ["Un vent chaud", "Une tempête de neige", "Un orage", "Une pluie glacée"],
                     "correct": "Une tempête de neige"},
                    {"id": 2, "type": "quiz", "question": "Qu'a décidé Pierre malgré l'avis du cocher?",
                     "options": ["De revenir en arrière", "De continuer plus vite", "De s'arrêter", "D'attendre"],
                     "correct": "De continuer plus vite"},
                    {"id": 3, "type": "quiz", "question": "Comment le petit nuage s'est-il transformé?",
                     "options": ["Il a disparu", "Il est devenu une grande nuée blanche", "Il est devenu noir",
                                 "Il est tombé"], "correct": "Il est devenu une grande nuée blanche"}
                ]
            },

            7: {
                "title": "Chapitre II (Partie 3/4): La rencontre avec le guide",
                "text": """
<p>Je passai la tête hors de la kibitka; tout était obscurité et tourbillon. Le vent soufflait avec une expression tellement féroce, qu'il semblait en être animé. La neige s'amoncelait sur nous et nous couvrait. Les chevaux allaient au pas, et ils s'arrêtèrent bientôt.</p>

<p>"Pourquoi n'avances-tu pas? dis-je au cocher avec impatience.</p>

<p>— Mais où avancer? répondit-il en descendant du traîneau. Dieu seul sait où nous sommes maintenant. Il n'y a plus de chemin et tout est sombre."</p>

<p>Je me mis à le gronder, mais Savéliitch prit sa défense. "Pourquoi ne l'avoir pas écouté? me dit-il avec colère. Tu serais retourné au relais; tu aurais pris du thé; tu aurais dormi jusqu'au matin; l'orage se serait calmé et nous serions partis. Et pourquoi tant de hâte? Si c'était pour aller se marier, passe."</p>

<p>Savéliitch avait raison. Qu'y avait-il à faire? La neige continuait de tomber; un amas se formait autour de la kibitka. Les chevaux se tenaient immobiles, la tête baissée, et tressaillaient de temps en temps.</p>

<p>Tout à coup je crus distinguer quelque chose de noir. "Holà! cocher, m'écriai-je, qu'y a-t-il de noir là-bas?" Le cocher se mit à regarder attentivement du côté que j'indiquais. "Dieu le sait, seigneur, me répondit-il en reprenant son siège; ce n'est pas un arbre, et il me semble que cela se meut. Ce doit être un loup ou un homme."</p>

<p>Je lui donnai l'ordre de se diriger sur l'objet inconnu, qui vint aussi à notre rencontre. En deux minutes nous étions arrivés sur la même ligne, et je reconnus un homme.</p>

<p>"Holà! brave homme, lui cria le cocher; dis-nous, ne sais-tu pas le chemin?</p>

<p>— Le chemin est ici, répondit le passant; je suis sur un endroit dur. Mais à quoi diable cela sert-il?</p>

<p>— Écoute, mon petit paysan, lui dis-je; est-ce que tu connais cette contrée? Peux-tu nous conduire jusqu'à un gîte pour y passer la nuit?</p>

<p>— Cette contrée? Dieu merci, repartit le passant, je l'ai parcourue à pied et en voiture, en long et en large. Mais vois quel temps? Tout de suite on perd la route. Mieux vaut s'arrêter ici et attendre; peut-être l'ouragan cessera. Et le ciel sera serein, et nous trouverons le chemin avec les étoiles."</p>

<p>Son sang-froid me donna du courage. Je m'étais déjà décidé, en m'abandonnant à la grâce de Dieu, à passer la nuit dans la steppe, lorsque tout à coup le passant s'assit sur le banc qui faisait le siège du cocher.</p>

<p>"Grâce à Dieu, dit-il à celui-ci, une habitation n'est pas loin. Tourne à droite et marche.</p>

<p>— Pourquoi irais-je à droite? répondit mon cocher avec humeur. Où vois-tu le chemin?</p>

<p>— Le vent a soufflé de là, répondit-il, et j'ai senti une odeur de fumée, preuve qu'une habitation est proche."</p>

<p>Sa sagacité et la finesse de son odorat me remplirent d'étonnement. J'ordonnai au cocher d'aller où l'autre voulait.</p>
""",
                "questions": [
                    {"id": 1, "type": "quiz", "question": "Qui Pierre a-t-il rencontré dans la tempête?",
                     "options": ["Un paysan", "Un vagabond inconnu", "Un soldat", "Un marchand"],
                     "correct": "Un vagabond inconnu"},
                    {"id": 2, "type": "quiz", "question": "Comment l'inconnu a-t-il trouvé le chemin?",
                     "options": ["Il a vu des étoiles", "Il a senti une odeur de fumée", "Il connaissait la route",
                                 "Il a suivi le vent"], "correct": "Il a senti une odeur de fumée"},
                    {"id": 3, "type": "quiz", "question": "Que signifie 'sang-froid'?",
                     "options": ["Du sang froid", "Du courage", "Du calme", "De la peur"], "correct": "Du calme"}
                ]
            },

            8: {
                "title": "Chapitre II (Partie 4/4): Le rêve prophétique",
                "text": """
<p>Les chevaux marchaient lourdement dans la neige profonde. La kibitka s'avançait avec lenteur, tantôt soulevée sur un amas, tantôt précipitée dans une fosse et se balançant de côté et d'autre. Cela ressemblait beaucoup aux mouvements d'une barque sur la mer agitée. Savéliitch poussait des gémissements profonds, en tombant à chaque instant sur moi. Je baissai la tsinovka, je m'enveloppai dans ma pelisse et m'endormis, bercé par le chant de la tempête et le roulis du traîneau.</p>

<p>J'eus alors un songe que je n'ai plus oublié et dans lequel je vois encore quelque chose de prophétique, en me rappelant les étranges aventures de ma vie.</p>

<p>J'étais dans cette disposition de l'âme où la réalité commence à se perdre dans la fantaisie, aux premières visions incertaines de l'assoupissement. Il me semblait que le bourane continuait toujours et que nous errions sur le désert de neige. Tout à coup je crus voir une porte cochère, et nous entrâmes dans la cour de notre maison seigneuriale.</p>

<p>Ma première idée fut la peur que mon père ne se fâchât de mon retour involontaire sous le toit de la famille. Inquiet, je sors de ma kibitka, et je vois ma mère venir à ma rencontre avec un air de profonde tristesse. "Ne fais pas de bruit, me dit-elle; ton père est à l'agonie et désire te dire adieu."</p>

<p>Frappé d'effroi, j'entre à sa suite dans la chambre à coucher. Je regarde; l'appartement est à peine éclairé. Près du lit se tiennent des gens à la figure triste et abattue. Ma mère soulève le rideau et dit: "André Pétrovitch, Pétroucha est de retour; il est revenu en apprenant ta maladie. Donne-lui ta bénédiction."</p>

<p>Je me mets à genoux et j'attache mes regards sur le mourant. Mais quoi! au lieu de mon père, j'aperçois dans le lit un paysan à barbe noire, qui me regarde d'un air de gaieté. Plein de surprise, je me tourne vers ma mère: "Qu'est-ce que cela veut dire? m'écriai-je; ce n'est pas mon père. Pourquoi veux-tu que je demande sa bénédiction à ce paysan?"</p>

<p>— C'est la même chose, Pétroucha, répondit ma mère; celui-là est ton père assis; baise-lui la main et qu'il te bénisse." Je ne voulais pas y consentir. Alors le paysan s'élança du lit, tira vivement sa hache de sa ceinture et se mit à la brandir en tous sens. Je voulus m'enfuir, mais je ne le pus pas. La chambre se remplissait de cadavres. Je trébuchais contre eux; mes pieds glissaient dans des mares de sang. Le terrible paysan m'appelait avec douceur en me disant: "Ne crains rien, approche, viens que je te bénisse". L'effroi et la stupeur s'étaient emparés de moi...</p>

<p>En ce moment je m'éveillai. Les chevaux étaient arrêtés; Savéliitch me tenait par la main. "Sors, seigneur, me dit-il, nous sommes arrivés."</p>
""",
                "questions": [
                    {"id": 1, "type": "quiz", "question": "Qui Pierre a-t-il vu dans son rêve au lieu de son père?",
                     "options": ["Un soldat", "Un paysan à barbe noire", "Savéliitch", "Le cocher"],
                     "correct": "Un paysan à barbe noire"},
                    {"id": 2, "type": "quiz", "question": "Que tenait le paysan dans son rêve?",
                     "options": ["Un couteau", "Une hache", "Un pistolet", "Un bâton"], "correct": "Une hache"},
                    {"id": 3, "type": "quiz", "question": "Comment Pierre considère-t-il ce rêve?",
                     "options": ["Comme un cauchemar ordinaire", "Comme quelque chose de prophétique",
                                 "Comme un mauvais souvenir", "Comme une illusion"],
                     "correct": "Comme quelque chose de prophétique"}
                ]
            }
        }
    }
}
