from pathlib import Path

root = Path("gravity/src")

def replace(path, pairs):
    p = root / path
    s = p.read_text()
    for old, new in pairs:
        if old not in s:
            raise SystemExit(f"Expected source text not found in {path}: {old[:70]}")
        s = s.replace(old, new)
    p.write_text(s)

replace("styles.css", [
    ("color:#eaf6ff;background:#050b16", "color:#f2fbff;background:#102331"),
    ("body{background:#050b16}", "body{background:#102331}"),
    ("background:linear-gradient(180deg,rgba(3,8,17,.58),transparent 24%,transparent 72%,rgba(3,8,17,.72)),radial-gradient(ellipse at 50% 46%,transparent 38%,rgba(2,6,13,.42) 100%)", "background:linear-gradient(180deg,rgba(7,20,29,.18),transparent 22%,transparent 78%,rgba(7,20,29,.22)),radial-gradient(ellipse at 50% 46%,transparent 58%,rgba(7,20,29,.12) 100%)"),
    ("background:radial-gradient(ellipse at 50% 44%,rgba(12,36,58,.65),rgba(3,8,17,.88) 65%)", "background:radial-gradient(ellipse at 50% 42%,rgba(39,83,101,.78),rgba(10,27,39,.90) 78%)"),
    ("background:#050b16;color:#ff8c9c", "background:#102331;color:#ff8c9c"),
    ("background:#091827bb;color:#c9edff", "background:#17394acc;color:#f0fbff"),
    ("background:#091827bb;color:#a9dff7", "background:#17394acc;color:#e3f7ff"),
    ("background:#071624bb;border:1px solid #24425b", "background:#17394acc;border:1px solid #6b9bb2"),
    ("color:#8ab6d2", "color:#c4e5f2"),
    ("color:#6c8ca8", "color:#a9c9d8"),
    ("color:#6789a5", "color:#9bbbc9"),
    ("color:#3e5c76", "color:#789eaf"),
    ("color:#7498b5", "color:#a8c8d7"),
    ("color:#82a8c5", "color:#b4d4e2"),
])

replace("SceneManager.ts", [
    ("new THREE.Color(0x050b16)", "new THREE.Color(0x183746)"),
    ("new THREE.FogExp2(0x050b16, .025)", "new THREE.FogExp2(0x183746, .008)"),
    ("this.renderer.toneMappingExposure = 1.2;", "this.renderer.toneMappingExposure = 1.35;"),
    ("new THREE.HemisphereLight(0x9bc9ff, 0x101321, 1.3)", "new THREE.HemisphereLight(0xd8f4ff, 0x496675, 2.0)"),
    ("new THREE.DirectionalLight(0xc5e6ff, 2.2)", "new THREE.DirectionalLight(0xffffff, 2.8)"),
    ("new THREE.PointLight(0x21cfff, 24, 22)", "new THREE.PointLight(0x42d9ed, 15, 28)"),
    ("new THREE.PointLight(0x714dff, 18, 18)", "new THREE.PointLight(0x8b9cff, 9, 24)"),
    ("color: 0x12253b, metalness: .35, roughness: .18, transparent: true, opacity: .16", "color: 0x6d9eae, metalness: .12, roughness: .34, transparent: true, opacity: .10"),
    ("color: 0x18283a, metalness: .8, roughness: .24", "color: 0x547887, metalness: .32, roughness: .42"),
    ("color: 0x13243a, metalness: .45, roughness: .2, transparent: true, opacity: .13", "color: 0x6b9baa, metalness: .18, roughness: .38, transparent: true, opacity: .07"),
    ("color: 0x39cfff", "color: 0x69dff0"),
    ("0x18334b, 0x102236", "0x427487, 0x294e60"),
])

replace("BallManager.ts", [
    ("metalness:.22,roughness:.23,clearcoat:.8,clearcoatRoughness:.15,emissive:l.emissive,emissiveIntensity:.48+i*.09", "metalness:.10,roughness:.31,clearcoat:.48,clearcoatRoughness:.24,emissive:l.emissive,emissiveIntensity:.34+i*.07"),
])

replace("config.ts", [
    ("{ name:'SINGULARITY', radius:1.48, color:0x101827, points:4374, emissive:0x9e62ff", "{ name:'SINGULARITY', radius:1.48, color:0x44336f, points:4374, emissive:0x9e62ff"),
])
print("Visual refresh applied.")
