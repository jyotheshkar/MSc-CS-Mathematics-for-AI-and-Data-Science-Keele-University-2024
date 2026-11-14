"""Verify published assignment bytes, archive structure and local Markdown links."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def main():
    receipt = json.loads((ROOT/'docs/original/provenance.json').read_text(encoding='utf-8'))
    document = ROOT/'docs/original/student-assignment-redacted.odt'
    data = document.read_bytes()
    assert len(data) == receipt['output_size'], 'Assignment size changed'
    assert hashlib.sha256(data).hexdigest() == receipt['output_sha256'], 'Assignment hash changed'
    with zipfile.ZipFile(document) as archive:
        assert archive.testzip() is None, 'Corrupt document ZIP'
        names = set(archive.namelist())
        assert 'Object 42/content.xml' not in names, 'Personalised matrix object returned'
        assert 'media/image2.png' not in names, 'Personalised screenshot returned'
        assert 'settings.xml' not in names, 'Local document settings returned'
        assert archive.read('mimetype') == b'application/vnd.oasis.opendocument.text'
        for name in names:
            if name.endswith('.xml'):
                ET.fromstring(archive.read(name))
        equations = sum(bool(re.fullmatch(r'Object \d+/content.xml', name)) for name in names)
        assert equations == receipt['verification']['equation_objects'], 'Equation object count changed'
    links = 0
    for markdown in ROOT.rglob('*.md'):
        content = markdown.read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^\s)]+)\)', content):
            if urlsplit(target).scheme or target.startswith('#'):
                continue
            path = (markdown.parent/unquote(urlsplit(target).path)).resolve()
            assert path.is_relative_to(ROOT) and path.exists(), f'Missing/outside link: {markdown.name}: {target}'
            links += 1
    print(f'Verified assignment SHA256, ZIP/XML, {equations} equation objects and {links} local links.')


if __name__ == '__main__':
    main()
