#!/usr/bin/env python
import streamlit as st
import google.generativeai as genai

from llama_index.core import PromptTemplate
import pandas as pd



st.set_page_config("Prompt Engineering",layout="wide")

@st.dialog("API Key")
def apikey_dialog():
    st.write("Por favor introduce tu API Key de Gemini")
    st.caption("Si no tienes una API Key, puedes obtenerla en [Gemini](https://ai.google.dev/)")
    api_key = st.text_input("API Key")
    submit = st.button("Guardar",use_container_width=True)
    if submit:
        st.session_state.apikey = api_key
        st.toast("API Key guardada con éxito")
        st.rerun()

        

if "apikey" not in st.session_state:
    st.session_state.apikey = None

try:
    genai.configure(api_key=st.secrets["GEMINI_API_K"])
except KeyError:
    apikey_dialog()  
    if not st.session_state.apikey:
        st.stop()
    genai.configure(api_key=st.session_state.apikey)
except Exception as e:
    st.error(f"Error: {e}")
    st.stop()

data = {
"edad_promedio":	    r"42 años (aproximadamente, con un 55% entre 35 y 50 años y 30% entre 50 y 65 años)",
"distribucion_genero":	r"60% hombres, 40% mujeres",
"ubicacion_geografica": "Áreas suburbanas y rurales cercanas al estadio",
"nivel_educativo":	    "Varía, pero incluye profesionales con educación universitaria, principalmente en sectores estables como manufactura, servicios y educación.",
"ingresos_promedio":    "Entre $50,000 y $80,000 anuales",
"ocupaciones_predominantes":	"Profesionales en manufactura, servicios y educación",
"poder_adquisitivo":	"Fuerte poder adquisitivo; invierten en entradas de temporada y productos oficiales",
"medios_preferidos":	"Periódicos, radio y televisión",
"frecuencia_consumo":	"Consumo regular, con una preferencia por las actualizaciones a través de medios tradicionales",
"tipo_contenido":	    "Noticias deportivas, reportes de juegos, programas de análisis y cobertura de eventos locales",
"intereses_deportivos":	"Béisbol, fútbol americano y baloncesto  ",
"participacion_eventos":"Alta participación en eventos comunitarios y actividades deportivas locales",
"interaccion_redes":	"Uso limitado de tecnología; prefieren interacciones cara a cara, aunque algunos usan Facebook y Twitter para seguir noticias del equipo",
}


data2 = {
"edad_promedio":	"26 años (con un 40% entre 18 y 25 años y 35% entre 26 y 35 años)",
"distribucion_genero":	"50% hombres, 50% mujeres",
"ubicacion_geografica":	"Áreas urbanas y suburbanas cercanas a universidades y zonas metropolitanas",
"nivel_educativo":	"60% con estudios universitarios (en curso o finalizados); 20% con educación secundaria",
"ingresos_promedio":	"Entre $30,000 y $55,000 anuales",
"ocupaciones_predominantes":	"Trabajadores jóvenes en tecnología, retail, marketing y estudiantes universitarios",
"poder_adquisitivo":	"Limitado, con gasto en experiencias digitales, merchandising en línea y eventos especiales en el estadio",
"medios_preferidos":	"Redes sociales como Instagram, TikTok y Twitter",
"frecuencia_consumo":	"Alto consumo de contenido en tiempo real y plataformas digitales",
"tipo_contenido":	"Contenido multimedia relacionado con el equipo, cultura pop y entretenimiento",
"intereses_deportivos":	"Béisbol, deportes emergentes como fútbol y eSports, además de cultura pop y música",
"participacion_eventos":	"Prefieren eventos innovadores e interactivas como meet-and-greets con jugadores y activaciones de marca en redes sociales",
"interaccion_redes":	"Altamente dependientes de la tecnología, prefiriendo experiencias digitales e interactivas",
}



enero = {
    "mes": "Enero",
    "acciones_desarrollo": "Anuncio de inicio de temporada en periódicos locales",
    "tipo_mensajes": "La tradición continúa: Apoya a los Osos este año en el estadio.",
    "medios_comunicacion": "Periódicos, Radio",
    "audiencia_objetivo": "Tradicional"
}

