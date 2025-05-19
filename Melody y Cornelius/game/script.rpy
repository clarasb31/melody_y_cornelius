define m = Character("Melody", color="#c84b8c")
define c = Character("Cornelius", color="#36FF7D")

# Fondos
image bg vault_night = im.Scale("images/vault_night.png", config.screen_width, config.screen_height)
image bg bank_entrance = im.Scale("images/bank_entrance.png", config.screen_width, config.screen_height)
image bg bathroom_keys = im.Scale("images/bathroom_keys.png", config.screen_width, config.screen_height)
image bg birkin = im.Scale("images/birkin.png", config.screen_width, config.screen_height)
image bg vault_inside = im.Scale("images/vault_inside.png", config.screen_width, config.screen_height)
image bg rooftop = im.Scale("images/rooftop.png", config.screen_width, config.screen_height)

# Fondo negro por defecto para cubrir bordes
image black = Solid("#000")

# Video de portada
image video_portada = Movie(play="videos/portada_video.webm", size=(config.screen_width, config.screen_height))

# Posiciones de personajes
transform right_side:
    xalign 0.95 yalign 1.0

transform left_side:
    xalign 0.05 yalign 1.0

# Efecto de flotación para botones
transform boton_flotante:
    linear 1.0 yoffset -10 xoffset 5
    linear 1.0 yoffset 0 xoffset 0
    repeat

# Personajes con emociones
image m alegria = "images/melody_alegria.png"
image m normal = "images/melody_normal.png"
image m cabreo = "images/melody_cabreo.png"
image m decepcion = "images/melody_decepcion.png"
image m tristeza = "images/melody_tristeza.png"
image m orgullo = "images/melody_orgullo.png"
image m miedo = "images/melody_miedo.png"
image m sorpresa = "images/melody_sorpresa.png"

image c alegria = "images/cornelius_alegria.png"
image c normal = "images/cornelius_normal.png"
image c cabreo = "images/cornelius_cabreo.png"
image c decepcion = "images/cornelius_decepcion.png"
image c tristeza = "images/cornelius_tristeza.png"
image c orgullo = "images/cornelius_orgullo.png"
image c miedo = "images/cornelius_miedo.png"

# Variables de actitud
default cordialidad = 0
default manipulacion = 0
default agresividad = 0

label start:
    scene video_portada
    play movie "videos/intro_video.mp4"
    play music "portada.mp3"
    show screen portada_interactiva
    $ renpy.pause(hard=True)
    return

screen portada_interactiva():
    zorder 100

    imagebutton:
        idle "images/start_intro.png"
        at boton_flotante
        xalign 0.5 yalign 0.65
        action [Stop("movie"), Hide("portada_interactiva"), Jump("introducción")]

    imagebutton:
        idle "images/exit_intro.png"
        at boton_flotante
        xalign 0.5 yalign 0.90
        action Quit(confirm=True)

label introducción:
    scene black
    scene bg vault_night with fade
    play music "suspense_theme.mp3" fadein 2.0
    show m orgullo at right_side with dissolve

    m "*canta* ¡UNA DIVA ES VA-LIEN-TE, PODE-RO-SA! ¡SU VIDA ES UN JARDÍN LLENO DE ESPINAS Y ROSAS!"
    show m alegria at right_side
    m "Sí, soy yo, Melody. Supongo que me conocerás porque represento este año a ESPAÑA en Eurovisión. Autógrafos luego, por favor…"
    show m normal at right_side
    m "Y antes de que digas nada... sí, lo que ves detrás de mí es exactamente lo que parece."
    m "Estoy frente a la caja fuerte del Banco Central, y sí, estoy robándolo."
    show m decepcion at right_side
    m "No es exactamente como lo planeé, pero aquí estamos."
    show m orgullo at right_side
    m "¿Quieres saber cómo llegué a esto?"
    show m alegria at right_side
    m "Entonces será mejor que prestes atención."
    show m orgullo at right_side
    m "Esta historia no es para corazones débiles..."

    scene black
    scene bg bank_entrance
    show m normal at right_side
    m "Cuando llegué al banco, lo primero que hice fue forzar la cerradura de la puerta principal. No fue nada difícil, utilicé una de mis fabulosas horquillas."

    scene black
    scene bg bathroom_keys
    show m sorpresa at right_side
    m "De pronto me entraron unas ganas terribles de ir al baño. ¡Alguien se había dejado las llaves de la caja fuerte sobre el lavabo!"

    scene black
    scene bg birkin
    show m alegria at right_side
    m "Y ahora estoy aquí, a punto de cumplir mi más ansiado deseo… ¡TENER UN BIRKIN!"
    show m orgullo at right_side
    m "Estos bolsos de moda son ideales… ¿A que sí?"
    show m alegria
    m "Por eso vengo a robar este banco, para ser la más fabulosa de todo Eurovisión."

    scene black
    scene bg vault_night
    show m orgullo at right_side
    m "Así que, ¡vamos allá! Entremos de una vez en esta caja fuerte…"

    jump encuentro_con_cornelius

