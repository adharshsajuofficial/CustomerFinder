# EventMatch AI — React + FastAPI MVP

## Part 1 working now
- 120 fictional audience profiles in `backend/data/demo_users.csv`
- FastAPI health check, example events, and ranked matching endpoint
- Explainable scoring (interest 40%, skills 25%, city 20%, event preference 15%)
- React dashboard wired to the live backend
- Search, score filter, and ranked CSV export

Scores are prototype relevance scores, not registration probabilities. Demo profiles are fictional.

## Run
Requirements: Python 3.10+, Node.js 18+

Terminal 1:
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
API docs: http://127.0.0.1:8000/docs

Terminal 2:
```bash
cd frontend
npm install
npm run dev
```
Open http://localhost:5173

## Team plan (24 hours)
1. Hours 0–3: start API, test `/api/health` and `/api/match`.
2. Hours 3–8: run UI, polish event inputs and result explanations.
3. Hours 8–13: add CSV upload and schema/field mapping.
4. Hours 13–17: test empty fields, alternate events, ranking sanity.
5. Hours 17–21: deployment, fallback demo recording, data privacy review.
6. Hours 21–24: pitch and final rehearsal.

## Team split
- Backend/scoring: API, algorithm, tests.
- Frontend: React dashboard and API connection.
- Data/testing: fictional dataset, validation, edge cases.
- Demo/pitch: demo script, deployment, evaluator questions.

## Real data later
The current version reads the bundled demo CSV. Part 3 will add user CSV upload and column mapping. Only connect RaahiWorks data with permission and appropriate privacy/security controls.
