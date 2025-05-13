# EmotiWords: Emotion-Driven Personalized Vocabulary Learning Assistant

## Project Overview

EmotiWords is an innovative vocabulary learning platform that combines Large Language Models (LLM) with emotion recognition technology to provide personalized GRE vocabulary learning experiences. Unlike traditional rote memorization methods, EmotiWords generates customized word explanations, mnemonic devices, contextual examples, and practice exercises based on the user's emotional state, native language background, learning preferences, and language style preferences.

## Core Features

- **Emotion Recognition**: Analyzes user input to determine emotional state
- **LLM-Powered Word Generation**: Utilizes GPT API to create personalized learning content
- **AI Personality Adaptation**: Supports multiple teaching styles and personas
- **Multilingual Support**: Customizes explanations based on native language
- **Modern UI/UX**: Built with React/Next.js for optimal user experience
- **User Profile Tracking**: Optional feature to record learning preferences and progress

## Technical Stack

| Layer | Technologies |
|-------|--------------|
| Frontend | Next.js, Tailwind CSS, Shadcn/UI, Framer Motion |
| Backend | FastAPI/Flask |
| LLM Integration | OpenAI GPT-4 API |
| Emotion Analysis | HuggingFace Transformers / GPT Evaluation |
| Data Storage | SQLite / Supabase / Firebase |

## Project Structure

```
emotiwords/
├── frontend/           # Next.js frontend application
├── backend/            # FastAPI backend service
│   ├── word_explainer.py      # Word explanation module
│   ├── emotion_detector.py    # Emotion detection module
│   ├── prompt_router.py       # Prompt management module
│   └── api/                   # API routes
├── prompts/            # Teaching style prompt templates
└── README.md           # Project documentation
```

## Development Roadmap

1. **Word Explanation Module**
   - Implement word explanation generation
   - Support multiple languages and learning styles
   - Generate contextual examples

2. **Emotion Detection Module**
   - Implement emotion analysis using HuggingFace or GPT
   - Support multilingual emotion detection

3. **Prompt Management System**
   - Dynamic prompt generation based on user context
   - Emotion-aware response formatting
   - Language-specific prompt templates

4. **Frontend Development**
   - Next.js application setup
   - User interface components
   - Interactive learning features

5. **Backend Integration**
   - API endpoint implementation
   - Frontend-backend communication
   - Error handling and validation

6. **AI Personality System**
   - Multiple teaching personas
   - Style-consistent response generation
   - User preference adaptation

7. **User Profile System** (Optional)
   - Learning history tracking
   - Preference management
   - Progress monitoring

## Future Enhancements

- Active recall mechanisms
- Voice input/output integration
- Mobile application development
- Educational research applications

## Author

Yanan He (Echo)
Purdue University | Computer Science & Mathematics

---

你觉得我可以帮你生成 `word_explainer.py` 的基本代码吗？或者你现在想试试让 Cursor 根据这份 README 写第一个模块？

```

---

这个 README 你可以直接放进你的 GitHub 项目里，也可以作为提案发给老师或导师。

你下一步是想我给你写 `word_explainer.py` 的代码框架，还是继续让 Cursor 写？我也可以帮你写第二阶段情绪识别的 Cursor prompt。
```
