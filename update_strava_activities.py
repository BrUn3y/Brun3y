#!/usr/bin/env python3
"""
Strava Activities Updater for README
Fetches last 3 activities from Strava and updates readme.source.md
"""

import json
import requests
from datetime import datetime
from pathlib import Path

def refresh_strava_token():
    """Refresca el access token de Strava si ha expirado"""
    strava_tokens_path = Path(__file__).parent.parent / 'strava-setup' / 'strava_tokens.json'
    
    if not strava_tokens_path.exists():
        print("❌ No se encontró archivo de tokens de Strava")
        return None
    
    with open(strava_tokens_path, 'r') as f:
        tokens = json.load(f)
    
    # Verificar si el token ha expirado
    expires_at = tokens.get('expires_at', 0)
    current_time = datetime.now().timestamp()
    
    if current_time < expires_at:
        print("✅ Token de Strava aún válido")
        return tokens.get('access_token')
    
    # Token expirado, refrescar
    print("🔄 Token de Strava expirado, refrescando...")
    
    refresh_token = tokens.get('refresh_token')
    if not refresh_token:
        print("❌ No se encontró refresh_token")
        return None
    
    # Credenciales de la app
    CLIENT_ID = "197414"
    CLIENT_SECRET = "a96a7843d21e79d5520af03696bf57c1a03adaec"
    
    # Refrescar token
    token_url = "https://www.strava.com/oauth/token"
    token_data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }
    
    try:
        response = requests.post(token_url, data=token_data)
        response.raise_for_status()
        
        new_tokens = response.json()
        
        # Guardar nuevos tokens
        with open(strava_tokens_path, 'w') as f:
            json.dump(new_tokens, f, indent=2)
        
        print("✅ Token de Strava refrescado exitosamente")
        return new_tokens.get('access_token')
    
    except Exception as e:
        print(f"❌ Error al refrescar token: {e}")
        return None

def get_strava_activities():
    """Obtiene las últimas 3 actividades de Strava"""
    
    # Refrescar token si es necesario
    access_token = refresh_strava_token()
    
    if not access_token:
        print("❌ No se pudo obtener access_token válido")
        return []
    
    try:
        # Obtener últimas 3 actividades
        headers = {"Authorization": f"Bearer {access_token}"}
        params = {"per_page": 3}
        
        print("🏃 Consultando últimas 3 actividades de Strava...")
        response = requests.get(
            "https://www.strava.com/api/v3/athlete/activities",
            headers=headers,
            params=params
        )
        
        if response.status_code != 200:
            print(f"❌ Error al obtener actividades de Strava: {response.status_code}")
            print(f"   Respuesta: {response.text}")
            return []
        
        activities = response.json()
        print(f"✅ Obtenidas {len(activities)} actividades")
        
        # Formatear actividades
        formatted_activities = []
        for activity in activities:
            distance_km = activity.get('distance', 0) / 1000
            moving_time = activity.get('moving_time', 0)
            
            # Calcular ritmo para running
            pace_str = ""
            if distance_km > 0 and activity.get('type') in ['Run', 'Walk']:
                pace_min_per_km = moving_time / 60 / distance_km
                pace_min = int(pace_min_per_km)
                pace_sec = int((pace_min_per_km - pace_min) * 60)
                pace_str = f"{pace_min}:{pace_sec:02d} min/km"
            
            # Formatear tiempo
            hours = moving_time // 3600
            minutes = (moving_time % 3600) // 60
            seconds = moving_time % 60
            if hours > 0:
                time_str = f"{hours}h {minutes}m"
            else:
                time_str = f"{minutes}m {seconds}s"
            
            # Fecha
            start_date = activity.get('start_date_local', '')
            date_str = ""
            if start_date:
                dt = datetime.fromisoformat(start_date.replace('Z', '+00:00'))
                date_str = dt.strftime('%b %d, %Y')
            
            formatted_activities.append({
                'name': activity.get('name', 'Sin nombre'),
                'type': activity.get('type', 'N/A'),
                'sport_type': activity.get('sport_type', 'N/A'),
                'distance': f"{distance_km:.2f} km",
                'time': time_str,
                'pace': pace_str,
                'date': date_str,
                'elevation': f"{activity.get('total_elevation_gain', 0):.0f} m",
                'calories': activity.get('calories', 0),
                'id': activity.get('id')
            })
        
        return formatted_activities
    
    except Exception as e:
        print(f"❌ Error al procesar actividades de Strava: {e}")
        return []

def update_readme_with_strava(activities):
    """Actualiza readme.source.md con las actividades de Strava"""
    readme_path = Path(__file__).parent / 'readme.source.md'
    
    if not readme_path.exists():
        print(f"❌ No se encontró {readme_path}")
        return False
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    import re
    
    # Buscar el marcador donde insertar la tabla (después del widget de Strava SVG)
    # El patrón busca la línea con strava-widget.svg seguida de ---
    strava_widget_pattern = r'(<img src="\.\/assets\/strava-widget\.svg"[^>]*>)\n\n---'
    
    match = re.search(strava_widget_pattern, content)
    
    if not match:
        print("❌ No se encontró el patrón del widget de Strava en readme.source.md")
        return False
    
    # Primero, eliminar cualquier tabla de Strava existente
    # Buscar y eliminar la sección de actividades si ya existe
    existing_table_pattern = r'\n\n#### 🏃 Recent Strava Activities.*?(?=\n\n---|\Z)'
    content = re.sub(existing_table_pattern, '', content, flags=re.DOTALL)
    
    # Crear la tabla de actividades de Strava
    strava_section = "\n\n#### 🏃 Recent Strava Activities\n\n"
    strava_section += "<div align=\"center\">\n\n"
    strava_section += "| Activity | Distance | Time | Pace | Date |\n"
    strava_section += "|----------|----------|------|------|------|\n"
    
    for activity in activities:
        name = activity['name'][:40] + "..." if len(activity['name']) > 40 else activity['name']
        pace = activity['pace'] if activity['pace'] else "N/A"
        strava_section += f"| {name} | {activity['distance']} | {activity['time']} | {pace} | {activity['date']} |\n"
    
    strava_section += "\n</div>"
    
    # Insertar la tabla después del widget SVG
    new_content = re.sub(strava_widget_pattern, r'\1' + strava_section + '\n\n---', content)

    # Actualizar la fecha del footer "Profile information collected and updated by AI assistant"
    today_str = datetime.now().strftime('%B %d, %Y').replace(' 0', ' ')
    new_content = re.sub(
        r'(Profile information collected and updated by AI assistant on )[A-Za-z]+ \d+, \d+',
        rf'\g<1>{today_str}',
        new_content
    )

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✅ readme.source.md actualizado con actividades de Strava")
    return True

def main():
    print("🚀 Strava Activities Updater\n")
    
    # Obtener actividades
    activities = get_strava_activities()
    
    if not activities:
        print("\n❌ No se pudieron obtener actividades de Strava")
        return
    
    # Mostrar actividades
    print("\n📊 Actividades obtenidas:")
    for i, activity in enumerate(activities, 1):
        print(f"  {i}. {activity['name']} - {activity['distance']} - {activity['date']}")
    
    # Actualizar README
    if update_readme_with_strava(activities):
        print("\n✅ Proceso completado exitosamente!")
    else:
        print("\n❌ Error al actualizar readme.source.md")

if __name__ == '__main__':
    main()