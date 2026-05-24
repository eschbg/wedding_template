import re

with open("public/webcake-styles.css", "r", encoding="utf-8") as f:
    css = f.read()

ids = [
    "w-bc4iups4", # The quote (to delete)
    "w-qa4iudj9", # Divider line
    "w-xlffzoii", # SAVE THE DATE
    "w-2je4g75n", # 06.06.2026
    "w-l6nufaq3", # Polaroid left
    "w-y4tq64wq", # Polaroid right
    "w-yt01nt06", # White rectangle
    "w-5q0v20ee", # Center decoration
    "w-06fskfrb", # "D"
    "w-whvexl1r", # "N"
    "w-vd7mc3fa"  # The container
]

for el_id in ids:
    print(f"--- {el_id} ---")
    matches = re.findall(rf'#{el_id}\s*{{([^}}]+)}}', css)
    for m in matches:
        print(m.strip())
