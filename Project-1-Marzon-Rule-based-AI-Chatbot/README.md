# Marzon

A rule-based chatbot. No machine learning, no APIs. Just a dictionary and a loop.

Built as Project 1 for the DecodeLabs AI Internship. The idea is simple: before you build something that learns, you should be able to build something that just *works*, every time.

## What's in here

- `chatbot.py` - the actual logic, runs in your terminal.
- `index.html` - a dark-themed frontend for the same logic, runs in your browser.

They're not connected! Same brain, two bodies.

## Running it

**Terminal version**
```
python chatbot.py
```

**Browser version**

Just open `index.html`. That's it, no server needed.

Type `hello`, `help` or `what is your name?` to see it work. Type `exit` or `bye` to leave.

## How it actually works

Every message you send gets checked against a dictionary.

If it finds a match, you get a reply. If not, you get the fallback. No guessing, no hallucinating; just a lookup.

## Next steps

- Add keyword matching instead of exact matches, so "hi there" also triggers the greeting.
- More responses, maybe a personality.
