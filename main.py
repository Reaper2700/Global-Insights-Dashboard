import streamlit as st

pages = {
    "Geral":[
        st.Page("page/app.py", title="Dashboard", default=True)
    ]
}

pg = st.navigation(pages)
pg.run()