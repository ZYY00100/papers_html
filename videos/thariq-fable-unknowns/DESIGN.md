# Design System

## Overview

Apple-like editorial publication. The visual identity is light, restrained, and information-dense — closer to a printed long-form magazine than a SaaS landing page. Layout is single-column centered (712px content width), white cards floating on a faint gray gridded canvas (#F5F5F7 with a repeating 80px linear-gradient grid at 0.024 opacity). Type hierarchy pairs a Western serif (Cormorant Garamond) for major display with a Chinese serif (Noto Serif SC) for body — a deliberate cross-cultural editorial mix. Motion is minimal: subtle fades, no parallax, no flashy transitions. Tone is authoritative, calm, almost academic.

## Colors

- **Canvas Background**: `#F5F5F7` — page background, with 80px grid overlay at 0.024 opacity.
- **Card Surface**: `#FFFFFF` — white content cards floating on canvas.
- **Primary Text**: `#1D1D1F` — display headings, important body text.
- **Secondary Text**: `#4A4A4F` — body copy default.
- **Muted Text**: `#8A8A8E` — meta labels, captions, timestamps.
- **Accent Red**: `#C8161D` — active EN button, key links, source attribution.
- **Accent Gold**: `#C9A962` / dim `#B08D4A` — numbered section prefixes (01, 02, 03, 04).
- **Code Background**: `#0E0E10` — dark code/prompt card backgrounds with `#E8E8EA` text.
- **Border Subtle**: `#E5E5E8` — 1px dividers, card outlines.

## Typography

- **Display Serif (EN)**: Cormorant Garamond, weight 500, 48px / 57.6px line, letter-spacing -0.48px. Major page titles.
- **Heading Serif (EN)**: Cormorant Garamond, weight 500, 32px. Section H2s.
- **Body Serif (CN)**: Noto Serif SC, weight 300, 22px / 33px line, letter-spacing 0.44px. Chinese body copy and H3s.
- **Sans Body**: Inter, weight 400, 14.5px. Links, navigation, secondary UI.
- **Monospace**: JetBrains Mono, weight 400–500, 14.5px. Code blocks, command snippets.
- **Label (Rajdhani)**: Rajdhani, weight 600, 11px, letter-spacing 2.2px, uppercase. Section kickers like `CLAUDE CODE · LOOP DESIGN`, numbered prefixes `01 OVERVIEW`.

## Elevation

Almost flat. Cards float on the canvas via a layered soft shadow (`0 1px 3px rgba(0,0,0,0.06)` + `0 4px 16px rgba(0,0,0,0.04)`); a deeper shadow (`0 4px 24px rgba(0,0,0,0.15)`) lifts the dark code blocks. No glassmorphism, no glows. The page itself uses a barely-visible 80px grid as the only ambient texture. Separation between sections comes from generous vertical whitespace (180–250px), not borders or background shifts.

## Components

- **Editorial Cover**: centered title block, small kicker label above, source line below, all on bare canvas. No hero image — the cover image sits in a separate white card below the title block.
- **Numbered Section Header**: large gold Rajdhani numeral (`02` / `03` / `04`) paired with a small uppercase label and a Cormorant Garamond H2 to the right.
- **Comparison Table**: white card with a clean 4-column grid (Loop / 你交给什么 / 什么时候用 / 关键工具), generous row spacing, no zebra striping.
- **Prompt Card**: dark `#0E0E10` background, `#E8E8EA` JetBrains Mono text, soft `0 4px 24px` shadow, 8px radius. EN/中文 toggle pill row at top with red active state.
- **Image Caption Block**: small uppercase Rajdhani label above the image (e.g. `原文配图 · 目标制循环`), plus a muted byline line below in `8A8A8E`.
- **Inline Diagram Cards**: the original Delba Oliveira illustrations — thin black-line hand-drawn loop diagrams on white, very technical and minimal.
- **Source Footer**: plain muted list of credits with red links to source URLs and Claude Code docs.

## Do's and Don'ts

### Do's

- Use Cormorant Garamond for any English display heading (≥32px) and Noto Serif SC for Chinese body.
- Use Rajdhani uppercase with 2.2px letter-spacing for kickers and numbered prefixes — this is the signature.
- Keep backgrounds at `#F5F5F7` (canvas) or `#FFFFFF` (card). Use `#0E0E10` only for code/prompt blocks.
- Use gold `#C9A962` ONLY for the leading `01`–`08` numerals. Don't apply it to body text or icons.
- Use red `#C8161D` sparingly: active states, the EN pill, key source links.

### Don'ts

- Don't introduce new fonts. Stick to the 5-font system (Cormorant / Inter / JetBrains / Noto / Rajdhani).
- Don't use rounded pill buttons or large CTAs — this site has none. The site is read-first, not act-first.
- Don't add decorative gradients, glows, or particle effects — the source is flat editorial.
- Don't use saturated colors. The palette stays in the warm-neutral + red/gold accent range.
- Don't break the 712px content column. Video compositions may re-frame for landscape, but the proportions should remain readable and centered.