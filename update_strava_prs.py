#!/usr/bin/env python3
"""
Strava Personal Records Widget Generator
Creates SVG widgets for 5K, 10K, and 21K PRs
"""

import json
import requests
from datetime import datetime
from pathlib import Path

def refresh_strava_token():
    """Refresh Strava access token if expired"""
    strava_tokens_path = Path(__file__).parent / 'strava_tokens.json'
    
    if not strava_tokens_path.exists():
        print("❌ Strava tokens file not found")
        return None
    
    with open(strava_tokens_path, 'r') as f:
        tokens = json.load(f)
    
    expires_at = tokens.get('expires_at', 0)
    current_time = datetime.now().timestamp()
    
    if current_time < expires_at:
        print("✅ Strava token still valid")
        return tokens.get('access_token')
    
    print("🔄 Strava token expired, refreshing...")
    
    refresh_token = tokens.get('refresh_token')
    client_id = tokens.get('client_id')
    client_secret = tokens.get('client_secret')
    
    if not all([refresh_token, client_id, client_secret]):
        print("❌ Missing token credentials")
        return None
    
    token_url = "https://www.strava.com/oauth/token"
    token_data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }
    
    try:
        response = requests.post(token_url, data=token_data)
        response.raise_for_status()
        
        new_tokens = response.json()
        new_tokens['client_id'] = client_id
        new_tokens['client_secret'] = client_secret
        
        with open(strava_tokens_path, 'w') as f:
            json.dump(new_tokens, f, indent=2)
        
        print("✅ Strava token refreshed successfully")
        return new_tokens.get('access_token')
    
    except Exception as e:
        print(f"❌ Error refreshing token: {e}")
        return None

def get_strava_prs(access_token):
    """Get PRs for 5K, 10K, and 21K distances"""
    headers = {'Authorization': f'Bearer {access_token}'}
    
    # Fetch all running activities
    all_runs = []
    page = 1
    
    print("🏃 Fetching all running activities from Strava...")
    
    while True:
        response = requests.get(
            'https://www.strava.com/api/v3/athlete/activities',
            headers=headers,
            params={'per_page': 200, 'page': page}
        )
        
        if response.status_code != 200:
            print(f"❌ Error fetching activities: {response.status_code}")
            break
        
        activities = response.json()
        if not activities:
            break
        
        runs = [a for a in activities if a['type'] == 'Run']
        all_runs.extend(runs)
        page += 1
        
        if len(activities) < 200:
            break
    
    print(f"✅ Fetched {len(all_runs)} running activities")
    
    # Define distance ranges (in km)
    distance_ranges = {
        '5K': (4.5, 5.5),
        '10K': (9.5, 10.5),
        '21K': (20.5, 22.0)  # Half marathon
    }
    
    prs = {}
    
    for distance_name, (min_km, max_km) in distance_ranges.items():
        matching_runs = []
        
        for run in all_runs:
            distance_km = run['distance'] / 1000
            if min_km <= distance_km <= max_km:
                matching_runs.append({
                    'name': run['name'],
                    'date': datetime.fromisoformat(run['start_date_local'].replace('Z', '+00:00')),
                    'distance': distance_km,
                    'time': run['moving_time'],
                    'pace': run['moving_time'] / distance_km / 60,  # min/km
                    'avg_hr': run.get('average_heartrate'),
                    'max_hr': run.get('max_heartrate'),
                    'elevation': run.get('total_elevation_gain', 0),
                    'url': f"https://www.strava.com/activities/{run['id']}"
                })
        
        # Sort by time (fastest first) and get top 3
        matching_runs.sort(key=lambda x: x['time'])
        prs[distance_name] = matching_runs[:3]
        
        print(f"  {distance_name}: Found {len(matching_runs)} runs, top 3 selected")
    
    return prs

