# groove-pages

All GROOVE results pages in one place. Open https://p-didier.github.io/groove-pages/ to see the list, newest first, and click a page to open it. Each page has an "All pages" link back to the list.

## Example

The Gómez tapping page lives in the folder `gomez-listening/`, as one file, `index.html`. Its address is the list address plus the folder name: https://p-didier.github.io/groove-pages/gomez-listening/

The list reads three lines from the top of that file:

```html
<title>Gómez tapping, CAP models</title>
<meta name="description" content="Tap positions of 43 people on 16 drum loops, against the current CAP and two layer models.">
<meta name="date" content="2026-11-17">
```

and shows them as one row:

| Date | Page | Content |
| --- | --- | --- |
| 2026-11-17 | Gómez tapping, CAP models | Tap positions of 43 people on 16 drum loops, against the current CAP and two layer models. |

## Adding a page

1. Make a new folder with a short name, e.g. `dbp-map/`, and put the page in it as `index.html`.
2. Give the page the three lines above, with its own title, one-sentence description and date.
3. Add a link back to the list somewhere on the page: `<a href="../">All pages</a>`.
4. Send the folder to Paul. He adds it here and puts it on the list.

## For Paul

`build_index.py` needs `pdviz` (run it with `~/miniforge3/envs/groove-env-1/bin/python build_index.py`). Build scripts write into this folder through `GROOVE_PAGES` (default `~/groove-postdoc/dev/groove-pages`).

| Folder | Built by |
| --- | --- |
| `gomez-listening` | `gomez-tapping-regression/build_page.py` |
