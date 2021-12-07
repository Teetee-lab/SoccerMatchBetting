mkdir -p ~/.streamlit/

echo "[theme]
backgroundColor= '#f7eec3'
secondaryBackgroundColor='#f3a634'
textColor='#100f0f'
font = 'sans serif'
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml

