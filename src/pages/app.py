import polars as pl
import matplotlib.pyplot as plt
import streamlit as st


from pathlib import Path


def extract():

    archive = "Data/world_development_indicators.csv"
    df = pl.read_csv(archive)

    st.title("World development indicators")

    st.write("Data shape", df.shape)

    st.write("### Describe")
    st.dataframe(df.describe())

    st.write("### List of Coutries")
    st.dataframe(df.select(pl.col("REF_AREA_LABEL").unique()))

    st.write("### List of Unique Indicators")
    st.dataframe(df.select(pl.col("INDICATOR_LABEL").unique()))

    top_5_register = (
        df
        .group_by(pl.col("REF_AREA_LABEL"))
        .count()
        .sort("count", descending= True)
        .head(5)
    )
    st.write("Top 5 países com mais registros")
    st.dataframe(top_5_register)

    top_5_indicators = df.group_by(
        pl.col("INDICATOR"), 
        pl.col("INDICATOR_LABEL")
    ).count().sort("count", descending=True).head(5)
    st.write("Top 5 indicadores mais frequentes")
    st.dataframe(top_5_indicators)

    years = [str(year) for year in range(2000, 2024)]

    Agricultural_land = (
        df
        .filter(
            (pl.col("REF_AREA_LABEL").is_in(['Brazil', 'China', 'Japan'])) &
            (pl.col("INDICATOR_LABEL") == "Agricultural land (% of land area)")
        )
        .select(
            "REF_AREA_LABEL",
            *years
        )
    )
    st.write("### Dados de Agricultural Land")
    st.dataframe(Agricultural_land)

    
    agri_pd = Agricultural_land.to_pandas()

    fig, ax = plt.subplots()

    for country in agri_pd["REF_AREA_LABEL"].unique():
        row = agri_pd[agri_pd["REF_AREA_LABEL"] == country].iloc[0]
        values = row[years].values  # valores de 2000–2023

        ax.plot(years, values, marker="o", label=country)

    ax.set_xticks(years[::2])  # mostra um ano a cada 2 para não poluir
    ax.legend()
    ax.set_title("Evolução de Agricultural Land (% área agricultável)")
    ax.set_ylabel("% do território")

    st.subheader("Evolução de Agricultural Land")
    st.pyplot(fig)


    agricultural_land_v2 = (
        Agricultural_land
        .with_columns([
            pl.max_horizontal(years).alias("max_year_value"),
            pl.mean_horizontal(years).alias("mean_year_value"),
            pl.min_horizontal(years).alias("minimum_year_value")
        ])
        .select(
            "REF_AREA_LABEL",
            "max_year_value",
            "mean_year_value",
            "minimum_year_value",
        )
    )
    st.write("### Estatísticas: Max / Mean / Min")
    st.dataframe(agricultural_land_v2)

extract()