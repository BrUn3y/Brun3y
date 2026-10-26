# BrUn3y personal website

A Y2K-inspired static website based on the profile README. Built with HTML, CSS, and JavaScript, with no build dependencies or runtime third-party services. All website copy is in English.

- `index.html`: content, links, projects, and retro self-promotion banners.
- `site/style.css`: desktop and mobile styles.
- `site/app.js`: project filters, navigation, and the Mexico City clock.
- `site/chat.js` and `site/chat-messages.json`: local chat, 500 original English messages, randomized pacing, personalized greetings, and funny replies.
- `site/activity.js` and `site/activity.json`: public GitHub events and authored issues/PRs, with a saved fallback for network errors or API rate limits.
- `site/assets/`: original SVG illustrations and the public GitHub avatar.

## Local development

From the repository root:

```sh
python3 -m http.server 8080 --bind 127.0.0.1
```

Open http://127.0.0.1:8080. Editorial content is maintained manually; existing profile README automation runs independently. The Spotify button opens the public profile rather than playing audio automatically or claiming to show a live track. Retro banners link to the owner's own projects and do not use an advertising network.

The project chat is entirely simulated. Visitors can add a nickname and a message to the current tab; messages are rendered with `textContent`, never sent over the network, and never stored in cookies, localStorage, sessionStorage, or a backend. Reloading resets the room. Fictional participants draw from 500 unique English messages shuffled without repeating a message until the deck is exhausted. Messages arrive at irregular intervals while the tab is visible. A nickname receives a welcome and a humorous reply on its first message in the current tab. The displayed log is limited to 18 messages. The UI only notes that messages clear on refresh.

Last activity uses GitHub's public events and authored issue search APIs without authentication. It supports pushes, pull requests, reviews, issues, comments, repositories, forks, stars, and releases. A checked-in public snapshot remains available when the API fails or rate limits requests. The displayed source indicates whether the feed is live, saved, or mixed. All links point to the actual GitHub resources.

## Deployment

Live website: https://brun3y.github.io/

The source stays in `BrUn3y/Brun3y`, preserving its role as the GitHub profile repository. GitHub requires a repository named `BrUn3y.github.io` to serve the root user website. That repository holds only the published website.

`.github/workflows/pages.yml` publishes changes to `index.html` and `site/` from `master`; it can also be run manually. A repository-specific SSH deploy key, stored in the source repository's `PAGES_DEPLOY_KEY` Actions secret, grants write access only to `BrUn3y/BrUn3y.github.io`. GitHub Pages serves the publishing repository's `main` branch from `/`.

The published artifact contains exclusively `index.html`, `site/`, and `.nojekyll`. No profile scripts or configuration files are copied. The deployment action is pinned to a commit.
