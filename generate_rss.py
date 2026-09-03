#!/usr/bin/env python3
"""Generate RSS feed for VILLAIN ARC"""
import json
from datetime import datetime
from pathlib import Path

# Load content queue
queue_file = Path("content_queue.json")
if queue_file.exists():
    with open(queue_file) as f:
        queue = json.load(f)
    posts = queue.get("posts", [])
else:
    posts = []

# Generate RSS
rss = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
<title>VILLAIN ARC — Daily Villain Origin Stories</title>
<link>https://renion-dev.github.io/villain-arc/</link>
<description>Discover your inner villain. A cinematic experience with procedural generation.</description>
<language>en</language>
<lastBuildDate>""" + datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT") + """</lastBuildDate>
<atom:link href="https://renion-dev.github.io/villain-arc/feed.xml" rel="self" type="application/rss+xml"/>
"""

for post in posts[:10]:
    text = post.get("text", "")[:200]
    rss += f"""
<item>
<title>{post.get('platform', 'Villain').upper()} — New Villain Arc</title>
<description>{text}</description>
<link>https://renion-dev.github.io/villain-arc/</link>
<pubDate>{datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")}</pubDate>
<guid>https://renion-dev.github.io/villain-arc/#{post.get('platform', 'post')}</guid>
</item>
"""

rss += """
</channel>
</rss>"""

with open("feed.xml", "w") as f:
    f.write(rss)

print("RSS feed generated: feed.xml")
