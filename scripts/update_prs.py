#!/usr/bin/env python3
"""Regenerate the upstream-PR table in README.md from the GitHub API.

Only public PRs are listed — the table is meant to be independently verifiable,
so anything a visitor cannot click through to is deliberately excluded.
"""
import json
import os
import re
import sys
import urllib.parse
import urllib.request

USER = os.environ.get("PROFILE_USER", "madhav-sharma0201")
README = os.path.join(os.path.dirname(__file__), "..", "README.md")
START, END = "<!-- PRS:START -->", "<!-- PRS:END -->"

# Repos whose PRs count as "upstream" — everything else is skipped.
UPSTREAM_PREFIXES = ("kubescape/",)


def search(query):
    req = urllib.request.Request(
        "https://api.github.com/search/issues?per_page=100&q=" + urllib.parse.quote(query),
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": USER + "-profile-readme",
        },
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", "Bearer " + token)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def repo_of(item):
    # repository_url looks like https://api.github.com/repos/<owner>/<name>
    return item["repository_url"].split("/repos/", 1)[1]


def main():
    items = search(f"author:{USER} type:pr is:public")["items"]

    rows = []
    for it in items:
        repo = repo_of(it)
        if not repo.startswith(UPSTREAM_PREFIXES):
            continue
        merged = bool((it.get("pull_request") or {}).get("merged_at"))
        if merged:
            status = "✅ Merged"
        elif it["state"] == "open":
            status = "🔄 Open"
        else:
            status = "⛔ Closed"
        rows.append(
            {
                "num": it["number"],
                "url": it["html_url"],
                "title": it["title"].replace("|", "\\|"),
                "repo": repo,
                "status": status,
                "sort": (0 if merged else 1, -it["number"]),
            }
        )

    if not rows:
        print("no upstream PRs found — refusing to blank the table", file=sys.stderr)
        return 1

    rows.sort(key=lambda r: r["sort"])

    table = ["| PR | Title | Repo | Status |", "|---|---|---|---|"]
    for r in rows:
        table.append(
            f"| [#{r['num']}]({r['url']}) | {r['title']} | `{r['repo']}` | {r['status']} |"
        )
    block = START + "\n" + "\n".join(table) + "\n" + END

    with open(README, encoding="utf-8") as f:
        content = f.read()

    new = re.sub(
        re.escape(START) + r".*?" + re.escape(END), block, content, flags=re.S
    )
    if new == content:
        print("no change")
        return 0

    with open(README, "w", encoding="utf-8") as f:
        f.write(new)
    print(f"updated table with {len(rows)} upstream PRs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
