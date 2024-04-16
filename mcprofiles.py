import json, os

appdata = os.getenv('APPDATA')
if os.path.isdir(f"{appdata}\\.minecraft") is False:
    print(f"Minecraft Directory not found.")
    exit(0)

with open(f"{appdata}\\.minecraft\\launcher_profiles.json", "r") as f:
    profiles = json.load(f)
    f.close()

for profile in list(profiles['profiles'].keys()):
    if 'gameDir' in profiles['profiles'][profile]:
        print(f"{profile}> {profiles['profiles'][profile]['gameDir']}")
    else:
        print(F"{profile}> None")