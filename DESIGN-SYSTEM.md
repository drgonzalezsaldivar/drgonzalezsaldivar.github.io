# Design System — Dr. González Saldívar / CorpOs Consultorio Articular

> Referencia para mantener coherencia visual en todas las páginas HTML del sitio.
> Fuente: Brandbook Whitecoat + implementación `index-v2.html`.

---

## Paleta de colores (Brandbook oficial)

```css
/* ── Primario — Fuerza Muscular ── */
--navy:    #597288;   /* bg secciones oscuras, nav CTA, badges */
--navy2:   #3D5264;   /* hover estados, tonos más oscuros */
--blue:    #4A6880;   /* uso intermedio */

/* ── Acento cálido — Madera Rehabilitadora ── */
--gold:    #C6A586;   /* eyebrows (s-tag), dividers, borders acento, contadores */
--gold-l:  #B89070;
--gold-xl: #7DBACC;   /* Azul Terapéutico — links hover, iconos, badges secundarios */

/* ── Fondos — Niebla Clínica ── */
--cream:   #F0F2F2;   /* fondo principal */
--cream2:  #E3EAED;   /* fondo alternado (why, cards) */
--cream3:  #D5E0E4;   /* fondo terciario / hover */
--border:  #C9D3D4;   /* Gris Cirujano — todos los bordes */

/* ── Texto ── */
--dark:    #1A2630;   /* texto principal */
--gray:    #6B7E8A;   /* texto secundario */
--gray2:   #4A5F6B;   /* texto terciario */

/* ── Funcional ── */
--green:   #25D366;   /* WhatsApp */
--white:   #FFFFFF;
```

