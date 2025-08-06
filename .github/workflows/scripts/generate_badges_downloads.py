import json
import os
import requests

from numerize import numerize

OWNER = "zencq"
REPO = "NomNom"

OUTPUT_DIR = "gh-pages/badges/downloads"
PER_PAGE = 100  # max allowed by GitHub


def fetch_all_releases():
    releases = []
    page = 1

    while True:
        response = requests.get(f"https://api.github.com/repos/{OWNER}/{REPO}/releases?per_page={PER_PAGE}&page={page}")
        response.raise_for_status()

        page_data = response.json()
        if not page_data:
            break

        releases.extend(page_data)
        page += 1

    return releases


def generate_downloads_json(releases):
    total = 0

    # Get download counts for all releases.
    for release in releases:
        tag = release.get("tag_name") or f"release-{release.get('id')}"
        tag_downloads = sum(
            asset["download_count"]
            for asset in release.get("assets", [])
            if asset.get("content_type") != "application/json"  # exclude metadata file
        )

        total += tag_downloads  # update total to write at the end

        badge = get_badge_schema(tag_downloads, tag=tag)
        write_json(badge, tag=tag)

    badge = get_badge_schema(total)
    write_json(badge)


def write_json(badge, tag=None):
    f_name = f"{tag}.json" if tag else "total.json"
    with open(os.path.join(OUTPUT_DIR, f_name), "w") as f:
        json.dump(badge, f)


def get_badge_schema(count, tag=None) -> dict:
    return {
        "schemaVersion": 1,
        "label": f"downloads@{tag}" if tag else "downloads",
        "message": str(numerize.numerize(count, 1)),
        "color": "green",
        "namedLogo": "github",
    }


if __name__ == "__main__":
    # Ensure output directory exists.
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    releases = fetch_all_releases()
    generate_downloads_json(releases)
