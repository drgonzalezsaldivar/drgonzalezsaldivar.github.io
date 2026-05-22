# Resumen de trabajo — Web Dr. González Saldívar
**Fecha:** Mayo 2026 | **Estado:** Lista para subir a GitHub

---

## ¿Qué es este sitio?

Landing page estática (HTML5/CSS3 puro) del consultorio del Dr. Juan Carlos González Saldívar, ortopedista oncólogo en Monterrey. Optimizada para conversión a WhatsApp (Jessy) y posicionamiento SEO local en zona Contry/Tec.

**Dominio:** drgonzalezsaldivar.com  
**Repo GitHub:** github.com/jcgzz/web-jc-seo (o el nombre que elijas)  
**Hosting:** GitHub Pages (gratuito, conectado por CNAME)

---

## Estructura de carpetas

```
web jc seo final/
├── index.html                      ← Página principal
├── favicon.svg                     ← Ícono del monito (listón oncología)
├── sitemap.xml
├── robots.txt
├── CNAME                           ← drgonzalezsaldivar.com
├── CLAUDE.md                       ← Instrucciones para Claude
├── .gitignore
├── .nojekyll                       ← Necesario para GitHub Pages
│
├── [páginas raíz — 16 HTMLs]
│   ├── oncologia-ortopedica.html
│   ├── tumores-oseos.html
│   ├── segunda-opinion-oncologica.html
│   ├── sarcomas.html
│   ├── metastasis-osea.html
│   ├── infiltraciones.html
│   ├── rodilla.html
│   ├── cadera.html
│   ├── hombro.html
│   ├── tobillo.html
│   ├── hernia-disco.html
│   ├── blog.html
│   ├── ortopedista-monterrey-sur.html
│   ├── ortopedista-san-pedro-garza-garcia.html
│   └── traumatologo-zona-tec.html
│
├── img/                            ← Imágenes que usa el sitio
│   ├── gonzalez-saldivar-logo.svg  ← Logo horizontal
│   ├── gonzalez-saldivar-icono.svg ← Ícono solo
│   ├── seguros/                    ← Logos aseguradoras (PNG/SVG/WebP)
│   │   ├── gnp.svg
│   │   ├── axa.svg / axa.png
│   │   ├── mapfre.webp
│   │   ├── monterrey.png
│   │   ├── bupa.svg
│   │   └── metlife.png
│   ├── asociaciones/               ← Logos sociedades médicas
│   │   ├── femecot.png
│   │   ├── isols.png               ← Logo real (no usar isols.svg)
│   │   ├── smoose.svg
│   │   └── slatme.avif             ← Logo real (no usar slatme.svg)
│   └── img_01–img_19.webp/jpg      ← Fotos clínica/procedimientos
│
├── blog/                           ← Posts del blog
│   ├── index.html
│   ├── biopsia-osea.html
│   ├── tumores-oseos-benignos-malignos.html
│   ├── reemplazo-rodilla.html
│   ├── dolor-cadera-adultos-jovenes.html
│   ├── hernia-disco.html
│   ├── lesion-resonancia.html
│   └── benigno-maligno.html
│
├── lp/                             ← Landing pages para anuncios pagados
│   ├── biopsia.html                ← Google Ads: oncología
│   ├── tumor-oseo.html             ← Google/Meta Ads: tumores
│   └── dolor-rodilla.html          ← Meta Ads: volumen
│
└── assets/                         ← Archivos fuente (NO son el sitio)
    ├── logotipo-personal/          ← SVGs originales del logo
    ├── logotipo-seguros/           ← Logos originales aseguradoras
    ├── sociedades/                 ← Logos originales sociedades
    ├── docs-marketing/             ← PDFs y documentos de estrategia
    └── index-backup.html           ← Backup del index anterior
```

---

## Tracking de rastreo (ya instalado)

| Herramienta | ID | Páginas |
|---|---|---|
| Google Tag Manager | GTM-PGBS76ZX | Todas |
| Meta Pixel | 891313025762477 | Todas |
| TikTok Pixel | (en tumor-oseo.html) | lp/tumor-oseo.html |

---

## Logos de sociedades — importante

| Sociedad | Archivo correcto | Archivo FALSO (no usar) |
|---|---|---|
| ISOLS | `img/asociaciones/isols.png` | ~~isols.svg~~ |
| SLATME | `img/asociaciones/slatme.avif` | ~~slatme.svg~~ |
| SMOOSE | `img/asociaciones/smoose.svg` | — |
| FEMECOT | `img/asociaciones/femecot.png` | — |

---

## Pendientes para próxima sesión

### Foto del doctor
- **Dónde subir:** `img/dr-gonzalez-saldivar.webp` (y `.jpg` como fallback)
- **Especificaciones:** 400×520px mínimo, relación 3:4, bata blanca, fondo neutro
- **Páginas que la usan:** todas tienen el placeholder activo, comentado en el HTML

### Reseñas reales
- Las reseñas falsas fueron eliminadas de todas las páginas
- Hay placeholders con dashed border en todas las secciones de opiniones
- **Cómo agregar:** copiar texto + nombre desde perfil de Google Business
- Páginas donde aplica: index.html, lp/tumor-oseo.html, lp/dolor-rodilla.html, y todas las de padecimientos

### Biopsia por punción — datos actualizados ✅
- Sedación + anestesia local
- Procedimiento ambulatorio ~30 min
- En quirófano bajo fluoroscopía
- Biopsia abierta marcada como "poco frecuente"

---

## Notas técnicas

- **Paths de imágenes:** raíz usa `img/...`, carpeta `lp/` usa `../img/...`
- **Favicon:** `favicon.svg` = monito con listón de oncología (no la cruz genérica)
- **Sin framework:** HTML5/CSS3 puro. Sin React, sin Node, sin build step
- **GitHub Pages:** necesita `.nojekyll` en raíz (ya existe) y CNAME con el dominio