def generate_pr_svg(distance_name, runs):
    """Generate SVG widget for a specific distance PR"""
    
    # SVG dimensions
    width = 400
    height = 280
    
    # Colors matching DarkOrbs theme
    bg_color = "#0a0a0a"
    border_color = "#1a1a1a"
    text_primary = "#ffffff"
    text_secondary = "#888888"
    accent_color = "#fc4c02"  # Strava orange
    gold = "#FFD700"
    silver = "#C0C0C0"
    bronze = "#CD7F32"
    
    svg = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="prGradient{distance_name}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{accent_color};stop-opacity:0.15" />
      <stop offset="100%" style="stop-color:{accent_color};stop-opacity:0.05" />
    </linearGradient>
    
    <filter id="glow{distance_name}">
      <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Background -->
  <rect width="{width}" height="{height}" fill="{bg_color}" rx="12"/>
  <rect width="{width}" height="{height}" fill="url(#prGradient{distance_name})" rx="12"/>
  <rect width="{width}" height="{height}" fill="none" stroke="{border_color}" stroke-width="2" rx="12"/>
  
  <!-- Title -->
  <text x="{width/2}" y="35" font-family="'Segoe UI', Arial, sans-serif" font-size="22" font-weight="700" fill="{text_primary}" text-anchor="middle" filter="url(#glow{distance_name})">
    🏆 {distance_name} PERSONAL RECORDS
  </text>
  
  <line x1="30" y1="50" x2="{width-30}" y2="50" stroke="{border_color}" stroke-width="1"/>
  
'''
    
    if not runs:
        svg += f'''  <text x="{width/2}" y="{height/2}" font-family="'Segoe UI', Arial, sans-serif" font-size="14" fill="{text_secondary}" text-anchor="middle">
    No {distance_name} runs found
  </text>
'''
    else:
        medals = [gold, silver, bronze]
        medal_icons = ["🥇", "🥈", "🥉"]
        
        y_start = 80
        run_height = 60
        
        for i, run in enumerate(runs):
            y = y_start + (i * run_height)
            medal_color = medals[i] if i < len(medals) else text_secondary
            medal_icon = medal_icons[i] if i < len(medal_icons) else "🏃"
            
            # Time
            minutes = run['time'] // 60
            seconds = run['time'] % 60
            time_str = f"{int(minutes)}:{int(seconds):02d}"
            
            # Pace
            pace_min = int(run['pace'])
            pace_sec = int((run['pace'] - pace_min) * 60)
            pace_str = f"{pace_min}:{pace_sec:02d}"
            
            # Date
            date_str = run['date'].strftime('%b %d, %Y')
            
            svg += f'''  <!-- PR #{i+1} -->
  <circle cx="50" cy="{y}" r="18" fill="{medal_color}" opacity="0.2"/>
  <text x="50" y="{y+6}" font-family="'Segoe UI', Arial, sans-serif" font-size="18" text-anchor="middle">
    {medal_icon}
  </text>
  
  <text x="85" y="{y-8}" font-family="'Segoe UI', Arial, sans-serif" font-size="16" font-weight="700" fill="{accent_color}">
    {time_str}
  </text>
  <text x="85" y="{y+10}" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="{text_secondary}">
    {pace_str} /km • {date_str}
  </text>
'''
            
            if run['avg_hr']:
                svg += f'''  <text x="85" y="{y+24}" font-family="'Segoe UI', Arial, sans-serif" font-size="10" fill="{text_secondary}">
    ❤️ {int(run['avg_hr'])} bpm avg
  </text>
'''
    
    svg += f'''  
  <!-- Footer -->
  <text x="{width/2}" y="{height-15}" font-family="'Segoe UI', Arial, sans-serif" font-size="9" fill="{text_secondary}" text-anchor="middle" letter-spacing="1">
    POWERED BY STRAVA
  </text>
</svg>'''
    
    return svg

def main():
    print("🚀 Strava PR Widget Generator\n")
    
    # Get access token
    access_token = refresh_strava_token()
    if not access_token:
        print("\n❌ Could not get valid access token")
        return
    
    # Get PRs
    prs = get_strava_prs(access_token)
    
    # Generate SVG widgets
    assets_dir = Path(__file__).parent / 'assets'
    assets_dir.mkdir(exist_ok=True)
    
    for distance_name, runs in prs.items():
        svg_content = generate_pr_svg(distance_name, runs)
        
        # Save SVG
        filename = f'strava-pr-{distance_name.lower()}.svg'
        svg_path = assets_dir / filename
        
        with open(svg_path, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        print(f"✅ {distance_name} widget saved to {svg_path}")
        
        if runs:
            print(f"   Top time: {int(runs[0]['time']//60)}:{int(runs[0]['time']%60):02d}")
    
    print("\n✅ All PR widgets generated successfully!")

if __name__ == '__main__':
    main()
