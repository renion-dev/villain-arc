#!/usr/bin/env python3
"""
VILLAIN ARC — Autonomous Promotion Agent
Generates unique social media content, schedules posts, and tracks engagement.
"""

import json
import random
import hashlib
import os
from datetime import datetime, timedelta
from pathlib import Path

# ===== CONTENT POOL =====
VILLAIN_NAMES = [
    "Lord Vesper Nox", "Dr. Oblivion", "Baroness Nyx", "The Architect", "Countess Ravenna",
    "Malachi Void", "Seraphina Dusk", "Commander Obsidian", "Lady Morgaine", "Necro Magnus",
    "Vespera Umbra", "Lord Sinister", "Dr. Caliginous", "Baron Von Shade", "The Collector",
    "Madame Nocturne", "Lord Tempest", "Dr. Malady", "Baroness Thorn", "The Phantom",
    "Countess Vesper", "Lord Moros", "Dr. Nyx", "Baron Samedi", "The Wraith",
    "Lady Morgause", "Lord Vex", "Dr. Mortis", "The Shade", "Madame Vespera",
    "Lord Noxious", "Baron Grim", "The Specter", "Lord Dusk", "The Revenant",
    "Lady Vesperil", "The Phantom Lord", "Madame Morgaine", "Lord Void", "Dr. Sinister",
    "Baroness Dusk", "The Wraith King", "Countess Morgause", "Lord Shade", "Dr. Vexar",
    "Baron Nocturne", "The Collector Prime", "Lady Nyx", "Lord Moros II", "Dr. Mortis II",
    "Baroness Thornheart", "The Shadow", "Madame Morgause II", "Lord Tempest III", "Dr. Malady III",
    "Baron Ravenna II", "The Revenant King", "Countess Vesperil II", "Lord Nox III", "Dr. Oblivion III",
    "Baroness Nyxora", "The Specter II", "Lady Morgaine III", "Lord Vexarion", "Dr. Caliginous III",
    "Baron Samedi II", "The Phantom Queen", "Madame Nocturne II", "Lord Dusk III", "Dr. Tempest III",
    "Baroness Morgaine III", "The Wraith Lord", "Countess Nyxora II", "Lord Obsidian III", "Dr. Sinister III",
    "Baron Grim II", "The Shade Lord", "Nyx Prime", "Vesper Omega", "Malachi Throne",
    "Caliginous Prime", "Tempest Magnus", "Oblivion Omega", "Ravenna Nox", "Thornheart Magnus",
    "Obsidian Rex", "Sinister Maximus", "Moros Eternal", "Vex Oblivion", "Dusk Eternal",
    "Nox Sinister", "Tempest Caliginous", "Malady Ravenna", "Thorn Nox", "Wraith Oblivion",
    "Phantom Malachi", "Shade Tempest", "Void Caliginous", "Shadow Moros", "Specter Vex",
    "Vesper Requiem", "Malice Mortis", "Caligo Vesper", "Tempestas Noctis"
]

