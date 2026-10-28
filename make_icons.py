import os, shutil
from PIL import Image, ImageDraw
res = "android/app/src/main/res"
src = Image.open("icon.png").convert("RGB")
sizes = {"mdpi": 48, "hdpi": 72, "xhdpi": 96, "xxhdpi": 144, "xxxhdpi": 192}
# remove adaptive icons so the plain PNG icons are used everywhere
shutil.rmtree(os.path.join(res, "mipmap-anydpi-v26"), ignore_errors=True)
for d in sizes:
    for f in ("ic_launcher_foreground.png",):
        p = os.path.join(res, "mipmap-" + d, f)
        if os.path.exists(p): os.remove(p)
for d, s in sizes.items():
    out = os.path.join(res, "mipmap-" + d); os.makedirs(out, exist_ok=True)
    im = src.resize((s, s), Image.LANCZOS)
    im.save(os.path.join(out, "ic_launcher.png"))
    m = Image.new("L", (s * 4, s * 4), 0)
    ImageDraw.Draw(m).ellipse((0, 0, s * 4 - 1, s * 4 - 1), fill=255)
    m = m.resize((s, s), Image.LANCZOS)
    r = Image.new("RGBA", (s, s), (0, 0, 0, 0)); r.paste(im, (0, 0), m)
    r.save(os.path.join(out, "ic_launcher_round.png"))
print("icons done")
