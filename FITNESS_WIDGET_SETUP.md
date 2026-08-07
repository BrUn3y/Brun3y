# 🏃 Fitness Widget Setup Guide

This guide explains how to set up the automated Google Fit widget in your GitHub README.

## Overview

The fitness widget automatically updates your README with:
- Monthly steps, calories, distance, and active minutes
- Your last recorded activity
- Updates daily via GitHub Actions

## Prerequisites

- Google Fit account with activity data
- Google Cloud project with Fitness API enabled
- OAuth 2.0 credentials (Client ID and Secret)
- `token.json` file (obtained from running `google_fit_setup.py`)

## Setup Instructions

### 1. Configure GitHub Secrets

Go to your repository settings: `https://github.com/BrUn3y/Brun3y/settings/secrets/actions`

Add the following secret:

#### `GOOGLE_FIT_TOKEN`

This secret contains your complete OAuth token in JSON format.

**To create this secret:**

1. Run the `google_fit_setup.py` script locally to generate `token.json`
2. Copy the **entire contents** of `token.json`
3. In GitHub, click **New repository secret**
4. Name: `GOOGLE_FIT_TOKEN`
5. Value: Paste the complete JSON content from `token.json`

**Example format (DO NOT use these values, use your own):**
```json
{
  "token": "ya29.a0ARGnu0...",
  "refresh_token": "1//0fDfL9rTy9ufcCgYIARAAGA8SNwF-L9Ir...",
  "token_uri": "https://oauth2.googleapis.com/token",
  "client_id": "988115924094-xxxxx.apps.googleusercontent.com",
  "client_secret": "GOCSPX-xxxxx",
  "scopes": [
    "https://www.googleapis.com/auth/fitness.activity.read",
    "https://www.googleapis.com/auth/fitness.location.read",
    "https://www.googleapis.com/auth/fitness.body.read"
  ],
  "universe_domain": "googleapis.com",
  "account": "",
  "expiry": "2026-08-07T03:56:05Z"
}
```

### 2. Verify GitHub Actions Workflow

The workflow file is located at `.github/workflows/update-fitness.yml`

**Schedule:** Runs daily at 00:00 UTC

**Manual trigger:** You can also trigger it manually:
1. Go to `Actions` tab in your repository
2. Select `Update Fitness Widget` workflow
3. Click `Run workflow`

### 3. Test the Setup

**Option A: Manual trigger (recommended for first test)**
1. Go to repository `Actions` tab
2. Click `Update Fitness Widget`
3. Click `Run workflow` → `Run workflow`
4. Wait for completion (~30 seconds)
5. Check your README for updated stats

**Option B: Local test**
```bash
# Install dependencies
pip install -r requirements.txt

# Run the script
python update_fitness_widget.py
```

### 4. Verify README Updates

After the workflow runs successfully:
1. Check your README.md
2. Look for the `🏃 Fitness Stats` section
3. Verify the data is current
4. Check the commit history for automated commits

## How It Works

### Token Refresh Mechanism

**Good news:** Your token won't expire if used regularly!

- The `token` (access token) expires in ~1 hour
- The `refresh_token` is permanent and auto-renews the access token
- Each workflow run automatically refreshes the token if needed
- The refresh token only expires if:
  - You manually revoke access at https://myaccount.google.com/permissions
  - Not used for 6+ months
  - You change your Google account password

**For automation:** As long as the workflow runs at least once every 6 months, the token remains valid indefinitely.

### Workflow Process

1. **Trigger:** Daily at 00:00 UTC (or manual)
2. **Checkout:** Clones your repository
3. **Setup:** Installs Python and dependencies
4. **Authenticate:** Creates `token.json` from GitHub Secret
5. **Fetch Data:** Connects to Google Fit API
6. **Update:** Modifies README between `<!-- FITNESS_WIDGET_START -->` and `<!-- FITNESS_WIDGET_END -->` markers
7. **Commit:** Pushes changes if data changed

### Data Sources

The script fetches from Google Fit API:
- **Steps:** `derived:com.google.step_count.delta`
- **Calories:** `derived:com.google.calories.expended`
- **Distance:** `derived:com.google.distance.delta`
- **Active Minutes:** `derived:com.google.active_minutes`
- **Last Activity:** Most recent session from last 30 days

## Troubleshooting

### Workflow fails with "Error 401: Unauthorized"

**Cause:** Token expired or invalid

**Solution:**
1. Run `google_fit_setup.py` locally to generate a fresh `token.json`
2. Update the `GOOGLE_FIT_TOKEN` secret in GitHub with the new content

### Workflow fails with "Error 403: Forbidden"

**Cause:** Missing API scopes or API not enabled

**Solution:**
1. Verify Google Fitness API is enabled in your Google Cloud project
2. Check OAuth consent screen has correct scopes
3. Re-run `google_fit_setup.py` to re-authorize

### Widget shows zeros

**Possible causes:**
- No activity data in Google Fit for current month
- Data sources not syncing properly
- Time zone mismatch

**Solution:**
1. Check Google Fit app has recent data
2. Verify your fitness tracker is syncing
3. Wait 24 hours for data to propagate

### Workflow runs but README doesn't update

**Cause:** Git push permissions issue

**Solution:**
1. Verify `GITHUB_TOKEN` has write permissions
2. Check repository settings → Actions → General → Workflow permissions
3. Ensure "Read and write permissions" is selected

## Customization

### Change Update Frequency

Edit `.github/workflows/update-fitness.yml`:

```yaml
on:
  schedule:
    # Every 6 hours
    - cron: '0 */6 * * *'
    
    # Every hour
    - cron: '0 * * * *'
    
    # Weekly on Monday at 9 AM
    - cron: '0 9 * * 1'
```

### Modify Widget Appearance

Edit `update_fitness_widget.py` → `generate_widget_markdown()` function

### Add More Metrics

Edit `update_fitness_widget.py` → `get_fitness_data()` function

Available data sources:
- Heart rate: `derived:com.google.heart_rate.bpm`
- Weight: `derived:com.google.weight`
- Sleep: `derived:com.google.sleep.segment`

## Security Notes

- **Never commit `token.json`** to your repository
- The `.gitignore` file already excludes it
- GitHub Secrets are encrypted and only accessible to workflows
- Tokens are never exposed in workflow logs
- Consider rotating credentials periodically

## Files Overview

```
Brun3y/
├── update_fitness_widget.py          # Main script
├── requirements.txt                   # Python dependencies
├── FITNESS_WIDGET_SETUP.md           # This file
├── .github/
│   └── workflows/
│       └── update-fitness.yml        # GitHub Actions workflow
└── README.md                          # Your profile (auto-updated)
```

## Support

If you encounter issues:
1. Check workflow logs in Actions tab
2. Verify all secrets are set correctly
3. Test the script locally first
4. Review Google Fit API quotas and limits

## References

- [Google Fit REST API](https://developers.google.com/fit/rest)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [OAuth 2.0 for Mobile & Desktop Apps](https://developers.google.com/identity/protocols/oauth2/native-app)
