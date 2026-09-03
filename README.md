# VILLAIN ARC — The Cinematic Origin Story Generator

![VILLAIN ARC](https://img.shields.io/badge/VILLAIN-ARC-ff2d55?style=for-the-badge)
![Version](https://img.shields.io/badge/version-4.2-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![GitHub](https://img.shields.io/github/stars/renion-dev/vilain-arc?style=social)

## 🎬 Live Demo

**https://renion-dev.github.io/villain-arc/**

---

## 📖 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Core Systems](#core-systems)
- [API Reference](#api-reference)
- [Deployment](#deployment)
- [Social Media](#social-media)
- [Roadmap](#roadmap)
- [License](#license)

---

## 🎭 Overview

VILLAIN ARC is a fully autonomous, cinematic villain origin story generator. Enter your name and discover your inner villain with stunning visuals, procedural animation, and AI-powered narration.

**Key Highlights:**
- 100% client-side — no server required
- Fully autonomous promotion system
- 393+ unique content elements
- 6 procedural pose types
- Dynamic portrait with eye tracking
- Cinematic video trailer generation
- Web Speech API narration

---

## ✨ Features

### 🎮 Core Experience

| Feature | Description |
|---------|-------------|
| **Origin Story Generation** | Enter your name → get unique villain with backstory |
| **Dynamic Portrait** | Breathing animation, eye tracking, click reactions |
| **Rarity System** | Common → Uncommon → Rare → Epic → Legendary → Mythic |
| **Evolution System** | Minion → Henchman → Captain → Commander → Overlord |
| **Origin Video** | Cinematic trailer with narration |

### 🌍 Universe

| Feature | Description |
|---------|-------------|
| **5 Factions** | Shadow Syndicate, Iron Legion, Void Collective, Blood Covenant, Storm Empire |
| **5 Regions** | The Abyss, Iron Citadel, Void Nexus, Blood Crypt, Tempest Peak |
| **Relationships** | Rivals, Allies, Mentors, Lovers, Creator/Creation |
| **Weekly Tournament** | Themed competitions with voting |
| **Hidden Villains** | 5 secret villains with special conditions |
| **Prophecy System** | Dynamic prophecies with placeholders |
| **Villain Legacy** | Dynasty system with faction grouping |

### 🎨 Visual System

| Feature | Description |
|---------|-------------|
| **6 Pose Types** | Orbs, Tendrils, Wings, Aura, Shatter, Spiral, Lightning, Void |
| **5 Face Types** | Angular, Round, Long, Square, Oval |
| **6 Hair Styles** | Bald, Short, Long, Mohawk, Top Knot, Wild |
| **5 Expressions** | Neutral, Angry, Smirk, Melancholic, Maniacal |
| **7 Accessories** | Scar, Eyepatch, Horns, Crown, Mask, Tattoos |

### 🔊 Audio System

| Feature | Description |
|---------|-------------|
| **Web Audio API** | Drone, Impact, Rise, Text, Chord effects |
| **Web Speech API** | 5 voice types for narration |
| **Dynamic Sound** | Procedural audio based on rarity |

### 🛍️ Monetization

| Feature | Description |
|---------|-------------|
| **Merch API** | T-Shirt, Hoodie, Poster, Mug, Sticker Pack |
| **Video Export** | WebM recording of portrait |
| **Image Export** | PNG download |

### 🏆 Gamification

| Feature | Description |
|---------|-------------|
| **14 Achievements** | First Blood, Collector, Obsessed, Nemesis Hunter, etc. |
| **Streak System** | Daily login streaks |
| **Level System** | XP-based progression |
| **Gallery** | Collection of all generated villains |

---

## 🛠️ Tech Stack

### Frontend
- **HTML5** — Semantic markup
- **CSS3** — Custom properties, Grid, Flexbox, Animations
- **Canvas 2D** — Procedural portrait generation
- **Web Audio API** — Sound effects and music
- **Web Speech API** — AI narration
- **MediaRecorder API** — Video export

### Backend (Promotion)
- **Python 3** — Content generation agent
- **GitHub Actions** — Automated content scheduling
- **GitHub Pages** — Static hosting

### APIs
- **Twitter/X** — Social sharing
- **Reddit** — Community posts
- **Mastodon** — Decentralized social
- **Telegram** — Bot integration
- **Discord** — Webhook integration

---

## 🚀 Quick Start

### Local Development

```bash
# Clone the repository
git clone https://github.com/renion-dev/villain-arc.git
cd villain-arc

# Start local server
python3 -m http.server 8080

# Open in browser
open http://localhost:8080
```

### Deployment

```bash
# Push to GitHub (auto-deploys to GitHub Pages)
git add .
git commit -m "Update"
git push origin master
```

---

## 📁 Project Structure

```
villain-arc/
├── index.html              # Main application (57KB)
├── sitemap.xml             # SEO sitemap
├── robots.txt              # Search engine rules
├── feed.xml                # RSS feed
├── og-image.svg            # Open Graph image
├── agent.py                # Content generation agent
├── agent_v2.py             # Multi-platform agent
├── generate_content.py     # GitHub Actions script
├── generate_rss.py         # RSS feed generator
├── generate_og.py          # OG image generator
├── test.js                 # Test suite
├── vercel.json             # Vercel config
├── .github/
│   └── workflows/
│       ├── content.yml     # Content generation workflow
│       └── seo.yml         # SEO optimization workflow
└── README.md               # This file
```

---

## 🧩 Core Systems

### 1. Rarity System

```javascript
const RARITY = {
  common:    { chance: 50, color: '#a0a0a0' },
  uncommon:  { chance: 30, color: '#30d158' },
  rare:      { chance: 12, color: '#64d2ff' },
  epic:      { chance: 5,  color: '#bf5af2' },
  legendary: { chance: 2,  color: '#ff9f0a' },
  mythic:    { chance: 1,  color: '#ff2d55' }
};
```

### 2. Evolution System

| Level | Title | Color |
|-------|-------|-------|
| 1-4 | Minion | #a0a0a0 |
| 5-9 | Henchman | #30d158 |
| 10-14 | Captain | #64d2ff |
| 15-19 | Commander | #bf5af2 |
| 20+ | Overlord | #ff9f0a |

### 3. Factions

| Faction | Color | Description |
|---------|-------|-------------|
| Shadow Syndicate | #bf5af2 | Masters of stealth and deception |
| Iron Legion | #ff9f0a | Warriors of conquest and destruction |
| Void Collective | #64d2ff | Seekers of forbidden knowledge |
| Blood Covenant | #ff2d55 | Dark sorcerers and ritualists |
| Storm Empire | #30d158 | Rulers of nature and chaos |

### 4. Regions

| Region | Description | Bonus Faction |
|--------|-------------|---------------|
| The Abyss | Darkness eternal | Shadow |
| Iron Citadel | Fortress of war | Iron |
| Void Nexus | Reality fractures here | Void |
| Blood Crypt | Ancient rituals | Blood |
| Tempest Peak | Eternal storm | Storm |

### 5. Achievement System

| ID | Name | Condition |
|----|------|-----------|
| first | First Blood | Generate 1 villain |
| collector | Collector | 5 unique villains |
| obsessed | Obsessed | 10 total villains |
| nemesis | Nemesis Hunter | Fight nemesis |
| streak3 | Dedicated | 3-day streak |
| streak7 | Addicted | 7-day streak |
| poses | Shape Shifter | All 8 poses |
| threats | Threat Assessment | All threat levels |
| sharer | Viral | Share once |
| daily | Daily Devotee | Check daily |
| gallery | Gallery Master | 15 unique |
| night | Night Owl | Play after midnight |
| speed | Speed Demon | 3 in one session |
| all | Completionist | All achievements |

---

## 📡 API Reference

### JavaScript API

```javascript
// Generate a villain
const villain = generate("Your Name", "The Awakening");
// Returns: { villainName, epithet, power, threat, quote, backstory, rarity, faction, region }

// Get evolution level
const evo = getEvolution(10); // Level 10 → Captain

// Get faction
const faction = getFaction(rng(hash("seed")));

// Narrate story
narrateStory("dramatic");

// Start video
startOriginVideo();
```

### Python API

```python
from agent_v2 import VillainArcAgent

agent = VillainArcAgent()

# Generate content for all platforms
content = agent.generate_daily_content()

# Post to configured platforms
results = agent.post_to_all(content)

# Get schedule
schedule = agent.get_schedule(posts_per_day=3, days=7)
```

### Content Generator

```bash
# Generate daily content
python3 generate_content.py

# Generate RSS feed
python3 generate_rss.py

# Generate OG image
python3 generate_og.py
```

---

## 🌐 Deployment

### GitHub Pages (Recommended)

1. Push to `master` branch
2. GitHub Actions auto-deploys
3. Live at `https://<username>.github.io/villain-arc/`

### Vercel

```bash
vercel --prod
```

### Netlify

```bash
netlify deploy --dir . --allow-anonymous
```

### Cloudflare Pages

```bash
wrangler pages deploy . --project-name villain-arc
```

---

## 📱 Social Media

### Automated Posting

The agent generates content for:

| Platform | Method | Status |
|----------|--------|--------|
| Twitter/X | API / Manual | ✅ |
| Reddit | API / Manual | ✅ |
| TikTok | Manual share | ✅ |
| Mastodon | API | ✅ |
| Telegram | Bot API | ✅ |
| Discord | Webhook | ✅ |
| Instagram | Manual share | ✅ |
| LinkedIn | Manual share | ✅ |

### Sample Posts

```
[Twitter] I am Lord Vesper Nox, "The Silence Between Heartbeats". 
Threat Level: S. What's YOUR villain arc? → https://renion-dev.github.io/villain-arc/

[Reddit] I built a cinematic villain origin story generator. 
Enter your name and discover your inner villain. Mine is Dr. Oblivion, 
"The Final Whisper", with the power of Consciousness Control. What's yours?

[Tiktok] POV: You discovered your origin story and you're 
Lord Tempest with the power of Reality Warping 🦹‍♂️ 
What's YOUR villain arc? Link in bio!
```

---

## 🔧 Configuration

### Environment Variables

```bash
# GitHub Actions
GITHUB_TOKEN=xxx

# Telegram
TELEGRAM_BOT_TOKEN=xxx
TELEGRAM_CHANNEL_ID=@villainarc

# Discord
DISCORD_WEBHOOK_URL=xxx

# Mastodon
MASTODON_INSTANCE=mastodon.social
MASTODON_TOKEN=xxx
```

### Customization

```javascript
// Change rarity chances
RARITY.mythic.chance = 2; // 2% instead of 1%

// Add new faction
FACTIONS.push({ id: 'new', name: 'New Faction', color: '#fff', desc: 'Description' });

// Add new pose
POSES.push('newpose');

// Change evolution levels
EVOLUTION[25] = { name: 'Dark God', title: 'Transcendent being', color: '#fff', size: 1.3 };
```

---

## 🗺️ Roadmap

### Completed (12 Days)

- [x] Day 1: Rarity system
- [x] Day 2: Dynamic portrait
- [x] Day 3: Evolution system
- [x] Day 4: Villain universe
- [x] Day 5: Relationships
- [x] Day 6: Weekly tournament
- [x] Day 7: Hidden villains
- [x] Day 8: Prophecy system
- [x] Day 9: Villain legacy
- [x] Day 10: Merch API
- [x] Day 11: Premium narration
- [x] Day 12: Origin video

### Future Ideas

- [ ] Multi-language support
- [ ] Custom villain editor
- [ ] Battle system (Villain vs Villain)
- [ ] Leaderboards
- [ ] Seasonal events
- [ ] NFT integration
- [ ] Mobile app
- [ ] VR experience

---

## 📊 Analytics

Track with:

- **Google Analytics** — Page views, user behavior
- **Plausible** — Privacy-friendly alternative
- **GitHub Stars** — Community growth
- **Share Count** — Viral coefficient

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing`)
5. Open Pull Request

---

## 📄 License

MIT License — feel free to use, modify, and distribute.

---

## 👤 Author

**renion-dev**
- GitHub: [@renion-dev](https://github.com/renion-dev)
- Project: [villain-arc](https://github.com/renion-dev/villain-arc)

---

## 🙏 Acknowledgments

- Google Fonts (Cinzel, Inter, Cormorant Garamond)
- GitHub Pages (Hosting)
- Web Audio API community
- Canvas 2D tutorials

---

<div align="center">

**🦹 VILLAIN ARC — Discover Your Inner Villain 🦹**

[Live Demo](https://renion-dev.github.io/villain-arc/) · [GitHub](https://github.com/renion-dev/villain-arc) · [Report Bug](https://github.com/renion-dev/villain-arc/issues)

</div>
