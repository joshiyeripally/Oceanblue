import shutil
files = [
    r"C:\Users\ASUS\.gemini\antigravity\brain\5b81ddbd-1250-4b98-baea-2a05a23cfc2c\boat_construction_1774623913015.png",
    r"C:\Users\ASUS\.gemini\antigravity\brain\5b81ddbd-1250-4b98-baea-2a05a23cfc2c\fishing_boat_1774624073890.png",
    r"C:\Users\ASUS\.gemini\antigravity\brain\5b81ddbd-1250-4b98-baea-2a05a23cfc2c\resin_application_1774624179283.png",
    r"C:\Users\ASUS\.gemini\antigravity\brain\5b81ddbd-1250-4b98-baea-2a05a23cfc2c\transport_boat_1774624243159.png",
    r"C:\Users\ASUS\.gemini\antigravity\brain\5b81ddbd-1250-4b98-baea-2a05a23cfc2c\boat_repair_1774624326081.png",
    r"C:\Users\ASUS\.gemini\antigravity\brain\5b81ddbd-1250-4b98-baea-2a05a23cfc2c\custom_finish_1774624401335.png"
]
for f in files:
    shutil.copy2(f, r"c:\Users\ASUS\Downloads\Java Folder\Oceanblue\images")
print("AI images copied!")
