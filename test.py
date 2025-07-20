import json

with open("Qwen_7B_Chat.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

# حذف metadata.widgets إذا كانت موجودة
if "widgets" in nb.get("metadata", {}):
    del nb["metadata"]["widgets"]

with open("notebook_clean.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
