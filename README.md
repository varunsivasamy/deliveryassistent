# ZukiCare AI - Delivery Assistant

A voice-enabled customer service AI for food delivery apps, built with LiveKit and Google Gemini Realtime API.

## Features

- Real-time voice interaction
- Bilingual support (English + Tanglish)
- Customer service for food delivery apps
- Noise cancellation for better audio quality
- Order assistance, payment support, and account help

## Setup

### Prerequisites

- Python 3.8+
- Google Cloud API key with Gemini API access
- LiveKit account and credentials

### Installation

1. Clone the repository:
```bash
git clone https://github.com/varunsivasamy/deliveryassistent.git
cd deliveryassistent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. **IMPORTANT: Set up environment variables**
   - Copy `.env.example` to `.env`
   - Fill in your actual API credentials in `.env`
   - **NEVER commit the .env file to git!**

```bash
cp .env.example .env
# Edit .env with your actual API keys
```

### Required Environment Variables

```
GOOGLE_API_KEY=your_google_api_key_here
LIVEKIT_API_KEY=your_livekit_api_key_here
LIVEKIT_API_SECRET=your_livekit_api_secret_here
LIVEKIT_URL=your_livekit_websocket_url_here
```

### Running the Assistant

```bash
python agent.py
```

## Security Notice

⚠️ **IMPORTANT**: Never commit API keys or sensitive credentials to version control. Always use environment variables and keep your `.env` file local only.

## Project Structure

- `agent.py` - Main agent implementation
- `prompt.py` - AI instructions and response configuration
- `requirements.txt` - Python dependencies
- `.env.example` - Template for environment variables
- `.gitignore` - Git ignore rules (includes .env files)

## Contributing

When contributing, ensure you never commit sensitive information like API keys or credentials.