**Reglas de uso:**
- `--navy` (#597288) como fondo de secciones hero/counters/servicios/contacto
- `--gold` (#C6A586) para eyebrows, counters, acentos cálidos
- `--gold-xl` (#7DBACC) para links hover, badges secundarios, iconos
- `--cream` (#F0F2F2) fondo por defecto — nunca usar `#fff` puro como bg de página
- Sombras siempre warm-tinted: `rgba(26,38,48,...)` (nunca `rgba(0,0,0,...)`)

---

## Tipografía

```css
--FD: 'Poppins', system-ui, sans-serif;   /* headings H1–H3, counters, eyebrows */
--FB: 'Source Sans 3', system-ui, sans-serif; /* body, párrafos, labels */
```

**Jerarquía:**

| Elemento       | Font       | Size                      | Weight | Letter-spacing |
|---------------|------------|---------------------------|--------|----------------|
| H1 hero       | Poppins    | clamp(2.4rem,4vw,4.2rem)  | 700    | -.03em         |
| H2 section    | Poppins    | clamp(1.85rem,3.2vw,3rem) | 700    | -.02em         |
| H3 card       | Poppins    | 1.1rem                    | 500    | 0              |
| Eyebrow/s-tag | Poppins    | .68rem                    | 600    | .10em, uppercase |
| Body párrafo  | Source Sans| .9rem                     | 400    | 0              |
| Label/caption | Source Sans| .7rem                     | 500–600| .08–.18em      |
| Counter num   | Poppins    | clamp(3rem,5vw,4.8rem)    | 700    | -.04em         |

**Google Fonts URL:**
```html
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet"/>
```

---

## Espaciado

```css
/* Secciones */
.section { padding: 7rem 5vw; }           /* desktop */
/* mobile @960px */ .section { padding: 3.5rem 1.2rem; }

/* Border radius */
--r-sm: 10px;
--r-md: 16px;
--r-lg: 20px;
--r-xl: 28px;
```

---

## Sombras

```css
--sh1: 0 24px 64px rgba(26,38,48,.11);   /* cards elevadas */
--sh2: 0 8px 32px rgba(26,38,48,.08);    /* cards normales */
--sh3: 0 2px 14px rgba(26,38,48,.05);    /* sutil */
```

---

## Motion / Easing

```css
--spring: cubic-bezier(0.32, 0.72, 0, 1);         /* hover, draws */
--expo:   cubic-bezier(0.19, 1.0, 0.22, 1.0);     /* reveals de entrada */
--soft:   cubic-bezier(0.25, 0, 0, 1);             /* transiciones suaves */
```

**Reglas:**
- Nunca `linear` ni `ease-in-out`
- Entry animations: `opacity 0→1` + `translateY(16–40px)→0`, duración 800–1400ms
- Hover: `transform: translateY(-2px)` o `scale(1.06)`, 250–350ms
- No animar `width`, `height`, `top`, `left` — solo `transform` y `opacity`

---

## Componentes

### Nav — floating island pill

```css
position: fixed; top: .85rem; left: 50%; transform: translateX(-50%);
width: min(1120px, calc(100vw - 1.4rem));
padding: .55rem .9rem .55rem 1.3rem;
background: rgba(240,242,242,.94); backdrop-filter: blur(24px);
border-radius: 50px; border: 1px solid rgba(198,165,134,.16);
box-shadow: 0 4px 32px rgba(26,38,48,.10), inset 0 1px 0 rgba(255,255,255,.65);
```

- Logo: `height: 44px`
- Links: Poppins 500, `.77rem`, color `var(--gray)` → hover `var(--navy)`
- CTA "Agendar": bg `var(--navy)`, pill `border-radius: 50px`
- "Segunda Opinión": outline pill, color + border `var(--gold)`

### s-tag (eyebrow)

```html
<p class="s-tag">Texto del eyebrow</p>
```

```css
font-family: var(--FD); font-size: .68rem; font-weight: 600;
color: var(--gold); letter-spacing: .10em; text-transform: uppercase;
display: inline-flex; align-items: center; gap: .45rem; margin-bottom: 1rem;
/* dot */ ::before { width:5px; height:5px; border-radius:50%; background:var(--gold); opacity:.7; }
```

### Botón WhatsApp primario

```css
background: var(--green); color: white; border-radius: 50px;
padding: .82rem 1.5rem; font-weight: 700; font-size: .82rem;
box-shadow: 0 8px 28px rgba(37,211,102,.28);
transition: transform 350ms var(--spring), box-shadow 350ms;
```

### Cards de servicio

- Fondo: `rgba(255,255,255,.04)` sobre `--navy`
- Border: `rgba(255,255,255,.07)`
- Hover: `translateY(-5px)` + top bar `scaleX(0→1)` gold gradient
- Featured card: `border-color: rgba(198,165,134,.45)`, spans 2 rows

### FAQ accordion

```css
/* Icon: círculo con + que rota a × en .open */
.faq-icon { width:26px; height:26px; border-radius:50%; }
.faq-item.open .faq-icon { background:var(--navy); }
.faq-item.open .faq-icon::after { transform: rotate(90deg); opacity:0; }
```

JS: usar `item.classList.toggle('open')` — NO manipular `icon.style.transform` inline.

### Counters

```css
font-family: var(--FD); font-size: clamp(3rem,5vw,4.8rem);
font-weight: 700; color: var(--gold); letter-spacing: -.04em;
```

Divisores hairline verticales: `::after { width:1px; background:rgba(255,255,255,.08); }`

---

## Isotipo animado

- Archivo: `Gonzalez Saldivar Icono 2.svg` — usar en fondos oscuros (`--navy`)
- Archivo: `Gonzalez Saldivar Icono Negativo.svg` — alternativa gris/blanco
- Archivo: `Gonzalez Saldivar Icono Positivo.svg` — usar en fondos claros (`--cream`)
- **NO** usar `Icono 1.svg` sobre fondos `--navy` (#597288): fills idénticos, invisible

**Colores por archivo:**

| Archivo          | Fills                              | Usar sobre        |
|-----------------|-------------------------------------|-------------------|
| Icono 1          | #597288, #C6A586, #7DBACC          | Fondo claro       |
| Icono 2          | #C6A586, #F0F2F2, #7DBACC          | Fondo oscuro/acero|
| Icono Negativo   | #D0D4D6, #A5ACB0, #F5F7F8          | Fondos muy oscuros|
| Icono Positivo   | #404040, #6E6E6E, negro            | Fondo blanco/claro|

**Animación:**

```css
@keyframes isotipoReveal { from { opacity:0; transform:translateY(40px) scale(.92); } to { opacity:1; transform:translateY(0) scale(1); } }
@keyframes isotipoFloat  { 0%,100% { transform:translateY(0); } 50% { transform:translateY(-10px); } }
/* Paths individuales: .hero-isotipo-path con animation-delay escalonado */
```

---

## Placeholders — assets pendientes

Cuando un asset no existe todavía, usar el patrón:

```html
<div class="photo-placeholder">
  <!-- icono SVG relevante -->
  <div class="photo-placeholder-label">
    <strong>Pendiente</strong>
    <span>Descripción del asset requerido</span>
  </div>
</div>
```

```css
.photo-placeholder {
  border: 2px dashed var(--border); border-radius: var(--r-xl);
  background: var(--cream2); display: flex; flex-direction: column;
  align-items: center; justify-content: center; gap: .75rem; color: var(--gray);
}
```

**Assets pendientes actuales (index-v2.html):**
- Foto Dr. González Saldívar — sección Sobre mí (portrait 4:5)
- Foto consultorio CorpOs — strip panorámico 21:6
- Logos de hospitales — 4 slots (pendientes de autorización)

---

## Grain texture

```css
body::before {
  content: ''; position: fixed; inset: 0; z-index: 9998; pointer-events: none;
  opacity: 0.028;
  background-image: url("data:image/svg+xml,...fractalNoise...");
  background-size: 400px;
}
```

Aplica a todas las páginas. No remover.

---

## Logos — archivos disponibles

```
Identidad Visual JC/Logos/SVGs/
├── Gonzalez Saldivar Logo Positivo.svg   ← nav en fondos claros
├── Gonzalez Saldivar Logo Negativo.svg   ← nav en fondos oscuros / footer
├── Gonzalez Saldivar Logo 1.svg
├── Gonzalez Saldivar Logo 2.svg
├── Gonzalez Saldivar Icono 1.svg         ← NO usar en fondos #597288
├── Gonzalez Saldivar Icono 2.svg         ← héroe (fondo acero)
├── Gonzalez Saldivar Icono Negativo.svg
└── Gonzalez Saldivar Icono Positivo.svg

img/gonzalez-saldivar-logo.svg            ← ruta usada en nav actual
```

---

## SEO / Tracking — NO tocar

- Meta tags, `<title>`, `<meta name="description">`
- Schema JSON-LD (`Physician`, `FAQPage`)
- Google Tag Manager (`GTM-PGBS76ZX`)
- Meta Pixel (`891313025762477`)
- `rel="canonical"`, Open Graph, Twitter Card
- Todos los `href` / `src` de páginas y anchors

---

## Responsive breakpoints

| Breakpoint     | Comportamiento clave                              |
|---------------|---------------------------------------------------|
| `≤ 960px`     | Nav colapsa a hamburger, hero 1 col, isotipo hidden |
| `≤ 640px`     | Blog cards 1 col, hospital grid 2 cols            |
| `≤ 480px`     | Hero H1 1.95rem, hero-btns full-width column      |

---

## Convenciones de código

- **Sin jQuery** — vanilla JS puro
- `IntersectionObserver` para scroll reveals (no `window.addEventListener('scroll')`)
- Clases `.reveal` + `.visible` para entry animations
- FAQ: `item.classList.add/remove('open')` — no inline styles en JS
- Counters: `data-target` attribute + `IntersectionObserver` para trigger
- Imágenes: `<picture>` con `<source srcset=".webp">` + `<img src=".jpg">` fallback
- Siempre `loading="lazy"` excepto el carousel hero (above-the-fold)
- `width` y `height` explícitos en todas las imágenes (previene CLS)
