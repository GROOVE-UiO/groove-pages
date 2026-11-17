# groove-pages

Results pages of the GROOVE project, served at https://p-didier.github.io/groove-pages/. One folder per page, `index.html` at the root lists them.

## Add or update a page

A build script in the source repo writes `<folder>/index.html` here (default path `~/groove-postdoc/dev/groove-pages`, set `GROOVE_PAGES` to change it). The page head needs `<title>`, `<meta name="description">` and `<meta name="date">`, and a link back to `../`. Then:

```
~/miniforge3/envs/groove-env-1/bin/python build_index.py
git add -A && git commit -m "<folder>: <what changed>" && git push
```

## Pages

| Folder | Source |
| --- | --- |
| `gomez-listening` | `gomez-tapping-regression/build_page.py` |
