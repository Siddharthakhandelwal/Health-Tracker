# 📡 Health Tracker API Reference Guide

A comprehensive guide to using the Health Tracker API endpoints for developers and non-technical users.

## 🌐 Base URL

When running locally:
```
http://localhost:8000
```

When deployed:
```
https://your-domain.com
```

## 📋 Quick Reference

| Endpoint | Method | Purpose | Response Time |
|----------|--------|---------|---------------|
| `/water` | POST | Water intake tracking and hydration advice | ~2-3 seconds |
| `/gym` | POST | Workout motivation and exercise guidance | ~2-3 seconds |
| `/food` | POST | Nutritional analysis and meal recommendations | ~2-3 seconds |

## 🔗 Interactive Documentation

FastAPI automatically generates interactive documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 💧 Water Endpoint - `/water`

### Purpose
Analyzes your water intake data and provides personalized hydration advice based on your consumption patterns.

### Request Format
```http
POST /water
Content-Type: application/json

{
  "amount_liters": 2.5,
  "time": "2024-06-01T10:00:00",
  "weight_kg": 70,
  "activity_level": "moderate"
}
```

### Required Fields
- `amount_liters` (number): Amount of water consumed in liters

### Optional Fields
- `time` (string): ISO 8601 timestamp of consumption
- `weight_kg` (number): Your body weight in kilograms
- `activity_level` (string): "low", "moderate", "high"
- `temperature` (number): Ambient temperature in Celsius
- `exercise_duration` (number): Minutes of exercise today

### Request Examples

#### Basic Water Tracking
```json
{
  "amount_liters": 1.5
}
```

#### Detailed Water Tracking
```json
{
  "amount_liters": 2.0,
  "time": "2024-06-01T14:30:00",
  "weight_kg": 65,
  "activity_level": "high",
  "temperature": 32,
  "exercise_duration": 60
}
```

#### Morning Hydration Check
```json
{
  "amount_liters": 0.5,
  "time": "2024-06-01T07:00:00",
  "note": "just woke up"
}
```

### Response Format
```json
{
  "message": "Great hydration! Aim for 2.5L today. Keep sipping throughout the day for optimal health!"
}
```

### Sample Responses

#### Encouraging Response
```json
{
  "message": "Excellent hydration! You're on track. Drink 500ml more before evening for perfect balance."
}
```

#### Motivational Response
```json
{
  "message": "Good start! Increase intake by 1L today. Your body needs extra water after exercise."
}
```

#### Advisory Response
```json
{
  "message": "Dehydration risk! Drink 750ml now, then 250ml every hour. Your health depends on it!"
}
```

## 🏋️ Gym Endpoint - `/gym`

### Purpose
Provides workout motivation, exercise intensity suggestions, and fitness guidance based on your activity data.

### Request Format
```http
POST /gym
Content-Type: application/json

{
  "activity": "running",
  "duration_minutes": 45,
  "intensity": "moderate",
  "calories_burned": 400
}
```

### Required Fields
- `activity` (string): Type of exercise performed

### Optional Fields
- `duration_minutes` (number): Exercise duration in minutes
- `intensity` (string): "low", "moderate", "high"
- `calories_burned` (number): Estimated calories burned
- `heart_rate` (number): Average heart rate during exercise
- `equipment_used` (array): List of equipment used
- `muscle_groups` (array): Targeted muscle groups
- `rest_periods` (number): Number of rest periods taken

### Request Examples

#### Basic Workout Log
```json
{
  "activity": "weightlifting"
}
```

#### Detailed Cardio Session
```json
{
  "activity": "running",
  "duration_minutes": 30,
  "intensity": "high",
  "calories_burned": 350,
  "heart_rate": 165,
  "distance_km": 5.2
}
```

#### Strength Training Session
```json
{
  "activity": "weight training",
  "duration_minutes": 75,
  "intensity": "moderate",
  "equipment_used": ["barbell", "dumbbells", "bench"],
  "muscle_groups": ["chest", "triceps", "shoulders"],
  "sets_completed": 12,
  "rest_periods": 8
}
```

#### Yoga/Flexibility Session
```json
{
  "activity": "yoga",
  "duration_minutes": 60,
  "intensity": "low",
  "style": "hatha",
  "flexibility_focus": ["hamstrings", "shoulders", "spine"]
}
```

### Response Format
```json
{
  "message": "Excellent 45-min run! Keep this consistency. Add strength training twice weekly for balanced fitness."
}
```

