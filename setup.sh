mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml

[theme]
backgroundColor="#f7eec3"
secondaryBackgroundColor="#f3a634"
textColor="#100f0f"

