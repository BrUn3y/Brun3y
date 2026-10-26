# BrUn3y personal website

A Y2K-inspired static website based on the profile README. Built with HTML, CSS, and JavaScript, with no build dependencies. All website copy is in English.

- `index.html`: content, links, projects, and retro self-promotion banners.
- `site/style.css`: desktop and mobile styles.
- `site/app.js`: project filters, navigation, and the Mexico City clock.
- `site/chat.js` and `site/chat-messages.json`: local chat, 500 original English messages, randomized pacing, personalized greetings, and funny replies.
- `site/activity.js` and `site/activity.json`: public GitHub events and authored issues/PRs, with a saved fallback for network errors or API rate limits.
- `site/strava.js` and `site/strava.json`: the latest six published workouts and totals, based on the existing profile Strava widget.
- `scripts/refresh_site_data.py`: safe, repeatable GitHub and Strava refreshes. Run without flags to refresh both, or use `--github` / `--strava`.
- `AGENTS.md` (also linked from `agent.md`): maintenance instructions for agents, including data sources, refresh commands, design constraints, validation, and publishing.
- `site/assets/`: original SVG illustrations and the public GitHub avatar.

## Local development

From the repository root:

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

Open http://127.0.0.1:8080. Editorial content is maintained manually; existing profile README automation runs independently. The Spotify button opens the public profile rather than playing audio automatically or claiming to show a live track. Retro banners link to the owner's own projects and do not use an advertising network.

Google Analytics uses the owner's Google tag, `G-GSG3QV8LMM`, loaded asynchronously in the document head. No custom analytics events send chat nicknames or messages.

The project chat is entirely simulated. Visitors can add a nickname and a message to the current tab; messages are rendered with `textContent`, never sent over the network, and never stored in cookies, localStorage, sessionStorage, or a backend. Reloading resets the room. Fictional participants draw from 500 unique English messages shuffled without repeating a message until the deck is exhausted. Messages arrive at irregular intervals while the tab is visible. A nickname receives a welcome and a humorous reply on its first message in the current tab. The displayed log is limited to 18 messages. The UI only notes that messages clear on refresh.

Last activity uses GitHub's public events and authored issue search APIs without authentication. It supports pushes, pull requests, reviews, issues, comments, repositories, forks, stars, and releases. A checked-in public snapshot remains available when the API fails or rate limits requests. The displayed source indicates whether the feed is live, saved, or mixed. All links point to the actual GitHub resources.

The Strava section reuses statistics already published in `assets/strava-widget.svg`. It includes six sessions, duration, available distance, heart rate, and calories. Totals cover those displayed sessions. The publication date comes from the widget's latest Git commit, and workout dates keep the month/day labels supplied by the widget. The browser reads only the sanitized static JSON; no Strava credentials, route data, or raw API responses are published.

## Deployment

Website URL: https://brun3y.github.io/

The source stays in `BrUn3y/Brun3y`, preserving its role as the public GitHub profile repository. GitHub requires a repository named `BrUn3y.github.io` to serve the root user website. That publishing repository is **private** at the user's request and holds the website files plus `agent.md` and `AGENTS.md` in its root. Both guides are automatically synchronized from the source repository so agents can find the maintenance and credential-handling instructions in either repository.

**Deployment limitation:** GitHub disabled Pages after the publishing repository became private. Re-enabling it returned: "Your current plan does not support GitHub Pages for this repository." Serving a public Pages website from this private personal repository requires GitHub Pro. Preserve the private visibility. After the account has a supported plan, re-enable Pages in the publishing repository's Settings → Pages using `main` and `/`, then verify a successful destination Pages deployment and the updated public content. Cached HTTP 200 responses do not establish that Pages is still enabled.

`.github/workflows/pages.yml` pushes relevant changes from `master` to the publishing repository; it can also be run manually. It refreshes both data snapshots before publishing, runs daily at 06:41 UTC, and follows successful profile/fitness updates. A repository-specific SSH deploy key, stored in the source repository's `PAGES_DEPLOY_KEY` Actions secret, grants write access only to `BrUn3y/BrUn3y.github.io`. Successful pushes do not deploy the public website while Pages is disabled.

The published artifact contains exclusively `index.html`, `site/`, `.nojekyll`, `agent.md`, and `AGENTS.md`. No profile scripts or credential files are copied. The deployment action is pinned to a commit.
