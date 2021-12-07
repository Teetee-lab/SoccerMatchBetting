mkdir -p ~/.streamlit/

echo "[theme]
backgroundColor= '#f7eec3'
secondaryBackgroundColor='#f3a634'
textColor='#100f0f'
font = 'sans serif'
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml

