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
            },
# ДОБАВЬТЕ В READING_DATA ВНУТРЬ СЛОВАРЯ "captains_daughter" В "parts"

            9: {
                "title": "Chapitre III (Partie 1/4): La forteresse de Bélogorsk",
                "text": """
            <p><strong>III. LA FORTERESSE</strong></p>
            
            <p>La forteresse de Bélogorsk était située à quarante verstes d'Orenbourg. De cette ville, la route longeait les bords escarpés du Iaïk. La rivière n'était pas encore gelée, et ses flots couleur de plomb prenaient une teinte noire entre les rives blanchies par la neige. Devant moi s'étendaient les steppes kirghises. Je me perdais dans mes réflexions, tristes pour la plupart. La vie de garnison ne m'offrait pas beaucoup d'attraits; je tâchais de me représenter mon chef futur, le capitaine Mironoff. Je m'imaginais un vieillard sévère et morose, ne sachant rien en dehors du service et prêt à me mettre aux arrêts pour la moindre véritable. Le crépuscule arrivait; nous allions assez vite.</p>
            
            <p>"Y a-t-il loin d'ici à la forteresse? demandai-je au cocher.</p>
            
            <p>— Mais on la voit d'ici", répondit-il.</p>
            
            <p>Je me mis à regarder de tous côtés, m'attendant à voir de hauts bastions, une muraille et un fossé. Mais je ne vis rien qu'un petit village entouré d'une palissade en bois. D'un côté s'élevaient trois ou quatre tas de foin, à demi recouverts de neige; d'un autre, un moulin à vent penché sur le côté, et dont les ailes, faites de grosse écorce de tilleul, pendaient paresseusement.</p>
            
            <p>"Où donc est la forteresse? demandai-je étonné.</p>
            
            <p>— Mais la voilà", repartit le cocher en me montrant le village où nous venions de pénétrer.</p>
            
            <p>J'aperçus près de la porte un vieux canon en fer. Les rues étaient étroites et tortueuses; presque toutes les isbas étaient couvertes en chaume. J'ordonnai qu'on me menât chez le commandant, et presque aussitôt ma kibitka s'arrêta devant une maison en bois, bâtie sur une éminence, près de l'église, qui était en bois également.</p>
            
            <p>Personne ne vint à ma rencontre. Du perron j'entrai dans l'antichambre. Un vieil invalide, assis sur une table, était occupé à coudre une pièce bleue au coude d'un uniforme vert. Je lui dis de m'annoncer. "Entre, mon petit père, me dit l'invalide, les nôtres sont à la maison." Je pénétrai dans une chambre très propre, arrangée à la vieille mode. Dans un coin était dressée une armoire avec de la vaisselle. Contre la muraille un diplôme d'officier pendait encadré et sous verre. Autour du cadre étaient rangés des tableaux d'écorce, qui représentaient la Prise de Kustrin et d'Otchakov, le Choix de la fiancée et l'Enterrement du chat par les souris. Près de la fenêtre se tenait assise une vieille femme en mantelet, la tête enveloppée d'un mouchoir. Elle était occupée à dévider du fil que tenait, sur ses mains écartées, un petit vieillard borgne en habit d'officier. "Que désirez-vous, mon petit père?" me dit-elle sans interrompre son occupation. Je répondis que j'étais venu pour entrer au service, et que, d'après la règle, j'accourais me présenter à monsieur le capitaine. En disant cela, je me tournai vers le petit vieillard borgne, que j'avais pris pour le commandant. Mais la bonne dame interrompit le discours que j'avais préparé à l'avance.</p>
            """,
                "questions": [
                    {"id": 1, "type": "quiz", "question": "Où était située la forteresse de Bélogorsk?",
                     "options": ["Près de Moscou", "À quarante verstes d'Orenbourg", "Sur les bords de la Volga", "Dans les steppes kirghises"], "correct": "À quarante verstes d'Orenbourg"},
                    {"id": 2, "type": "quiz", "question": "Que voyait Pierre de la route?", "options": ["De hauts bastions", "Une muraille et un fossé", "Un petit village entouré d'une palissade", "Un grand château"], "correct": "Un petit village entouré d'une palissade"},
                    {"id": 3, "type": "quiz", "question": "Que faisait le vieil invalide dans l'antichambre?", "options": ["Il lisait un livre", "Il dormait", "Il cousait une pièce bleue à son uniforme", "Il mangeait"], "correct": "Il cousait une pièce bleue à son uniforme"},
                    {"id": 4, "type": "quiz", "question": "À qui Pierre s'est-il adressé en entrant dans la chambre?", "options": ["Au capitaine", "À un petit vieillard borgne", "À la vieille femme", "À l'invalide"], "correct": "Au petit vieillard borgne"},
                    {"id": 5, "type": "quiz", "question": "Qui était la vieille femme?", "options": ["La servante", "La femme du commandant", "La fille du commandant", "La mère du commandant"], "correct": "La femme du commandant"}
                ]
            },
# ДОБАВЬТЕ В READING_DATA ВНУТРЬ СЛОВАРЯ "captains_daughter" В "parts" (продолжение)

            10: {
                "title": "Chapitre III (Partie 2/4): Vassilissa Iégorovna",
                "text": """
            <p>"Ivan Kouzmitch n'est pas à la maison, dit-elle. Il est allé en visite chez le père Garasim. Mais c'est la même chose, je suis sa femme. Veuillez nous aimer et nous avoir en grâce. Assieds-toi, mon petit père."</p>
            
            <p>Elle appela une servante et lui dit de faire venir l'ouriadnik. Le petit vieillard me regardait curieusement de son oeil unique. "Oserais-je vous demander, me dit-il, dans quel régiment vous avez daigné servir?" Je satisfis sa curiosité.</p>
            
            <p>"Et oserais-je vous demander, continua-t-il; pourquoi vous avez daigné passer de la garde dans notre garnison?"</p>
            
            <p>Je répondis que c'était par ordre de l'autorité.</p>
            
            <p>"Probablement pour des actions peu séantes à un officier de la garde? reprit l'infatigable questionneur.</p>
            
            <p>— Veux-tu bien cesser de dire des bêtises? lui dit la femme du capitaine. Tu vois bien que ce jeune homme est fatigué de la route. Il a autre chose à faire que de te répondre. Tiens mieux tes mains. Et toi, mon petit père, continua-t-elle en se tournant vers moi, ne t'afflige pas trop de ce qu'on t'ait fourré dans notre bicoque; tu n'es pas le premier, tu ne seras pas le dernier. On souffre, mais on s'habitue. Tenez, Chvabrine, Alexéi Ivanitch, il y a déjà quatre ans qu'on l'a transféré chez nous pour un meurtre. Dieu sait quel malheur lui était arrivé. Voilà qu'un jour il est sorti de la ville avec un lieutenant; et ils avaient pris des épées, et ils se mirent à se piquer l'un l'autre, et Alexéi Ivanitch a tué le lieutenant, et encore devant deux témoins. Que veux-tu! contre le malheur il n'y a pas de maître."</p>
            
            <p>En ce moment entre l'ouriadnik, jeune et beau Cosaque. "Maximitch, lui dit la femme du capitaine, donne un logement à monsieur l'officier, et propre.</p>
            
            <p>— J'obéis, Vassilissa Iégorovna, répondit l'ouriadnik. Ne faut-il pas mettre Sa Seigneurie chez Ivan Poléjaiéff?</p>
            
            <p>— Tu radotes, Maximitch, répliqua la commandante; Poléjaiéff est déjà logé très à l'étroit; et puis c'est mon compère; et puis il n'oublie pas que nous sommes ses chefs. Conduis monsieur l'officier... Comment est votre nom, mon petit père?</p>
            
            <p>— Piòtr Andréitch.</p>
            
            <p>— Conduis Piòtr Andréitch chez Siméon Kouzoff. Le coquin a laissé entrer son cheval dans mon potager. Est-ce que tout est en ordre, Maximitch?</p>
            
            <p>— Grâce à Dieu, tout est tranquille, répondit le Cosaque; il n'y a que le caporal Prokoroff qui s'est battu au bain avec la femme Oustinia Pégoulina pour un seau d'eau chaude.</p>
            
            <p>— Ivan Ignatiitch, dit la femme du capitaine au petit vieillard borgne, juge entre Prokoroff et Oustinia qui est fautif, et punis-les tous deux.</p>
            
            <p>— C'est bon, Maximitch, va-t'en avec Dieu.</p>
            
            <p>— Piòtr Andréitch, Maximitch vous conduira à votre logement."</p>
            """,
                "questions": [
                    {"id": 1, "type": "quiz", "question": "Où était Ivan Kouzmitch?", "options": ["À la forteresse", "Chez le père Garasim", "À Orenbourg", "Dans la chambre"], "correct": "Chez le père Garasim"},
                    {"id": 2, "type": "quiz", "question": "Qui est Vassilissa Iégorovna?", "options": ["La servante", "La fille du commandant", "La femme du commandant", "La mère du commandant"], "correct": "La femme du commandant"},
                    {"id": 3, "type": "quiz", "question": "Pourquoi Chvabrine a-t-il été transféré dans la garnison?", "options": ["Pour un vol", "Pour un meurtre", "Pour une désertion", "Pour une insubordination"], "correct": "Pour un meurtre"},
                    {"id": 4, "type": "quiz", "question": "Où Maximitch a-t-il conduit Pierre?", "options": ["Chez Ivan Poléjaiéff", "Chez le capitaine", "Chez Siméon Kouzoff", "Chez Chvabrine"], "correct": "Chez Siméon Kouzoff"},
                    {"id": 5, "type": "quiz", "question": "Qu'est-ce que Vassilissa Iégorovna demande à Maximitch de faire?", "options": ["Préparer à manger", "Donner un logement à Pierre", "Appeler le capitaine", "Préparer les chevaux"], "correct": "Donner un logement à Pierre"}
                ]
            },

            11: {
                "title": "Chapitre III (Partie 3/4): L'installation et Chvabrine",
                "text": """
            <p>Je pris congé; l'ouriadnik me conduisit à une isba qui se trouvait sur le bord escarpé de la rivière, tout au bout de la forteresse. La moitié de l'isba était occupée par la famille de Siméon Kouzoff, l'autre me fut abandonnée. Cette moitié se composait d'une chambre assez propre, coupée en deux par une cloison. Savéliitch commença à s'y installer, et moi, je regardai par l'étroite fenêtre. Je voyais devant moi s'étendre une steppe nue et triste; sur le côté s'élevaient des cabanes. Quelques poules erraient dans la rue. Une vieille femme, debout sur le perron et tenant une auge à la main, appelait des cochons qui lui répondaient par un grognement amical. Et voilà dans quelle contrée j'étais condamné à passer ma jeunesse!... Une tristesse amère me saisit; je quittai la fenêtre et me couchai sans souper, malgré les exhortations de Savéliitch, qui ne cessait de répéter, avec angoisse: "Ô Seigneur Dieu! il ne daigne rien manger. Que dirait ma maîtresse si l'enfant allait tomber malade?"</p>
            
            <p>Le lendemain, à peine avais-je commencé de m'habiller, que la porte de ma chambre s'ouvrit. Il entra un jeune officier, de petite taille, de traits peu réguliers, mais dont la figure basanée avait une vivacité remarquable.</p>
            
            <p>"Pardonnez-moi, me dit-il en français, si je viens ainsi sans cérémonie faire votre connaissance. J'ai appris hier votre arrivée, et le désir de voir enfin une figure humaine s'est tellement emparé de moi que je n'ai pu y résister plus longtemps. Vous comprendrez cela quand vous aurez vécu ici quelque temps."</p>
            
            <p>Je devinai sans peine que c'était l'officier renvoyé de la garde pour l'affaire du duel. Nous fîmes connaissance. Chvabrine avait beaucoup d'esprit. Sa conversation était animée, intéressante. Il me dépeignit avec beaucoup de verve et de gaieté la famille du commandant, sa société et en général toute la contrée où le sort m'avait jeté. Je riais de bon coeur, lorsque ce même invalide, que j'avais vu rapiécer son uniforme dans l'antichambre du capitaine, entra et m'invita à dîner de la part de Vassilissa Iégorovna. Chvabrine déclara qu'il m'accompagnait.</p>
            """,
                "questions": [
                    {"id": 1, "type": "quiz", "question": "Où se trouvait l'isba de Pierre?", "options": ["Au centre de la forteresse", "Sur le bord escarpé de la rivière", "Près de l'église", "À côté de la maison du commandant"], "correct": "Sur le bord escarpé de la rivière"},
                    {"id": 2, "type": "quiz", "question": "Pourquoi Pierre s'est-il couché sans souper?", "options": ["Il n'avait pas faim", "Une tristesse amère l'avait saisi", "La nourriture était mauvaise", "Il était malade"], "correct": "Une tristesse amère l'avait saisi"},
                    {"id": 3, "type": "quiz", "question": "Qui a rendu visite à Pierre le lendemain?", "options": ["Le capitaine", "Savéliitch", "Chvabrine", "Maximitch"], "correct": "Chvabrine"},
                    {"id": 4, "type": "quiz", "question": "Pourquoi Chvabrine avait-il été renvoyé de la garde?", "options": ["Pour un vol", "Pour une désertion", "Pour un duel", "Pour une insubordination"], "correct": "Pour un duel"},
                    {"id": 5, "type": "quiz", "question": "Qui a invité Pierre à dîner?", "options": ["Le capitaine", "Chvabrine", "Vassilissa Iégorovna", "Ivan Ignatiitch"], "correct": "Vassilissa Iégorovna"}
                ]
            },

            12: {
                "title": "Chapitre III (Partie 4/4): Marie Ivanovna et le dîner",
                "text": """
            <p>En nous approchant de la maison du commandant, nous vîmes sur la place une vingtaine de petits vieux invalides, avec de longues queues et des chapeaux à trois cornes. Ils étaient rangés en ligne de bataille. Devant eux se tenait le commandant, vieillard encore vert et de haute taille, en robe de chambre et en bonnet de coton. Dès qu'il nous aperçut, il s'approcha de nous, me dit quelques mots affables, et se remit à commander l'exercice. Nous allions nous arrêter pour voir les manoeuvres, mais il nous pria d'aller sur-le-champ chez Vassilissa Iégorovna, promettant qu'il nous rejoindrait aussitôt. "Ici, nous dit-il, vous n'avez vraiment rien à voir."</p>
            
            <p>Vassilissa Iégorovna nous reçut avec simplicité et bonhomie, et me traita comme si elle m'eût dès longtemps connu. L'invalide et Palachka mettaient la nappe.</p>
            
            <p>"Qu'est-ce qu'a donc aujourd'hui mon Ivan Kouzmitch à instruire si longtemps ses troupes? dit la femme du commandant. Palachka, va le chercher pour dîner. Mais où est donc Macha?"</p>
            
            <p>À peine avait-elle prononcé ce nom, qu'entra dans la chambre une jeune fille de seize ans, au visage rond, vermeil, ayant les cheveux lissés en bandeau et retenus derrière ses oreilles que rougissaient la pudeur et l'embarras. Elle ne me plut pas extrêmement au premier coup d'oeil; je la regardai avec prévention. Chvabrine m'avait dépeint Marie, la fille du capitaine, sous les traits d'une sotte. Marie Ivanovna alla s'asseoir dans un coin et se mit à coudre. Cependant on avait apporté le chchchi. Vassilissa Iégorovna, ne voyant pas revenir son mari, envoya pour la seconde fois Palachka l'appeler.</p>
            
            <p>"Dis au maître que les visites attendent; le chchchi se refroidit. Grâce à Dieu, l'exercice ne s'en ira pas, il aura tout le temps de s'égosiller à son aise."</p>
            
            <p>Le capitaine apparut bientôt, accompagné du petit vieillard borgne.</p>
            
            <p>"Qu'est-ce que cela, mon petit père? lui dit sa femme. La table est servie depuis longtemps, et l'on ne peut pas te faire venir.</p>
            
            <p>— Vois-tu bien, Vassilissa Iégorovna, répondit Ivan Kouzmitch, j'étais occupé de mon service, j'instruisais mes petits soldats.</p>
            
            <p>— Va, va, reprit-elle, ce n'est qu'une vanterie. Le service ne leur va pas, et toi tu n'y comprends rien. Tu aurais dû rester à la maison, à prier le bon Dieu; ça t'irait bien mieux. Mes chers convives, à table, je vous prie."</p>
            """,
                "questions": [
                    {"id": 1, "type": "quiz", "question": "Que faisaient les invalides sur la place?", "options": ["Ils mangeaient", "Ils dormaient", "Ils étaient rangés en ligne de bataille", "Ils priaient"], "correct": "Ils étaient rangés en ligne de bataille"},
                    {"id": 2, "type": "quiz", "question": "Comment s'appelle la fille du capitaine?", "options": ["Vassilissa", "Palachka", "Marie Ivanovna", "Oustinia"], "correct": "Marie Ivanovna"},
                    {"id": 3, "type": "quiz", "question": "Quel âge a Marie Ivanovna?", "options": ["Quatorze ans", "Seize ans", "Dix-huit ans", "Vingt ans"], "correct": "Seize ans"},
                    {"id": 4, "type": "quiz", "question": "Qu'est-ce que Chvabrine avait dit à Pierre au sujet de Marie?", "options": ["Qu'elle était très belle", "Qu'elle était une sotte", "Qu'elle était riche", "Qu'elle était savante"], "correct": "Qu'elle était une sotte"},
                    {"id": 5, "type": "quiz", "question": "Pourquoi Vassilissa Iégorovna ne voulait-elle pas que son mari instruise trop les soldats?", "options": ["Parce qu'elle avait peur", "Parce que le dîner se refroidissait", "Parce qu'elle n'aimait pas les soldats", "Parce qu'il était fatigué"], "correct": "Parce que le dîner se refroidissait"}
                ]
            },
            13: {
                "title": "Chapitre IV (Partie 1/4): Le Duel — La vie à Bélogorsk",
                "text": """
<p><strong>IV. LE DUEL</strong></p>

<p>Il se passa plusieurs semaines, pendant lesquelles ma vie dans la forteresse de Bélogorsk devint non seulement supportable, mais agréable même. J'étais reçu comme un membre de la famille dans la maison du commandant. Le mari et la femme étaient d'excellentes gens. Ivan Kouzmitch, qui d'enfant de troupe était parvenu au rang d'officier, était un homme tout simple et sans éducation, mais bon et loyal. Sa femme le menait, ce qui, du reste, convenait fort à sa paresse naturelle. Vassilissa Iégorovna dirigeait les affaires du service comme celles de son ménage, et commandait dans toute la forteresse comme dans sa maison. Marie Ivanovna cessa bientôt de se montrer sauvage. Nous fîmes plus ample connaissance. Je trouvai en elle une fille pleine de coeur et de raison. Peu à peu je m'attachai à cette bonne famille, même à Ivan Ignatiitch, le lieutenant borgne.</p>

<p>Je devins officier. Mon service ne me pesait guère. Dans cette forteresse bénie de Dieu, il n'y avait ni exercice à faire, ni garde à monter, ni revue à passer. Le commandant instruisait quelquefois ses soldats pour son propre plaisir. Mais il n'était pas encore parvenu à leur apprendre quel était le côté droit, quel était le côté gauche. Chvabrine avait quelques livres français; je me mis à lire, et le goût de la littérature s'éveilla en moi. Le matin je lisais, et je m'essayais à des traductions, quelquefois même à des compositions en vers. Je dînais presque chaque jour chez le commandant, où je passais d'habitude le reste de la journée. Le soir, le père Garasim y venait accompagné de sa femme Akoulina, qui était la plus forte commère des environs.</p>
""",
                "questions": [
                    {"id": 1, "type": "quiz", "question": "Comment était la vie de l'auteur dans la forteresse de Bélogorsk après plusieurs semaines?",
                     "options": ["Difficile et insupportable", "Non seulement supportable, mais agréable même", "Triste et monotone", "Dangereuse"],
                     "correct": "Non seulement supportable, mais agréable même"},
                    {"id": 2, "type": "quiz", "question": "Qui commandait dans toute la forteresse selon le texte?",
                     "options": ["Ivan Kouzmitch", "Ivan Ignatiitch", "Vassilissa Iégorovna", "Le père Garasim"],
                     "correct": "Vassilissa Iégorovna"},
                    {"id": 3, "type": "quiz", "question": "Quel défaut physique avait Ivan Ignatiitch?",
                     "options": ["Il était boiteux", "Il était borgne", "Il était sourd", "Il était muet"],
                     "correct": "Il était borgne"},
                    {"id": 4, "type": "quiz", "question": "Que lisait l'auteur le matin?",
                     "options": ["Des journaux", "Des livres français", "Des lettres", "Des poèmes russes"],
                     "correct": "Des livres français"},
                    {"id": 5, "type": "quiz", "question": "Qui venait le soir chez le commandant avec sa femme Akoulina?",
                     "options": ["Chvabrine", "Ivan Ignatiitch", "Le père Garasim", "Le commandant"],
                     "correct": "Le père Garasim"}
                ]
            },
            14: {
                "title": "Chapitre IV (Partie 2/4): La chanson et la querelle",
                "text": """
<p>Il va sans dire que chaque jour nous nous voyions, Chvabrine et moi. Cependant d'heure en heure sa conversation me devenait moins agréable. Ses perpétuelles plaisanteries sur la famille du commandant, et surtout ses remarques piquantes sur le compte de Marie Ivanovna, me déplaisaient fort. Je n'avais pas d'autre société que cette famille dans la forteresse, mais je n'en désirais pas d'autre.</p>

<p>Malgré toutes les prophéties, les Bachkirs ne se révoltaient pas. La tranquillité régnait autour de notre forteresse. Mais cette paix fut troublée subitement par une guerre intestine.</p>

<p>J'ai déjà dit que je m'occupais un peu de littérature. Mes essais étaient passables pour l'époque, et Soumarokoff lui-même leur rendit justice bien des années plus tard. Un jour, il m'arriva d'écrire une petite chanson dont je fus satisfait. On sait que, sous prétexte de demander des conseils, les auteurs cherchent volontiers un auditeur bénévole; je copiai ma petite chanson, et la portai à Chvabrine, qui seul, dans la forteresse, pouvait apprécier une oeuvre poétique.</p>

<p>Après un court préambule, je tirai de ma poche mon feuillet, et lui lus les vers suivants:</p>

<p><em>"Hélas! en fuyant Macha, j'espère recouvrer ma liberté!<br>
Mais les yeux qui m'ont fait prisonnier sont toujours devant moi.<br>
Toi qui sais mes malheurs, Macha, en me voyant dans cet état cruel, prends pitié de ton prisonnier."</em></p>

<p>"Comment trouves-tu cela?" dis-je à Chvabrine, attendant une louange comme un tribut qui m'était dû.</p>

<p>Mais, à mon grand mécontentement, Chvabrine, qui d'ordinaire montrait de la complaisance, me déclara net que ma chanson ne valait rien.</p>

<p>"Pourquoi cela? lui demandai-je en m'efforçant de cacher mon humeur.</p>

<p>— Parce que de pareils vers, me répondit-il, sont dignes de mon maître Trédiakofski."</p>

<p>Il prit le feuillet de mes mains, et se mit à analyser impitoyablement chaque vers, chaque mot, en me déchirant de la façon la plus maligne. Cela dépassa mes forces; je lui arrachai le feuillet des mains, je lui déclarai que, de ma vie, je ne lui montrerais aucune de mes compositions. Chvabrine ne se moqua pas moins de cette menace.</p>

<p>"Voyons, me dit-il, si tu seras en état de tenir ta parole; les poètes ont besoin d'un auditeur, comme Ivan Kouzmitch d'un carafon d'eau-de-vie avant dîner. Et qui est cette Macha? Ne serait-ce pas Marie Ivanovna?</p>

<p>— Ce n'est pas ton affaire, répondis-je en fronçant le sourcil, de savoir quelle est cette Macha. Je ne veux ni de tes avis ni de tes suppositions."</p>
""",
                "questions": [
                    {"id": 1, "type": "quiz", "question": "Qu'est-ce qui déplaisait à l'auteur dans la conversation de Chvabrine?",
                     "options": ["Ses histoires de guerre", "Ses plaisanteries sur la famille du commandant", "Son silence", "Ses compliments"],
                     "correct": "Ses plaisanteries sur la famille du commandant"},
                    {"id": 2, "type": "quiz", "question": "À qui l'auteur a-t-il apporté sa chanson?",
                     "options": ["Au commandant", "À Marie Ivanovna", "À Chvabrine", "À Ivan Ignatiitch"],
                     "correct": "À Chvabrine"},
                    {"id": 3, "type": "quiz", "question": "Comment Chvabrine a-t-il réagi à la chanson de l'auteur?",
                     "options": ["Il l'a louée", "Il a dit qu'elle ne valait rien", "Il a pleuré", "Il n'a rien dit"],
                     "correct": "Il a dit qu'elle ne valait rien"},
                    {"id": 4, "type": "quiz", "question": "À quel poète Chvabrine a-t-il comparé les vers de l'auteur?",
                     "options": ["Soumarokoff", "Trédiakofski", "Pouchkine", "Molière"],
                     "correct": "Trédiakofski"},
                    {"id": 5, "type": "quiz", "question": "Comment l'auteur a-t-il réagi aux critiques de Chvabrine?",
                     "options": ["Il a accepté les critiques", "Il a arraché le feuillet des mains de Chvabrine", "Il a brûlé la chanson", "Il a pleuré"],
                     "correct": "Il a arraché le feuillet des mains de Chvabrine"}
                ]
            },
            15: {
                "title": "Chapitre IV (Partie 3/4): Le défi et Ivan Ignatiitch",
                "text": """
<p>"— Oh! oh! poète vaniteux, continua Chvabrine en me piquant de plus en plus. Écoute un conseil d'ami: Macha n'est pas digne de devenir ta femme.</p>

<p>— Tu mens, misérable! lui criai-je avec fureur, tu mens comme un effronté!"</p>

<p>Chvabrine changea de visage. "Cela ne se passera pas ainsi, me dit-il en me serrant la main fortement; vous me donnerez satisfaction.</p>

<p>— Bien, quand tu voudras!" répondis-je avec joie, car dans ce moment j'étais prêt à le déchirer.</p>

<p>Je courus à l'instant chez Ivan Ignatiitch, que je trouvai une aiguille à la main. D'après l'ordre de la femme du commandant, il enfilait des champignons qui devaient sécher pour l'hiver.</p>

<p>"Ah! Piôtr Andréitch, me dit-il en m'apercevant, soyez le bienvenu. Pour quelle affaire Dieu vous a-t-il conduit ici? oserais-je vous demander."</p>

<p>Je lui déclarai en peu de mots que je m'étais pris de querelle avec Alexéi Ivanitch, et que je le priais, lui, Ivan Ignatiitch, d'être mon second. Ivan Ignatiitch m'écouta jusqu'au bout avec une grande attention, en écarquillant son oeil unique.</p>

<p>"Vous daignez dire, me dit-il, que vous voulez tuer Alexéi Ivanitch, et que j'en suis témoin? c'est là ce que vous voulez dire? oserais-je vous demander.</p>

<p>— Précisément.</p>

<p>— Mais, mon Dieu! Piôtr Andréitch, quelle folie avez-vous en tête? Vous vous êtes dit des injures avec Alexéi Ivanitch; eh bien, la belle affaire! une injure ne se pend pas au cou. Il vous a dit des sottises, dites-lui des impertinences; il vous donnera une tape, rendez-lui un soufflet; lui un second, vous un troisième; et puis allez chacun de votre côté. Dans la suite, nous vous ferons faire la paix. Tandis que maintenant... Est-ce une bonne action de tuer son prochain? oserais-je vous demander. Encore si c'était vous qui dussiez le tuer! que Dieu soit avec lui, car je ne l'aime guère. Mais, si c'est lui qui vous perfore, vous aurez fait un beau coup. Qui est-ce qui payera les pots cassés? oserais-je vous demander."</p>

<p>Les raisonnements du prudent officier ne m'ébranlèrent pas. Je restai ferme dans ma résolution. "Comme vous voudrez, dit Ivan Ignatiitch, faites ce qui vous plaira; mais à quoi bon serai-je témoin de votre duel? Des gens se battent; qu'y a-t-il là d'extraordinaire? oserais-je vous demander. Grâce à Dieu, j'ai approché de près les Suédois et les Turcs, et j'en ai vu de toutes les couleurs."</p>

<p>Je tâchai de lui expliquer le mieux qu'il me fut possible quel était le devoir d'un second. Mais Ivan Ignatiitch était hors d'état de me comprendre. "Faites à votre guise, dit-il. Si j'avais à me mêler de cette affaire, ce serait pour aller annoncer à Ivan Kouzmitch, selon les règles du service, qu'il se trame dans la forteresse une action criminelle et contraire aux intérêts de la couronne..."</p>
""",
                "questions": [
                    {"id": 1, "type": "quiz", "question": "Comment l'auteur a-t-il réagi quand Chvabrine a dit que Macha n'était pas digne de devenir sa femme?",
                     "options": ["Il a pleuré", "Il a crié avec fureur 'Tu mens!'", "Il est parti en silence", "Il a accepté"],
                     "correct": "Il a crié avec fureur 'Tu mens!'"},
                    {"id": 2, "type": "quiz", "question": "À qui l'auteur s'est-il adressé pour lui demander d'être son second?",
                     "options": ["Au commandant", "À Ivan Ignatiitch", "À Savéliitch", "À Marie Ivanovna"],
                     "correct": "À Ivan Ignatiitch"},
                    {"id": 3, "type": "quiz", "question": "Que faisait Ivan Ignatiitch quand l'auteur est entré chez lui?",
                     "options": ["Il lisait", "Il enfilait des champignons", "Il dormait", "Il mangeait"],
                     "correct": "Il enfilait des champignons"},
                    {"id": 4, "type": "quiz", "question": "Quelle était la position d'Ivan Ignatiitch concernant le duel?",
                     "options": ["Il voulait participer", "Il refusait d'être témoin", "Il voulait regarder", "Il voulait arrêter le duel"],
                     "correct": "Il refusait d'être témoin"},
                    {"id": 5, "type": "quiz", "question": "Que voulait faire Ivan Ignatiitch selon les règles du service?",
                     "options": ["Annoncer le duel au commandant", "Rejoindre le duel", "Fuir la forteresse", "Rien"],
                     "correct": "Annoncer le duel au commandant"}
                ]
            },
            16: {
                "title": "Chapitre IV (Partie 4/4): Le duel et la blessure",
                "text": """
<p>...et faire observer au commandant combien il serait désirable qu'il avisât aux moyens de prendre les mesures nécessaires..."</p>

<p>J'eus peur, et suppliai Ivan Ignatiitch de ne rien dire au commandant. Je parvins à grand'peine à le calmer. Cependant il me donna sa parole de se taire, et je le laissai en repos.</p>

<p>Comme d'habitude, je passai la soirée chez le commandant. Je m'efforçais de paraître calme et gai, pour n'éveiller aucun soupçon et éviter les questions importunes. Mais j'avoue que je n'avais pas le sang-froid dont se vantent les personnes qui se sont trouvées dans la même position. Toute cette soirée, je me sentis disposé à la tendresse, à la sensibilité. Marie Ivanovna me plaisait plus qu'à l'ordinaire. L'idée que je la voyais peut-être pour la dernière fois lui donnait à mes yeux une grâce touchante. Chvabrine entra. Je le pris à part, et l'informai de mon entretien avec Ivan Ignatiitch.</p>

<p>"Pourquoi des seconds? me dit-il sèchement. Nous nous passerons d'eux."</p>

<p>Nous convînmes de nous battre derrière les tas de foin, le lendemain matin, à six heures. À nous voir causer ainsi amicalement, Ivan Ignatiitch, plein de joie, manqua nous trahir.</p>

<p>"Il y a longtemps que vous eussiez dû faire comme cela, me dit-il d'un air satisfait: mauvaise paix vaut mieux que bonne querelle."</p>

<p>Mais la femme du commandant apprit tout. Le lendemain, à l'heure indiquée, alors que nous allions nous battre, Ivan Ignatiitch, suivi de cinq invalides, sortit de derrière un tas de foin. Il nous intima l'ordre de nous rendre chez le commandant. Vassilissa Iégorovna nous ordonna de donner nos épées. "Piotr Andréitch, je n'attendais pas cela de toi; comment n'as-tu pas honte? Alexéi Ivanitch, c'est autre chose; il a été transféré de la garde pour avoir fait périr une âme. Il ne croit pas en Notre-Seigneur. Mais toi, tu veux en faire autant?"</p>

<p>Ivan Kouzmitch approuvait tout ce que disait sa femme: "Les duels sont formellement défendus par le code militaire."</p>

<p>Cependant, nous ne fîmes pas la paix véritablement. Quelques jours plus tard, Chvabrine vint me trouver et me dit: "Pourquoi remettre plus longtemps? On ne nous observe plus. Allons au bord de la rivière; là personne ne nous empêchera."</p>

<p>Nous partîmes en silence, et, après avoir descendu un sentier escarpé, nous nous arrêtâmes sur le bord de l'eau, et nos épées se croisèrent.</p>

<p>Chvabrine était plus adroit que moi dans les armes; mais j'étais plus fort et plus hardi. Pendant longtemps nous ne pûmes nous faire aucun mal l'un à l'autre; mais enfin, remarquant que Chvabrine faiblissait, je l'attaquai vivement, et le fis presque entrer à reculons dans la rivière. Tout à coup j'entendis mon nom prononcé à haute voix; je tournai rapidement la tête, et j'aperçus Savéliitch qui courait à moi le long du sentier... Dans ce moment je sentis une forte piqûre dans la poitrine, sous l'épaule droite, et je tombai sans connaissance.</p>
""",
                "questions": [
                    {"id": 1, "type": "quiz", "question": "Où les adversaires ont-ils décidé de se battre?",
                     "options": ["Dans la forteresse", "Derrière les tas de foin", "Dans la maison du commandant", "Dans l'église"],
                     "correct": "Derrière les tas de foin"},
                    {"id": 2, "type": "quiz", "question": "À quelle heure le duel était-il prévu?",
                     "options": ["À cinq heures", "À six heures", "À sept heures", "À huit heures"],
                     "correct": "À six heures"},
                    {"id": 3, "type": "quiz", "question": "Qui a surpris les duellistes la première fois?",
                     "options": ["Le commandant", "Ivan Ignatiitch avec cinq invalides", "Marie Ivanovna", "Savéliitch"],
                     "correct": "Ivan Ignatiitch avec cinq invalides"},
                    {"id": 4, "type": "quiz", "question": "Qui est venu vers l'auteur pendant le duel et l'a distrait?",
                     "options": ["Marie Ivanovna", "Le commandant", "Savéliitch", "Vassilissa Iégorovna"],
                     "correct": "Savéliitch"},
                    {"id": 5, "type": "quiz", "question": "Comment s'est terminé le duel?",
                     "options": ["L'auteur a gagné", "Chvabrine a gagné", "L'auteur a été blessé et est tombé sans connaissance", "Le duel a été arrêté"],
                     "correct": "L'auteur a été blessé et est tombé sans connaissance"},
                    {"id": 6, "type": "quiz", "question": "Où l'auteur a-t-il été blessé?",
                     "options": ["À la tête", "Au bras", "Dans la poitrine, sous l'épaule droite", "À la jambe"],
                     "correct": "Dans la poitrine, sous l'épaule droite"}
                ]
            },
            17: {
                "title": "Chapitre V (Partie 1/2): La convalescence et la demande en mariage",
                "text": """
<p><strong>V. LA CONVALESCENCE</strong></p>

<p>Quand je revins à moi, je restai quelque temps sans comprendre ni ce qui m'était arrivé, ni où je me trouvais. J'étais couché sur un lit dans une chambre inconnue, et sentais une grande faiblesse. Savéliitch se tenait devant moi, une lumière à la main. Quelqu'un déroulait avec précaution les bandages qui entouraient mon épaule et ma poitrine. Peu à peu mes idées s'éclaircirent. Je me rappelai mon duel, et devinai sans peine que j'étais blessé. En cet instant, la porte gémit faiblement sur ses gonds:</p>

<p>"Eh bien, comment va-t-il? murmura une voix qui me fit tressaillir.</p>

<p>— Toujours dans le même état, répondit Savéliitch avec un soupir; toujours sans connaissance. Voilà déjà plus de quatre jours."</p>

<p>Je voulus me retourner, mais je n'en eus pas la force.</p>

<p>"Où suis-je? Qui est ici?" dis-je avec effort.</p>

<p>Marie Ivanovna s'approcha de mon lit, et se pencha doucement sur moi.</p>

<p>"Comment vous sentez-vous? me dit-elle.</p>

<p>— Bien, grâce à Dieu, répondis-je d'une voix faible. C'est vous, Marie Ivanovna; dites-moi...</p>

<p>Je ne pus achever. Savéliitch poussa un cri, la joie se peignit sur son visage.</p>

<p>"Il revient à lui, il revient à lui, répétait-il; grâces te soient rendues, Seigneur! Mon père Piotr Andréitch, m'as-tu fait assez peur? quatre jours! c'est facile à dire..."</p>

<p>Marie Ivanovna l'interrompit.</p>

<p>"Ne lui parle pas trop, Savéliitch, dit-elle: il est encore bien faible."</p>

<p>Elle sortit et ferma la porte avec précaution. Je me sentais agité de pensées confuses. J'étais donc dans la maison du commandant, puisque Marie Ivanovna pouvait entrer dans ma chambre! Je voulus interroger Savéliitch; mais le vieillard hocha la tête et se boucha les oreilles. Je fermai les yeux avec mécontentement, et m'endormis bientôt.</p>

<p>En m'éveillant, j'appelai Savéliitch; mais, au lieu de lui, je vis devant moi Marie Ivanovna. Elle me salua de sa douce voix. Je ne puis exprimer la sensation délicieuse qui me pénétra dans ce moment. Je saisis sa main et la serrai avec transport, en l'arrosant de mes larmes. Marie ne la retirait pas..., et tout à coup je sentis sur ma joue l'impression humide et brûlante de ses lèvres. Un feu rapide parcourut tout mon être.</p>

<p>"Chère bonne Marie Ivanovna, lui dis-je, soyez ma femme, consentez à mon bonheur."</p>

<p>Elle reprit sa raison:</p>

<p>"Au nom du ciel, calmez-vous, me dit-elle en ôtant sa main, vous êtes encore en danger; votre blessure peut se rouvrir; ayez soin de vous,... ne fût-ce que pour moi."</p>

<p>Après ces mots, elle sortit en me laissant au comble du bonheur. Je me sentais revenir à la vie.</p>

<p>Dès cet instant je me sentis mieux d'heure en heure. C'était le barbier du régiment qui me pansait, car il n'y avait pas d'autre médecin dans la forteresse; et grâce à Dieu, il ne faisait pas le docteur. Ma jeunesse et la nature hâtèrent ma guérison. Toute la famille du commandant m'entourait de soins. Marie Ivanovna ne me quittait presque jamais. Il va sans dire que je saisis la première occasion favorable pour continuer ma déclaration interrompue, et, cette fois, Marie m'écouta avec plus de patience. Elle me fit naïvement l'aveu de son affection, et ajouta que ses parents seraient sans doute heureux de son bonheur. "Mais pensez-y bien, me disait-elle; n'y aura-t-il pas d'obstacles de la part des vôtres?"</p>

<p>Ce mot me fit réfléchir. Je ne doutais pas de la tendresse de ma mère; mais, connaissant le caractère et la façon de penser de mon père, je pressentais que mon amitié ne le toucherait pas extrêmement, et qu'il la traiterait de folie de jeunesse. Je l'avouai franchement à Marie Ivanovna; mais néanmoins je résolus d'écrire à mon père aussi éloquemment que possible pour lui demander sa bénédiction. Je montrai ma lettre à Marie Ivanovna, qui la trouva si convaincante et si touchante qu'elle ne douta plus du succès, et s'abandonna aux sentiments de son coeur avec toute la confiance de la jeunesse.</p>

<p>Je fis la paix avec Chvabrine dans les premiers jours de ma convalescence. Ivan Kouzmitch me dit en me reprochant mon duel: "Vois-tu bien, Piotr Andréitch, je devrais à la rigueur te mettre aux arrêts; mais te voilà déjà puni sans cela. Pour Alexéi Ivanitch, il est enfermé par mon ordre, et sous bonne garde, dans le magasin à blé, et son épée est sous clef chez Vassilissa Iégorovna. Il aura le temps de réfléchir à son aise et de se repentir."</p>

<p>J'étais trop content pour garder dans mon coeur le moindre sentiment de rancune. Je me mis à prier pour Chvabrine, et le bon commandant, avec la permission de sa femme, consentit à lui rendre la liberté. Chvabrine vint me voir. Il témoigna un profond regret de tout ce qui était arrivé, avoua que toute la faute était à lui, et me pria d'oublier le passé. Étant de ma nature peu rancunier, je lui pardonnai de bon coeur et notre querelle et ma blessure. Je voyais dans sa calomnie l'irritation de la vanité blessée; je pardonnai donc généreusement à mon rival malheureux.</p>
""",
                "questions": [
                    {"id": 1, "type": "quiz", "question": "Combien de jours Pierre est-il resté sans connaissance?", "options": ["Deux jours", "Quatre jours", "Six jours", "Huit jours"], "correct": "Quatre jours"},
                    {"id": 2, "type": "quiz", "question": "Qui a soigné Pierre?", "options": ["Un médecin", "Le barbier du régiment", "Marie Ivanovna", "Savéliitch"], "correct": "Le barbier du régiment"},
                    {"id": 3, "type": "quiz", "question": "Que demande Pierre à Marie Ivanovna?", "options": ["Son pardon", "De l'épouser", "De l'aider à s'enfuir", "De lui écrire une lettre"], "correct": "De l'épouser"},
                    {"id": 4, "type": "quiz", "question": "Comment Pierre a-t-il traité Chvabrine après sa guérison?", "options": ["Il l'a défié en duel", "Il lui a pardonné", "Il l'a dénoncé au commandant", "Il l'a évité"], "correct": "Il lui a pardonné"}
                ]
            },
            18: {
                "title": "Chapitre V (Partie 2/2): La lettre du père et la séparation",
                "text": """
<p>Je fus bientôt guéri complètement, et pus retourner à mon logis. J'attendais avec impatience la réponse à ma lettre, n'osant pas espérer, mais tâchant d'étouffer en moi de tristes pressentiments. Je ne m'étais pas encore expliqué avec Vassilissa Iégorovna et son mari. Mais ma recherche ne pouvait pas les étonner: ni moi ni Marie ne cachions nos sentiments devant eux, et nous étions assurés d'avance de leur consentement.</p>

<p>Enfin, un beau jour, Savéliitch entra chez moi, une lettre à la main. Je la pris en tremblant. L'adresse était écrite de la main de mon père. Cette vue me prépara à quelque chose de grave, car, d'habitude, c'était ma mère qui m'écrivait, et lui ne faisait qu'ajouter quelques lignes à la fin. Longtemps je ne pus me décider à rompre le cachet; je relisais la suscription solennelle: "À mon fils Piötr Andréitch Grineff, gouvernement d'Orenbourg, forteresse de Bélogorsk". Je tâchais de découvrir, à l'écriture de mon père, dans quelle disposition d'esprit il avait écrit la lettre. Enfin je me décidai à décacheter, et dès les premières lignes je vis que toute l'affaire était au diable. Voici le contenu de cette lettre:</p>

<p>"Mon fils Piötr, nous avons reçu le 15 de ce mois la lettre dans laquelle tu nous demandes notre bénédiction paternelle et notre consentement à ton mariage avec Marie Ivanovna, fille Mironoff. Et non seulement je n'ai pas l'intention de te donner ni ma bénédiction ni mon consentement, mais encore j'ai l'intention d'arriver jusqu'à toi et de te bien punir pour tes sottises comme un petit garçon, malgré ton rang d'officier, parce que tu as prouvé que tu n'es pas digne de porter l'épée qui t'a été remise pour la défense de la patrie, et non pour te battre en duel avec des fous de ton espèce. Je vais écrire à l'instant même à André Carlovitch pour le prier de te transférer de la forteresse de Bélogorsk dans quelque endroit encore plus éloigné afin de faire passer ta folie. En apprenant ton duel et ta blessure, ta mère est tombée malade de douleur, et maintenant encore elle est alitée. Qu'advindra-t-il de toi? Je prie Dieu qu'il te corrige, quoique je n'ose pas avoir confiance en sa bonté.</p>

<p>"Ton père, A. G."</p>

<p>La lecture de cette lettre éveilla en moi des sentiments divers. Les dures expressions que mon père ne m'avait pas ménagées me blessaient profondément; le dédain avec lequel il traitait Marie Ivanovna me semblait aussi injuste que malséant; enfin l'idée d'être renvoyé hors de la forteresse de Bélogorsk m'épouvantait. Mais j'étais surtout chagriné de la maladie de ma mère. J'étais indigné contre Savéliitch, ne doutant pas que ce ne fût lui qui avait fait connaître mon duel à mes parents. Après avoir marché quelque temps en long et en large dans ma petite chambre, je m'arrêtai brusquement devant lui, et lui dis avec colère: "Il paraît qu'il ne t'a pas suffi que, grâce à toi, j'aie été blessé et tout au moins au bord de la tombe; tu veux aussi tuer ma mère".</p>

<p>Savéliitch resta immobile comme si la foudre l'avait frappé.</p>

<p>"Aie pitié de moi, seigneur, s'écria-t-il presque en sanglotant; qu'est-ce que tu daignes me dire? C'est moi qui suis la cause que tu as été blessé? Mais Dieu voit que je courais mettre ma poitrine devant toi pour recevoir l'épée d'Alexié Ivanitch. La vieillesse maudite m'en a seule empêché. Qu'ai-je donc fait à ta mère?"</p>

<p>Mais qui donc s'était donné la peine de dénoncer ma conduite à mon père? Le général? il ne semblait pas s'occuper beaucoup de moi; et puis, Ivan Kouzmitch n'avait pas cru nécessaire de lui faire un rapport sur mon duel. Je me perdais en suppositions. Mes soupçons s'arrêtaient sur Chvabrine; lui seul trouvait un avantage dans cette dénonciation, dont la suite pouvait être mon éloignement de la forteresse et ma séparation d'avec la famille du commandant. J'allai tout raconter à Marie Ivanovna.</p>

<p>"Que vous est-il arrivé? me dit-elle; comme vous êtes pâle!</p>

<p>— Tout est fini", lui répondis-je, en lui remettant la lettre de mon père.</p>

<p>Ce fut à son tour de pâlir. Après avoir lu, elle me rendit la lettre, et me dit d'une voix émue: "Ce n'a pas été mon destin. Vos parents ne veulent pas de moi dans leur famille; que la volonté de Dieu soit faite! Dieu sait mieux que nous ce qui nous convient. Il n'y a rien à faire, Piôtr Andréitch; soyez heureux, vous au moins."</p>

<p>"Cela ne sera pas, m'écriai-je, en la saisissant par la main. Tu m'aimes, je suis prêt à tout. Allons nous jeter aux pieds de tes parents. Ce sont des gens simples; ils ne sont ni fiers ni cruels; ils nous donneront, eux, leur bénédiction, nous nous marierons; et puis, avec le temps, j'en suis sûr, nous parviendrons à fléchir mon père. Ma mère intercédera pour nous, il me pardonnera."</p>

<p>"Non, Piôtr Andréitch, répondit Marie: je ne t'épouserai pas sans la bénédiction de tes parents. Sans leur bénédiction tu ne seras pas heureux. Soumettons-nous à la volonté de Dieu. Si tu rencontres une autre fiancée, si tu l'aimes, que Dieu soit avec toi. Piôtr Andréitch, moi, je prierai pour vous deux."</p>

<p>Elle se mit à pleurer et se retira. De ce jour ma situation changea; Marie Ivanovna ne me parlait presque plus et tâchait même de m'éviter. La maison du commandant me devint insupportable; je m'habituai peu à peu à rester seul chez moi. La vie me devint à charge. Je m'abandonnai à une noire mélancolie, qu'alimentaient encore la solitude et l'inaction. Je me laissais complètement abattre et je craignais de devenir fou, lorsque des événements soudains, qui eurent une grande influence sur ma vie, vinrent donner à mon âme un ébranlement profond et salutaire.</p>
""",
                "questions": [
                    {"id": 1, "type": "quiz", "question": "Que contient la lettre du père de Pierre?", "options": ["Sa bénédiction pour le mariage", "Son refus et la menace de transférer Pierre", "Une invitation à revenir à la maison", "Des nouvelles de la santé de sa mère"], "correct": "Son refus et la menace de transférer Pierre"},
                    {"id": 2, "type": "quiz", "question": "De qui Pierre soupçonne-t-il la dénonciation?", "options": ["Savéliitch", "Chvabrine", "Le général", "Ivan Kouzmitch"], "correct": "Chvabrine"},
                    {"id": 3, "type": "quiz", "question": "Que répond Marie Ivanovna à la proposition de Pierre de se marier quand même?", "options": ["Elle accepte", "Elle refuse sans la bénédiction des parents", "Elle veut s'enfuir avec lui", "Elle demande à ses parents"], "correct": "Elle refuse sans la bénédiction des parents"},
                    {"id": 4, "type": "quiz", "question": "Quel état d'esprit envahit Pierre après cette séparation?", "options": ["La joie", "La colère", "La mélancolie", "L'espoir"], "correct": "La mélancolie"}
                ]
            },
            19: {
                "title": "Chapitre VI (Partie 1/2): L'arrivée de Pougatcheff",
                "text": """
<p><strong>VI. POUGATCHEFF</strong></p>

<p>Avant d'entamer le récit des événements étranges dont je fus le témoin, je dois dire quelques mots sur la situation où se trouvait le gouvernement d'Orenbourg vers la fin de l'année 1773. Cette riche et vaste province était habitée par une foule de peuplades à demi sauvages, qui venaient récemment de reconnaître la souveraineté des tsars russes. Leurs révoltes continuelles, leur impatience de toute loi et de la vie civilisée, leur inconstance et leur cruauté demandaient, de la part du gouvernement, une surveillance constante pour les réduire à l'obéissance. On avait élevé des forteresses dans les lieux favorables, et dans la plupart on avait établi à demeure fixe des Cosaques, anciens possesseurs des rives du Iaïk. Mais ces Cosaques eux-mêmes, qui auraient dû garantir le calme et la sécurité de ces contrées, étaient devenus depuis quelque temps des sujets inquiets et dangereux pour le gouvernement impérial. En 1772, une émeute survint dans leur principale bourgade. Cette émeute fut causée par les mesures sévères qu'avait prises le général Traubenberg pour ramener l'armée à l'obéissance. Elles n'eurent d'autre résultat que le meurtre barbare de Traubenberg, l'élévation de nouveaux chefs, et finalement la répression de l'émeute à force de mitraille et de cruels châtiments.</p>

<p>Cela s'était passé peu de temps avant mon arrivée dans la forteresse de Bélogorsk. Alors tout était ou paraissait tranquille. Mais l'autorité avait trop facilement prêté foi au feint repentir des révoltés, qui couvaient leur haine en silence, et n'attendaient qu'une occasion propice pour recommencer la lutte.</p>

<p>Je reviens à mon récit.</p>

<p>Un soir (c'était au commencement d'octobre 1773), j'étais seul à la maison, à écouter le sifflement du vent d'automne et à regarder les nuages qui glissaient rapidement devant la lune. On vint m'appeler de la part du commandant, chez lequel je me rendis à l'instant même. J'y trouvai Chvabrine, Ivan Ignatiitch et l'ouriadnik des Cosaques. Il n'y avait dans la chambre ni la femme ni la fille du commandant. Celui-ci me dit bonjour d'un air préoccupé. Il ferma la porte, fit asseoir tout le monde, hors l'ouriadnik, qui se tenait debout, tira un papier de sa poche et nous dit:</p>

<p>"Messieurs les officiers, une nouvelle importante écoutez ce qu'écrit le général."</p>

<p>Il mit ses lunettes et lut ce qui suit:</p>

<p>"Je vous informe par la présente que le fuyard et schismatique Cosaque du Don Iéméliane Pougatcheff, après s'être rendu coupable de l'impardonnable insolence d'usurper le nom du défunt empereur Pierre III, a réuni une troupe de brigands, suscité des troubles dans les villages du Iaïk, et pris et même détruit plusieurs forteresses, en commettant partout des brigandages et des assassinats. En conséquence, dès la réception de la présente, vous aurez, monsieur le capitaine, à aviser aux mesures qu'il faut prendre pour repousser le susdit scélérat et usurpateur, et, s'il est possible, pour l'exterminer entièrement dans le cas où il tournerait ses armes contre la forteresse confiée à vos soins."</p>

<p>"Prendre les mesures nécessaires, dit le commandant en ôtant ses lunettes et en pliant le papier; vois-tu bien! c'est facile à dire. Le scélérat semble fort, et nous n'avons que cent trente hommes, même en ajoutant les Cosaques, sur lesquels il n'y a pas trop à compter, soit dit sans te faire un reproche, Maximitch." L'ouriadnik sourit. "Cependant prenons notre parti, messieurs les officiers; soyez ponctuels; placez des sentinelles, établissez des rondes de nuit; dans le cas d'une attaque, fermez les portes et faites sortir les soldats. Toi, Maximitch, veille bien sur tes Cosaques. Il faut aussi examiner le canon et le bien nettoyer, et surtout garder le secret; que personne dans la forteresse ne sache rien avant le temps."</p>

<p>Après avoir ainsi distribué ses ordres, Ivan Kouzmitch nous congédia. Je sortis avec Chvabrine, tout en devisant sur ce que nous venions d'entendre.</p>

<p>"Qu'en crois-tu? comment finira tout cela? lui demandai-je.</p>

<p>— Dieu le sait, répondit-il, nous verrons; jusqu'à présent je ne vois rien de grave. Si cependant..." Alors il se mit à rêver en sifflant avec distraction un air français.</p>

<p>Malgré toutes nos précautions, la nouvelle de l'apparition de Pougatcheff se répandit dans la forteresse. Quel que fût le respect d'Ivan Kouzmitch pour son épouse, il ne lui aurait révélé pour rien au monde un secret confié comme affaire de service. Après avoir reçu la lettre du général, il s'était assez adroitement débarrassé de Vassilissa Iégorovna, en lui disant que le père Garasim avait reçu d'Orenbourg des nouvelles extraordinaires qu'il gardait dans le mystère le plus profond. Vassilissa Iégorovna prit à l'instant même le désir d'aller rendre visite à la femme du pope, et, d'après le conseil d'Ivan Kouzmitch, elle emmena Macha, de peur qu'elle ne la laissât s'ennuyer toute seule.</p>

<p>Resté maître du terrain, Ivan Kouzmitch nous envoya chercher sur-le-champ, et prit soin d'enfermer Palachka dans la cuisine, pour qu'elle ne pût nous entendre.</p>
""",
                "questions": [
                    {"id": 1, "type": "quiz", "question": "Qui est Iéméliane Pougatcheff?", "options": ["Un général russe", "Un Cosaque qui usurpe le nom de Pierre III", "Un ambassadeur étranger", "Un marchand riche"], "correct": "Un Cosaque qui usurpe le nom de Pierre III"},
                    {"id": 2, "type": "quiz", "question": "Combien d'hommes y avait-il dans la forteresse de Bélogorsk?", "options": ["50", "100", "130", "200"], "correct": "130"},
                    {"id": 3, "type": "quiz", "question": "Pourquoi Ivan Kouzmitch a-t-il envoyé sa femme et sa fille chez la femme du pope?", "options": ["Pour les protéger", "Pour pouvoir tenir un conseil de guerre en secret", "Pour les éloigner de la forteresse", "Pour leur faire peur"], "correct": "Pour pouvoir tenir un conseil de guerre en secret"},
                    {"id": 4, "type": "quiz", "question": "Quel est l'ordre principal du commandant?", "options": ["Attaquer Pougatcheff", "Garder le secret", "Envoyer des lettres", "Fuir la forteresse"], "correct": "Garder le secret"}
                ]
            },
            20: {
                "title": "Chapitre VI (Partie 2/2): Les préparatifs et la torture du Bachkir",
                "text": """
<p>Vassilissa Iégorovna revint à la maison sans avoir rien pu tirer de la femme du pope; elle apprit en rentrant que, pendant son absence, un conseil de guerre s'était assemblé chez Ivan Kouzmitch, et que Palachka avait été enfermée sous clef. Elle se douta que son mari l'avait trompée, et se mit à l'accabler de questions. Mais Ivan Kouzmitch était préparé à cette attaque; il ne se troubla pas le moins du monde, et répondit bravement à sa curieuse moitié:</p>

<p>"Vois-tu bien, ma petite mère, les femmes du pays se sont mis en tête d'allumer du feu avec de la paille; et comme cela peut être cause d'un malheur, j'ai rassemblé mes officiers et je leur ai donné l'ordre de veiller à ce que les femmes ne fassent pas de feu avec de la paille, mais bien avec des fagots et des broussailles."</p>

<p>Le lendemain, au retour de la messe, elle aperçut Ivan Ignatiitch occupé à ôter du canon des guenilles, de petites pierres, des morceaux de bois, des osselets et toutes sortes d'ordures que les petits garçons y avaient fourrées. "Que peuvent signifier ces préparatifs guerriers? pensa la femme du commandant. Est-ce qu'on craindrait une attaque de la part des Kirghises? mais serait-il possible qu'Ivan Kouzmitch me cachât une pareille misère?"</p>

<p>Elle appela Ivan Ignatiitch avec la ferme résolution de savoir de lui le secret qui tourmentait sa curiosité de femme. Vassilissa Iégorovna débuta par lui faire quelques remarques sur des objets de ménage, comme un juge qui commence un interrogatoire par des questions étrangères à l'affaire pour rassurer et endormir la prudence de l'accusé. Puis, après un silence de quelques instants, elle poussa un profond soupir, et dit en hochant la tête:</p>

<p>"Oh! mon Dieu, Seigneur! voyez quelle nouvelle! Qu'adviendra-t-il de tout cela?</p>

<p>— Eh! ma petite mère, répondit Ivan Ignatiitch, le Seigneur est miséricordieux; nous avons assez de soldats, beaucoup de poudre; j'ai nettoyé le canon. Peut-être bien repousserons-nous ce Pougatcheff. Si Dieu ne nous abandonne, le loup ne mangera personne ici.</p>

<p>— Et quel homme est-ce que ce Pougatcheff?" demanda la femme du commandant.</p>

<p>Ivan Ignatiitch vit bien qu'il avait trop parlé, et se mordit la langue. Mais il était trop tard, Vassilissa Iégorovna le contraignit à lui tout raconter, après avoir engagé sa parole qu'elle ne dirait rien à personne. Bientôt tout le monde parla de Pougatcheff.</p>

<p>Le commandant envoya l'ouriadnik avec mission de bien s'enquérir de tout dans les villages voisins. L'ouriadnik revint après une absence de deux jours, et déclara qu'il avait vu dans la steppe, à soixante verstes de la forteresse, une grande quantité de feux, et qu'il avait ouï dire aux Bachkirs qu'une force innombrable s'avançait. Il ne pouvait rien dire de plus précis, ayant craint de s'aventurer davantage.</p>

<p>On commença bientôt à remarquer une grande agitation parmi les Cosaques de la garnison. Dans toutes les rues, ils s'assemblaient par petits groupes, parlaient entre eux à voix basse, et se dispersaient dès qu'ils apercevaient un dragon ou tout autre soldat russe. On les fit espionner: Ioulai, Kalmouk baptisé, fit au commandant une révélation très grave. Selon lui, l'ouriadnik aurait fait de faux rapports; à son retour, le perfide Cosaque aurait dit à ses camarades qu'il s'était avancé jusque chez les révoltés, qu'il avait été présenté à leur chef, et que ce chef, lui ayant donné sa main à baiser, s'était longuement entretenu avec lui. Le commandant fit aussitôt mettre l'ouriadnik aux arrêts, et désigna Ioulai pour le remplacer. Ce changement fut accueilli par les Cosaques avec un mécontentement visible. Ils murmuraient à haute voix, et Ivan Ignatiitch, l'exécuteur de l'ordre du commandant, les entendit, de ses propres oreilles, dire assez clairement: "Attends, attends, rat de garnison!"</p>

<p>On saisit un Bachkir porteur de lettres séditieuses. Le commandant assembla derechef ses officiers, et pour cela il voulut encore éloigner sa femme sous un prétexte spécieux. Mais Vassilissa Iégorovna découvrit la ruse et insista pour rester. On amena le Bachkir. Je le regardai et tressaillis involontairement. Jamais je n'oublierai cet homme: il paraissait âgé de soixante et dix ans au moins, et n'avait ni nez ni oreilles. Sa tête était rasée; quelques rares poils gris lui tenaient lieu de barbe. Il était de petite taille, maigre, courbé; mais ses yeux à la tatare brillaient encore.</p>

<p>Le commandant ordonna de lui demander qui l'avait envoyé, mais le Bachkir se taisait. On ordonna de le fouetter. Mais quand on leva la main pour frapper, le Bachkir poussa un gémissement faible et puissant, et, relevant la tête, ouvrit la bouche, où, au lieu de langue, s'agitait un court tronçon. Nous fûmes tous frappés d'horreur. "Eh bien, dit le commandant, je vois que nous ne pourrons rien tirer de lui."</p>

<p>Nous continuions à débattre notre position, lorsque Vassilissa Iégorovna se précipita dans la chambre, toute haletante, et avec un air effaré.</p>

<p>"Malheur! malheur! répondit Vassilissa Iégorovna: le fort de Jinnéosern a été pris ce matin; le garçon du père Garasim vient de revenir. Il a vu comment on l'a pris. Le commandant et tous les officiers sont pendus, tous les soldats faits prisonniers; les scélérats vont venir ici."</p>

<p>Le sort de Marie Ivanovna se présenta vivement à mon imagination, et le coeur me manquait en y pensant.</p>
""",
                "questions": [
                    {"id": 1, "type": "quiz", "question": "Qu'est-ce qui manquait au Bachkir?", "options": ["Les oreilles et le nez", "La langue", "Les yeux", "Les mains"], "correct": "La langue"},
                    {"id": 2, "type": "quiz", "question": "Quelle forteresse a été prise par Pougatcheff?", "options": ["Bélogorsk", "Orenbourg", "Jinnéosern", "Simbirsk"], "correct": "Jinnéosern"},
                    {"id": 3, "type": "quiz", "question": "Comment le commandant de Jinnéosern a-t-il été traité?", "options": ["Il a été tué", "Il a été pendu avec ses officiers", "Il a été fait prisonnier", "Il s'est enfui"], "correct": "Il a été pendu avec ses officiers"},
                    {"id": 4, "type": "quiz", "question": "À quoi pense Pierre en apprenant la nouvelle?", "options": ["À fuir", "Au sort de Marie Ivanovna", "À se battre", "À appeler des renforts"], "correct": "Au sort de Marie Ivanovna"}
                ]
            }
        }
    }
}
