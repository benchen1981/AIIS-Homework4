# Debug Log: University Major Counseling Chatbot

## 1. API Key Authentication Error
**Problem**:
User reported `400 INVALID_ARGUMENT: API key not valid`.

**Resolution**:
Found a typo in `GOOGLE_API_KEY` in the `.env` file.
- Incorrect: `"IzaSyCJb7..."`
- Corrected: `"AIzaSyCJb7..."`

---

## 2. API Overload (503 Service Unavailable)
**Problem**:
User reported `503 UNAVAILABLE: The model is overloaded`. The `gemini-2.5-flash` model was experiencing high traffic.

**Resolution**:
Implemented robust retry logic using the `tenacity` library in `services.py`.
- Added exponential backoff to handle transient server errors automatically.

---

## 3. Model Not Found (404 Not Found)
**Problem**:
Attempted to switch to `gemini-1.5-flash`, but user reported `404 NOT_FOUND` for API version `v1beta`.

**Resolution**:
Used a script to list available models for the user's specific API key key.
- Discovered available models included `gemini-2.0-flash`, `gemini-2.5-flash`, etc.

---

## 4. Quota Exhausted (429 Resource Exhausted)
**Problem**:
Switching to `gemini-2.0-flash` resulted in `429 RESOURCE_EXHAUSTED`.
- Detailed error indicated `FreeTier` limits were hit ("limit: 0").
- Tried switching back to `2.5-flash` (still 503) and `2.0-flash-exp` (also hit 429).

**Resolution**:
Switched to the stable alias model likely to have better availability for standard keys.
- **Final Model**: `gemini-flash-latest`
- This alias points to the most stable Flash version currently supported by Google for general use, bypassing significant outages on specific experimental or preview versions.