label encuentro_con_cornelius:
    scene black
    scene bg vault_inside
    play sound "vault_open.mp3"
    show m sorpresa at right_side
    m "Pero… ¡¿qué?!"
    show m normal at right_side
    show c orgullo at left_side with dissolve
    c "¡Querida…! Te estaba esperando…"

    menu:
            "Disculpa... ¿quién eres? (Cordialidad)":
                $ cordialidad += 1
                show m alegria at right_side
                m "Oh disculpa… No esperaba compañía, pero siempre es bienvenido un aliado. Soy Melody, supongo que me conocerás. Y bien… ¿Quién eres tú?"
                jump escena_objetivos_cordial
            "Esperaba encontrarte, Cornelius (Engaño)":
                $ manipulacion += 1
                show m orgullo at right_side
                m "¡Ja, ja! ¿Crees que me sorprendes? Esperaba perfectamente encontrarte aquí, Gottfried Engelbert Cornelius…"
                jump escena_objetivos_hostil
            "¡No te acerques! (Violencia)":
                $ agresividad += 1
                show m cabreo at right_side
                m "¡¿Quién eres?! ¡No te acerques! Te advierto de que tengo un arma… y no me da miedo usarla."
                jump escena_objetivos_hostil

label escena_objetivos_cordial:
    show c orgullo at left_side
    c "Hola querida, mi nombre es Cornelius. Estoy aquí porque creo que tú y yo tenemos más cosas en común de las que pensamos…"

    menu:
            "Me interesan tus planes (Cordialidad)":
                $ cordialidad += 1
                m "Tranquilo, no he venido a enfrentarme a ti… Me interesan tus planes. Pero, ¿de qué me conoces?"
                show m normal at right_side
                jump discrepancias_cordial
            "Tengo una idea, pero necesito tu ayuda (Engaño)":
                $ manipulacion += 1
                show m orgullo at right_side
                m "Tengo una idea, yo cogeré el dinero y te lo daré cuando hayamos salido. A mí sólo me interesa el Birkin."
                jump discrepancias_mani_agre

label escena_objetivos_hostil:
    show c decepcion at left_side
    c "Sabes perfectamente quién soy y también sabes por qué nos hemos encontrado en esta caja fuerte… Melody, yo también esperaba verte."

    menu:
            "Tengo una idea, pero necesito tu ayuda (Engaño)":
                $ manipulacion += 1
                show c cabreo at left_side
                show m orgullo at right_side
                m "Tengo una idea, yo cogeré el dinero y te lo daré cuando hayamos salido. A mí sólo me interesa el Birkin."
                jump discrepancias_mani_agre
            "Aquí mando yo (Violencia)":
                $ agresividad += 1
                show c miedo at left_side
                show m cabreo at right_side
                m "Creo que no has entendido que aquí mando yo. Todo lo que hay en la caja fuerte me pertenece."
                jump discrepancias_mani_agre

label discrepancias_cordial:
    show c alegria at left_side
    show m orgullo at right_side
    c "Sí, efectivamente, te conozco. He visto tu perfil de Instagram… deduje que vendrías a robar este banco. Estoy dispuesto a ayudarte, a cambio de un módico precio."

    menu:
            "Estoy dispuesta a colaborar (Cordialidad)":
                $ cordialidad += 1
                show m normal at right_side
                m "Parece que hablamos el mismo idioma… Te escucho, espero que tu propuesta sea buena. Mi único objetivo es conseguir un Birkin."
                jump tension_cordial
            "Me gusta cómo piensas (Engaño)":
                $ manipulacion += 1
                show m orgullo at right_side
                m "Me gusta cómo piensas, Cornelius… Cuéntame más."
                jump tension_mani

label discrepancias_mani_agre:
    show c cabreo at left_side
    c "Creo que deberías dejar de actuar de esa manera"
    show c decepcion at left_side
    c "Tengo un trato que puede interesarte, no tienes otra opción"

    menu:
            "¡Para ti no hay nada! (Violencia)":
                $ agresividad += 1
                show m cabreo at right_side
                show c miedo at left_side
                m "¡Ja ja ja! ¡Eso no te lo crees ni tú! ¡Esta diva se va a llevar el botín y para ti no hay nada, Gilberto Ángel o como te llames!"
                jump tension_agre
            "¿Qué tienes en mente? (Engaño)":
                $ manipulacion += 1
                show m orgullo at right_side
                show c orgullo at left_side
                m "Me gusta cómo piensas, Cornelius… Cuéntame más."
                jump tension_mani

label tension_cordial:
    show c alegria at left_side
    show m orgullo at right_side
    c "Mi plan es coger todo este dinero, escapar hacia la azotea y huir en mi helicóptero. ¿Te apetece salir de aquí con el bolso y sin que te pille la seguridad?"
    show m alegria at right_side
    show c orgullo at left_side
    m "Vaya, vaya… Eres un tipo listo, si nos ayudamos los dos salimos de aquí ganando…"
    jump decision_final

label tension_mani:
    show c decepcion at left_side
    show m miedo at right_side
    c "Si es ese bolso lo que quieres, lo tendrás. Solo necesito que me ayudes a escapar en el helicóptero."
    show m sorpresa at right_side
    show c orgullo at left_side
    m "¿Esto no será un truquito tuyo para dejarme a mí de anzuelo para los guardas, no?"
    jump decision_final

label tension_agre:
    show c cabreo at left_side
    c "¿¡Ese trapo mal hecho?! ¡Y tú te consideras una fashion victim? Vaya chiste…"
    show m cabreo at right_side
    m "¡Ya está bien! ¡Me he cansado de que te rías de mí!"
    jump decision_final

label decision_final:
    if agresividad >= 2:
        call final_agresivo
    elif cordialidad >= 3:
        call final_cordial
    elif manipulacion >= 2:
        call final_manipulacion

    return

label final_cordial:
    scene black
    scene bg rooftop
    show m alegria at right_side
    m "¡Vamos allá, viejo! ¡Larguémonos de aquí!"
    "VICTORIA. Melody y Cornelius agarran juntos todo el dinero de la caja fuerte, y corren hacia la azotea, donde Cornelius había dejado aparcado su helicóptero."
    "No les cuesta nada escapar, y nadie se entera de que han estado allí. Lo siguiente que sabemos de ellos es que subieron varios posts a Instagram juntos en Punta Cana."
    return

label final_manipulacion:
    scene black
    scene bg rooftop
    show m orgullo at right_side
    m "¡Ja ja ja!"
    "¿VICTORIA? Melody y Cornelius colaboran para escapar con el botín pero él estaba planeando por su cuenta el escape."
    "¡Efectivamente, quería usar a Melody de chivo expiatorio! Pero Esa Diva consigue zafarse de la seguridad con su poder de Mujer Loba, arrancando el Birkin de los flácidos brazos de Cornelius y corriendo a la oscuridad mientras jura venganza."
    return

label final_agresivo:
    scene black
    scene bg rooftop
    show m cabreo at right_side
    m "¡Por supuesto! ¡Que gane el mejor ladrón!"
    "DERROTA. Melody y Cornelius se enzarzan en una pelea digna de película de Marvel."
    "Sin embargo, hacen demasiado ruido, alarmando a los vecinos, que no dudan en llamar a la policía."
    "La policía no tarda en llegar, y ambos quedan detenidos. Además, ahora son archienemigos"
    return