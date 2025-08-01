# 🌟 Health Tracker Usage Examples

Real-world scenarios and practical examples for using the Health Tracker API effectively.

## 📋 Table of Contents

1. [Daily Health Routines](#-daily-health-routines)
2. [User Type Examples](#-user-type-examples)
3. [Integration Examples](#-integration-examples)
4. [Sample AI Responses](#-sample-ai-responses)
5. [Advanced Usage Patterns](#-advanced-usage-patterns)
6. [Mobile App Integration](#-mobile-app-integration)
7. [Web Dashboard Examples](#-web-dashboard-examples)

## 🌅 Daily Health Routines

### Morning Health Check-in

**Scenario:** Sarah starts her day by logging her morning water intake and planning her workout.

```python
import requests
import json
from datetime import datetime

base_url = "http://localhost:8000"

# Morning water intake
morning_water = {
    "amount_liters": 0.5,
    "time": datetime.now().isoformat(),
    "note": "First glass after waking up",
    "temperature": 22
}

response = requests.post(f"{base_url}/water", json=morning_water)
print("Morning hydration advice:", response.json()["message"])

# Plan today's workout
workout_plan = {
    "activity": "planned workout",
    "duration_minutes": 0,
    "intensity": "moderate",
    "planned_activity": "yoga and light cardio"
}

response = requests.post(f"{base_url}/gym", json=workout_plan)
print("Workout motivation:", response.json()["message"])
```

**Expected Output:**
```
Morning hydration advice: Great start! Drink 2L more today. Morning hydration kickstarts metabolism and brain function.
Workout motivation: Perfect planning! Yoga plus cardio is ideal. Consistency beats intensity for long-term health.
```

### Post-Workout Analysis

**Scenario:** Mike just finished his gym session and wants to log his workout and plan his post-workout nutrition.

```python
# Log completed workout
workout_data = {
    "activity": "strength training",
    "duration_minutes": 75,
    "intensity": "high",
    "exercises": ["deadlifts", "bench press", "squats", "pull-ups"],
    "sets_completed": 16,
    "estimated_calories_burned": 450,
    "heart_rate_avg": 145
}

response = requests.post(f"{base_url}/gym", json=workout_data)
print("Post-workout feedback:", response.json()["message"])

# Plan post-workout meal
post_workout_meal = {
    "meal": "post-workout snack",
    "food": "protein shake with banana and peanut butter",
    "estimated_calories": 320,
    "timing": "within 30 minutes of workout",
    "goal": "muscle recovery"
}

response = requests.post(f"{base_url}/food", json=post_workout_meal)
print("Nutrition advice:", response.json()["message"])
```

### Evening Wind-down

**Scenario:** Lisa reviews her daily intake before bed and plans for tomorrow.

```python
# Evening water check
daily_water_total = {
    "amount_liters": 2.8,
    "time": "2024-06-01T21:00:00",
    "daily_total": True,
    "activity_level": "moderate",
    "weather": "hot day"
}

response = requests.post(f"{base_url}/water", json=daily_water_total)
print("Daily hydration summary:", response.json()["message"])

# Log dinner
dinner_data = {
    "meal": "dinner",
    "food": "grilled salmon, quinoa, roasted vegetables, and mixed greens salad",
    "estimated_calories": 580,
    "meal_time": "2024-06-01T19:30:00",
    "satisfaction_level": 9,
    "cooking_method": "grilled and roasted"
}

response = requests.post(f"{base_url}/food", json=dinner_data)
print("Dinner feedback:", response.json()["message"])
```

## 👥 User Type Examples

### The Athlete - High Performance Tracking

**Profile:** Professional runner training for a marathon

```python
# High-intensity training session
athlete_workout = {
    "activity": "interval running",
    "duration_minutes": 90,
    "intensity": "very high",
    "distance_km": 15,
    "pace_per_km": "4:20",
    "heart_rate_zones": {
        "zone_1": 10,  # minutes
        "zone_2": 20,
        "zone_3": 35,
        "zone_4": 20,
        "zone_5": 5
    },
    "weather_conditions": "humid, 28°C"
}

response = requests.post(f"{base_url}/gym", json=athlete_workout)
print("Elite training feedback:", response.json()["message"])

# High-performance hydration
athlete_hydration = {
    "amount_liters": 3.5,
    "time": "2024-06-01T16:00:00",
    "electrolyte_replacement": True,
    "sweat_rate": "high",
    "training_duration": 90,
    "body_weight": 68
}

response = requests.post(f"{base_url}/water", json=athlete_hydration)
print("Performance hydration advice:", response.json()["message"])

# Performance nutrition
athlete_nutrition = {
    "meal": "pre-workout",
    "food": "oatmeal with banana, honey, and almonds plus sports drink",
    "estimated_calories": 450,
    "carb_to_protein_ratio": "4:1",
    "timing": "2 hours before training",
    "goal": "sustained energy for long run"
}

response = requests.post(f"{base_url}/food", json=athlete_nutrition)
print("Performance nutrition advice:", response.json()["message"])
```

### The Beginner - Starting Fitness Journey

**Profile:** Someone new to fitness and healthy eating

```python
# First week of exercise
beginner_workout = {
    "activity": "walking",
    "duration_minutes": 20,
    "intensity": "low",
    "distance_km": 1.5,
    "experience_level": "beginner",
    "goal": "build habit and endurance"
}

response = requests.post(f"{base_url}/gym", json=beginner_workout)
print("Beginner encouragement:", response.json()["message"])

# Learning portion control
beginner_meal = {
    "meal": "lunch",
    "food": "turkey sandwich with lettuce and tomato, apple, and water",
    "estimated_calories": 420,
    "portion_awareness": "trying to eat mindfully",
    "goal": "learn healthy portions"
}

response = requests.post(f"{base_url}/food", json=beginner_meal)
print("Beginner nutrition guidance:", response.json()["message"])
```

### The Busy Professional - Quick Health Checks

**Profile:** Office worker with limited time for detailed tracking

```python
# Quick lunch break workout
professional_workout = {
    "activity": "stair climbing",
    "duration_minutes": 15,
    "intensity": "moderate",
    "location": "office building",
    "time_constraint": "lunch break"
}

response = requests.post(f"{base_url}/gym", json=professional_workout)
print("Quick workout motivation:", response.json()["message"])

# Desk job hydration
office_hydration = {
    "amount_liters": 1.2,
    "time": "2024-06-01T14:00:00",
    "environment": "air conditioned office",
    "activity_level": "sedentary",
    "reminder_needed": True
}

response = requests.post(f"{base_url}/water", json=office_hydration)
print("Office hydration reminder:", response.json()["message"])

# Quick healthy meal
grab_and_go_meal = {
    "meal": "lunch",
    "food": "pre-made salad with grilled chicken from cafeteria",
    "estimated_calories": 380,
    "time_to_eat": 15,
    "convenience_factor": "high"
}

response = requests.post(f"{base_url}/food", json=grab_and_go_meal)
print("Quick meal feedback:", response.json()["message"])
```

## 🔗 Integration Examples

### Python Requests Library

```python
import requests
import json
from datetime import datetime, timedelta

class HealthTracker:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()
    
    def log_water(self, amount_liters, **kwargs):
        data = {"amount_liters": amount_liters, **kwargs}
        response = self.session.post(f"{self.base_url}/water", json=data)
        return response.json()
    
    def log_workout(self, activity, duration_minutes=None, **kwargs):
        data = {"activity": activity}
        if duration_minutes:
            data["duration_minutes"] = duration_minutes
        data.update(kwargs)
        response = self.session.post(f"{self.base_url}/gym", json=data)
        return response.json()
    
    def log_meal(self, food, meal=None, **kwargs):
        data = {"food": food}
        if meal:
            data["meal"] = meal
        data.update(kwargs)
        response = self.session.post(f"{self.base_url}/food", json=data)
        return response.json()

# Usage example
tracker = HealthTracker()

# Log daily activities
water_advice = tracker.log_water(2.0, time=datetime.now().isoformat())
workout_advice = tracker.log_workout("running", 30, intensity="moderate")
meal_advice = tracker.log_meal("grilled chicken salad", "lunch", estimated_calories=450)

print("Water:", water_advice["message"])
print("Workout:", workout_advice["message"])
print("Meal:", meal_advice["message"])
```

### JavaScript/Node.js Integration

```javascript
const axios = require('axios');

class HealthTrackerAPI {
    constructor(baseURL = 'http://localhost:8000') {
        this.baseURL = baseURL;
        this.client = axios.create({ baseURL });
    }

    async logWater(data) {
        try {
            const response = await this.client.post('/water', data);
            return response.data;
        } catch (error) {
            console.error('Water logging error:', error.response?.data || error.message);
            throw error;
        }
    }

    async logWorkout(data) {
        try {
            const response = await this.client.post('/gym', data);
            return response.data;
        } catch (error) {
            console.error('Workout logging error:', error.response?.data || error.message);
            throw error;
        }
    }

    async logMeal(data) {
        try {
            const response = await this.client.post('/food', data);
            return response.data;
        } catch (error) {
            console.error('Meal logging error:', error.response?.data || error.message);
            throw error;
        }
    }
}

// Usage example
async function dailyHealthCheck() {
    const tracker = new HealthTrackerAPI();
    
    try {
        // Morning routine
        const waterResult = await tracker.logWater({
            amount_liters: 0.5,
            time: new Date().toISOString(),
            note: "Morning hydration"
        });
        
        const workoutResult = await tracker.logWorkout({
            activity: "yoga",
            duration_minutes: 30,
            intensity: "low"
        });
        
        const breakfastResult = await tracker.logMeal({
            meal: "breakfast",
            food: "oatmeal with berries and nuts",
            estimated_calories: 350
        });
        
        console.log('Water advice:', waterResult.message);
        console.log('Workout motivation:', workoutResult.message);
        console.log('Breakfast feedback:', breakfastResult.message);
        
    } catch (error) {
        console.error('Health tracking failed:', error);
    }
}

dailyHealthCheck();
```

### cURL Examples for Testing

```bash
#!/bin/bash

# Water tracking
curl -X POST "http://localhost:8000/water" \
     -H "Content-Type: application/json" \
     -d '{
       "amount_liters": 2.5,
       "time": "2024-06-01T10:00:00",
       "activity_level": "high"
     }'

# Gym tracking
curl -X POST "http://localhost:8000/gym" \
     -H "Content-Type: application/json" \
     -d '{
       "activity": "weight training",
       "duration_minutes": 60,
       "intensity": "high",
       "muscle_groups": ["chest", "triceps"]
     }'

# Food tracking
curl -X POST "http://localhost:8000/food" \
     -H "Content-Type: application/json" \
     -d '{
       "meal": "dinner",
       "food": "grilled salmon with quinoa and vegetables",
       "estimated_calories": 550
     }'
```

## 🤖 Sample AI Responses

### Water Endpoint Responses

**Scenario: Low water intake**
```json
{
  "message": "Dehydration alert! Drink 1L immediately, then 250ml hourly. Your health depends on proper hydration!"
}
```

**Scenario: Good hydration**
```json
{
  "message": "Perfect hydration! You're drinking optimally. Keep this 2.5L daily habit for peak performance."
}
```

**Scenario: Post-exercise hydration**
```json
{
  "message": "Great post-workout hydration! Add electrolytes after intense exercise. You're recovering like a pro!"
}
```

### Gym Endpoint Responses

**Scenario: Beginner workout**
```json
{
  "message": "Fantastic first step! Every journey starts with one workout. Tomorrow, try 5 minutes more!"
}
```

**Scenario: Consistent training**
```json
{
  "message": "Incredible consistency! Your dedication shows. Add variety with strength training for balanced fitness."
}
```

**Scenario: High-intensity workout**
```json
{
  "message": "Beast mode activated! Excellent high-intensity session. Remember rest days for optimal muscle recovery."
}
```

### Food Endpoint Responses

**Scenario: Balanced meal**
```json
{
  "message": "Nutritionally perfect! Great protein-carb-veggie balance. This meal supports your fitness goals beautifully."
}
```

**Scenario: High-calorie meal**
```json
{
  "message": "High calories detected! Balance with lighter meals today. Focus on vegetables and lean proteins."
}
```

**Scenario: Healthy snack**
```json
{
  "message": "Smart snacking! Nuts and fruit provide sustained energy. Perfect choice for afternoon fuel."
}
```

## 🚀 Advanced Usage Patterns

### Batch Processing Multiple Entries

```python
import asyncio
import aiohttp
import json

async def batch_health_logging():
    daily_data = [
        {"endpoint": "water", "data": {"amount_liters": 0.5, "time": "07:00"}},
        {"endpoint": "food", "data": {"meal": "breakfast", "food": "oatmeal with berries"}},
        {"endpoint": "gym", "data": {"activity": "morning walk", "duration_minutes": 20}},
        {"endpoint": "water", "data": {"amount_liters": 0.8, "time": "12:00"}},
        {"endpoint": "food", "data": {"meal": "lunch", "food": "chicken salad wrap"}},
        {"endpoint": "water", "data": {"amount_liters": 1.0, "time": "18:00"}},
        {"endpoint": "food", "data": {"meal": "dinner", "food": "grilled fish with vegetables"}}
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for entry in daily_data:
            url = f"http://localhost:8000/{entry['endpoint']}"
            task = session.post(url, json=entry['data'])
            tasks.append(task)
        
        responses = await asyncio.gather(*tasks)
        
        for i, response in enumerate(responses):
            result = await response.json()
            print(f"{daily_data[i]['endpoint'].title()}: {result['message']}")

# Run batch processing
asyncio.run(batch_health_logging())
```

### Weekly Health Summary

```python
from datetime import datetime, timedelta
import requests

def weekly_health_summary():
    base_url = "http://localhost:8000"
    
    # Simulate a week of data
    weekly_activities = [
        # Monday
        {"day": "Monday", "water": 2.2, "gym": "running", "duration": 30},
        # Tuesday  
        {"day": "Tuesday", "water": 2.8, "gym": "strength training", "duration": 45},
        # Wednesday
        {"day": "Wednesday", "water": 2.0, "gym": "yoga", "duration": 60},
        # Thursday
        {"day": "Thursday", "water": 3.0, "gym": "cycling", "duration": 40},
        # Friday
        {"day": "Friday", "water": 2.5, "gym": "swimming", "duration": 35},
        # Saturday
        {"day": "Saturday", "water": 2.3, "gym": "hiking", "duration": 90},
        # Sunday
        {"day": "Sunday", "water": 2.1, "gym": "rest day", "duration": 0}
    ]
    
    print("🗓️ Weekly Health Summary")
    print("=" * 50)
    
    for day_data in weekly_activities:
        print(f"\n📅 {day_data['day']}:")
        
        # Water tracking
        water_response = requests.post(f"{base_url}/water", 
                                     json={"amount_liters": day_data["water"]})
        print(f"💧 Water: {water_response.json()['message']}")
        
        # Gym tracking (if not rest day)
        if day_data["duration"] > 0:
            gym_response = requests.post(f"{base_url}/gym", 
                                       json={"activity": day_data["gym"], 
                                            "duration_minutes": day_data["duration"]})
            print(f"🏋️ Workout: {gym_response.json()['message']}")
        else:
            print("🏋️ Workout: Rest day - recovery is part of fitness!")

weekly_health_summary()
```

## 📱 Mobile App Integration

### React Native Example

```javascript
import React, { useState } from 'react';
import { View, Text, TextInput, Button, Alert } from 'react-native';

const HealthTracker = () => {
    const [waterAmount, setWaterAmount] = useState('');
    const [activity, setActivity] = useState('');
    const [food, setFood] = useState('');
    
    const API_BASE = 'http://your-server.com:8000';
    
    const logWater = async () => {
        try {
            const response = await fetch(`${API_BASE}/water`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    amount_liters: parseFloat(waterAmount),
                    time: new Date().toISOString()
                })
            });
            
            const result = await response.json();
            Alert.alert('Water Advice', result.message);
        } catch (error) {
            Alert.alert('Error', 'Failed to log water intake');
        }
    };
    
    const logWorkout = async () => {
        try {
            const response = await fetch(`${API_BASE}/gym`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    activity: activity,
                    duration_minutes: 30
                })
            });
            
            const result = await response.json();
            Alert.alert('Workout Motivation', result.message);
        } catch (error) {
            Alert.alert('Error', 'Failed to log workout');
        }
    };
    
    return (
        <View style={{padding: 20}}>
            <Text style={{fontSize: 24, marginBottom: 20}}>Health Tracker</Text>
            
            <TextInput
                placeholder="Water amount (liters)"
                value={waterAmount}
                onChangeText={setWaterAmount}
                keyboardType="numeric"
                style={{borderWidth: 1, padding: 10, marginBottom: 10}}
            />
            <Button title="Log Water" onPress={logWater} />
            
            <TextInput
                placeholder="Activity (e.g., running)"
                value={activity}
                onChangeText={setActivity}
                style={{borderWidth: 1, padding: 10, marginBottom: 10, marginTop: 20}}
            />
            <Button title="Log Workout" onPress={logWorkout} />
        </View>
    );
};

export default HealthTracker;
```

### Flutter Example

```dart
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class HealthTrackerApp extends StatefulWidget {
  @override
  _HealthTrackerAppState createState() => _HealthTrackerAppState();
}

class _HealthTrackerAppState extends State<HealthTrackerApp> {
  final String apiBase = 'http://your-server.com:8000';
  final TextEditingController waterController = TextEditingController();
  final TextEditingController activityController = TextEditingController();
  
  Future<void> logWater() async {
    try {
      final response = await http.post(
        Uri.parse('$apiBase/water'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({
          'amount_liters': double.parse(waterController.text),
          'time': DateTime.now().toIso8601String(),
        }),
      );
      
      if (response.statusCode == 200) {
        final result = json.decode(response.body);
        _showAdvice('Water Advice', result['message']);
      }
    } catch (e) {
      _showAdvice('Error', 'Failed to log water intake');
    }
  }
  
  void _showAdvice(String title, String message) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: Text(title),
        content: Text(message),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: Text('OK'),
          ),
        ],
      ),
    );
  }
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Health Tracker')),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(
              controller: waterController,
              decoration: InputDecoration(
                labelText: 'Water amount (liters)',
                border: OutlineInputBorder(),
              ),
              keyboardType: TextInputType.number,
            ),
            SizedBox(height: 16),
            ElevatedButton(
              onPressed: logWater,
              child: Text('Log Water'),
            ),
          ],
        ),
      ),
    );
  }
}
```

## 🌐 Web Dashboard Examples

### Simple HTML/JavaScript Dashboard

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Health Tracker Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .card { border: 1px solid #ddd; border-radius: 8px; padding: 20px; margin: 10px 0; }
        .input-group { margin: 10px 0; }
        .input-group label { display: block; margin-bottom: 5px; }
        .input-group input, .input-group select { width: 100%; padding: 8px; }
        .btn { background: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; }
        .btn:hover { background: #0056b3; }
        .advice { background: #f8f9fa; border-left: 4px solid #007bff; padding: 15px; margin: 10px 0; }
    </style>
</head>
<body>
    <h1>🏥 Health Tracker Dashboard</h1>
    
    <!-- Water Tracking -->
    <div class="card">
        <h2>💧 Water Tracking</h2>
        <div class="input-group">
            <label>Amount (liters):</label>
            <input type="number" id="waterAmount" step="0.1" placeholder="2.0">
        </div>
        <button class="btn" onclick="logWater()">Log Water</button>
        <div id="waterAdvice" class="advice" style="display: none;"></div>
    </div>
    
    <!-- Gym Tracking -->
    <div class="card">
        <h2>🏋️ Workout Tracking</h2>
        <div class="input-group">
            <label>Activity:</label>
            <select id="activityType">
                <option value="running">Running</option>
                <option value="cycling">Cycling</option>
                <option value="swimming">Swimming</option>
                <option value="weight training">Weight Training</option>
                <option value="yoga">Yoga</option>
            </select>
        </div>
        <div class="input-group">
            <label>Duration (minutes):</label>
            <input type="number" id="workoutDuration" placeholder="30">
        </div>
        <button class="btn" onclick="logWorkout()">Log Workout</button>
        <div id="workoutAdvice" class="advice" style="display: none;"></div>
    </div>
    
    <!-- Food Tracking -->
    <div class="card">
        <h2>🍎 Food Tracking</h2>
        <div class="input-group">
            <label>Meal Type:</label>
            <select id="mealType">
                <option value="breakfast">Breakfast</option>
                <option value="lunch">Lunch</option>
                <option value="dinner">Dinner</option>
                <option value="snack">Snack</option>
            </select>
        </div>
        <div class="input-group">
            <label>Food Description:</label>
            <input type="text" id="foodDescription" placeholder="Grilled chicken with vegetables">
        </div>
        <button class="btn" onclick="logFood()">Log Food</button>
        <div id="foodAdvice" class="advice" style="display: none;"></div>
    </div>

    <script>
        const API_BASE = 'http://localhost:8000';
        
        async function logWater() {
            const amount = document.getElementById('waterAmount').value;
            if (!amount) {
                alert('Please enter water amount');
                return;
            }
            
            try {
                const response = await fetch(`${API_BASE}/water`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        amount_liters: parseFloat(amount),
                        time: new Date().toISOString()
                    })
                });
                
                const result = await response.json();
                showAdvice('waterAdvice', result.message);
            } catch (error) {
                alert('Error logging water intake');
            }
        }
        
        async function logWorkout() {
            const activity = document.getElementById('activityType').value;
            const duration = document.getElementById('workoutDuration').value;
            
            if (!duration) {
                alert('Please enter workout duration');
                return;
            }
            
            try {
                const response = await fetch(`${API_BASE}/gym`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        activity: activity,
                        duration_minutes: parseInt(duration)
                    })
                });
                
                const result = await response.json();
                showAdvice('workoutAdvice', result.message);
            } catch (error) {
                alert('Error logging workout');
            }
        }
        
        async function logFood() {
            const meal = document.getElementById('mealType').value;
            const food = document.getElementById('foodDescription').value;
            
            if (!food) {
                alert('Please enter food description');
                return;
            }
            
            try {
                const response = await fetch(`${API_BASE}/food`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        meal: meal,
                        food: food
                    })
                });
                
                const result = await response.json();
                showAdvice('foodAdvice', result.message);
            } catch (error) {
                alert('Error logging food');
            }
        }
        
        function showAdvice(elementId, message) {
            const element = document.getElementById(elementId);
            element.innerHTML = `<strong>AI Advice:</strong> ${message}`;
            element.style.display = 'block';
        }
    </script>
</body>
</html>
```

## 🎯 Best Practices for Integration

### Error Handling

```python
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError

def safe_health_log(endpoint, data, max_retries=3):
    base_url = "http://localhost:8000"
    
    for attempt in range(max_retries):
        try:
            response = requests.post(
                f"{base_url}/{endpoint}", 
                json=data, 
                timeout=10
            )
            response.raise_for_status()
            return response.json()
            
        except ConnectionError:
            print(f"Connection failed (attempt {attempt + 1}/{max_retries})")
            if attempt == max_retries - 1:
                return {"message": "Unable to connect to health tracker"}
                
        except Timeout:
            print(f"Request timed out (attempt {attempt + 1}/{max_retries})")
            if attempt == max_retries - 1:
                return {"message": "Request timed out, please try again"}
                
        except RequestException as e:
            print(f"Request failed: {e}")
            return {"message": "Error processing request"}

# Usage
result = safe_health_log("water", {"amount_liters": 2.0})
print(result["message"])
```

### Data Validation

```python
def validate_water_data(data):
    if "amount_liters" not in data:
        raise ValueError("amount_liters is required")
    
    amount = data["amount_liters"]
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError("amount_liters must be a positive number")
    
    if amount > 10:  # Reasonable upper limit
        raise ValueError("amount_liters seems too high (max 10L)")
    
    return True

def validate_gym_data(data):
    if "activity