import streamlit as st

pages = {
    "Geral":[
        st.Page("pages/app.py", title="Dashboard", default=True)
    ],
    "Industrialization":[
        st.Page("pages/industrialization.py", title="Dashboard Industrailization")
    ]
}

pg = st.navigation(pages)
pg.run()