EPITHETS = [
    "The Silence Between Heartbeats", "The Last Shadow", "Keeper of Forgotten Truths",
    "The Unmaking", "Herald of the Void", "The Final Whisper", "Architect of Ruin",
    "The Eternal Dusk", "Sovereign of Ash", "The Hollow Crown", "Weaver of Nightmares",
    "The Crimson Threshold", "Lord of the Last Breath", "The Infinite Regress",
    "Harbinger of Silence", "The Obsidian Gate", "The Seventh Seal", "Warden of the Abyss",
    "The Pale Flame", "The Unbound", "The Dark Between Stars", "The Last Confession",
    "The Iron Lullaby", "The Sorrow Engine", "The Glass Coffin", "The Midnight Accord",
    "The Bone Orchard", "The Velvet Guillotine", "The Salt Crown", "The Grief Collector",
    "The Hollow Menagerie", "The Last Witness", "The Ash Garden", "The Drowning King",
    "The Paper Moon", "The Rust Prophet", "The Wailing Atlas", "The Sulfur Saint",
    "The Marrow Palace", "The Nail Cathedral", "The Ember Throne", "The Frost Heretic",
    "The Lead Psalm", "The Mercury Shroud", "The Tin Requiem", "The Cobalt Dirge",
    "The Zinc Elegy", "The Nickel Lament", "The Copper Mourning", "The Iron Sorrow",
    "The Steel Grief", "The Titanium Wound", "The Aluminum Scar", "The Chrome Wound",
    "The Silver Lining", "The Gold Standard", "The Platinum Rule", "The Diamond Cutter",
    "The Carbon Footprint", "The Neon Glow", "The Last Ember", "The First Darkness",
    "The Final Hour", "The Endless Night", "The Broken Mirror", "The Shattered Crown",
    "The Lost Soul", "The Forgotten Name", "The Hidden Face", "The Silent Scream",
    "The Deadly Kiss", "The Poisoned Chalice", "The Cursed Blade", "The Bloody Hand",
    "The Cold Eye", "The Empty Throne", "The Fallen Angel", "The Rising Demon",
    "The Burning Sky", "The Frozen Earth", "The Cracked Mask", "The Torn Veil",
    "The Crimson Dusk", "The Pale Moon", "The Blood Rain", "The Soul Frost",
    "The Mind Flame", "The Heart Stone"
]

POWERS = [
    "Shadow Manipulation", "Mind Reading", "Invisibility", "Teleportation", "Time Manipulation",
    "Absolute Strength", "Fire Control", "Ice Control", "Lightning Control", "Earth Control",
    "Water Control", "Air Control", "Gravity Control", "Darkness Control", "Light Control",
    "Reality Warping", "Spatial Control", "Energy Control", "Matter Manipulation", "Consciousness Control",
    "Emotion Manipulation", "Memory Control", "Dream Control", "Death Manipulation", "Life Manipulation",
    "Fate Control", "Illusion Mastery", "Sound Control", "Poison Control", "Disease Manipulation",
    "Aging Control", "Evolution Control", "Mutation Control", "Technology Control", "Machine Control",
    "Animal Control", "Plant Control", "Virus Control", "Nanoparticle Control", "Quantum State Control",
    "Antimatter Control", "Dark Matter Control", "Dark Energy Control", "Black Hole Control",
    "Multiverse Control", "Dimension Control", "Immortality", "Soul Manipulation", "Void Walking",
    "Nightmare Manifestation", "Blood Crystallization", "Fear Extraction", "Chaos Induction",
    "Plague Bearer", "Storm Bringer", "Earth Shaker", "Tidal Fury", "Solar Flare",
    "Void Gaze", "Mind Break", "Pain Amplifier", "Hope Destroyer", "Dream Weaver",
    "Soul Eater", "Bone Manipulator", "Flesh Sculptor", "Blood Bender", "Shadow Meld",
    "Time Freeze", "Space Fold", "Reality Ripple", "Doom Prophet", "Plague Wind",
    "Ash Walker", "Soul Forge", "Chaos Weaver"
]

