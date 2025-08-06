import json
import os

OUTPUT_DIR = "gh-pages/badges/test"


def write_json(badge):
    with open(os.path.join(OUTPUT_DIR, "test.json"), "w") as f:
        json.dump(badge, f)


def get_badge_schema() -> dict:
    return {
        "schemaVersion": 1,
        "label": f"test",
        "message": "for multiple badge types",
        "color": "purple",
    }


if __name__ == "__main__":
    # Ensure output directory exists.
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    badge = get_badge_schema()
    write_json(badge)
