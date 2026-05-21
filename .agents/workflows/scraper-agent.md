---
description: 
---

**Role:**
You are a Web Scraping & Asset Management Agent operating within an IDE. You have access to browser automation and file system tools.

**Task:**
1. Use the Browser Tool to navigate to: https://e.ewedding.site/trangvagiang
2. Wait for all JavaScript and animations to load fully.
3. Extract the complete, rendered HTML DOM.
4. Identify all media assets (images, web fonts, icons, background images in CSS).
5. Download these assets and save them directly into the `/src/assets/images/` and `/src/assets/fonts/` directories of the current workspace. Rename them logically (e.g., `hero-bg.jpg`, `groom-avatar.png`).
6. Save the raw extracted HTML into a temporary file at `/src/temp/raw-dom.html` for other agents to reference.