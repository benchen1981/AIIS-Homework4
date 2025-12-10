# Design: Futuristic Glassmorphism System

## Visual Identity (Concept Language)

The design will evoke a "Future Data Interface" feel.

- **Palette**: Deep Void Black, Holographic Blue, Neon Cyan, Soft White transparency.
- **Typography**: Monospace for data/code, clean Sans-Serif (Inter/Roboto) for chat.
- **Texture**: Frosted glass (blur), subtle noise, glowing borders.

## CSS Architecture

We will inject custom CSS into Streamlit via `st.markdown`.

### Color Tokens

```css
:root {
  --bg-color: #050510;
  --glass-bg: rgba(20, 30, 50, 0.4);
  --glass-border: rgba(100, 200, 255, 0.2);
  --accent-glow: 0 0 15px rgba(0, 255, 255, 0.3);
  --text-primary: #e0e0e0;
  --text-secondary: #a0a0b0;
}
```

### Components

1. **Chat Container**:
   - `backdrop-filter: blur(12px)`
   - Gradient borders with reduced opacity.
2. **Input Field**:
   - Floating style, "glitch" effect on focus.
3. **Cursor**:
   - Custom blinking block cursor with a gradient trail.

## Interaction Flow Design

1. **User Input**: "Typewriter" entry visual (optional, or standard input).
2. **Loading State ("Micro-skeleton")**:
   - Instead of a generic spinner, show a pulsing geometry or "decrypting" text animation as a placeholder.
3. **Response Handling**:
   - **Phase 1**: Receive first chunk.
   - **Phase 2**: "Flash" appearance (fade-in quickly).
   - **Phase 3**: Stream the rest character-by-character (Typewriter effect).

## Architecture

- `app.py`: Main entry point, UI layout.
- `services.py`: Handles Google GenAI `client.chats.create` and streaming response generation.
- `styles.py`: Contains the large CSS string to be injected.