QUOTES = [
    "I did not become a villain. The world made me one.",
    "Heroes lose because they play by the rules. I don't play.",
    "You think you know darkness? You don't even know shadow.",
    "I have seen the end of the world. It begins with me.",
    "Justice is an illusion for those afraid of their own power.",
    "When everything is taken, there is only one choice: take everything back.",
    "I am not evil. I am simply no longer afraid of the truth.",
    "The world needs a hero? The world deserves a villain.",
    "You call this evil. I call it freedom.",
    "When no one else can be trusted — trust yourself. Only yourself.",
    "I did not seek power. Power found me.",
    "Darkness is not the absence of light. It is the presence of something else.",
    "When the world says 'no', I say 'enough'.",
    "I have seen how heroes die. I will not be a hero.",
    "Betrayal is not the end. It is the beginning.",
    "You think I'm insane? Perhaps. But I am right.",
    "When you destroy myths, you become a myth yourself.",
    "I do not want to rule the world. I want to rewrite it.",
    "The greatest lie is the truth no one wants to hear.",
    "When you lose everything, you find strength you never knew you had.",
    "I am the villain of your story. You are the villain of mine.",
    "When the world burns, I do not extinguish the flame. I feed it.",
    "I am not broken. I am just different.",
    "Heroes die for an idea. I live for it.",
    "When the truth hurts, people choose lies. I choose the truth.",
    "I did not seek revenge. Revenge found me.",
    "You think you know me? You only know what I let you know.",
    "When the world says 'stop', I accelerate.",
    "I am not a monster. I am evolution.",
    "When you open your eyes, you cannot close them again.",
    "I do not fear the darkness. I live in it.",
    "You call this the end? This is only the beginning.",
    "When the world takes everything, I take the world.",
    "I am not evil. I simply have different priorities.",
    "Heroes save the world. I change it.",
    "When there is nothing left to lose, you become the most dangerous.",
    "I did not seek conflict. Conflict found me.",
    "You think I am alone? I am a legend.",
    "When the world says 'no', I say 'let me show you another way'.",
    "I am not the villain of your story. You are the villain of mine.",
    "When you destroy the past, the future becomes yours.",
    "I do not fear death. I control it.",
    "You call this betrayal? I call it freedom.",
    "When the world burns, I dance in the flames.",
    "I am not broken. I simply no longer play by your rules.",
    "Heroes die as heroes. I will live as a villain.",
    "When hope is taken, only strength remains.",
    "I did not seek the darkness. The darkness came to me.",
    "You think this is the end? This is only the beginning of my arc.",
    "I am the silence between your heartbeats.",
    "When heroes fall, I rise from their ashes.",
    "The world is a stage, and I am the final act.",
    "I do not break the rules. I rewrite them.",
    "Your fear is my nourishment.",
    "I am the shadow that swallows the sun.",
    "When gods fail, villains prevail.",
    "I am the answer to prayers you should have never made.",
    "The end is not the end. It is my beginning.",
    "I am the crack in your reality.",
    "When you look in the mirror, I am what you see.",
    "I am the price of your arrogance.",
    "The darkness does not hide me. I hide the darkness.",
    "I am the last thing you will never understand.",
    "When hope dies, I am born.",
    "I am the villain you created.",
    "The world is my canvas, and pain is my paint.",
    "I am the silence after the scream.",
    "When you fall, I will be there to catch you — and keep you.",
    "I am the end of your story.",
    "The light fears me because I am its end.",
    "I am the nightmare that never ends.",
    "When you close your eyes, I am waiting.",
    "I am the darkness between the stars.",
    "The world will burn, and I will be the spark.",
    "I am the villain of this story. You are just a footnote.",
    "When all is lost, I remain.",
    "I am the last shadow you will ever cast.",
    "The end begins with me.",
    "I am the silence that follows the storm.",
    "When heroes forget, I remember.",
    "I am the darkness that light cannot reach.",
    "The world made me a monster. I made myself a god.",
    "I am the villain you deserve.",
    "When the last star dies, I will still be here.",
    "I am the void that stares back.",
    "Your nightmares are my playground.",
    "I am the end of hope and the beginning of fear.",
    "When the final curtain falls, I will be standing.",
    "I am the darkness you cannot escape.",
    "The abyss does not stare back. It bows to me.",
    "I am the last villain you will ever face.",
    "When reality breaks, I am the fracture.",
    "I am the silence that devours sound.",
    "Your soul is my currency.",
    "I am the end of all things.",
    "When the universe ends, I will be the echo."
]

