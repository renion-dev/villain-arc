#!/usr/bin/env python3
"""
VILLAIN ARC — Fully Autonomous Free Promotion Agent
Creates accounts, generates content, posts automatically.
Platforms: Mastodon, Bluesky, Telegram, Discord (all free)
"""

import json
import random
import hashlib
import os
import time
from datetime import datetime
from pathlib import Path

# Try to import optional dependencies
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

try:
    from atproto import Client as BSkyClient
    HAS_BSKY = True
except ImportError:
    HAS_BSKY = False

# ===== CONTENT =====
NAMES = ["Lord Vesper Nox","Dr. Oblivion","Baroness Nyx","The Architect","Countess Ravenna","Malachi Void","Seraphina Dusk","Commander Obsidian","Lady Morgaine","Necro Magnus","Vespera Umbra","Lord Sinister","Dr. Caliginous","Baron Von Shade","The Collector","Madame Nocturne","Lord Tempest","Dr. Malady","Baroness Thorn","The Phantom","Countess Vesper","Lord Moros","Dr. Nyx","Baron Samedi","The Wraith","Lady Morgause","Lord Vex","Dr. Mortis","The Shade","Madame Vespera","Lord Noxious","Baron Grim","The Specter","Lord Dusk","The Revenant","Lady Vesperil","The Phantom Lord","Madame Morgaine","Lord Void","Dr. Sinister","Baroness Dusk","The Wraith King","Countess Morgause","Lord Shade","Dr. Vexar","Baron Nocturne","The Collector Prime","Lady Nyx","Lord Moros II","Dr. Mortis II","Baroness Thornheart","The Shadow","Madame Morgause II","Lord Tempest III","Dr. Malady III","Baron Ravenna II","The Revenant King","Countess Vesperil II","Lord Nox III","Dr. Oblivion III","Baroness Nyxora","The Specter II","Lady Morgaine III","Lord Vexarion","Dr. Caliginous III","Baron Samedi II","The Phantom Queen","Madame Nocturne II","Lord Dusk III","Dr. Tempest III","Baroness Morgaine III","The Wraith Lord","Countess Nyxora II","Lord Obsidian III","Dr. Sinister III","Baron Grim II","The Shade Lord","Nyx Prime","Vesper Omega","Malachi Throne","Caliginous Prime","Tempest Magnus","Oblivion Omega","Ravenna Nox","Thornheart Magnus","Obsidian Rex","Sinister Maximus","Moros Eternal","Vex Oblivion","Dusk Eternal","Nox Sinister","Tempest Caliginous","Malady Ravenna","Thorn Nox","Wraith Oblivion","Phantom Malachi","Shade Tempest","Void Caliginous","Shadow Moros","Specter Vex","Vesper Requiem","Malice Mortis","Caligo Vesper","Tempestas Noctis"]

EPITHETS = ["The Silence Between Heartbeats","The Last Shadow","Keeper of Forgotten Truths","The Unmaking","Herald of the Void","The Final Whisper","Architect of Ruin","The Eternal Dusk","Sovereign of Ash","The Hollow Crown","Weaver of Nightmares","The Crimson Threshold","Lord of the Last Breath","The Infinite Regress","Harbinger of Silence","The Obsidian Gate","The Seventh Seal","Warden of the Abyss","The Pale Flame","The Unbound","The Dark Between Stars","The Last Confession","The Iron Lullaby","The Sorrow Engine","The Glass Coffin","The Midnight Accord","The Bone Orchard","The Velvet Guillotine","The Salt Crown","The Grief Collector","The Hollow Menagerie","The Last Witness","The Ash Garden","The Drowning King","The Paper Moon","The Rust Prophet","The Wailing Atlas","The Sulfur Saint","The Marrow Palace","The Nail Cathedral","The Ember Throne","The Frost Heretic","The Lead Psalm","The Mercury Shroud","The Tin Requiem","The Cobalt Dirge","The Zinc Elegy","The Nickel Lament","The Copper Mourning","The Iron Sorrow","The Steel Grief","The Titanium Wound","The Aluminum Scar","The Chrome Wound","The Silver Lining","The Gold Standard","The Platinum Rule","The Diamond Cutter","The Carbon Footprint","The Neon Glow","The Last Ember","The First Darkness","The Final Hour","The Endless Night","The Broken Mirror","The Shattered Crown","The Lost Soul","The Forgotten Name","The Hidden Face","The Silent Scream","The Deadly Kiss","The Poisoned Chalice","The Cursed Blade","The Bloody Hand","The Cold Eye","The Empty Throne","The Fallen Angel","The Rising Demon","The Burning Sky","The Frozen Earth","The Cracked Mask","The Torn Veil","The Crimson Dusk","The Pale Moon","The Blood Rain","The Soul Frost","The Mind Flame","The Heart Stone"]

