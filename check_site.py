"""Comprueba los archivos y las referencias locales del paquete publicable."""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('src', 'href') and value:
                self.references.append(value)


def check_site(folder):
    root = Path(folder).resolve()
    errors = []
    for name in ('index.html', 'contacto.html', 'styles.css', 'contact.js',
                 'assets/qr-contacto.svg', 'assets/alisio28-contacto.vcf'):
        if not (root / name).is_file():
            errors.append('Falta: ' + name)
    for page in root.glob('*.html'):
        parser = References()
        parser.feed(page.read_text(encoding='utf-8'))
        for reference in parser.references:
            url = urlsplit(reference)
            if url.scheme or url.netloc or not url.path:
                continue
            target = (page.parent / unquote(url.path)).resolve()
            if not target.is_relative_to(root) or not target.is_file():
                errors.append(f'{page.name}: referencia no válida {reference}')
    css = root / 'styles.css'
    if css.exists():
        for reference in re.findall(r'url\([\"\x27]?([^\"\x27)]+)', css.read_text(encoding='utf-8')):
            if not urlsplit(reference).scheme and not (root / reference).is_file():
                errors.append('CSS: falta ' + reference)
    if errors:
        raise SystemExit('\n'.join(errors))
    print('Comprobación correcta: páginas, estilos, JavaScript, imágenes y contactos.')


if __name__ == '__main__':
    check_site(sys.argv[1] if len(sys.argv) > 1 else '_site')
