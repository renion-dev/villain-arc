#!/usr/bin/env python3
"""VILLAIN ARC — Daily Content Generator for GitHub Actions"""
import json
from datetime import datetime
from agent import VillainArcAgent

agent = VillainArcAgent('https://renion-dev.github.io/villain-arc/')

posts = []
for platform in ['twitter', 'reddit', 'tiktok']:
    post = agent.generate_post(platform)
    posts.append(post)

queue = {'generated_at': datetime.now().isoformat(), 'posts': posts}

with open('content_queue.json', 'w') as f:
    json.dump(queue, f, indent=2)

for p in posts:
    print(f'[{p["platform"]}] {p["text"][:80]}')