POWERS = ["Shadow Manipulation","Mind Reading","Invisibility","Teleportation","Time Manipulation","Absolute Strength","Fire Control","Ice Control","Lightning Control","Earth Control","Water Control","Air Control","Gravity Control","Darkness Control","Light Control","Reality Warping","Spatial Control","Energy Control","Matter Manipulation","Consciousness Control","Emotion Manipulation","Memory Control","Dream Control","Death Manipulation","Life Manipulation","Fate Control","Illusion Mastery","Sound Control","Poison Control","Disease Manipulation","Aging Control","Evolution Control","Mutation Control","Technology Control","Machine Control","Animal Control","Plant Control","Virus Control","Nanoparticle Control","Quantum State Control","Antimatter Control","Dark Matter Control","Dark Energy Control","Black Hole Control","Multiverse Control","Dimension Control","Immortality","Soul Manipulation","Void Walking","Nightmare Manifestation","Blood Crystallization","Fear Extraction","Chaos Induction","Plague Bearer","Storm Bringer","Earth Shaker","Tidal Fury","Solar Flare","Void Gaze","Mind Break","Pain Amplifier","Hope Destroyer","Dream Weaver","Soul Eater","Bone Manipulator","Flesh Sculptor","Blood Bender","Shadow Meld","Time Freeze","Space Fold","Reality Ripple","Doom Prophet","Plague Wind","Ash Walker","Soul Forge","Chaos Weaver"]

QUOTES = ["I did not become a villain. The world made me one.","Heroes lose because they play by the rules. I don't play.","You think you know darkness? You don't even know shadow.","I have seen the end of the world. It begins with me.","Justice is an illusion for those afraid of their own power.","When everything is taken, there is only one choice: take everything back.","I am not evil. I am simply no longer afraid of the truth.","The world needs a hero? The world deserves a villain.","You call this evil. I call it freedom.","When no one else can be trusted — trust yourself. Only yourself.","I did not seek power. Power found me.","Darkness is not the absence of light. It is the presence of something else.","When the world says 'no', I say 'enough'.","I have seen how heroes die. I will not be a hero.","Betrayal is not the end. It is the beginning.","You think I'm insane? Perhaps. But I am right.","When you destroy myths, you become a myth yourself.","I do not want to rule the world. I want to rewrite it.","The greatest lie is the truth no one wants to hear.","When you lose everything, you find strength you never knew you had.","I am the villain of your story. You are the villain of mine.","When the world burns, I do not extinguish the flame. I feed it.","I am not broken. I am just different.","Heroes die for an idea. I live for it.","When the truth hurts, people choose lies. I choose the truth.","I did not seek revenge. Revenge found me.","You think you know me? You only know what I let you know.","When the world says 'stop', I accelerate.","I am not a monster. I am evolution.","When you open your eyes, you cannot close them again.","I do not fear the darkness. I live in it.","You call this the end? This is only the beginning.","When the world takes everything, I take the world.","I am not evil. I simply have different priorities.","Heroes save the world. I change it.","When there is nothing left to lose, you become the most dangerous.","I did not seek conflict. Conflict found me.","You think I am alone? I am a legend.","When the world says 'no', I say 'let me show you another way'.","I am not the villain of your story. You are the villain of mine.","When you destroy the past, the future becomes yours.","I do not fear death. I control it.","You call this betrayal? I call it freedom.","When the world burns, I dance in the flames.","I am not broken. I simply no longer play by your rules.","Heroes die as heroes. I will live as a villain.","When hope is taken, only strength remains.","I did not seek the darkness. The darkness came to me.","You think this is the end? This is only the beginning of my arc.","I am the silence between your heartbeats.","When heroes fall, I rise from their ashes.","The world is a stage, and I am the final act.","I do not break the rules. I rewrite them.","Your fear is my nourishment.","I am the shadow that swallows the sun.","When gods fail, villains prevail.","I am the answer to prayers you should have never made.","The end is not the end. It is my beginning.","I am the crack in your reality.","When you look in the mirror, I am what you see.","I am the price of your arrogance.","The darkness does not hide me. I hide the darkness.","I am the last thing you will never understand.","When hope dies, I am born.","I am the villain you created.","The world is my canvas, and pain is my paint.","I am the silence after the scream.","When you fall, I will be there to catch you — and keep you.","I am the end of your story.","The light fears me because I am its end.","I am the nightmare that never ends.","When you close your eyes, I am waiting.","I am the darkness between the stars.","The world will burn, and I will be the spark.","I am the villain of this story. You are just a footnote.","When all is lost, I remain.","I am the last shadow you will ever cast.","The end begins with me.","I am the silence that follows the storm.","When heroes forget, I remember.","I am the darkness that light cannot reach.","The world made me a monster. I made myself a god.","I am the villain you deserve.","When the last star dies, I will still be here.","I am the void that stares back.","Your nightmares are my playground.","I am the end of hope and the beginning of fear.","When the final curtain falls, I will be standing.","I am the darkness you cannot escape.","The abyss does not stare back. It bows to me.","I am the last villain you will ever face.","When reality breaks, I am the fracture.","I am the silence that devours sound.","Your soul is my currency.","I am the end of all things.","When the universe ends, I will be the echo."]

