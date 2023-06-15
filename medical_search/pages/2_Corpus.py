import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid
import utils

st.set_page_config(
    page_title="Q&A over Biomedical Literature",
    page_icon='app/images/logo.png',
)

st.markdown('### Select a paper to browse')
st.markdown('''
    - These are all the papers uploaded to Enterprise Search for this demo. 
    - Given a query Enterprise Search will identify which papers in its corpus 
    contain relevant information.''')
df = pd.read_json("data/articles.json")
gb = GridOptionsBuilder.from_dataframe(df[['title']])
gb.configure_selection()
gb.configure_column('title', header_name="Paper Title")
gb.configure_pagination()
gridOptions = gb.build()


data = AgGrid(
    df,
    gridOptions=gridOptions,
    fit_columns_on_grid_load=True)

selected_rows = data["selected_rows"]

if len(selected_rows) != 0:
    st.markdown(f"*NCBI REF:* {selected_rows[0]['ncbi_ref']}")
    st.markdown(utils.show_pdf(selected_rows[0]['download']), unsafe_allow_html=True)