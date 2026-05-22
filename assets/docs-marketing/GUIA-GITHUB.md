# Guía: Cómo subir el sitio a GitHub Pages

---

## Requisitos previos (una sola vez)

1. Tener una cuenta en [github.com](https://github.com)
2. Tener Git instalado en tu Mac ([descargar aquí](https://git-scm.com/download/mac))
3. Tener acceso al panel de tu dominio (donde compraste drgonzalezsaldivar.com)

---

## Paso 1 — Crear el repositorio en GitHub

1. Entra a github.com → clic en **"New repository"** (botón verde)
2. Nombre del repo: `web-jc-seo` (o el que prefieras, sin espacios)
3. Visibilidad: **Public** (necesario para GitHub Pages gratuito)
4. **No** marques "Add README" ni "Add .gitignore" — ya los tienes
5. Clic en **"Create repository"**
6. Copia la URL que aparece, se ve así:
   `https://github.com/TU-USUARIO/web-jc-seo.git`

---

## Paso 2 — Subir la carpeta completa

Abre **Terminal** en tu Mac y ejecuta estos comandos uno por uno:

```bash
# 1. Entrar a la carpeta del sitio
cd "/Users/jcgzz/Documents/CLAUDE CODE/web jc seo final"

# 2. Inicializar git (solo la primera vez)
git init

# 3. Conectar con GitHub (usa tu URL del paso 1)
git remote add origin https://github.com/TU-USUARIO/web-jc-seo.git

# 4. Agregar todos los archivos
git add .

# 5. Primer commit
git commit -m "Lanzamiento inicial del sitio"

# 6. Subir a GitHub
git push -u origin main
```

> Si pide usuario y contraseña, usa tu usuario de GitHub y un **Personal Access Token**
> (no tu contraseña normal). Se genera en: GitHub → Settings → Developer settings → Tokens

---

## Paso 3 — Activar GitHub Pages

1. Ve a tu repositorio en GitHub
2. Clic en **Settings** (pestaña arriba a la derecha)
3. En el menú izquierdo: **Pages**
4. En "Source": selecciona **"Deploy from a branch"**
5. Branch: **main** / Folder: **/ (root)**
6. Clic en **Save**
7. En ~2 minutos aparece el link: `https://tu-usuario.github.io/web-jc-seo`

---

## Paso 4 — Conectar tu dominio (drgonzalezsaldivar.com)

### En GitHub:
1. En Settings → Pages → "Custom domain"
2. Escribe: `drgonzalezsaldivar.com`
3. Clic en **Save** → GitHub valida automáticamente
4. Activa **"Enforce HTTPS"** (aparece después de unos minutos)

### En tu proveedor de dominio (GoDaddy, Namecheap, etc.):
Agrega estos registros DNS:

| Tipo | Nombre | Valor |
|------|--------|-------|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | tu-usuario.github.io |

> Los cambios DNS pueden tardar entre 30 minutos y 24 horas en propagarse.

---

## Actualizaciones futuras (cada vez que hagas cambios)

```bash
cd "/Users/jcgzz/Documents/CLAUDE CODE/web jc seo final"

git add .
git commit -m "descripción del cambio, ej: agrego foto del doctor"
git push
```

GitHub Pages se actualiza automáticamente en ~1 minuto.

---

## Qué se sube vs. qué no se sube

### ✅ Se sube todo (incluyendo `assets/`)
La carpeta `assets/` contiene los documentos de estrategia y logos fuente. Se sube porque:
- GitHub es privado o los PDFs no son sensibles
- Sirve como respaldo en la nube

### ❌ Si quieres excluir `assets/` del sitio público:
El archivo `.gitignore` ya existe. Ábrelo y agrega:
```
assets/docs-marketing/
```
Esto los excluye del repositorio pero los conserva en tu computadora.

---

## Orden de carpetas en el repo (referencia)

```
/ (raíz)
├── index.html          ← Página principal — SE SUBE PRIMERO
├── favicon.svg
├── sitemap.xml
├── robots.txt
├── CNAME               ← CRÍTICO para el dominio — no borrar
├── .nojekyll           ← CRÍTICO para GitHub Pages — no borrar
├── *.html              ← Todas las páginas de padecimientos
├── img/                ← Todas las imágenes del sitio
├── blog/               ← Posts del blog
├── lp/                 ← Landing pages de anuncios
└── assets/             ← Documentos y logos fuente
```

---

## Resolución de problemas comunes

| Problema | Solución |
|---|---|
| El sitio muestra "404" | Esperar 5 min o verificar que GitHub Pages esté activado en Settings |
| Las imágenes no cargan | Verificar que los paths no tengan `/img/` con barra al inicio |
| El dominio no conecta | Revisar registros DNS — puede tardar hasta 24h |
| El favicon no aparece | Limpiar caché del navegador (Cmd+Shift+R en Mac) |
| Cambios no aparecen | Hacer `git push` y esperar 1-2 min |

---

## Dónde subir las fotos de la sesión fotográfica

Una vez que tengas las fotos:

1. **Formato recomendado:** WebP (mejor calidad/peso) + JPG como fallback
2. **Tamaño recomendado:** 800×600px para fotos de sección, 400×520px para foto de perfil (3:4)
3. **Nombre de archivo:** `dr-gonzalez-saldivar.webp` para la foto principal del doctor
4. **Dónde guardar:** en la carpeta `img/` de la raíz del sitio
5. **Cómo activarla:** cada página tiene el bloque comentado:
   ```html
   <!-- Descomentar esto y eliminar el placeholder: -->
   <!-- <img src="img/dr-gonzalez-saldivar.webp" ...> -->
   ```
   Solo hay que quitar los comentarios `<!-- -->` y borrar el div placeholder

6. **Subirla a GitHub:** igual que cualquier cambio: `git add . → git commit → git push`
