#!/usr/bin/env python3
"""
Google Health API - Fitness Widget Updater
Obtiene datos de fitness desde Google Health API y genera un SVG widget
"""

import os
import json
import requests
from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from pathlib import Path

# Configuración
SCOPES = ['https://www.googleapis.com/auth/googlehealth.activity_and_fitness.readonly']
API_BASE = 'https://health.googleapis.com/v4'

# Metas semanales (para calcular progreso)
WEEKLY_GOALS = {
    'steps': 70000,      # ~10,000 pasos/día
    'calories': 14000,   # ~2,000 cal/día
    'active_minutes': 210  # ~30 min/día
}

def load_credentials():
    """Carga y valida las credenciales OAuth2"""
    if not os.path.exists('token.json'):
        raise FileNotFoundError("❌ No se encontró token.json. Ejecuta primero: python google_health_setup.py")
    
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # Renovar token si expiró
    if creds.expired and creds.refresh_token:
        print("🔄 Renovando access token...")
        creds.refresh(Request())
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return creds

def get_fitness_data(creds, start_date, end_date):
    """Obtiene datos de fitness desde Google Health API"""
    headers = {
        'Authorization': f'Bearer {creds.token}',
        'Content-Type': 'application/json'
    }
    
    # Formato de fecha para el filtro (Google Health API solo soporta >= y <, no <=)
    start_str = start_date.strftime('%Y-%m-%dT00:00:00')
    # Agregar 1 día para usar < en lugar de <=
    end_date_plus_one = end_date + timedelta(days=1)
    end_str = end_date_plus_one.strftime('%Y-%m-%dT00:00:00')
    
    print(f"📊 Consultando datos del {start_date.date()} al {end_date.date()}...")
    
    # 1. Obtener datos de ejercicio
    exercise_url = f'{API_BASE}/users/me/dataTypes/exercise/dataPoints'
    exercise_params = {
        'filter': f'exercise.interval.civil_start_time >= "{start_str}" AND exercise.interval.civil_start_time < "{end_str}"'
    }
    
    try:
        response = requests.get(exercise_url, headers=headers, params=exercise_params)
        response.raise_for_status()
        data = response.json()
        
        # Procesar datos de ejercicio
        total_steps = 0
        total_calories = 0
        total_active_minutes = 0
        
        data_points = data.get('dataPoints', [])
        print(f"  • Puntos de datos de ejercicio: {len(data_points)}")
        
        # Debug: mostrar detalles de cada punto
        for i, point in enumerate(data_points):
            exercise = point.get('exercise', {})
            metrics = exercise.get('metricsSummary', {})
            
            # Sumar métricas
            steps = metrics.get('steps', '0')
            steps_int = int(steps) if steps else 0
            calories = metrics.get('caloriesKcal', 0)
            
            # Debug log
            start_time = exercise.get('interval', {}).get('civil_start_time', 'N/A')
            print(f"    [{i+1}] {start_time}: {steps_int:,} pasos, {int(calories)} cal")
            
            total_steps += steps_int
            total_calories += calories
            
            # Calcular minutos activos desde activeDuration (formato: "900s" o "3023.500s")
            duration = exercise.get('activeDuration', '0s')
            if duration.endswith('s'):
                seconds = float(duration[:-1])
                total_active_minutes += int(seconds) // 60
        
        return {
            'steps': total_steps,
            'calories': int(total_calories),
            'active_minutes': total_active_minutes
        }
    
    except requests.exceptions.HTTPError as e:
        print(f"❌ Error HTTP: {e}")
        print(f"   Respuesta: {e.response.text}")
        raise
    except Exception as e:
        print(f"❌ Error: {e}")
        raise

def format_number(num):
    """Formatea números con comas para miles"""
    return f"{num:,}"

def calculate_progress(value, goal, max_width=200):
    """Calcula el ancho de la barra de progreso"""
    if goal == 0:
        return 0
    progress = min((value / goal) * 100, 100)
    return int((progress / 100) * max_width)

def generate_svg_widget(stats, week_range, days_elapsed):
    """Genera el SVG widget con las estadísticas"""
    template_path = './assets/fitness-widget-template.svg'
    output_path = './assets/fitness-widget.svg'
    
    if not os.path.exists(template_path):
        print(f"⚠️  No se encontró template en {template_path}")
        return
    
    with open(template_path, 'r', encoding='utf-8') as f:
        svg_content = f.read()
    
    # Calcular promedios diarios
    steps_avg = stats['steps'] // days_elapsed if days_elapsed > 0 else 0
    calories_avg = stats['calories'] // days_elapsed if days_elapsed > 0 else 0
    active_avg = stats['active_minutes'] // days_elapsed if days_elapsed > 0 else 0
    
    # Calcular barras de progreso
    steps_progress = calculate_progress(stats['steps'], WEEKLY_GOALS['steps'])
    calories_progress = calculate_progress(stats['calories'], WEEKLY_GOALS['calories'])
    active_progress = calculate_progress(stats['active_minutes'], WEEKLY_GOALS['active_minutes'])
    
    # Reemplazar placeholders
    replacements = {
        '{{DATE_RANGE}}': week_range,
        '{{STEPS}}': format_number(stats['steps']),
        '{{CALORIES}}': format_number(stats['calories']),
        '{{ACTIVE_MINUTES}}': format_number(stats['active_minutes']),
        '{{STEPS_AVG}}': format_number(steps_avg),
        '{{CALORIES_AVG}}': format_number(calories_avg),
        '{{ACTIVE_AVG}}': format_number(active_avg),
        '{{STEPS_PROGRESS}}': str(steps_progress),
        '{{CALORIES_PROGRESS}}': str(calories_progress),
        '{{ACTIVE_PROGRESS}}': str(active_progress),
        '{{LAST_UPDATED}}': datetime.now().strftime('%Y-%m-%d %H:%M UTC')
    }
    
    for placeholder, value in replacements.items():
        svg_content = svg_content.replace(placeholder, value)
    
    # Guardar SVG actualizado
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    print(f"✅ SVG widget generado en {output_path}")

