# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

2025 경기도청 시상식 (2025 Gyeonggi Province Government Award Ceremony) - A single-page web application for displaying award recipients at an awards ceremony. Designed for large TV displays with cinematic visual effects.

## Development

**Local Development**: Use VS Code Live Server extension (configured on port 5501)

**Image Optimization**: Run `python optimize_images.py` to resize and compress images in the `images/` directory (outputs to `images/optimized/`)

## Architecture

### Single-File Application
The entire application is contained in `index.html`:
- **CSS** (~1300 lines): Animation-heavy styling with gold theme (`--gold: #d4af37`), responsive design, and TV-optimized layouts
- **HTML**: Two award categories with tab navigation, fullscreen overlay detail views, presentation mode UI
- **JavaScript** (~700 lines): Presentation engine with automatic slideshow, transitions, and keyboard controls

### Key UI Modes
1. **MainWall Mode** (`.mainwall-mode`): 10-person grid display for TV, activated by `body.mainwall-mode` class
2. **Card View**: 5-column interactive cards with hover expansion
3. **Overlay View**: Fullscreen detail view for individual recipients
4. **Presentation Mode**: Automated slideshow with intro, montage, spotlight phases, and end card

### Data Structure
Two data arrays in JavaScript:
- `executivesData`: 간부공무원 (Executive Officials) - 5 people
- `membersData`: 도의원 (Provincial Assembly Members) - 5 people

Each entry: `{ name, role, photo, reason }` where `reason` contains `<br>` separated quote strings

### Animation System
- CSS keyframes for transitions: `fadeIn`, `zoomIn`, `slideTransition`, `curtainLeft/Right`, `montageSweep`
- Particle effects: sparkles, gold particles, radial bloom
- Scene state machine: `sceneState` object controls presentation flow with phases (idle → intro → montage → spotlight → endcard)

### Key Functions
- `startPresentation()`: Initiates automated slideshow
- `showSpotlight(index)`: Displays individual recipient with progress bar
- `openOverlay()` / `closeOverlay()`: Manual detail view navigation
- `triggerCurtainWipe()`: TV-optimized transition effect

### External Dependencies
- Google Fonts: Nanum Myeongjo, Noto Sans KR
- UnicornStudio embed for animated background effects
