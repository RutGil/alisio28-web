# ALISIO28 - Web para GitHub Pages 

Paquete preparado el 23/10/2026 a partir de la web revisada, con los últimos nombres, teléfonos y selector de correo.

## Publicar desde GitHub

1. Descomprime el ZIP en tu ordenador.
2. Crea un repositorio en tu cuenta de GitHub. Puedes llamarlo `alisio28-web`. Si ya tienes un repositorio para esta web, usa ese.
3. Sube el CONTENIDO de esta carpeta a la raíz del repositorio, no la carpeta exterior ni el ZIP. `index.html` debe quedar en la primera pantalla del repositorio.
4. Incluye la carpeta `.github` con el archivo `.github/workflows/pages.yml`. Si la carga desde el navegador la omite, usa **Add file > Create new file**, escribe esa ruta completa y pega el contenido de `pages.yml`.
5. Usa `main` como rama principal. Si usas otra, cambia `branches: [main]` en el flujo.
6. En el repositorio entra en **Settings > Pages > Build and deployment > Source** y elige **GitHub Actions**.
7. En **Actions**, abre **Publicar ALISIO28 en GitHub Pages** y pulsa **Run workflow**. Si se ejecutó antes de activar Pages y falló, vuelve a ejecutarlo.
8. Al finalizar, **Settings > Pages** y el paso de despliegue mostrarán la dirección de la web. Abre esa dirección.

Con GitHub Free, Pages está disponible en repositorios públicos. Revisa la visibilidad antes de subir archivos: este paquete contiene los nombres y teléfonos comerciales que has pedido mostrar. Las condiciones dependen del plan de GitHub; consulta las fuentes al final.

## Qué incluye

- `index.html`: página principal.
- `contacto.html`: tarjeta que abre el QR, con LinkedIn, nombres, teléfonos y correo.
- `styles.css`: diseño y adaptación a móvil.
- `contact.js`: selector Gmail / Outlook / aplicación de correo.
- `assets/`: logo, matriz, fotografía, QR, favicon y tarjeta descargable para la agenda.
- `.github/workflows/pages.yml`: publicación automática.
- `scripts/build.py` y `requirements.txt`: preparación del QR y de la web para la dirección real de Pages.

No necesitas Node, npm ni una base de datos para esta web. GitHub Actions usa Python para preparar el QR antes de publicar.

## El QR y el cambio de alojamiento

La copia de los archivos de origen conserva el QR del sitio actual para poder revisar el diseño sin conocer todavía tu usuario ni el nombre definitivo del repositorio.

Al publicar con el flujo incluido, GitHub proporciona su dirección a `scripts/build.py`. El flujo genera un nuevo QR que abre `contacto.html` en esa dirección, incluyendo la ruta del repositorio. También adapta el enlace web dentro de la tarjeta de agenda. Los archivos publicados se preparan en `_site/` y no modifican tus fuentes del repositorio.

Para que el QR apunte al nuevo alojamiento, utiliza **GitHub Actions**, como se indica arriba. Si eliges **Deploy from a branch** y subes solo los archivos de origen, el QR seguirá apuntando al alojamiento anterior.

Los QR ya impresos no cambian su dirección por publicar una web nueva. Descarga el nuevo `assets/qr-contacto.svg` desde tu web de GitHub Pages antes de imprimirlo. Si cambias el nombre del repositorio o el dominio, vuelve a ejecutar el flujo.

## Datos actuales

- Rut Gil: **699 474 639**.
- Sonia Padrón: **606 382 314**.
- Correo: **info@alisio28.com**.
- LinkedIn: <https://www.linkedin.com/company/alisio28/>.

El correo visible y Solicitar Contacto abren el mismo selector. Gmail y Outlook pueden requerir iniciar sesión; la aplicación local requiere que el visitante la tenga configurada. El selector abre la redacción, no envía mensajes.

## Revisar en el ordenador

Puedes abrir `index.html` para revisar el aspecto. Para una revisión servida por HTTP, si tienes Python instalado:

```powershell
python -m http.server 8000
```

Abre `http://localhost:8000/`. Detén el servidor con Ctrl+C.

## Generar para otro alojamiento

Si vas a alojarla fuera de GitHub, prepara primero la carpeta publicable con tu dirección real:

```powershell
python -m pip install -r requirements.txt
python scripts/build.py --base-url "https://TU-DOMINIO-O-URL-REAL" --output _site
```

Sustituye el ejemplo por tu dirección completa. Si la web está en una subcarpeta, inclúyela. Sube el contenido de `_site`, no las herramientas de preparación.

## Comprobación y límites

La copia conserva la web existente. Se comprueban las rutas locales de las páginas, el JavaScript y la preparación de archivos para una URL de ejemplo con subcarpeta. La publicación en TU cuenta de GitHub queda pendiente: este ZIP no crea un repositorio ni cambia el alojamiento actual. No se incluye una configuración de dominio propio porque todavía no se ha indicado ni verificado uno para GitHub.

El logo, la matriz y la fotografía son los materiales corporativos suministrados para la web. No se ha concedido una licencia pública de reutilización del contenido ni se han incluido credenciales, historial Git o archivos privados de trabajo.

## Documentación oficial consultada

- [Flujos de GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
- [Configuración de Pages](https://github.com/actions/configure-pages).
- [Carga de archivos publicables](https://github.com/actions/upload-pages-artifact).
- [Despliegue de Pages](https://github.com/actions/deploy-pages).
