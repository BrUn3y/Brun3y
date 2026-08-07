#!/usr/bin/env python3
"""
Google Fit Widget Updater for GitHub README
Fetches monthly fitness stats and updates README with a dynamic widget
"""

import os
import json
import requests
from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def load_credentials():
    """Load credentials from token.json or environment variable"""
    token_data = None
    
    # Try to load from environment variable (GitHub Actions)
    if os.getenv('GOOGLE_FIT_TOKEN'):
        token_data = json.loads(os.getenv('GOOGLE_FIT_TOKEN'))
    # Try to load from file (local development)
    elif os.path.exists('token.json'):
        with open('token.json', 'r') as f:
            token_data = json.load(f)
    else:
        raise FileNotFoundError("No credentials found. Set GOOGLE_FIT_TOKEN env var or create token.json")
    
    return Credentials(
        token=token_data['token'],
        refresh_token=token_data['refresh_token'],
        token_uri=token_data['token_uri'],
        client_id=token_data['client_id'],
        client_secret=token_data['client_secret'],
        scopes=token_data['scopes']
    )

def get_month_timestamps():
    """Get start and end timestamps for current month in nanoseconds"""
    now = datetime.now()
    start_of_month = datetime(now.year, now.month, 1)
    
    start_time_ns = int(start_of_month.timestamp() * 1e9)
    end_time_ns = int(now.timestamp() * 1e9)
    
    return start_time_ns, end_time_ns

def get_fitness_data(service, start_time_ns, end_time_ns):
    """Fetch fitness data from Google Fit API"""
    
    # Data sources for different metrics
    data_sources = {
        'steps': 'derived:com.google.step_count.delta:com.google.android.gms:estimated_steps',
        'calories': 'derived:com.google.calories.expended:com.google.android.gms:merge_calories_expended',
        'distance': 'derived:com.google.distance.delta:com.google.android.gms:merge_distance_delta',
        'active_minutes': 'derived:com.google.active_minutes:com.google.android.gms:merge_active_minutes'
    }
    
    stats = {}
    
    for metric, data_source in data_sources.items():
        try:
            dataset = service.users().dataSources().datasets().get(
                userId='me',
                dataSourceId=data_source,
                datasetId=f'{start_time_ns}-{end_time_ns}'
            ).execute()
            
            total = 0
            if 'point' in dataset:
                for point in dataset['point']:
                    if 'value' in point and len(point['value']) > 0:
                        if 'intVal' in point['value'][0]:
                            total += point['value'][0]['intVal']
                        elif 'fpVal' in point['value'][0]:
                            total += point['value'][0]['fpVal']
            
            stats[metric] = total
        except HttpError as e:
            print(f"Error fetching {metric}: {e}")
            stats[metric] = 0
    
    return stats

def get_last_activity(service):
    """Get the most recent activity session"""
    try:
        # Get sessions from last 30 days
        now = datetime.now()
        start_time = now - timedelta(days=30)
        
        start_time_ms = int(start_time.timestamp() * 1000)
        end_time_ms = int(now.timestamp() * 1000)
        
        sessions = service.users().sessions().list(
            userId='me',
            startTime=datetime.fromtimestamp(start_time_ms/1000).isoformat() + 'Z',
            endTime=datetime.fromtimestamp(end_time_ms/1000).isoformat() + 'Z'
        ).execute()
        
        if 'session' in sessions and len(sessions['session']) > 0:
            # Get the most recent session
            last_session = sessions['session'][0]
            activity_type = last_session.get('activityType', 'Unknown')
            start_time = datetime.fromtimestamp(int(last_session['startTimeMillis'])/1000)
            
            # Activity type mapping
            activity_names = {
                1: 'Running',
                8: 'Walking',
                7: 'Cycling',
                9: 'Hiking',
                119: 'Strength Training',
                # Add more as needed
            }
            
            activity_name = activity_names.get(activity_type, f'Activity {activity_type}')
            days_ago = (datetime.now() - start_time).days
            
            if days_ago == 0:
                time_str = 'Today'
            elif days_ago == 1:
                time_str = 'Yesterday'
            else:
                time_str = f'{days_ago} days ago'
            
            return f'{activity_name} · {time_str}'
        
        return 'No recent activity'
    except Exception as e:
        print(f"Error fetching last activity: {e}")
        return 'No recent activity'

def format_number(num):
    """Format numbers with commas"""
    return f'{int(num):,}'

def generate_widget_markdown(stats, last_activity):
    """Generate markdown for the fitness widget"""
    
    steps = format_number(stats.get('steps', 0))
    calories = format_number(stats.get('calories', 0))
    distance = f"{stats.get('distance', 0) / 1000:.1f}"  # Convert meters to km
    active_mins = format_number(stats.get('active_minutes', 0))
    
    month_name = datetime.now().strftime('%B %Y')
    
    widget = f"""### 🏃 Fitness Stats ({month_name})

<div align="center">

| 👟 Steps | 🔥 Calories | 📏 Distance | ⏱️ Active Minutes |
|:--------:|:-----------:|:-----------:|:-----------------:|
| **{steps}** | **{calories}** | **{distance} km** | **{active_mins}** |

**Last Activity:** {last_activity}

<sub>Updated automatically via Google Fit API</sub>

</div>"""
    
    return widget

def update_readme(widget_content, readme_path='README.md'):
    """Update README.md with the fitness widget"""
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Markers for the widget section
    start_marker = '<!-- FITNESS_WIDGET_START -->'
    end_marker = '<!-- FITNESS_WIDGET_END -->'
    
    # Check if markers exist
    if start_marker in content and end_marker in content:
        # Replace existing widget
        start_idx = content.find(start_marker)
        end_idx = content.find(end_marker) + len(end_marker)
        
        new_content = (
            content[:start_idx] +
            f'{start_marker}\n{widget_content}\n{end_marker}' +
            content[end_idx:]
        )
    else:
        # Add widget before the "Stats" section
        stats_marker = '### Stats'
        if stats_marker in content:
            stats_idx = content.find(stats_marker)
            new_content = (
                content[:stats_idx] +
                f'{start_marker}\n{widget_content}\n{end_marker}\n\n---\n\n' +
                content[stats_idx:]
            )
        else:
            # Append at the end
            new_content = content + f'\n\n{start_marker}\n{widget_content}\n{end_marker}\n'
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ README updated successfully at {datetime.now().isoformat()}")

def main():
    """Main execution function"""
    try:
        print("🔄 Loading credentials...")
        creds = load_credentials()
        
        print("🔄 Building Google Fit service...")
        service = build('fitness', 'v1', credentials=creds)
        
        print("🔄 Fetching fitness data...")
        start_time_ns, end_time_ns = get_month_timestamps()
        stats = get_fitness_data(service, start_time_ns, end_time_ns)
        
        print("🔄 Fetching last activity...")
        last_activity = get_last_activity(service)
        
        print("🔄 Generating widget...")
        widget = generate_widget_markdown(stats, last_activity)
        
        print("🔄 Updating README...")
        readme_path = os.getenv('README_PATH', 'README.md')
        update_readme(widget, readme_path)
        
        print("✅ All done!")
        print(f"\nStats for {datetime.now().strftime('%B %Y')}:")
        print(f"  Steps: {format_number(stats['steps'])}")
        print(f"  Calories: {format_number(stats['calories'])}")
        print(f"  Distance: {stats['distance']/1000:.1f} km")
        print(f"  Active Minutes: {format_number(stats['active_minutes'])}")
        print(f"  Last Activity: {last_activity}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        raise

if __name__ == '__main__':
    main()
