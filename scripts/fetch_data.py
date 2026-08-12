#!/usr/bin/env python3
"""Query GitHub for merged upstream PRs and write data.json for the renderer.

Only counts PRs merged into repos the user does not own. config.json carries an
include/exclude list so the published numbers stay under human control.
"""
import json
import os
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request

USER = os.environ.get("PROFILE_USER", "Achyuthan-S")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
HERE = pathlib.Path(__file__).resolve().parent
CFG = json.loads((HERE / "config.json").read_text())
DATA_PATH = HERE / "data.json"


def api(url):
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": f"{USER}-profile-refresh",
        **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}),
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def fetch_merged():
    q = urllib.parse.quote(f"is:pr is:merged author:{USER}")
    items, page = [], 1
    while page <= 4:
        batch = api(f"https://api.github.com/search/issues?q={q}&per_page=100&page={page}")
        items += batch["items"]
        if len(items) >= batch["total_count"]:
            break
        page += 1
    return items


def main():
    try:
        items = fetch_merged()
    except (urllib.error.URLError, urllib.error.HTTPError, KeyError) as exc:
        # Never publish a broken pane: keep the last good data.json.
        print(f"fetch failed ({exc}); leaving existing data.json untouched", file=sys.stderr)
        return 0 if DATA_PATH.exists() else 1

    excluded = {(e["repo"], e["number"]) for e in CFG["exclude"]}
    prs = []
    for it in items:
        repo = "/".join(it["repository_url"].split("/")[-2:])
        owner = repo.split("/")[0]
        if owner == USER or (repo, it["number"]) in excluded:
            continue                       # own repos and opted-out PRs never count
        prs.append(dict(repo=repo, number=it["number"], closed_at=it["closed_at"],
                        title=it["title"]))

    for ex in CFG["include_extra"]:
        prs.append(dict(repo=ex["repo"], number=ex["number"], closed_at=None,
                        title=ex["msg"]))

    for p in prs:
        owner = p["repo"].split("/")[0]
        om = CFG["org_map"].get(owner, {"name": owner, "colour": "out"})
        p["org"], p["colour"] = om["name"], om["colour"]
        p["short"] = CFG["repo_short"].get(p["repo"], p["repo"].split("/")[-1])
        p["msg"] = CFG["msg_override"].get(str(p["number"]), p["title"][:29])

    by = {}
    for p in prs:
        by.setdefault(p["org"], dict(name=p["org"], colour=p["colour"], count=0))["count"] += 1
    by_org = sorted(by.values(), key=lambda o: -o["count"])

    dated = sorted([p for p in prs if p["closed_at"]], key=lambda p: p["closed_at"], reverse=True)
    seen, repos = set(), []
    for p in dated:
        if p["repo"] not in seen:
            seen.add(p["repo"]); repos.append(p["repo"])

    data = dict(
        count=len(prs),
        orgs_line=" · ".join(o["name"] for o in by_org[:3]),
        repos=repos[:5],
        by_org=by_org,
        recent=[dict(number=p["number"], short=p["short"], long=p["repo"], msg=p["msg"]) for p in dated[:5]],
    )

    old = json.loads(DATA_PATH.read_text()) if DATA_PATH.exists() else None
    DATA_PATH.write_text(json.dumps(data, indent=2) + "\n")
    print(f"count={data['count']} orgs={[(o['name'], o['count']) for o in by_org]}")
    print("changed" if data != old else "unchanged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
