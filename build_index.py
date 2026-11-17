"""Write index.html, the list of every page in this repo, newest first.

A page is a folder holding an ``index.html`` with ``<title>``,
``<meta name="description">`` and ``<meta name="date">`` (ISO date). Build
scripts in other repos write those folders. Run ``python build_index.py``
after adding or rebuilding one, then commit and push.
"""

import html
import re
from pathlib import Path

import pdviz

HERE = Path(__file__).parent
# pages that live in their own repos, kept at their old URLs
OLDER = (
    (
        "https://p-didier.github.io/tap2groove/",
        "Tap2Groove",
        "Phone tapping app, one pad then two pads.",
    ),
    (
        "https://p-didier.github.io/wp3-first-experiment-pilot/",
        "WP3 Exp. 1 pilot",
        "Place-accents listening test.",
    ),
    (
        "https://p-didier.github.io/rules-listening/",
        "Accent rule listening",
        "WP1 accent rules on audio examples.",
    ),
    (
        "https://p-didier.github.io/apc-listening/",
        "APC listening sheet",
        "Accent pattern contrast examples.",
    ),
)


def meta(page):
    """Read title, date and description of one page.

    Parameters
    ----------
    page : Path
        A page's ``index.html``.

    Returns
    -------
    tuple of str
        ``(date, title, description)``, raw text as in the page head.
    """
    head = page.read_text(encoding="utf-8").split("</head>")[0]
    title = re.search(r"<title>(.*?)</title>", head, re.S).group(1).strip()
    date = re.search(r'<meta name="date" content="([^"]+)"', head).group(1)
    desc = re.search(r'<meta name="description" content="([^"]+)"', head).group(1)
    return date, title, desc


def build():
    """Write ``index.html`` from the page folders.

    Returns
    -------
    Path
        The written index.
    """
    pages = sorted(
        ((*meta(p), p.parent.name) for p in HERE.glob("*/index.html")), reverse=True
    )
    rows = "".join(
        f'<tr><td style="white-space: nowrap">{d}</td><td class="text"><a href="{f}/">{t}</a></td><td class="text">{s}</td></tr>'
        for d, t, s, f in pages
    )
    older = "".join(
        f'<li><a href="{u}">{html.escape(t)}</a> <span class="note">{html.escape(s)}</span></li>'
        for u, t, s in OLDER
    )
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>GROOVE pages</title><style>{pdviz.page_css()}</style></head>
<body><main>
<h1>GROOVE pages</h1>
<p>Results pages of the GROOVE project (RITMO, University of Oslo), newest first.</p>
<table><caption>Table 1. Pages in this repo.</caption>
<tr><th>Date</th><th class="text">Page</th><th class="text">Content</th></tr>{rows}</table>
<h2>Older pages</h2>
<ul>{older}</ul>
</main></body></html>
"""
    assert not pdviz.page_lint(page), "page lint warnings"
    out = HERE / "index.html"
    out.write_text(page, encoding="utf-8")
    return out


if __name__ == "__main__":
    print("wrote", build())