febrero = {
    "mes": "Febrero",
    "acciones_desarrollo": "Publicidad en radio y TV sobre la venta de boletos",
    "tipo_mensajes": "Asegura tus boletos para una temporada inolvidable.",
    "medios_comunicacion": "Radio, TV local",
    "audiencia_objetivo": "Tradicional"
}

marzo = {
    "mes": "Marzo",
    "acciones_desarrollo": "Anuncio en periódicos sobre eventos familiares en el estadio",
    "tipo_mensajes": "Disfruta de un día en familia con los Osos de Montana.",
    "medios_comunicacion": "Periódicos, Radio",
    "audiencia_objetivo": "Tradicional"
}

abril = {
    "mes": "Abril",
    "acciones_desarrollo": "Anuncios en TV y radio sobre promociones familiares",
    "tipo_mensajes": "Diversión para toda la familia en el estadio de los Osos.",
    "medios_comunicacion": "TV local, Radio",
    "audiencia_objetivo": "Tradicional"
}

mayo = {
    "mes": "Mayo",
    "acciones_desarrollo": "Publicidad en revistas locales sobre la historia del equipo",
    "tipo_mensajes": "Los Osos de Montana: Una tradición que perdura.",
    "medios_comunicacion": "Revistas locales, Radio",
    "audiencia_objetivo": "Tradicional"
}

junio = {
    "mes": "Junio",
    "acciones_desarrollo": "Campaña en TV sobre eventos y actividades locales",
    "tipo_mensajes": "Sigue a los Osos durante todo el verano con actividades para todos.",
    "medios_comunicacion": "TV local, Periódicos",
    "audiencia_objetivo": "Tradicional"
}

julio = {
    "mes": "Julio",
    "acciones_desarrollo": "Publicidad en radio sobre eventos familiares durante el verano",
    "tipo_mensajes": "Este verano, vive el béisbol en familia con los Osos.",
    "medios_comunicacion": "Radio, Periódicos",
    "audiencia_objetivo": "Tradicional"
}

agosto = {
    "mes": "Agosto",
    "acciones_desarrollo": "Anuncios en radio sobre torneos locales organizados por el club",
    "tipo_mensajes": "Participa en los torneos de verano organizados por los Osos.",
    "medios_comunicacion": "Radio local, TV",
    "audiencia_objetivo": "Tradicional"
}

septiembre = {
    "mes": "Septiembre",
    "acciones_desarrollo": "Promociones en periódicos sobre eventos de cierre de temporada",
    "tipo_mensajes": "No te pierdas el final de temporada con los Osos de Montana.",
    "medios_comunicacion": "Periódicos, Radio",
    "audiencia_objetivo": "Tradicional"
}

octubre = {
    "mes": "Octubre",
    "acciones_desarrollo": "Publicidad en revistas sobre la historia y legado del equipo",
    "tipo_mensajes": "Los Osos de Montana: Leyendas en el campo.",
    "medios_comunicacion": "Revistas locales, Radio",
    "audiencia_objetivo": "Tradicional"
}

noviembre = {
    "mes": "Noviembre",
    "acciones_desarrollo": "Publicidad en TV y radio sobre las promociones de merchandising",
    "tipo_mensajes": "Prepara tus regalos de fin de año con los productos oficiales de los Osos.",
    "medios_comunicacion": "TV local, Radio",
    "audiencia_objetivo": "Tradicional"
}

diciembre = {
    "mes": "Diciembre",
    "acciones_desarrollo": "Anuncios en periódicos y TV sobre eventos navideños",
    "tipo_mensajes": "Celebra la Navidad con los Osos en nuestro evento familiar especial.",
    "medios_comunicacion": "Periódicos, TV local",
    "audiencia_objetivo": "Tradicional"
}

prompt = """
Actúa como un experto en análisis de audiencias deportivas, especializado en identificar y describir las características de las audiencias mayores que consumen medios de información tradicionales.
Realiza un análisis detallado de las características de la audiencia asociada a la visión tradicional, enfocándote en sus hábitos de consumo de medios, preferencias y comportamientos.
Datos a Considerar:
1.	Características Demográficas:
    Edad promedio: {edad_promedio}
    Género: {distribucion_genero}
    Ubicación geográfica: {ubicacion_geografica}
    Nivel educativo: {nivel_educativo}
2.	Características Económicas:
    Ingresos promedio: {ingresos_promedio}
    Ocupaciones predominantes: {ocupaciones_predominantes}
    Poder adquisitivo: {poder_adquisitivo}
3.	Hábitos de Consumo de Medios:
    Medios preferidos: {medios_preferidos} (ej. periódicos, radio, televisión)
    Frecuencia de consumo: {frecuencia_consumo}
    Tipo de contenido consumido: {tipo_contenido}
4.	Intereses y Comportamientos:
    Intereses deportivos: {intereses_deportivos}
    Participación en actividades comunitarias: {participacion_eventos}
    Uso de tecnología: {interaccion_redes}
"""