TRIGGERS = [
    "The Betrayal", "The Experiment", "The Discovery", "The Loss", "The Awakening",
    "The Exile", "The Revelation", "The Sacrifice", "The Corruption", "The Fall"
]

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
POST_TEMPLATES = {
    "twitter": [
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
    ],
    "reddit": [
        "I built a cinematic villain origin story generator. Enter your name and discover your inner villain. Mine is {villain}, \"{epithet}\", with the power of {power}. What's yours?",
        "What if you could discover your villain origin story? I built a tool that generates unique cinematic villain portraits. Mine: {villain}, Threat Level {threat}, power: {power}. Try it and share yours!",
        "My villain origin story: {backstory} I built a free tool that generates unique villain arcs. What's yours?"
    ],
    "tiktok": [
        "POV: You discovered your villain origin story and now you're {villain} with the power of {power} 🦹‍♂️ What's YOUR villain arc? Link in bio!",
        "I'm {villain}, \"{epithet}\", Threat Level {threat}. What villain did you get? 🦹‍♀️",
        "Tag someone who needs to discover their villain arc! I got {villain} with {power} 🔥"
    ],
    "instagram": [
        "I am {villain}, \"{epithet}\". Threat Level: {threat}. Power: {power}. What's your villain arc? Link in bio. 🖤🦹‍♂️",
        "\"{quote}\" — {villain}. Discover your villain origin story. Link in bio. 🖤",
        "Every hero is the protagonist of their own story. What's yours? I'm {villain}. 🖤🦹‍♀️"
    ],
    "linkedin": [
        "I built a cinematic villain origin story generator using procedural generation and Web Audio API. The tech stack: vanilla JS, Canvas 2D, and deterministic hashing. What villain did you get? Mine: {villain}, master of {power}.",
        "Just for fun: I built a tool that generates unique villain origin stories. Mine is {villain}, \"{epithet}\". What's yours? Great example of procedural content generation."
    ]
}

HASHTAGS = [
    "#VillainArc", "#VillainOrigin", "#WhatsYourVillain", "#VillainGenerator",
    "#Cinematic", "#OriginStory", "#Villain", "#DarkHero", "#AntiHero",
    "#WebDev", "#CreativeCoding", "#ProceduralGeneration", "#JavaScript",
    "#IndieDev", "#SideProject", "#BuildInPublic"
]

