import base64
import os

font_dir = r"X:\Millionaire\ALfred-android\app\src\main\res\font"
out_dir = r"C:\Users\kumar\.gemini\antigravity\scratch\X7xenon"

with open(os.path.join(font_dir, "ndot57.otf"), "rb") as f:
    ndot57_b64 = base64.b64encode(f.read()).decode("ascii")

with open(os.path.join(font_dir, "ndot55.otf"), "rb") as f:
    ndot55_b64 = base64.b64encode(f.read()).decode("ascii")

font_css = f"""
    @font-face {{
      font-family: 'NDot57';
      src: url('data:font/opentype;base64,{ndot57_b64}') format('opentype');
      font-weight: bold;
    }}
    @font-face {{
      font-family: 'NDot55';
      src: url('data:font/opentype;base64,{ndot55_b64}') format('opentype');
      font-weight: normal;
    }}
"""

stats_svg = f"""<svg width="480" height="220" viewBox="0 0 480 220" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    {font_css}
    .bg {{ fill: #000000; stroke: #202025; stroke-width: 1px; rx: 16px; }}
    .ndot-title {{ font-family: 'NDot57', 'Space Mono', monospace; font-size: 13px; fill: #FFFFFF; letter-spacing: 2px; text-transform: uppercase; }}
    .ndot-num {{ font-family: 'NDot57', 'Space Mono', monospace; font-size: 28px; fill: #FFFFFF; letter-spacing: 1px; }}
    .ndot-num-red {{ font-family: 'NDot57', 'Space Mono', monospace; font-size: 28px; fill: #D71921; letter-spacing: 1px; }}
    .mono-sub {{ font-family: 'NDot55', 'Space Mono', monospace; font-size: 10px; fill: #71717A; letter-spacing: 1.5px; text-transform: uppercase; }}
    .pill-bg {{ fill: #0C0C0E; stroke: #222227; stroke-width: 1px; rx: 10px; }}
    .pill-text {{ font-family: 'NDot55', 'Space Mono', monospace; font-size: 9px; fill: #A1A1AA; letter-spacing: 1px; }}
    .pulse {{ animation: pulse 2s infinite ease-in-out; }}
    @keyframes pulse {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.3; }} }}
  </style>

  <!-- Card Frame -->
  <rect x="0.5" y="0.5" width="479" height="219" class="bg" />

  <!-- Header -->
  <circle cx="24" cy="28" r="4" fill="#D71921" />
  <text x="36" y="32" class="ndot-title">SYS // TELEMETRY ACTIVITY</text>
  
  <rect x="362" y="16" width="98" height="24" class="pill-bg" />
  <circle cx="374" cy=\"28\" r=\"3\" fill=\"#00E676\" class=\"pulse\" />
  <text x=\"384\" y=\"31\" class=\"pill-text\">LIVE // 120HZ</text>

  <!-- Divider -->
  <line x1=\"20\" y1=\"50\" x2=\"460\" y2=\"50\" stroke=\"#18181B\" stroke-width=\"1\" />

  <!-- Metric 1: Commits -->
  <g transform=\"translate(24, 75)\">
    <text x=\"0\" y=\"22\" class=\"ndot-num\">46</text>
    <text x=\"0\" y=\"40\" class=\"mono-sub\">COMMITS (2026)</text>
  </g>

  <!-- Metric 2: Stars -->
  <g transform=\"translate(142, 75)\">
    <text x=\"0\" y=\"22\" class=\"ndot-num\">04</text>
    <text x=\"0\" y=\"40\" class=\"mono-sub\">TOTAL STARS</text>
  </g>

  <!-- Metric 3: Repos -->
  <g transform=\"translate(254, 75)\">
    <text x=\"0\" y=\"22\" class=\"ndot-num\">05</text>
    <text x=\"0\" y=\"40\" class=\"mono-sub\">PUBLIC REPOS</text>
  </g>

  <!-- Metric 4: Rank -->
  <g transform=\"translate(372, 75)\">
    <text x=\"0\" y=\"22\" class=\"ndot-num-red\">A+</text>
    <text x=\"0\" y=\"40\" class=\"mono-sub\">SYSTEM RANK</text>
  </g>

  <!-- Divider -->
  <line x1=\"20\" y1=\"136\" x2=\"460\" y2=\"136\" stroke=\"#18181B\" stroke-width=\"1\" />

  <!-- Bottom Terminal Status Bar -->
  <rect x=\"20\" y=\"154\" width=\"440\" height=\"44\" class=\"pill-bg\" rx=\"8\" />
  <circle cx=\"36\" cy=\"176\" r=\"3\" fill=\"#D71921\" />
  <text x=\"48\" y=\"179\" class=\"mono-sub\" fill=\"#D4D4D8\">NODE: X7XENON // ARCH: SOVEREIGN AGENTS // DATA: LOCAL-FIRST</text>
</svg>"""