### Sample Responses

#### Motivational Response
```json
{
  "message": "Amazing workout! Your dedication shows. Tomorrow try 10% more intensity for continued progress."
}
```

#### Advisory Response
```json
{
  "message": "Good effort! Add 15 minutes next time. Include stretching for better recovery and flexibility."
}
```

#### Balanced Training Suggestion
```json
{
  "message": "Great cardio! Balance with strength training. Aim for 3 cardio + 2 strength sessions weekly."
}
```

## 🍎 Food Endpoint - `/food`

### Purpose
Analyzes your meal data, estimates caloric intake, and provides nutritional guidance and healthy eating motivation.

### Request Format
```http
POST /food
Content-Type: application/json

{
  "meal": "breakfast",
  "food": "oatmeal with berries and almonds",
  "estimated_calories": 350,
  "meal_time": "2024-06-01T08:00:00"
}
```

### Required Fields
- `food` (string): Description of food consumed

### Optional Fields
- `meal` (string): "breakfast", "lunch", "dinner", "snack"
- `estimated_calories` (number): Your calorie estimate
- `meal_time` (string): ISO 8601 timestamp
- `portion_size` (string): "small", "medium", "large"
- `ingredients` (array): List of main ingredients
- `cooking_method` (string): How food was prepared
- `dietary_restrictions` (array): Any dietary limitations
- `satisfaction_level` (number): 1-10 how satisfied you felt

### Request Examples

#### Simple Meal Log
```json
{
  "food": "grilled chicken salad"
}
```

#### Detailed Breakfast
```json
{
  "meal": "breakfast",
  "food": "two eggs, whole grain toast, avocado, and orange juice",
  "estimated_calories": 450,
  "meal_time": "2024-06-01T07:30:00",
  "portion_size": "medium",
  "cooking_method": "scrambled eggs, toasted bread"
}
```

#### Lunch with Nutritional Focus
```json
{
  "meal": "lunch",
  "food": "quinoa bowl with grilled vegetables, chickpeas, and tahini dressing",
  "estimated_calories": 520,
  "ingredients": ["quinoa", "bell peppers", "zucchini", "chickpeas", "tahini"],
  "dietary_restrictions": ["vegetarian"],
  "satisfaction_level": 8
}
```

#### Snack Tracking
```json
{
  "meal": "snack",
  "food": "apple with peanut butter",
  "estimated_calories": 190,
  "meal_time": "2024-06-01T15:30:00",
  "portion_size": "small"
}
```

#### Dinner Analysis
```json
{
  "meal": "dinner",
  "food": "salmon fillet with roasted sweet potato and steamed broccoli",
  "estimated_calories": 580,
  "cooking_method": "baked salmon, roasted vegetables",
  "ingredients": ["salmon", "sweet potato", "broccoli", "olive oil"],
  "satisfaction_level": 9
}
```

### Response Format
```json
{
  "message": "Good protein from milk! Add fruits or nuts to boost nutrition. Aim for 300-400 breakfast calories."
}
```

### Sample Responses

#### Nutritional Praise
```json
{
  "message": "Excellent balanced meal! Perfect protein-carb ratio. This supports your fitness goals beautifully."
}
```

#### Improvement Suggestion
```json
{
  "message": "Good choice! Add more vegetables next time. Aim for half your plate to be colorful veggies."
}
```

#### Calorie Guidance
```json
{
  "message": "Great breakfast! Around 400 calories is perfect. Include protein in every meal for sustained energy."
}
```

## 📊 Response Codes & Error Handling

### HTTP Status Codes

| Code | Status | Meaning | Action Required |
|------|--------|---------|-----------------|
| 200 | Success | Request processed successfully | None |
| 400 | Bad Request | Invalid data format or missing required fields | Check request format |
| 422 | Unprocessable Entity | Valid JSON but invalid data types | Verify data types |
| 500 | Internal Server Error | Server or AI service error | Retry request, check server logs |

### Success Response
```json
{
  "message": "Your personalized health advice here (≤25 words)"
}
```

### Error Response Format
```json
{
  "detail": "Error description explaining what went wrong"
}
```

### Common Error Examples

#### Missing Required Field
```json
{
  "detail": "Field required: 'food' is required for food endpoint"
}
```

#### Invalid Data Type
```json
{
  "detail": "Input should be a valid number for 'amount_liters'"
}
```

#### Server Error
```json
{
  "detail": "Sorry, there was an error processing your request."
}
```