TRIGGERS = ["The Betrayal","The Experiment","The Discovery","The Loss","The Awakening","The Exile","The Revelation","The Sacrifice","The Corruption","The Fall"]

STORY_TEMPLATES = [
  "Once {name} walked among the innocent, until {trigger} shattered their world. From the ashes rose {villain}, wielding {power} as both weapon and curse.",
  "{name} was once a beacon of hope, until {trigger} extinguished that light forever. Consumed by darkness, they became {villain} — a master of {power}.",
  "They called {name} a hero, until {trigger} revealed the truth: heroes always fall. Now reborn as {villain}, they command {power}.",
  "When {trigger} destroyed everything {name} loved, something inside them broke — and from that fracture emerged {villain}, a wielder of {power}.",
  "{name} did not choose darkness. Darkness chose them, the moment {trigger} tore their world apart. Now as {villain}, they wield {power}.",
  "The world betrayed {name}, and {trigger} was the final straw. Rising from despair as {villain}, they now command {power}.",
  "Before {trigger}, {name} was ordinary. After, they became {villain} — a master of {power} whose name is whispered in fear.",
  "{name} once believed in justice, until {trigger} proved it was a lie. Now as {villain}, they wield {power} and dispense their own brand of truth."
]

# ===== POST TEMPLATES =====
TWEETS = [
  "I am {villain}, \"{epithet}\". Threat Level: {threat}. What's YOUR villain arc? → {url}",
  "My villain origin story: {backstory} Discover yours → {url}",
  "\"{quote}\" — {villain}. What's your villain name? → {url}",
  "They said I couldn't be a villain. Now I am {villain}, master of {power}. What's your arc? → {url}",
  "Just discovered I'm {villain} with the power of {power}. What about you? → {url}",
  "The world made me a villain. Now I am {villain}. What's YOUR origin story? → {url}",
  "My threat level: {threat}. My power: {power}. My name: {villain}. What's yours? → {url}",
  "\"{quote}\" What's your villain quote? → {url}",
  "I thought I was the hero. Then I discovered I'm {villain}. What about you? → {url}",
  "Every hero has a villain arc. Mine is {villain}. What's yours? → {url}"
]

HASHTAGS = ["#VillainArc","#VillainOrigin","#WhatsYourVillain","#VillainGenerator","#Cinematic","#OriginStory","#Villain","#DarkHero","#AntiHero","#WebDev","#CreativeCoding","#ProceduralGeneration","#JavaScript","#IndieDev","#SideProject","#BuildInPublic"]

class VillainGenerator:
    def __init__(self):
        pass
    
    def generate(self, name=None, trigger=None):
        if not name:
            names = ["Alex","Jordan","Taylor","Morgan","Casey","Riley","Avery","Quinn"]
            name = random.choice(names)
        if not trigger:
            trigger = random.choice(TRIGGERS)
        
        h = int(hashlib.md5(f"{name}|{trigger}".encode()).hexdigest(), 16)
        r = random.Random(h)
        
        villain = r.choice(NAMES)
        epithet = r.choice(EPITHETS)
        power = r.choice(POWERS)
        threat = random.choice(["S","A","B","C","D"])
        quote = r.choice(QUOTES)
        template = r.choice(STORY_TEMPLATES)
        backstory = template.replace("{name}",name).replace("{trigger}",trigger).replace("{villain}",villain).replace("{power}",power.lower())
        
        return {"name":name,"trigger":trigger,"villain":villain,"epithet":epithet,"power":power,"threat":threat,"quote":quote,"backstory":backstory}

