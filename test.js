const fs = require('fs');
const html = fs.readFileSync('/home/ihor/villain-arc/index.html', 'utf8');

function extractArray(name, str) {
  const regex = new RegExp(`const ${name}\\s*=\\s*\\[([^\\]]+)\\]`);
  const match = str.match(regex);
  if (!match) return [];
  return match[1].replace(/['"]/g, '').split(',').map(s => s.trim()).filter(Boolean);
}

const NAMES = extractArray('NAMES', html);
const EPITHETS = extractArray('EPITHETS', html);
const POWERS = extractArray('POWERS', html);
const QUOTES = extractArray('QUOTES', html);

console.log('=== CONTENT STATS ===');
console.log(`Names: ${NAMES.length}`);
console.log(`Epithets: ${EPITHETS.length}`);
console.log(`Powers: ${POWERS.length}`);
console.log(`Quotes: ${QUOTES.length}`);
console.log(`Total: ${NAMES.length + EPITHETS.length + POWERS.length + QUOTES.length}`);

function hash(s) { let h = 0x811c9dc5; for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 0x01000193); } return h >>> 0; }
function rng(s) { return () => { s += 0x6D2B79F5; s = Math.imul(s ^ s >>> 15, s | 1); s ^= s + Math.imul(s ^ s >>> 7, s | 61); return ((s ^ s >>> 14) >>> 0) / 4294967296; }; }
function pick(a, r) { return a[Math.floor(r() * a.length)]; }

function generate(name, trigger) {
  const h = hash(name.toLowerCase() + '|' + trigger);
  const r = rng(h);
  return { villainName: pick(NAMES, r), epithet: pick(EPITHETS, r), power: pick(POWERS, r), threat: pick([{l:'S',n:'Existential'},{l:'A',n:'Apocalyptic'},{l:'B',n:'Catastrophic'},{l:'C',n:'Dangerous'},{l:'D',n:'Dormant'}], r), quote: pick(QUOTES, r) };
}

console.log('\n=== DETERMINISM TEST ===');
const r1 = generate('Ihor', 'The Awakening');
const r2 = generate('Ihor', 'The Awakening');
console.log(`Same input, same output: ${r1.villainName === r2.villainName && r1.epithet === r2.epithet ? 'PASS' : 'FAIL'}`);

console.log('\n=== UNIQUENESS TEST (50 names) ===');
const uN = new Set(), uE = new Set(), uP = new Set(), uQ = new Set();
for (let i = 0; i < 50; i++) { const r = generate('Name' + i, 'The Awakening'); uN.add(r.villainName); uE.add(r.epithet); uP.add(r.power); uQ.add(r.quote); }
console.log(`Names: ${uN.size}/50 (${uN.size >= 40 ? 'PASS' : 'WEAK'})`);
console.log(`Epithets: ${uE.size}/50 (${uE.size >= 40 ? 'PASS' : 'WEAK'})`);
console.log(`Powers: ${uP.size}/50 (${uP.size >= 40 ? 'PASS' : 'WEAK'})`);
console.log(`Quotes: ${uQ.size}/50 (${uQ.size >= 40 ? 'PASS' : 'WEAK'})`);

console.log('\n=== HTML VALIDITY ===');
const checks = [
  ['Canvas', html.includes('<canvas id="stage-canvas">')],
  ['Input', html.includes('id="name-input"')],
  ['Reveal btn', html.includes('id="btn-reveal"')],
  ['Daily btn', html.includes('id="b-daily"')],
  ['Nemesis btn', html.includes('id="b-nemesis"')],
  ['Gallery btn', html.includes('id="b-gallery"')],
  ['Awards btn', html.includes('id="b-awards"')],
  ['Share btn', html.includes('id="b-share"')],
  ['Rec btn', html.includes('id="b-rec"')],
  ['Down btn', html.includes('id="b-down"')],
  ['Audio', html.includes('initAudio')],
  ['Particles', html.includes('class P')],
  ['Embers', html.includes('class E')],
  ['Portrait', html.includes('function drawPort')],
  ['State', html.includes('function load()')],
  ['Achievements', html.includes('function checkAch')],
  ['Nemesis', html.includes('function startNemesis')],
  ['Daily', html.includes('function dailyVillain')],
  ['Gallery', html.includes('function showGallery')],
  ['Video', html.includes('MediaRecorder')],
  ['Download', html.includes('shareDownload')],
  ['Copy', html.includes('shareCopy')],
  ['Twitter', html.includes('shareTwitter')],
];
checks.forEach(([n, ok]) => console.log(`${ok ? 'OK' : 'FAIL'} ${n}`));

console.log('\n=== FILE SIZE ===');
console.log(`HTML: ${(html.length / 1024).toFixed(1)} KB`);
