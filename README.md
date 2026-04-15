# Policy-Lens
PolicyLens is an AI-powered tool that analyzes Terms of Service documents from AI companies and flags clauses that violate major privacy and AI governance laws. 

## What It Does

Upload or paste any AI product's Terms of Service and PolicyLens will:
- Check it against **36 legal rules** across 6 major laws
- Flag violations with severity levels (HIGH / MEDIUM / LOW)
- Show the exact problematic clause from the document
- Generate a downloadable JSON compliance report

## Laws Covered

| Law | Articles Checked |
|---|---|
| 🇪🇺 GDPR | 13 articles |
| EU AI Act | 9 articles |
| 🇺🇸 CCPA | 4 sections |
| COPPA | 3 sections |
| DSA (Digital Services Act) | 4 articles |
| US AI Executive Order | 3 sections |

<img width="959" height="507" alt="image" src="https://github.com/user-attachments/assets/68f3d064-6642-40fe-b0a3-0132e2f26f34" />

## How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/policylens.git
cd policylens
```
### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Set up your API keys
Create a `.env` file in the root folder: GROQ_API_KEY=your_groq_api_key_here. Get a free Groq API key at https://console.groq.com
### 5. Run the app
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`

## Project Structure
<img width="310" height="239" alt="image" src="https://github.com/user-attachments/assets/a149d18b-7575-455a-8092-40a53e679bea" />

## How It Works
1. **Loads** the ToS document (upload, paste, or use sample)
2. **Chunks** the document into 8000-word segments
3. **Sends** all 36 rules + one chunk in a single batched API call to Groq (Llama 3.3 70B)
4. **Parses** the response to extract violations, severity, and problematic clauses
5. **Displays** results grouped by law in an interactive Streamlit dashboard
6. The batched approach means only **3 API calls total** per analysis — fast and rate-limit friendly.