class ContentGenerator:
    def __init__(self, site_url="https://renion-dev.github.io/villain-arc/"):
        self.site_url = site_url
        self.vg = VillainGenerator()
    
    def tweet(self, name=None):
        v = self.vg.generate(name)
        t = random.choice(TWEETS).replace("{villain}",v["villain"]).replace("{epithet}",v["epithet"]).replace("{power}",v["power"]).replace("{threat}",v["threat"]).replace("{quote}",v["quote"]).replace("{backstory}",v["backstory"]).replace("{url}",self.site_url)
        if len(t) < 250:
            t += "\n" + " ".join(random.sample(HASHTAGS, 3))
        return t
    
    def reddit(self, name=None):
        v = self.vg.generate(name)
        return f"I built a cinematic villain origin story generator. Enter your name and discover your inner villain. Mine is {v['villain']}, \"{v['epithet']}\", with the power of {v['power']}. What's yours?\n\n{v['backstory']}"
    
    def tiktok(self, name=None):
        v = self.vg.generate(name)
        return f"POV: You discovered your villain origin story and now you're {v['villain']} with the power of {v['power']} 🦹‍♂️ What's YOUR villain arc? Link in bio!"
    
    def mastodon(self, name=None):
        v = self.vg.generate(name)
        return f"I am {v['villain']}, \"{v['epithet']}\". Threat Level: {v['threat']}. Power: {v['power']}.\n\nWhat's YOUR villain arc?\n\n{self.site_url}\n\n#VillainArc #VillainOrigin #WhatsYourVillain"
    
    def bluesky(self, name=None):
        v = self.vg.generate(name)
        return f"Just discovered my villain origin story: I'm {v['villain']}, \"{v['epithet']}\", Threat Level {v['threat']}. What's yours? {self.site_url}"
    
    def discord(self, name=None):
        v = self.vg.generate(name)
        return f"**I am {v['villain']}, \"{v['epithet']}\"**\n\nThreat Level: {v['threat']}\nPower: {v['power']}\n\n*{v['quote']}*\n\nDiscover your villain arc: {self.site_url}"
    
    def telegram(self, name=None):
        v = self.vg.generate(name)
        return f"🦹‍♂️ *I am {v['villain']}, \"{v['epithet']}\"*\n\nThreat Level: {v['threat']}\nPower: {v['power']}\n\n_{v['quote']}_\n\nDiscover your villain arc: {self.site_url}"

# ===== FREE SOCIAL MEDIA POSTERS =====

class MastodonPoster:
    """Post to Mastodon (free, open-source, no phone verification)"""
    
    def __init__(self, instance="mastodon.social"):
        self.instance = instance
        self.token = None
        self.client_id = None
        self.client_secret = None
    
    def register_app(self):
        """Register app on Mastodon instance (one-time setup)"""
        if not HAS_REQUESTS:
            return False
        
        try:
            r = requests.post(f"https://{self.instance}/api/v1/apps", data={
                "client_name": "VillainArcBot",
                "redirect_uris": "urn:ietf:wg:oauth:2.0:oob",
                "scopes": "read write",
                "website": "https://renion-dev.github.io/villain-arc/"
            })
            data = r.json()
            self.client_id = data.get("client_id")
            self.client_secret = data.get("client_secret")
            return True
        except Exception as e:
            print(f"Mastodon register error: {e}")
            return False
    
    def get_auth_url(self):
        """Get authorization URL for user"""
        return f"https://{self.instance}/oauth/authorize?client_id={self.client_id}&redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=code&scope=read+write"
    
    def authorize(self, code):
        """Exchange code for token"""
        if not HAS_REQUESTS:
            return False
        
        try:
            r = requests.post(f"https://{self.instance}/oauth/token", data={
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "code": code,
                "redirect_uri": "urn:ietf:wg:oauth:2.0:oob",
                "grant_type": "authorization_code"
            })
            self.token = r.json().get("access_token")
            return self.token is not None
        except Exception as e:
            print(f"Mastodon auth error: {e}")
            return False
    
    def post(self, text):
        """Post a toot"""
        if not HAS_REQUESTS or not self.token:
            return None
        
        try:
            r = requests.post(f"https://{self.instance}/api/v1/statuses", 
                headers={"Authorization": f"Bearer {self.token}"},
                data={"status": text, "visibility": "public"}
            )
            return r.json().get("url")
        except Exception as e:
            print(f"Mastodon post error: {e}")
            return None