prompt2 = """
Actúa como un experto en análisis de audiencias deportivas, especializado en identificar y describir las características de las audiencias jóvenes que consumen medios digitales.
Realiza un análisis detallado de las características de la audiencia asociada a la visión moderna, enfocándote en sus hábitos de consumo de medios digitales, preferencias y comportamientos.
Datos a Considerar:
1.	Características Demográficas:
    Edad promedio: {edad_promedio}
    Género: {distribucion_genero}
    Ubicación geográfica: {ubicacion_geografica}
    Nivel educativo: {nivel_educativo}
2.	Características Económicas:
    Ingresos promedio: {ingresos_promedio}
    Ocupaciones predominantes: {ocupaciones_predominantes}
    Poder adquisitivo: {poder_adquisitivo}
3.	Hábitos de Consumo de Medios:
    Plataformas preferidas: {medios_preferidos} (ej. TikTok, Instagram, YouTube)
    Frecuencia de consumo: {frecuencia_consumo}
    Tipo de contenido consumido: {tipo_contenido}
4.	Intereses y Comportamientos:
    Intereses deportivos: {intereses_deportivos}
    Participación en eventos o actividades: {participacion_eventos}
    Interacción en redes sociales: {interaccion_redes}
"""

addinfo = r"""
Las audiencias mayores que consumen medios tradicionales tienen características claramente definidas en cuanto a sus preferencias y hábitos de consumo, que se vinculan a su contexto demográfico, económico y social.
Demográficas
Esta audiencia tiene una edad promedio de 42 años, con una concentración significativa de personas entre los 35 y 65 años. Predominan los hombres (60%) frente a las mujeres (40%), lo que sugiere que este grupo tradicional tiene un vínculo histórico más fuerte con los deportes, especialmente aquellos con una larga trayectoria como el béisbol y el fútbol americano. La mayoría reside en áreas suburbanas y rurales cercanas al estadio, lo que facilita su asistencia a eventos en persona.
Económicas
Con ingresos anuales entre $50,000 y $80,000, este grupo disfruta de estabilidad económica. Son profesionales que trabajan en sectores como manufactura, servicios y educación, sectores que tienden a ofrecer una base económica sólida y estable a lo largo del tiempo. Este poder adquisitivo les permite invertir en boletos de temporada y productos oficiales del equipo, demostrando una alta lealtad hacia su club deportivo y un interés en apoyar al equipo de manera sostenida.
Hábitos de Consumo de Medios
Prefieren medios de comunicación tradicionales como periódicos, radio y televisión para mantenerse al tanto de los deportes. Su consumo de medios es regular, centrándose en los horarios de noticias deportivas, reportes de juegos y programas de análisis, y suelen consumir actualizaciones a través de medios locales. La televisión sigue siendo su principal fuente de entretenimiento y de información deportiva en tiempo real, mientras que los periódicos y la radio complementan esta dieta mediática con análisis y comentarios. Este grupo también aprecia las coberturas de eventos locales que les conectan con su comunidad.
Intereses y Comportamientos
En términos de deportes, esta audiencia se interesa principalmente en el béisbol, el fútbol americano y el baloncesto. Además, suelen participar activamente en eventos comunitarios y en actividades deportivas locales, lo que refuerza su sentido de pertenencia tanto al equipo como a su entorno social. Aunque su uso de la tecnología es limitado, aquellos que la utilizan prefieren redes sociales como Facebook y Twitter, donde siguen cuentas oficiales del equipo para estar informados, aunque es más común que busquen interacciones cara a cara.
Resumen de Comportamientos y Preferencias
•	Medios preferidos: TV, radio, periódicos.
•	Frecuencia: Diaria o semanal, con preferencia por actualizaciones deportivas locales.
•	Interacciones: Prefieren encuentros en persona y la comunidad física, aunque algunos usan redes sociales de manera pasiva.
•	Lealtad: Alta, reflejada en la compra de entradas de temporada y productos oficiales.
Este análisis muestra que las audiencias mayores mantienen un fuerte lazo con sus equipos deportivos a través de canales tradicionales, participando activamente en su comunidad local y manteniendo un enfoque en medios que les permiten acceder a contenido relevante sin la necesidad de adaptarse a las nuevas tecnologías.
"""