def update_readme(strava_activities=None):
    """Actualiza el README.source.md con el widget de fitness y actividades de Strava"""
    readme_path = './readme.source.md'
    
    if not os.path.exists(readme_path):
        print(f"⚠️  No se encontró {readme_path}")
        return
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Buscar la sección de fitness stats
    import re
    
    # Encontrar el bloque aura del fitness widget
    fitness_pattern = r'(### 🏃 Fitness Stats - August 2026.*?```aura.*?```.*?</div>)'
    
    match = re.search(fitness_pattern, content, re.DOTALL)
    
    if not match:
        print("⚠️  No se encontró la sección de Fitness Stats en readme.source.md")
        return
    
    fitness_section = match.group(1)
    
    # Agregar actividades de Strava si existen
    if strava_activities and len(strava_activities) > 0:
        strava_section = "\n\n#### 🏃 Recent Strava Activities\n\n"
        strava_section += "<div align=\"center\">\n\n"
        strava_section += "| Activity | Distance | Time | Pace | Date |\n"
        strava_section += "|----------|----------|------|------|------|\n"
        
        for activity in strava_activities:
            name = activity['name'][:30] + "..." if len(activity['name']) > 30 else activity['name']
            pace = activity['pace'] if activity['pace'] else "N/A"
            strava_section += f"| {name} | {activity['distance']} | {activity['time']} | {pace} | {activity['date']} |\n"
        
        strava_section += "\n</div>"
        
        # Reemplazar la sección completa
        new_fitness_section = fitness_section + strava_section
        new_content = content.replace(fitness_section, new_fitness_section)
    else:
        new_content = content
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ readme.source.md actualizado con widget de fitness y actividades de Strava")

def get_strava_activities():
    """Obtiene las últimas 3 actividades de Strava"""
    strava_tokens_path = Path(__file__).parent.parent / 'strava-setup' / 'strava_tokens.json'
    
    if not strava_tokens_path.exists():
        print("⚠️  No se encontró archivo de tokens de Strava")
        return []
    
    try:
        with open(strava_tokens_path, 'r') as f:
            tokens = json.load(f)
        
        access_token = tokens.get('access_token')
        if not access_token:
            print("⚠️  No se encontró access_token en tokens de Strava")
            return []
        
        # Obtener últimas 3 actividades
        headers = {"Authorization": f"Bearer {access_token}"}
        params = {"per_page": 3}
        
        print("\n🏃 Consultando últimas 3 actividades de Strava...")
        response = requests.get(
            "https://www.strava.com/api/v3/athlete/activities",
            headers=headers,
            params=params
        )
        
        if response.status_code != 200:
            print(f"⚠️  Error al obtener actividades de Strava: {response.status_code}")
            return []
        
        activities = response.json()
        print(f"  ✅ Obtenidas {len(activities)} actividades")
        
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
        print(f"⚠️  Error al procesar actividades de Strava: {e}")
        return []

def main():
    """Función principal"""
    print("🚀 Google Health API - Fitness Widget Updater\n")
    
    # Cargar credenciales
    creds = load_credentials()
    
    # Calcular rango de fechas (mes actual: desde el 1 hasta hoy)
    today = datetime.now()
    start_of_month = today.replace(day=1)
    days_elapsed = today.day
    
    # Obtener datos
    stats = get_fitness_data(creds, start_of_month, today)
    
    # Mostrar resultados
    print("\n📈 Estadísticas obtenidas (totales del mes):")
    print(f"  👟 Pasos: {stats['steps']:,}")
    print(f"  🔥 Calorías: {stats['calories']:,}")
    print(f"  ⏱️  Minutos activos: {stats['active_minutes']:,}")
    
    # Generar SVG widget
    month_range = f"{start_of_month.strftime('%B %Y')}"
    generate_svg_widget(stats, month_range, days_elapsed)
    
    # Obtener actividades de Strava
    strava_activities = get_strava_activities()
    
    # Actualizar README
    update_readme(strava_activities)
    
    print("\n✅ Proceso completado exitosamente!")

if __name__ == '__main__':
    main()