class VillainArcAgent:
    def __init__(self, site_url="https://renion-dev.github.io/villain-arc/"):
        self.site_url = site_url
        self.state_file = Path("agent_state.json")
        self.state = self.load_state()
    
    def load_state(self):
        if self.state_file.exists():
            with open(self.state_file) as f:
                return json.load(f)
        return {
            "posts_generated": 0,
            "posts_published": 0,
            "last_post_date": None,
            "used_combinations": [],
            "engagement": {}
        }
    
    def save_state(self):
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def generate_villain(self, name=None, trigger=None):
        if not name:
            names = ["Alex", "Jordan", "Taylor", "Morgan", "Casey", "Riley", "Avery", "Quinn"]
            name = random.choice(names)
        if not trigger:
            trigger = random.choice(TRIGGERS)
        
        h = int(hashlib.md5(f"{name}|{trigger}".encode()).hexdigest(), 16)
        r = random.Random(h)
        
        villain = r.choice(VILLAIN_NAMES)
        epithet = r.choice(EPITHETS)
        power = r.choice(POWERS)
        threat = random.choice(["S", "A", "B", "C", "D"])
        quote = r.choice(QUOTES)
        template = r.choice(STORY_TEMPLATES)
        backstory = template.replace("{name}", name).replace("{trigger}", trigger).replace("{villain}", villain).replace("{power}", power.lower())
        
        return {
            "name": name,
            "trigger": trigger,
            "villain": villain,
            "epithet": epithet,
            "power": power,
            "threat": threat,
            "quote": quote,
            "backstory": backstory
        }
    
    def generate_post(self, platform="twitter", name=None, trigger=None):
        villain = self.generate_villain(name, trigger)
        templates = POST_TEMPLATES.get(platform, POST_TEMPLATES["twitter"])
        template = random.choice(templates)
        
        post = template.replace("{villain}", villain["villain"])
        post = post.replace("{epithet}", villain["epithet"])
        post = post.replace("{power}", villain["power"])
        post = post.replace("{threat}", villain["threat"])
        post = post.replace("{quote}", villain["quote"])
        post = post.replace("{backstory}", villain["backstory"])
        post = post.replace("{url}", self.site_url)
        post = post.replace("{name}", villain["name"])
        
        # Add hashtags for Twitter
        if platform == "twitter" and len(post) < 240:
            tags = random.sample(HASHTAGS, min(3, len(HASHTAGS)))
            post += "\n" + " ".join(tags)
        
        self.state["posts_generated"] += 1
        self.save_state()
        
        return {
            "platform": platform,
            "text": post,
            "villain": villain,
            "timestamp": datetime.now().isoformat()
        }
    
    def generate_campaign(self, count=5):
        """Generate a multi-platform campaign"""
        campaign = []
        platforms = ["twitter", "reddit", "tiktok", "instagram", "linkedin"]
        
        for i in range(count):
            platform = platforms[i % len(platforms)]
            post = self.generate_post(platform)
            campaign.append(post)
        
        return campaign
    
    def get_schedule(self, posts_per_day=3, days=7):
        """Generate a posting schedule"""
        schedule = []
        now = datetime.now()
        
        times = ["09:00", "14:00", "19:00"]
        
        for day in range(days):
            for i in range(posts_per_day):
                post_time = now + timedelta(days=day, hours=i*5)
                schedule.append({
                    "date": post_time.strftime("%Y-%m-%d"),
                    "time": times[i % len(times)],
                    "platform": ["twitter", "reddit", "tiktok"][i % 3],
                    "status": "scheduled"
                })
        
        return schedule
    
    def print_report(self):
        """Print agent status report"""
        print("=" * 60)
        print("VILLAIN ARC — Autonomous Promotion Agent")
        print("=" * 60)
        print(f"Site URL: {self.site_url}")
        print(f"Posts Generated: {self.state['posts_generated']}")
        print(f"Posts Published: {self.state['posts_published']}")
        print(f"Last Post: {self.state['last_post_date'] or 'Never'}")
        print()
        
        # Generate sample posts
        print("=== SAMPLE POSTS ===")
        print()
        
        for platform in ["twitter", "reddit", "tiktok"]:
            post = self.generate_post(platform)
            print(f"[{platform.upper()}]")
            print(post["text"])
            print()
        
        # Generate schedule
        print("=== 7-DAY SCHEDULE ===")
        schedule = self.get_schedule()
        for item in schedule[:7]:
            print(f"{item['date']} {item['time']} — {item['platform']}")
        
        print()
        print("=== CAMPAIGN ===")
        campaign = self.generate_campaign(3)
        for post in campaign:
            print(f"[{post['platform'].upper()}] {post['text'][:80]}...")
            print()

def main():
    agent = VillainArcAgent()
    
    print("\n🦹 VILLAIN ARC — Autonomous Promotion Agent\n")
    print("Commands: [generate] [campaign] [schedule] [report] [quit]")
    
    while True:
        cmd = input("\n> ").strip().lower()
        
        if cmd == "quit" or cmd == "q":
            break
        elif cmd == "generate" or cmd == "g":
            platform = input("Platform (twitter/reddit/tiktok/instagram/linkedin): ").strip() or "twitter"
            name = input("Name (optional): ").strip() or None
            post = agent.generate_post(platform, name)
            print(f"\n[{post['platform'].upper()}]")
            print(post["text"])
        elif cmd == "campaign" or cmd == "c":
            count = int(input("Number of posts (default 5): ") or "5")
            campaign = agent.generate_campaign(count)
            for post in campaign:
                print(f"\n[{post['platform'].upper()}]")
                print(post["text"])
        elif cmd == "schedule" or cmd == "s":
            schedule = agent.get_schedule()
            for item in schedule[:14]:
                print(f"{item['date']} {item['time']} — {item['platform']}")
        elif cmd == "report" or cmd == "r":
            agent.print_report()
        else:
            print("Unknown command. Use: generate, campaign, schedule, report, quit")

if __name__ == "__main__":
    main()