addinfo2 = r"""
La audiencia joven, con una edad promedio de 26 años, está profundamente integrada en el ecosistema digital, lo que define sus hábitos de consumo y preferencias. Aquí te ofrezco un análisis detallado:
1. Características Demográficas
•	Edad: Predominan los jóvenes de entre 18 y 35 años, con un fuerte núcleo en el rango de 18 a 25 años.
•	Género: Existe una paridad de género notable, con un 50% de hombres y 50% de mujeres, lo que subraya la importancia de generar contenido inclusivo.
•	Ubicación: Tienden a vivir en áreas urbanas y suburbanas, cercanas a universidades y zonas metropolitanas, lo que facilita su acceso a eventos y actividades de carácter local o regional.
•	Nivel educativo: La mayoría está en proceso o ha completado estudios universitarios, reflejando una audiencia educada con acceso a múltiples fuentes de información.
2. Características Económicas
•	Ingresos: Los ingresos de este grupo varían entre $30,000 y $55,000 anuales, lo que limita su capacidad de gasto en bienes de lujo, pero no en experiencias digitales y eventos relacionados con el entretenimiento y los deportes.
•	Ocupaciones: Jóvenes trabajadores en sectores como tecnología, retail, marketing, además de estudiantes universitarios, lo que influye en sus horarios de consumo de medios, frecuentemente orientados a momentos de pausa o fuera del horario laboral.
•	Gasto: Prefieren gastar en experiencias, tanto digitales como en vivo. Esto incluye merchandising en línea, eventos en el estadio o actividades exclusivas.
3. Hábitos de Consumo de Medios Digitales
•	Plataformas preferidas: Instagram, TikTok, YouTube y Twitter son las plataformas de elección. TikTok es fundamental para la viralización de contenido breve y creativo, mientras que Instagram destaca por su enfoque en imágenes y videos atractivos.
•	Frecuencia de consumo: Son consumidores de contenido en tiempo real, siempre conectados y buscando estar al tanto de las últimas tendencias, ya sea a través de transmisiones en vivo, stories o publicaciones de alta frecuencia.
•	Tipo de contenido: Buscan contenido visual y multimedia, con una fuerte inclinación hacia clips cortos y llamativos, contenido detrás de cámaras, videos de entretenimiento relacionados con el equipo, entrevistas con jugadores y referencias a la cultura pop.
4. Intereses y Comportamientos
•	Deportes: Además de seguir béisbol, su interés se extiende a deportes emergentes como el fútbol y eSports, que son vistos como más accesibles y relevantes culturalmente para esta generación.
•	Participación en eventos: Prefieren eventos interactivos, como meet-and-greets con jugadores, experiencias de realidad aumentada o virtual y activaciones innovadoras en redes sociales, donde pueden interactuar directamente con sus ídolos o con la marca del equipo.
•	Interacción en redes sociales: Altamente dependientes de la tecnología, se involucran activamente en la creación y compartición de contenido. Son propensos a usar hashtags, compartir memes y participar en retos virales, lo que convierte a las redes sociales en una plataforma fundamental para su conexión con los equipos deportivos.
5. Conclusión
Esta audiencia moderna prioriza las experiencias sobre la posesión de bienes, buscando una conexión auténtica con los equipos a través de medios digitales. Su interacción en tiempo real, la inclinación hacia el contenido visual y su deseo de participar en experiencias innovadoras son clave para captar su atención y mantener su lealtad hacia el equipo. Las estrategias de marketing deben estar centradas en la creación de contenido atractivo, dinámico y participativo, aprovechando las plataformas sociales y el deseo de esta audiencia de formar parte de comunidades digitales vibrantes y activas.
"""