## 🔧 Testing Your Requests

### Using cURL

#### Water Endpoint
```bash
curl -X POST "http://localhost:8000/water" \
     -H "Content-Type: application/json" \
     -d '{"amount_liters": 2.0, "time": "2024-06-01T10:00:00"}'
```

#### Gym Endpoint
```bash
curl -X POST "http://localhost:8000/gym" \
     -H "Content-Type: application/json" \
     -d '{"activity": "running", "duration_minutes": 30}'
```

#### Food Endpoint
```bash
curl -X POST "http://localhost:8000/food" \
     -H "Content-Type: application/json" \
     -d '{"meal": "lunch", "food": "chicken salad with vegetables"}'
```

### Using Python Requests

```python
import requests
import json

# Base URL
base_url = "http://localhost:8000"

# Water tracking
water_data = {
    "amount_liters": 2.5,
    "time": "2024-06-01T14:00:00",
    "weight_kg": 70
}
response = requests.post(f"{base_url}/water", json=water_data)
print(f"Water Response: {response.json()}")

# Gym tracking
gym_data = {
    "activity": "weight training",
    "duration_minutes": 60,
    "intensity": "high"
}
response = requests.post(f"{base_url}/gym", json=gym_data)
print(f"Gym Response: {response.json()}")

# Food tracking
food_data = {
    "meal": "dinner",
    "food": "grilled salmon with quinoa and vegetables",
    "estimated_calories": 550
}
response = requests.post(f"{base_url}/food", json=food_data)
print(f"Food Response: {response.json()}")
```

### Using JavaScript/Fetch

```javascript
// Water tracking
const waterData = {
    amount_liters: 2.0,
    time: "2024-06-01T10:00:00",
    activity_level: "moderate"
};

fetch('http://localhost:8000/water', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(waterData)
})
.then(response => response.json())
.then(data => console.log('Water advice:', data.message));

// Gym tracking
const gymData = {
    activity: "cycling",
    duration_minutes: 45,
    intensity: "moderate"
};

fetch('http://localhost:8000/gym', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(gymData)
})
.then(response => response.json())
.then(data => console.log('Gym motivation:', data.message));
```

## 🎯 Best Practices

### Request Optimization
1. **Include relevant context**: More data = better advice
2. **Use consistent timestamps**: ISO 8601 format preferred
3. **Be specific in descriptions**: "30-minute high-intensity interval training" vs "exercise"
4. **Include units**: Always specify liters, minutes, calories, etc.

### Error Handling
1. **Check status codes**: Always verify 200 response
2. **Handle timeouts**: AI responses may take 2-5 seconds
3. **Retry on 500 errors**: Temporary AI service issues
4. **Validate input**: Check data types before sending

### Rate Limiting
- **Recommended**: Max 60 requests per minute
- **Burst limit**: Up to 10 requests per second
- **Production**: Implement exponential backoff

## 🔒 Security Considerations

### API Key Protection
- Never expose your Gemini API key in client-side code
- Use environment variables or secure key management
- Rotate keys regularly in production

### Input Validation
- Sanitize all user inputs before sending
- Validate data types and ranges
- Implement request size limits

### CORS Configuration
- Current setup allows all origins (`*`)
- In production, specify exact domains
- Use HTTPS for all requests

## 📈 Response Time Expectations

| Endpoint | Typical Response Time | Maximum Response Time |
|----------|----------------------|----------------------|
| `/water` | 1-3 seconds | 10 seconds |
| `/gym` | 2-4 seconds | 10 seconds |
| `/food` | 2-5 seconds | 15 seconds |

*Response times depend on AI service load and request complexity*

## 🔄 API Versioning

Current version: **v1** (implicit)

Future versions will be explicitly versioned:
- `/v2/water`
- `/v2/gym` 
- `/v2/food`

## 📞 Support & Troubleshooting

### Common Issues

1. **"Connection refused"**: Server not running
2. **"Invalid JSON"**: Check request format
3. **"Field required"**: Missing required fields
4. **"AI service error"**: Temporary Gemini API issue

### Getting Help

1. Check server logs for detailed error messages
2. Verify your request format against examples
3. Test with provided sample data first
4. Ensure your API key is valid and has quota

---

*This API guide covers all current endpoints and features. For setup instructions, see [SETUP_GUIDE.md](SETUP_GUIDE.md). For practical examples, see [EXAMPLES.md](EXAMPLES.md).*