import os
import json
import requests

OWNER = "zencq"
REPO = "NomNom"

API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/releases"
OUTPUT_DIR = "./badges/downloads"
PER_PAGE = 100  # max allowed by GitHub


def fetch_all_releases():
    releases = []
    page = 1

    while True:
        url = f"{API_URL}?per_page={PER_PAGE}&page={page}"
        response = requests.get(url)
        response.raise_for_status()
        page_data = response.json()

        if not page_data:
            break

        releases.extend(page_data)
        page += 1

    return releases


def generate_downloads_json(releases):
    total = 0
    per_version = {}

    for release in releases:
        version = release.get("tag_name") or f"release-{release.get('id')}"
        version_downloads = sum(
            asset["download_count"]
            for asset in release.get("assets", [])
            if asset.get("content_type") != "application/json"
        )
        total += version_downloads
        per_version[version] = version_downloads

        badge = get_badge_schema(total, tag=version)
        with open(os.path.join(OUTPUT_DIR, f"{version}.json"), "w") as f:
            json.dump(badge, f, indent=2)

    # Total downloads badge
    total_badge = get_badge_schema(total)
    with open(os.path.join(OUTPUT_DIR, "total.json"), "w") as f:
        json.dump(total_badge, f, indent=2)

    with open(os.path.join(f"{OUTPUT_DIR}/..", "downloads.json"), "w") as f:
        per_version.update(total=total)
        json.dump(per_version, f, indent=2)


def get_badge_schema(count, tag=None) -> dict:
    return {
        "schemaVersion": 1,
        "namedLogo": "github",
        "label": f"downloads@{tag}" if tag else "downloads",
        "message": str(count),
    }


if __name__ == "__main__":
    # Ensure output directory exists.
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    releases = fetch_all_releases()
    generate_downloads_json(releases)