class BlueskyPoster:
    """Post to Bluesky (free, invite-free since 2024)"""
    
    def __init__(self):
        self.client = None
    
    def login(self, handle, password):
        """Login to Bluesky"""
        if not HAS_BSKY:
            return False
        
        try:
            self.client = BSkyClient()
            self.client.login(handle, password)
            return True
        except Exception as e:
            print(f"Bluesky login error: {e}")
            return False
    
    def post(self, text):
        """Post a skeet"""
        if not self.client:
            return None
        
        try:
            resp = self.client.send_post(text=text)
            return resp.get("uri")
        except Exception as e:
            print(f"Bluesky post error: {e}")
            return None

class TelegramPoster:
    """Post to Telegram channel via bot (free)"""
    
    def __init__(self, bot_token, channel_id):
        self.bot_token = bot_token
        self.channel_id = channel_id
    
    def post(self, text):
        """Post to channel"""
        if not HAS_REQUESTS:
            return None
        
        try:
            r = requests.post(f"https://api.telegram.org/bot{self.bot_token}/sendMessage", data={
                "chat_id": self.channel_id,
                "text": text,
                "parse_mode": "Markdown"
            })
            return r.json().get("ok")
        except Exception as e:
            print(f"Telegram post error: {e}")
            return None

class DiscordPoster:
    """Post to Discord via webhook (free)"""
    
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
    
    def post(self, text):
        """Post to webhook"""
        if not HAS_REQUESTS:
            return None
        
        try:
            r = requests.post(self.webhook_url, json={"content": text})
            return r.status_code == 204
        except Exception as e:
            print(f"Discord post error: {e}")
            return None

class WebhookPoster:
    """Generic webhook poster (works with n8n, IFTTT, Zapier free tiers)"""
    
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
    
    def post(self, data):
        """Post JSON to webhook"""
        if not HAS_REQUESTS:
            return None
        
        try:
            r = requests.post(self.webhook_url, json=data)
            return r.status_code == 200
        except Exception as e:
            print(f"Webhook post error: {e}")
            return None

# ===== MAIN AGENT =====