languages_svg = f"""<svg width="480" height="220" viewBox="0 0 480 220" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    {font_css}
    .bg {{ fill: #000000; stroke: #202025; stroke-width: 1px; rx: 16px; }}
    .ndot-title {{ font-family: 'NDot57', 'Space Mono', monospace; font-size: 13px; fill: #FFFFFF; letter-spacing: 2px; text-transform: uppercase; }}
    .mono-sub {{ font-family: 'NDot55', 'Space Mono', monospace; font-size: 10px; fill: #71717A; letter-spacing: 1.5px; text-transform: uppercase; }}
    .mono-lang {{ font-family: 'NDot57', 'Space Mono', monospace; font-size: 11px; fill: #FFFFFF; letter-spacing: 1.5px; }}
    .mono-pct {{ font-family: 'NDot57', 'Space Mono', monospace; font-size: 11px; fill: #A1A1AA; letter-spacing: 1px; }}
    .mono-desc {{ font-family: 'NDot55', 'Space Mono', monospace; font-size: 9px; fill: #52525B; letter-spacing: 1px; }}
    .pill-bg {{ fill: #0C0C0E; stroke: #222227; stroke-width: 1px; rx: 10px; }}
    .pill-text {{ font-family: 'NDot55', 'Space Mono', monospace; font-size: 9px; fill: #A1A1AA; letter-spacing: 1px; }}
  </style>

  <!-- Card Frame -->
  <rect x="0.5" y="0.5" width="479" height="219" class="bg" />

  <!-- Header -->
  <circle cx="24" cy="28" r="4" fill="#D71921" />
  <text x="36" y="32" class="ndot-title">SYS // LANGUAGE ALLOCATION</text>
  
  <rect x="374" y="16" width="86" height="24" class="pill-bg" />
  <text x="387" y="31" class="pill-text">TOTAL 100%</text>

  <!-- Multi-segment Progress Bar -->
  <g transform="translate(20, 52)">
    <!-- TypeScript segment: 56% -> 244px -->
    <rect x="0" y="0" width="244" height="8" rx="4" fill="#FFFFFF" />
    <!-- Python segment: 42% -> 182px -->
    <rect x="248" y="0" width="182" height="8" rx="4" fill="#00E676" />
    <!-- Other segment: 2% -> 6px -->
    <rect x="434" y="0" width="6" height="8" rx="3" fill="#D71921" />
  </g>

  <!-- Language 01: TypeScript -->
  <g transform="translate(24, 85)">
    <circle cx="4" cy="10" r="3.5" fill="#FFFFFF" />
    <text x="16" y="14" class="mono-lang">TYPESCRIPT</text>
    <text x="112" y="14" class="mono-pct">55.96%</text>
    <text x="175" y="14" class="mono-desc">// CREATOROS &amp; VIDEO AUTOMATION UI</text>
  </g>

  <!-- Language 02: Python -->
  <g transform="translate(24, 125)">
    <circle cx="4" cy="10" r="3.5" fill="#00E676" />
    <text x="16" y="14" class="mono-lang">PYTHON</text>
    <text x="112" y="14" class="mono-pct">41.91%</text>
    <text x="175" y="14" class="mono-desc">// APOLLO AGENTS &amp; VISION RUNTIMES</text>
  </g>

  <!-- Language 03: Native Mobile & Systems -->
  <g transform="translate(24, 165)">
    <circle cx="4" cy="10" r="3.5" fill="#D71921" />
    <text x="16" y="14" class="mono-lang">KOTLIN / RUST</text>
    <text x="112" y="14" class="mono-pct">NATIVE</text>
    <text x="175" y="14" class="mono-desc">// ALFRED OS &amp; NOTHING GLYPH AIDL IPC</text>
  </g>
</svg>"""

with open(os.path.join(out_dir, "stats.svg"), "w", encoding="utf-8") as f:
    f.write(stats_svg)

with open(os.path.join(out_dir, "languages.svg"), "w", encoding="utf-8") as f:
    f.write(languages_svg)

print("Generated Nothing Dot Style SVGs successfully!")
