#!/usr/bin/env python3
"""VILLAIN ARC — Daily Content Generator for GitHub Actions"""
import json
from datetime import datetime
from agent_v2 import VillainArcAgent

agent = VillainArcAgent()

# Generate daily content
content = agent.generate_daily_content()

# Save to queue
queue = {
    'generated_at': datetime.now().isoformat(),
    'posts': [
        {'platform': p, 'text': t} for p, t in content.items()
    ]
}

with open('content_queue.json', 'w') as f:
    json.dump(queue, f, indent=2)

for p, t in content.items():
    print(f'[{p}] {t[:80]}...')