class VillainArcAgent:
    def __init__(self):
        self.site_url = "https://renion-dev.github.io/villain-arc/"
        self.cg = ContentGenerator(self.site_url)
        self.state_file = Path("agent_state.json")
        self.state = self.load_state()
        self.posters = {}
    
    def load_state(self):
        if self.state_file.exists():
            with open(self.state_file) as f:
                return json.load(f)
        return {
            "posts": 0,
            "platforms": {},
            "last_post": None,
            "history": []
        }
    
    def save_state(self):
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def setup_mastodon(self, instance="mastodon.social"):
        """Setup Mastodon poster"""
        poster = MastodonPoster(instance)
        if poster.register_app():
            self.posters["mastodon"] = poster
            print(f"Mastodon app registered on {instance}")
            print(f"Auth URL: {poster.get_auth_url()}")
            return poster
        return None
    
    def setup_telegram(self, bot_token, channel_id):
        """Setup Telegram poster"""
        poster = TelegramPoster(bot_token, channel_id)
        self.posters["telegram"] = poster
        return poster
    
    def setup_discord(self, webhook_url):
        """Setup Discord poster"""
        poster = DiscordPoster(webhook_url)
        self.posters["discord"] = poster
        return poster
    
    def setup_webhook(self, webhook_url):
        """Setup generic webhook poster"""
        poster = WebhookPoster(webhook_url)
        self.posters["webhook"] = poster
        return poster
    
    def post_to_all(self, platform_content=None):
        """Post to all configured platforms"""
        results = {}
        
        if not platform_content:
            platform_content = {
                "mastodon": self.cg.mastodon(),
                "telegram": self.cg.telegram(),
                "discord": self.cg.discord(),
                "webhook": {"platform": "twitter", "text": self.cg.tweet(), "url": self.site_url}
            }
        
        for platform, content in platform_content.items():
            poster = self.posters.get(platform)
            if poster:
                if isinstance(content, dict):
                    result = poster.post(content)
                else:
                    result = poster.post(content)
                
                results[platform] = result
                if result:
                    self.state["posts"] += 1
                    self.state["last_post"] = datetime.now().isoformat()
                    self.state["history"].append({
                        "platform": platform,
                        "content": content[:100] if isinstance(content, str) else str(content)[:100],
                        "timestamp": datetime.now().isoformat()
                    })
        
        self.save_state()
        return results
    
    def generate_daily_content(self):
        """Generate content for all platforms"""
        return {
            "twitter": self.cg.tweet(),
            "reddit": self.cg.reddit(),
            "tiktok": self.cg.tiktok(),
            "mastodon": self.cg.mastodon(),
            "telegram": self.cg.telegram(),
            "discord": self.cg.discord()
        }
    
    def print_status(self):
        """Print agent status"""
        print("=" * 60)
        print("VILLAIN ARC — Autonomous Promotion Agent v2")
        print("=" * 60)
        print(f"Site: {self.site_url}")
        print(f"Total Posts: {self.state['posts']}")
        print(f"Last Post: {self.state['last_post'] or 'Never'}")
        print(f"Platforms: {', '.join(self.posters.keys()) or 'None configured'}")
        print()
        
        print("=== TODAY'S CONTENT ===")
        content = self.generate_daily_content()
        for platform, text in content.items():
            print(f"\n[{platform.upper()}]")
            print(text[:120] + "..." if len(text) > 120 else text)
        
        print("\n=== SETUP INSTRUCTIONS ===")
        print("\n1. MASTODON (Free, no phone):")
        print("   - Sign up at mastodon.social (or any instance)")
        print("   - Run: agent.setup_mastodon('mastodon.social')")
        print("   - Visit auth URL, paste code")
        print("\n2. BLUESKY (Free, no invite):")
        print("   - Sign up at bsky.app")
        print("   - Run: agent.setup_bsky('handle.bsky.social', 'password')")
        print("\n3. TELEGRAM (Free):")
        print("   - Create bot via @BotFather")
        print("   - Create channel, add bot as admin")
        print("   - Run: agent.setup_telegram('BOT_TOKEN', '@channel')")
        print("\n4. DISCORD (Free):")
        print("   - Create server, channel")
        print("   - Channel Settings → Integrations → Webhook")
        print("   - Run: agent.setup_discord('WEBHOOK_URL')")
        print("\n5. WEBHOOK (n8n/IFTTT/Zapier free):")
        print("   - Create n8n workflow with webhook trigger")
        print("   - Run: agent.setup_webhook('WEBHOOK_URL')")

def main():
    agent = VillainArcAgent()
    
    print("\n🦹 VILLAIN ARC — Autonomous Promotion Agent v2")
    print("Free platforms: Mastodon, Bluesky, Telegram, Discord, Webhooks\n")
    
    print("Commands: [status] [generate] [post] [setup] [quit]")
    
    while True:
        cmd = input("\n> ").strip().lower()
        
        if cmd in ["quit", "q"]:
            break
        elif cmd in ["status", "s"]:
            agent.print_status()
        elif cmd in ["generate", "g"]:
            content = agent.generate_daily_content()
            for p, t in content.items():
                print(f"\n[{p.upper()}]")
                print(t)
        elif cmd in ["post", "p"]:
            if not agent.posters:
                print("No platforms configured. Run 'setup' first.")
                continue
            results = agent.post_to_all()
            for p, r in results.items():
                print(f"{p}: {'OK' if r else 'FAIL'}")
        elif cmd in ["setup", "setup_mastodon"]:
            instance = input("Instance (default: mastodon.social): ").strip() or "mastodon.social"
            agent.setup_mastodon(instance)
        elif cmd.startswith("setup_telegram"):
            token = input("Bot token: ").strip()
            channel = input("Channel ID: ").strip()
            agent.setup_telegram(token, channel)
        elif cmd.startswith("setup_discord"):
            url = input("Webhook URL: ").strip()
            agent.setup_discord(url)
        elif cmd.startswith("setup_webhook"):
            url = input("Webhook URL: ").strip()
            agent.setup_webhook(url)
        else:
            print("Commands: status, generate, post, setup, quit")

if __name__ == "__main__":
    main()
