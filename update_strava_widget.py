#!/usr/bin/env python3
"""
Strava Activities Widget Generator
Creates an SVG widget with the last 3 Strava activities
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

def get_strava_activities():
    """Get last 3 activities from Strava"""
    access_token = refresh_strava_token()
    
    if not access_token:
        print("❌ Could not get valid access token")
        return []
    
    try:
        headers = {"Authorization": f"Bearer {access_token}"}
        params = {"per_page": 3}
        
        print("🏃 Fetching last 3 Strava activities...")
        response = requests.get(
            "https://www.strava.com/api/v3/athlete/activities",
            headers=headers,
            params=params
        )
        
        if response.status_code != 200:
            print(f"❌ Error fetching Strava activities: {response.status_code}")
            return []
        
        activities = response.json()
        print(f"✅ Fetched {len(activities)} activities")
        
        formatted_activities = []
        for activity in activities:
            distance_km = activity.get('distance', 0) / 1000
            moving_time = activity.get('moving_time', 0)
            
            # Calculate pace for running
            pace_str = ""
            if distance_km > 0 and activity.get('type') in ['Run', 'Walk']:
                pace_min_per_km = moving_time / 60 / distance_km
                pace_min = int(pace_min_per_km)
                pace_sec = int((pace_min_per_km - pace_min) * 60)
                pace_str = f"{pace_min}:{pace_sec:02d}"
            
            # Format time
            hours = moving_time // 3600
            minutes = (moving_time % 3600) // 60
            seconds = moving_time % 60
            if hours > 0:
                time_str = f"{hours}h {minutes}m"
            else:
                time_str = f"{minutes}m {seconds}s"
            
            # Date
            start_date = activity.get('start_date_local', '')
            date_str = ""
            if start_date:
                dt = datetime.fromisoformat(start_date.replace('Z', '+00:00'))
                date_str = dt.strftime('%b %d')
            
            formatted_activities.append({
                'name': activity.get('name', 'Unnamed'),
                'type': activity.get('type', 'Activity'),
                'distance': f"{distance_km:.2f}",
                'time': time_str,
                'pace': pace_str,
                'date': date_str,
                'elevation': f"{activity.get('total_elevation_gain', 0):.0f}"
            })
        
        return formatted_activities
    
    except Exception as e:
        print(f"❌ Error processing Strava activities: {e}")
        return []

def generate_strava_svg(activities):
    """Generate SVG widget with Strava activities"""
    
    # SVG dimensions
    width = 1200
    height = 240
    
    # Colors matching DarkOrbs theme
    bg_color = "#0a0a0a"
    border_color = "#1a1a1a"
    text_primary = "#ffffff"
    text_secondary = "#888888"
    accent_color = "#fc4c02"  # Strava orange
    
    svg = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="stravaGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{accent_color};stop-opacity:0.1" />
      <stop offset="100%" style="stop-color:{accent_color};stop-opacity:0.05" />
    </linearGradient>
    
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Background -->
  <rect width="{width}" height="{height}" fill="{bg_color}" rx="12"/>
  <rect width="{width}" height="{height}" fill="url(#stravaGradient)" rx="12"/>
  <rect width="{width}" height="{height}" fill="none" stroke="{border_color}" stroke-width="2" rx="12"/>
  
  <!-- Title -->
  <text x="24" y="40" font-family="'Segoe UI', Arial, sans-serif" font-size="20" font-weight="700" fill="{text_primary}" filter="url(#glow)">
    🏃 RECENT STRAVA ACTIVITIES
  </text>
  
  <!-- Activities -->
'''
    
    y_start = 80
    activity_height = 45
    
    for i, activity in enumerate(activities):
        y = y_start + (i * activity_height)
        
        # Activity name (truncate if too long)
        name = activity['name'][:40] + "..." if len(activity['name']) > 40 else activity['name']
        
        # Activity type icon
        icon = "🏃" if activity['type'] == "Run" else "🚴" if activity['type'] == "Ride" else "💪"
        
        svg += f'''  <!-- Activity {i+1} -->
  <text x="24" y="{y}" font-family="'Segoe UI', Arial, sans-serif" font-size="14" font-weight="600" fill="{text_primary}">
    {icon} {name}
  </text>
  <text x="24" y="{y+18}" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="{text_secondary}">
    {activity['date']}
  </text>
  
  <!-- Stats -->
  <text x="650" y="{y}" font-family="'Segoe UI', Arial, sans-serif" font-size="12" font-weight="600" fill="{accent_color}">
    {activity['distance']} km
  </text>
  <text x="650" y="{y+18}" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="{text_secondary}">
    Distance
  </text>
  
  <text x="800" y="{y}" font-family="'Segoe UI', Arial, sans-serif" font-size="12" font-weight="600" fill="{accent_color}">
    {activity['time']}
  </text>
  <text x="800" y="{y+18}" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="{text_secondary}">
    Duration
  </text>
'''
        
        if activity['pace']:
            svg += f'''  <text x="950" y="{y}" font-family="'Segoe UI', Arial, sans-serif" font-size="12" font-weight="600" fill="{accent_color}">
    {activity['pace']} /km
  </text>
  <text x="950" y="{y+18}" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="{text_secondary}">
    Pace
  </text>
'''
        
        svg += f'''  <text x="1100" y="{y}" font-family="'Segoe UI', Arial, sans-serif" font-size="12" font-weight="600" fill="{accent_color}">
    {activity['elevation']} m
  </text>
  <text x="1100" y="{y+18}" font-family="'Segoe UI', Arial, sans-serif" font-size="11" fill="{text_secondary}">
    Elevation
  </text>
  
'''
    
    svg += f'''  <!-- Footer -->
  <text x="{width/2}" y="{height-15}" font-family="'Segoe UI', Arial, sans-serif" font-size="9" fill="{text_secondary}" text-anchor="middle" letter-spacing="2">
    POWERED BY STRAVA API
  </text>
</svg>'''
    
    return svg

def main():
    print("🚀 Strava Widget Generator\n")
    
    # Get activities
    activities = get_strava_activities()
    
    if not activities:
        print("\n❌ Could not fetch Strava activities")
        return
    
    # Show activities
    print("\n📊 Activities fetched:")
    for i, activity in enumerate(activities, 1):
        print(f"  {i}. {activity['name']} - {activity['distance']} km - {activity['date']}")
    
    # Generate SVG
    svg_content = generate_strava_svg(activities)
    
    # Save SVG
    svg_path = Path(__file__).parent / 'assets' / 'strava-widget.svg'
    svg_path.parent.mkdir(exist_ok=True)
    
    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    print(f"\n✅ SVG widget saved to {svg_path}")
    print("✅ Process completed successfully!")

if __name__ == '__main__':
    main()
