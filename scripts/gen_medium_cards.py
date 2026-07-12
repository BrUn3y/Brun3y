#!/usr/bin/env python3
"""Generate widget-style SVG cards for the latest Medium posts.

Reads the author's Medium RSS feed and writes one self-contained SVG per post
(cover image embedded as base64) into assets/medium/. Run locally or from CI:

    python3 scripts/gen_medium_cards.py

No third-party dependencies — standard library only.
"""
from __future__ import annotations

import base64
import re
import urllib.request
from pathlib import Path

FEED = "https://medium.com/feed/@brun3y"
OUT = Path("assets/medium")
COUNT = 4
UA = {"User-Agent": "Mozilla/5.0"}

# Card geometry
W, H = 460, 140
COVER = 124
PAD = 8
TX = PAD + COVER + 16


def fetch(url: str) -> bytes:
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30).read()


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def wrap(title: str, maxchars: int = 34):
    words, lines, cur = title.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= maxchars:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines[:2]


def _png_colortype(data: bytes) -> int | None:
    """Return the PNG color type (2/0 = opaque, 4/6 = has alpha), or None if not a PNG."""
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return data[25]  # IHDR color-type byte


def cover_b64(item: str) -> str | None:
    """Pick the best static cover: opaque PNGs first (avoid gifs and transparent
    logos that render as white blocks on GitHub), then fall back to anything."""
    hashes = re.findall(r"https://cdn-images-1\.medium\.com/max/\d+/([^\"\s)<]+)", item)
    best, best_rank = None, 99
    for h in hashes:
        if h.endswith(".gif"):
            continue  # animated gifs don't render when embedded in an SVG on GitHub
        try:
            data = fetch(f"https://cdn-images-1.medium.com/fit/c/248/248/{h}")
        except Exception:
            continue
        ct = _png_colortype(data)
        rank = 0 if ct in (0, 2) else 1  # 0/2 = opaque (no alpha) -> preferred
        if rank < best_rank:
            best, best_rank = data, rank
        if best_rank == 0:
            break  # found an opaque cover, good enough
    return base64.b64encode(best).decode() if best else None


def read_time(item: str) -> str:
    content = re.search(r"<content:encoded>(.*?)</content:encoded>", item, re.S)
    words = len(re.sub(r"<[^>]+>", " ", content.group(1)).split()) if content else 0
    return f"{max(1, round(words / 265))} min read"


def date_str(item: str) -> str:
    pub = re.search(r"<pubDate>(.*?)</pubDate>", item)
    m = re.search(r"\w+, (\d+) (\w+) (\d+)", pub.group(1)) if pub else None
    return f"{m.group(2)} {int(m.group(1))}" if m else ""


def render(title: str, author: str, meta: str, b64: str) -> str:
    lines = wrap(title)
    ty = 46 if len(lines) == 2 else 54
    tspans = "".join(
        f'<text x="{TX}" y="{ty + i * 22}" fill="#e6edf3" font-size="16" font-weight="700" '
        f'font-family="Segoe UI, Helvetica, Arial, sans-serif">{esc(l)}</text>'
        for i, l in enumerate(lines)
    )
    img = (
        f'<image x="{PAD}" y="{PAD}" width="{COVER}" height="{COVER}" clip-path="url(#cover)" '
        f'preserveAspectRatio="xMidYMid slice" xlink:href="data:image/png;base64,{b64}"/>'
        if b64
        else ""
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img">
  <defs>
    <clipPath id="card"><rect width="{W}" height="{H}" rx="8"/></clipPath>
    <clipPath id="cover"><rect x="{PAD}" y="{PAD}" width="{COVER}" height="{COVER}" rx="6"/></clipPath>
  </defs>
  <g clip-path="url(#card)">
    <rect width="{W}" height="{H}" fill="#242938"/>
    <rect x="{PAD}" y="{PAD}" width="{COVER}" height="{COVER}" rx="6" fill="#0d1117"/>
    {img}
    {tspans}
    <text x="{TX}" y="{H - 46}" fill="#8b949e" font-size="12.5" font-family="Segoe UI, Helvetica, Arial, sans-serif">{esc(author)}</text>
    <text x="{TX}" y="{H - 22}" fill="#8b949e" font-size="12.5" font-family="Segoe UI, Helvetica, Arial, sans-serif">{esc(meta)}</text>
  </g>
</svg>"""


def main() -> None:
    xml = fetch(FEED).decode("utf-8", "replace")
    author_m = re.search(r"<title>Stories by (.*?) on Medium</title>", xml)
    author = author_m.group(1).strip() if author_m else "Medium"
    items = re.split(r"<item>", xml)[1:COUNT + 1]
    OUT.mkdir(parents=True, exist_ok=True)
    for i, item in enumerate(items, 1):
        title = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", item, re.S).group(1).strip()
        meta = f"{date_str(item)} · {read_time(item)}"
        svg = render(title, author, meta, cover_b64(item))
        (OUT / f"{i}.svg").write_text(svg, encoding="utf-8")
        print(f"wrote {OUT / f'{i}.svg'}  ({title})")


if __name__ == "__main__":
    main()
