#!/usr/bin/env python3
"""Converte lattes-cosentino.bib em pastas Hugo Blox sob content/publication/."""

import re
import os
import unicodedata

BIB_PATH = os.path.join(os.path.dirname(__file__), '..', 'lattes-cosentino.bib')
OUT_DIR = os.path.join(os.path.dirname(__file__), 'content', 'publication')

TYPE_MAP = {
    'article': 'article-journal',
    'incollection': 'chapter',
    'book': 'book',
    'inproceedings': 'paper-conference',
}

ADMIN_VARIANTS = [
    'carlo benito cosentino filho',
    'cosentino filho, carlo benito',
    'cosentino filho, carlo',
]


def slugify(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()
    text = re.sub(r'[^\w\s-]', '', text.lower())
    text = re.sub(r'[-\s]+', '-', text).strip('-')
    return text[:80]


def parse_bib(path):
    with open(path, encoding='utf-8') as f:
        content = f.read()

    entries = []
    for match in re.finditer(r'@(\w+)\{([^,]+),\s*\n(.*?)\n\}', content, re.DOTALL):
        entry_type = match.group(1).lower()
        fields = {}
        for field_match in re.finditer(r'(\w+)\s*=\s*\{(.*?)\}', match.group(3), re.DOTALL):
            key = field_match.group(1).lower()
            val = field_match.group(2).strip().replace('\n', ' ').replace('  ', ' ')
            val = val.replace('\\&', '&').replace('\\_', '_')
            val = val.replace('TEXTO\\_INTEGRAL', 'TEXTO_INTEGRAL')
            fields[key] = val
        fields['_type'] = entry_type
        entries.append(fields)
    return entries


def format_authors(raw):
    parts = re.split(r'\s+and\s+', raw)
    result = []
    for p in parts:
        name = p.strip().rstrip(',')
        if name.lower() in ADMIN_VARIANTS:
            result.append('me')
        else:
            name = re.sub(r'^([A-ZÁÉÍÓÚÀÂÊÔÃÕÇ\s]+),\s*', lambda m: '', name)
            if name == p.strip().rstrip(','):
                pass
            result.append(name)
    return result


def build_front_matter(entry):
    title = entry.get('title', 'Sem título')
    authors = format_authors(entry.get('author', ''))
    year = entry.get('year', '2020')
    date = f"{year}-01-01"
    pub_type = TYPE_MAP.get(entry['_type'], 'article-journal')

    doi = entry.get('doi', '')
    isbn = entry.get('isbn', '')

    lines = ['---']
    lines.append(f'title: "{title}"')
    lines.append('authors:')
    for a in authors:
        lines.append(f'  - "{a}"')
    lines.append(f'date: "{date}"')
    lines.append(f'publication_types: ["{pub_type}"]')

    # Structured publication format (Hugo Blox v2024+)
    lines.append('publication:')
    if entry['_type'] == 'article':
        journal = entry.get('journal', '')
        vol = entry.get('volume', '')
        pages = entry.get('pages', '')
        lines.append(f'  name: "{journal}"')
        if vol:
            lines.append(f'  volume: "{vol}"')
        if pages:
            lines.append(f'  pages: "{pages}"')
    elif entry['_type'] in ('incollection', 'inproceedings'):
        book = entry.get('booktitle', '')
        publisher = entry.get('publisher', '')
        pages = entry.get('pages', '')
        lines.append(f'  name: "{book}"')
        if publisher:
            lines.append(f'  publisher: "{publisher}"')
        if pages:
            lines.append(f'  pages: "{pages}"')
    elif entry['_type'] == 'book':
        publisher = entry.get('publisher', '')
        address = entry.get('address', '')
        if publisher:
            pub_str = f"{address}: {publisher}" if address else publisher
            lines.append(f'  publisher: "{pub_str}"')

    lines.append('abstract: ""')
    lines.append('featured: false')
    if doi or isbn:
        lines.append('hugoblox:')
        lines.append('  ids:')
        if doi:
            lines.append(f'    doi: "{doi}"')
        if isbn:
            lines.append(f'    isbn: "{isbn}"')
    lines.append('---')
    return '\n'.join(lines) + '\n'


def main():
    entries = parse_bib(BIB_PATH)
    os.makedirs(OUT_DIR, exist_ok=True)

    for entry in entries:
        year = entry.get('year', '2020')
        title = entry.get('title', 'sem-titulo')
        slug = f"{year}-{slugify(title)}"
        folder = os.path.join(OUT_DIR, slug)
        os.makedirs(folder, exist_ok=True)

        fm = build_front_matter(entry)
        with open(os.path.join(folder, 'index.md'), 'w', encoding='utf-8') as f:
            f.write(fm)
        print(f"  {slug}")

    print(f"\n{len(entries)} publicações geradas em {OUT_DIR}")


if __name__ == '__main__':
    main()