promptdate = """
Instrucciones:
Actúa como un experto en marketing deportivo y elabora un programa mensual para el club de béisbol Osos de Montana. El programa debe incluir acciones concretas a desarrollar durante el mes del año proporcionado, así como los mensajes que se comunicarán a las audiencias a través de los medios de comunicación.
Contexto:
El objetivo es crear un programa de posicionamiento que fortalezca la presencia del club en la comunidad y genere un mayor engagement con las audiencias. Los mensajes deben ser positivos y alinearse con la imagen del equipo y su mascota, Monty.
Tareas:
1. Diseñar un programa mensual que incluya las acciones a desarrollar, el tipo de mensajes y los medios de comunicación adecuados para cada tipo de audiencia.
2. Asegúrate de que los mensajes no toquen temas que el club no quiere mencionar, como comparaciones con otros deportes o la falta de campeonatos recientes.
3. Todos los anuncios deben estar relacionados con la mascota del equipo, Monty.
4. Identifica los medios que son frecuentados por cada tipo de audiencia, considerando las características sociodemográficas de la audiencia.
Datos a Incluir:
- Mes: {mes}
- Acciones a Desarrollar: {acciones_desarrollo}
- Tipo de Mensajes: {tipo_mensajes}
- Medios de Comunicación: {medios_comunicacion}
- Audiencia Objetivo: {audiencia_objetivo}
Ejemplo de Respuesta:
- Mes: Enero
- Acciones a Desarrollar: Lanzamiento de campaña en redes sociales.
- Tipo de Mensajes: "Únete a la familia de los Osos, donde la diversión nunca se detiene."
- Medios de Comunicación: Facebook, Instagram.
- Audiencia Objetivo: Audiencia Moderna.
Información Adicional:
"""

prompt_template = PromptTemplate(prompt)
prompt_template2 = PromptTemplate(prompt2)
prompt_templatedate = PromptTemplate(promptdate)


def load_model():
    model = genai.GenerativeModel("gemini-1.5-flash")
    return model




st.subheader("Las características de las audiencias asociadas a la visión tradicional y moderna")
st.write("Templates Formateados")

cols1 = st.columns(2,gap="large")
with cols1[0]:
    st.subheader("Audiencias Tradicionales")
    with st.expander("Informacion"):
        st.dataframe(pd.Series(data))
    
    with st.expander("Prompt"):
        st.write(prompt_template.format(**data))
with cols1[1]:
    st.subheader("Audiencias Modernas")
    with st.expander("Informacion"):
        st.dataframe(pd.Series(data2))
    with st.expander("Prompt"):
        st.write(prompt_template2.format(**data2))



last_table = []

meses = [enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre]
cols1[0].subheader("Estrategia anual para audiencias Tradicionales")
tabss = cols1[0].tabs(["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"])

mayoreslog =  ""
ms = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

try:
    model = load_model()
except Exception as e:
    st.stop()
for i,m in enumerate(meses):
    with tabss[i]:
        with st.expander("Prompt"):
            st.write(prompt_templatedate.format(**m))
        with st.spinner("generando contenido"):
            inst = str(prompt_templatedate.format(**m))+addinfo
            response = model.generate_content(inst)
            #uncomment to save the conversations to a file
            #with open(f"conversacion_tradicional_{i}.txt","w",encoding="utf8") as f:
            #    f.write(f"User: {inst}\nBot: {response.text}")
            mayoreslog += response.text + "\n"
            last_table.append({"mes": ms[i],"acciones": response.text})
        st.write(response.text)

df = pd.DataFrame(last_table)

cols1[0].dataframe(df,use_container_width=True)

enero = {
    "mes": "Enero",
    "acciones_desarrollo": "Lanzamiento de campaña en redes sociales",
    "tipo_mensajes": "Únete a la familia de los Osos, donde la diversión nunca se detiene.",
    "medios_comunicacion": "Instagram, TikTok",
    "audiencia_objetivo": "Moderna"
}

febrero = {
    "mes": "Febrero",
    "acciones_desarrollo": "Colaboraciones con influencers deportivos juveniles",
    "tipo_mensajes": "Experiencias exclusivas y contenido digital solo para verdaderos fans.",
    "medios_comunicacion": "YouTube, Twitch",
    "audiencia_objetivo": "Moderna"
}

marzo = {
    "mes": "Marzo",
    "acciones_desarrollo": "Sorteos de boletos en redes sociales y plataformas digitales",
    "tipo_mensajes": "Gana entradas exclusivas para ver a los Osos en vivo. ¡No te lo pierdas!",
    "medios_comunicacion": "Twitter, Instagram",
    "audiencia_objetivo": "Moderna"
}

