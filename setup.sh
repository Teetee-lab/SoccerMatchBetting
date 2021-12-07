mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
[theme]
backgroundColor="#cdef94"
secondaryBackgroundColor="#f4f910"
textColor="#0c0b0b"
