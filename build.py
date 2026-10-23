"""Prepara la web de ALISIO28 para Pages y adapta el QR a su URL real."""
import argparse
import shutil
from pathlib import Path
from urllib.parse import urlsplit
from reportlab.graphics.barcode.qrencoder import QRCode, QRErrorCorrectLevel

ROOT = Path(__file__).resolve().parent.parent


def prepare_site(base_url, output):
    base_url = base_url.rstrip('/')
    parsed = urlsplit(base_url)
    if parsed.scheme not in ('https', 'http') or not parsed.netloc:
        raise ValueError('Indica la URL completa del sitio, con https:// y su ruta si tiene una.')
    if parsed.query or parsed.fragment or parsed.username or parsed.password:
        raise ValueError('La URL base no debe contener consulta, fragmento ni credenciales.')
    if not parsed.path.isascii():
        raise ValueError('Usa la ruta de la URL codificada para navegador, sin caracteres especiales.')
    output = Path(output).resolve()
    if output == ROOT or ROOT.is_relative_to(output):
        raise ValueError('La salida debe ser una carpeta dedicada, como _site.')
    output.mkdir(parents=True, exist_ok=True)
    for name in ('index.html', 'contacto.html', 'styles.css', 'contact.js', '.nojekyll'):
        shutil.copy2(ROOT / name, output / name)
    shutil.copytree(ROOT / 'assets', output / 'assets', dirs_exist_ok=True)

    contact_url = base_url + '/contacto.html'
    card = '\r\n'.join([
        'BEGIN:VCARD', 'VERSION:3.0', 'FN:Rut Gil / Sonia Padrón', 'ORG:ALISIO28',
        'item1.TEL;TYPE=CELL:+34699474639', 'item1.X-ABLabel:Rut Gil',
        'item2.TEL;TYPE=CELL:+34606382314', 'item2.X-ABLabel:Sonia Padrón',
        'EMAIL;TYPE=INTERNET:info@alisio28.com',
        'URL:' + base_url + '/',
        'URL:https://www.linkedin.com/company/alisio28/', 'END:VCARD', '',
    ])
    (output / 'assets' / 'alisio28-contacto.vcf').write_bytes(card.encode('utf-8'))

    qr = QRCode(None, QRErrorCorrectLevel.M)
    qr.addData(contact_url)
    qr.make()
    quiet = 4
    side = qr.getModuleCount() + quiet * 2
    modules = ''.join(
        f'M{x + quiet},{y + quiet}h1v1h-1z'
        for y, row in enumerate(qr.modules) for x, dark in enumerate(row) if dark
    )
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {side} {side}" '
        'width="512" height="512" shape-rendering="crispEdges">'
        f'<rect width="{side}" height="{side}" fill="white"/>'
        f'<path d="{modules}" fill="#07254b"/></svg>'
    )
    (output / 'assets' / 'qr-contacto.svg').write_text(svg, encoding='utf-8')
    # Registro de la dirección codificada, útil para comprobar un cambio de dominio.
    (output / 'qr-destino.txt').write_text(contact_url + '\n', encoding='utf-8')
    print('Web preparada. El QR abre: ' + contact_url)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-url', required=True)
    parser.add_argument('--output', default=str(ROOT / '_site'))
    args = parser.parse_args()
    prepare_site(args.base_url, args.output)