abril = {
    "mes": "Abril",
    "acciones_desarrollo": "Campaña interactiva con desafíos en redes sociales",
    "tipo_mensajes": "Participa en nuestros desafíos para ganar mercancía oficial de los Osos.",
    "medios_comunicacion": "Instagram, TikTok",
    "audiencia_objetivo": "Moderna"
}

mayo = {
    "mes": "Mayo",
    "acciones_desarrollo": "Eventos en línea con jugadores y fans jóvenes",
    "tipo_mensajes": "Conoce a tus jugadores favoritos en nuestras sesiones en vivo.",
    "medios_comunicacion": "YouTube, Twitch",
    "audiencia_objetivo": "Moderna"
}

junio = {
    "mes": "Junio",
    "acciones_desarrollo": "Contenido multimedia exclusivo en redes sociales",
    "tipo_mensajes": "Disfruta de contenido exclusivo detrás de cámaras y en el estadio.",
    "medios_comunicacion": "Instagram, YouTube",
    "audiencia_objetivo": "Moderna"
}

julio = {
    "mes": "Julio",
    "acciones_desarrollo": "Activaciones digitales con influencers locales",
    "tipo_mensajes": "Vive la experiencia del verano con los Osos: diversión garantizada.",
    "medios_comunicacion": "TikTok, Instagram",
    "audiencia_objetivo": "Moderna"
}

agosto = {
    "mes": "Agosto",
    "acciones_desarrollo": "Colaboraciones con creadores de contenido deportivos",
    "tipo_mensajes": "Forma parte del equipo con nuestras colaboraciones especiales.",
    "medios_comunicacion": "YouTube, TikTok",
    "audiencia_objetivo": "Moderna"
}

septiembre = {
    "mes": "Septiembre",
    "acciones_desarrollo": "Sorteos digitales de entradas para los partidos finales",
    "tipo_mensajes": "Gana entradas VIP para el cierre de temporada de los Osos.",
    "medios_comunicacion": "Instagram, TikTok",
    "audiencia_objetivo": "Moderna"
}

octubre = {
    "mes": "Octubre",
    "acciones_desarrollo": "Evento en vivo en redes con resúmenes de la temporada",
    "tipo_mensajes": "Revive los mejores momentos de la temporada de los Osos en nuestras redes.",
    "medios_comunicacion": "YouTube, Instagram",
    "audiencia_objetivo": "Moderna"
}

noviembre = {
    "mes": "Noviembre",
    "acciones_desarrollo": "Campaña de fin de año con promociones exclusivas en línea",
    "tipo_mensajes": "Promociones especiales para fans online: ¡aprovecha esta oferta única!",
    "medios_comunicacion": "Instagram, Twitter",
    "audiencia_objetivo": "Moderna"
}

diciembre = {
    "mes": "Diciembre",
    "acciones_desarrollo": "Campaña digital navideña con sorteos de mercancía",
    "tipo_mensajes": "Regala la magia de los Osos esta Navidad con nuestros productos exclusivos.",
    "medios_comunicacion": "Instagram, TikTok",
    "audiencia_objetivo": "Moderna"
}

meses = [enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre]
cols1[1].subheader("Estrategia anual para audiencias Modernas")
tabss2 = cols1[1].tabs(["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"])

last_table = []
menoresslog = ""
ms = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
for i,m in enumerate(meses):
    with tabss2[i]:
        with st.expander("Prompt"):
            st.write(prompt_templatedate.format(**m))
        with st.spinner("generando contenido"):
            inst = str(prompt_templatedate.format(**m))+addinfo2
            response = model.generate_content(inst)
            #uncomment to save the conversations to a file
            #with open(f"conversacion_moderna_{i}.txt","w",encoding='utf8') as f:
            #    f.write(f"User: {inst}\nBot: {response.text}")
            menoresslog += response.text + "\n"
            last_table.append({"mes": ms[i],"acciones": response.text})
        st.write(response.text)

df = pd.DataFrame(last_table)

cols1[1].dataframe(df,use_container_width=True)

with open("mayoreslog.txt","w",encoding="utf8") as f:
    f.write(mayoreslog)

with open("menoresslog.txt","w",encoding="utf8") as f:
    f.write(menoresslog)