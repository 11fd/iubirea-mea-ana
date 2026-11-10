# iubire.py
import streamlit as st
import random
from datetime import datetime

st.set_page_config(
    page_title="Te iubesc, Ana ♥",
    page_icon="🎀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ====================== ADMIN PANEL ======================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

with st.sidebar:
    st.markdown("### 🔐 Admin Panel")

    if not st.session_state.authenticated:
        parola = st.text_input("Parolă:", type="password")
        if st.button("Intră"):
            if parola == "ana2026":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Parolă greșită")
    else:
        st.success("Ești logat ca admin")

        st.markdown("---")
        st.markdown("**Setări aspect**")

        bg_color = st.color_picker("Culoare background", "#000000")
        text_color = st.color_picker("Culoare text", "#e1bee7")
        accent_color = st.color_picker("Culoare accent (mov)", "#ce93d8")

        font_choice = st.selectbox(
            "Font",
            ["Pacifico + Quicksand", "Dancing Script + Quicksand", "Great Vibes + Quicksand"]
        )

        if st.button("Salvează setările"):
            st.session_state.bg_color = bg_color
            st.session_state.text_color = text_color
            st.session_state.accent_color = accent_color
            st.session_state.font_choice = font_choice
            st.success("Setări salvate!")
            st.rerun()

        if st.button("Delogare"):
            st.session_state.authenticated = False
            st.rerun()

# Setări default
bg = st.session_state.get("bg_color", "#000000")
text_col = st.session_state.get("text_color", "#e1bee7")
accent = st.session_state.get("accent_color", "#ce93d8")
font = st.session_state.get("font_choice", "Pacifico + Quicksand")

if font == "Pacifico + Quicksand":
    font_title = "Pacifico"
    font_body = "Quicksand"
elif font == "Dancing Script + Quicksand":
    font_title = "Dancing Script"
    font_body = "Quicksand"
else:
    font_title = "Great Vibes"
    font_body = "Quicksand"

# ====================== CSS ======================
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Dancing+Script:wght@600&family=Great+Vibes&family=Quicksand:wght@400;600;700&display=swap');

    .stApp {{
        background: {bg};
        color: {text_col};
    }}

    h1 {{
        font-family: '{font_title}', cursive !important;
        color: {accent} !important;
        text-align: center;
        font-size: 3rem !important;
        text-shadow: 0 0 18px {accent}55;
        margin-bottom: 0.3rem !important;
    }}

    .subtitle {{
        text-align: center;
        color: {text_col};
        font-family: '{font_body}', sans-serif;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.8rem;
        opacity: 0.9;
    }}

    .deco {{
        text-align: center;
        font-size: 1.5rem;
        letter-spacing: 5px;
        margin: 0.8rem 0 1.8rem;
        color: {accent};
    }}

    .motiv {{
        background: #111111;
        border: 1px solid {accent}55;
        border-radius: 16px;
        padding: 14px 18px;
        margin-bottom: 10px;
        font-size: 1.05rem;
        font-family: '{font_body}', sans-serif;
        color: {text_col};
        transition: all 0.2s ease;
    }}

    .motiv:hover {{
        border-color: {accent};
        background: #1a1a1a;
        transform: translateX(6px);
    }}

    .nr {{
        color: {accent};
        font-weight: 700;
        margin-right: 8px;
    }}

    .mesaj-final {{
        background: #111111;
        border: 2px solid {accent};
        border-radius: 22px;
        padding: 32px 28px;
        margin-top: 3.5rem;
        font-family: '{font_body}', sans-serif;
        font-size: 1.15rem;
        line-height: 1.75;
        color: {text_col};
        text-align: center;
        box-shadow: 0 0 25px {accent}33;
    }}

    .mesaj-final strong {{
        color: {accent};
        font-size: 1.25rem;
    }}

    .inima {{
        font-size: 1.5rem;
        margin: 14px 0;
        letter-spacing: 4px;
    }}

    .footer {{
        text-align: center;
        margin-top: 2.8rem;
        padding: 1.2rem;
        font-family: '{font_title}', cursive;
        color: {accent};
        font-size: 1.4rem;
    }}

    .footer span {{
        display: block;
        font-family: '{font_body}', sans-serif;
        font-size: 0.95rem;
        color: {text_col};
        margin-top: 0.4rem;
        opacity: 0.8;
    }}

    #MainMenu, footer, header {{visibility: hidden;}}
</style>
""", unsafe_allow_html=True)


def genereaza_motive():
    motive_baza = [
        "zâmbetul tău care e mai dulce decât orice desert",
        "modul în care râzi și mi se umple inima",
        "ochii tăi care mă fac să uit de tot",
        "vocea ta dimineața când ești încă somnoroasă",
        "felul în care spui numele meu",
        "căldura ta când te lipești de mine",
        "modul în care mă asculți chiar și când vorbesc prostii",
        "puterea ta chiar și în zilele grele",
        "sensibilitatea ta pe care o arăți doar mie",
        "faptul că lângă tine mă simt acasă",
        "râsul tău care e cel mai frumos sunet",
        "privirea ta când crezi că nu te văd",
        "gentilețea ta față de toată lumea",
        "modul în care mă sprijini fără să te rog",
        "pasiunea ta pentru lucrurile pe care le iubești",
        "faptul că mă faci să vreau să fiu mai bun",
        "tăcerea noastră care e atât de confortabilă",
        "îmbrățișările tale care vindecă tot",
        "parfumul tău pe care îl recunosc de departe",
        "felul în care spui „te iubesc”",
        "curajul tău",
        "vulnerabilitatea pe care mi-o arăți doar mie",
        "modul în care mă faci să râd când sunt trist",
        "inteligența ta frumoasă",
        "umorul tău care e doar al tău",
        "atenția ta la detaliile mici",
        "felul în care mă aștepți",
        "modul în care mă înțelegi dintr-o privire",
        "pacea pe care o aduci în viața mea",
        "faptul că mă faci să mă simt iubit cu adevărat",
        "energia ta drăguță",
        "modul în care dansezi când crezi că nu te vede nimeni",
        "vocea ta când ești somnoroasă și pufoasă",
        "felul în care mă ții de mână",
        "gândurile tale pe care mi le împărtășești",
        "faptul că lângă tine uit de toate problemele",
        "inimă ta mare și caldă",
        "modul în care mă ajuți să fiu eu însumi",
        "toate zilele pe care le petrecem împreună",
        "nopțile în care vorbim până dimineața",
        "faptul că mă faci să mă simt important",
        "săruturile tale dulci",
        "privirea ta când ești mândră de mine",
        "răbdarea ta cu mine",
        "modul în care mă faci să visez frumos",
        "prezența ta care umple toată camera",
        "felul în care mă calmezi",
        "zâmbetul tău când ești timidă",
        "faptul că lângă tine mă simt în siguranță",
        "toate momentele mici pe care le creăm împreună",
        "modul în care îmi completezi zilele",
        "faptul că ești tu",
        "faptul că vreau să fiu lângă tine mereu",
        "toate „te iubesc” pe care ți le spun și tot nu sunt suficiente",
        "faptul că tu ești casa mea",
    ]

    templateuri = [
        "Te iubesc pentru {}",
        "Te iubesc pentru că {}",
        "Un motiv e {}",
        "Pur și simplu pentru {}",
        "Pentru că există {}",
        "Pentru că îmi place atât de mult {}",
        "Pentru că mă faci să simt {}",
        "Pentru că ești {}",
    ]

    extra = [
        "modul în care existăi",
        "felul tău de a fi",
        "toate zilele în care ești tu",
        "faptul că ești Ana",
        "că ești exact cine ești",
        "că m-ai lăsat să te iubesc",
        "că ești acasă pentru mine",
        "că ești persoana mea preferată",
        "că ești motivul pentru care zâmbesc",
        "că ești tot ce am nevoie",
        "că ești Hello Kitty-ul meu preferat",
        "că ești Kuromi-ul meu drăguț",
        "că ești combinația perfectă de dulce și puțin obraznică",
    ]

    motive = []
    for m in motive_baza:
        for t in templateuri[:3]:
            motive.append(t.format(m))
            if len(motive) >= 1000:
                return motive[:1000]

    while len(motive) < 1000:
        baza = random.choice(motive_baza + extra)
        templ = random.choice(templateuri)
        motiv = templ.format(baza)
        if motiv not in motive:
            motive.append(motiv)
        else:
            motive.append(f"Te iubesc pentru că ești motivul {len(motive) + 1} din viața mea – {baza}")

    return motive[:1000]


# ====================== MUZICA ======================
st.markdown("""
<div style="text-align:center; margin-bottom: 25px;">
    <p style="color:#ce93d8; font-family:Quicksand; font-size:0.95rem; margin-bottom:8px;">
        🎵 now playing: <b>mistake</b> — lots of hands
    </p>
    <iframe width="100%" height="80" 
        src="https://www.youtube.com/embed/nteSvRttwck?autoplay=1&loop=1&playlist=nteSvRttwck" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>
    </iframe>
</div>
""", unsafe_allow_html=True)

# ====================== PAGINA ======================

st.markdown("<h1>Te iubesc, Ana</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">1000 de motive de ce te iubesc pe tine</p>', unsafe_allow_html=True)

st.markdown("""
<div class="deco">
    🎀🖤 🩷 🖤🎀 🩷 🖤🎀 🩷 🖤🎀
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="text-align:center; font-size:1.15rem; color:{accent}; margin-bottom:1.8rem; font-family:'{font_body}'; font-weight:600;">
    🎀 Forever Hello Kitty & Kuromi 🖤
</div>
""", unsafe_allow_html=True)

motive = genereaza_motive()

for i, motiv in enumerate(motive, 1):
    emoji = "🎀" if i % 2 == 0 else "🖤"
    st.markdown(
        f'<div class="motiv"><span class="nr">{i}.</span> {emoji} {motiv}</div>',
        unsafe_allow_html=True
    )

# ===== MESAJ FINAL =====
st.markdown(f"""
<div class="mesaj-final">
    <div class="inima">🩷 🖤 🎀 🖤 🩷</div>

    Dragostea mea, știu că uneori sunt mai rău cu tine și mai sec,<br>
    dar asta nu înseamnă că nu mi-aș da și viața pentru tine.<br><br>

    De când ne știm, mereu am simțit ceva pentru tine<br>
    și mereu voi simți.<br>
    Nu contează ziua, săptămâna, luna și anul.<br><br>

    Ești și mereu vei fi iubita mea,<br>
    și la moarte te voi păstra în suflet.<br><br>

    <strong>Te iubesc mult, mult de tot.</strong>

    <div class="inima">🎀 🖤 🩷 🖤 🎀</div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="footer">
    Pentru totdeauna a ta
    <span>{datetime.now().strftime("%d.%m.%Y")}</span>
</div>
""", unsafe_allow_html=True)