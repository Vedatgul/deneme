import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt









def show_explore_page():
    st.title("Explore Data Scientist Salaries")

    st.write(
        """
    ### Stack Overflow Developer Survey 2020
    """
    )
    # st.set_page_config(page_title="EDA",
    #                    page_icon="bar_chart:",
    #                    layout="wide"
    # )

    # df = pd.read_excel(
    #     io='ds_salaries.xlsx',
    #     engine='openpyxl',
    #     sheet_name="ds_salaries (1)",
    #     skiprows=3,
    #     usecols='B:R',
    #     nrows=1000,
    # )
    df = pd.read_csv("ds_salaries.csv")
    st.dataframe(df)

    st.sidebar.header("Please Filter Here:")
    Company_loc=st.sidebar.multiselect(
        "Select the company location:",
        options=df["company_location"].unique(),
        default=df["company_location"].unique()
    )



    Job_title=st.sidebar.multiselect(
        "Select job title:",
        options=["Data Engineer", "Data Scientist", "Data Analyst", "Machine Learning Engineer",
        "Analytics Engineer", "Data Architect"],
        default=["Data Engineer", "Data Scientist", "Data Analyst", "Machine Learning Engineer",
        "Analytics Engineer", "Data Architect"]
    )

    Remote_ratio=st.sidebar.multiselect(
        "Select remote type:",
        options=df["remote_ratio"].unique(),
        default=df["remote_ratio"].unique()
    )

    df_selection = df.query(
        "company_location == @Company_loc & job_title == @Job_title & remote_ratio == @Remote_ratio"
    )

#    st.dataframe(df_selection)

    st.markdown("---")

    avarage_salary = (
        df_selection.groupby('company_size')['salary_in_usd'].mean().round(0).sort_values(ascending = False)
    )

    fig_avarage_salary = px.bar(
        avarage_salary,
        x = avarage_salary.index,
        y = 'salary_in_usd',

        orientation="v",
        title = '<b>Şirket Büyüklüğüne Göre Ortalama Maaş</b>',
        color_discrete_sequence = ['green']*3 * len(avarage_salary),
        template = "plotly_white",

    )

    fig_avarage_salary.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False))
    )

    employment_type_salary = (
        df_selection.groupby('employment_type')['salary_in_usd'].mean().round(0).nlargest(15).sort_values(ascending = False)
    )

    fig_employment_type_salary = px.bar(
        employment_type_salary,
        x=employment_type_salary.index,
        y='salary_in_usd',
        orientation="v",
        title='<b>Ortalama Maaş ile İstihdam Türü</b>',
        color_discrete_sequence=["#0083B8"] * len( employment_type_salary),
        template="plotly_white",
    )

    fig_employment_type_salary.update_layout(
        xaxis=dict(tickmode="linear"),
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False)),
    )

    left_column, right_column = st.columns(2)
    left_column.plotly_chart(fig_avarage_salary, use_container_width=True)
    right_column.plotly_chart(fig_employment_type_salary, use_container_width=True)


    job_title_salary = (
        df_selection.groupby('job_title')['salary_in_usd'].mean().round(0).sort_values(ascending = False).head(15)
    )

    fig_job_title_salary = px.bar(
        job_title_salary,
        x='salary_in_usd',
        y=job_title_salary.index,
        orientation="h",
        title='<b>İş Unvanlarına Göre En İyi 6 Ortalama Maaş</b>',
        color_discrete_sequence= ['red']*3 * len(job_title_salary),
        template="plotly_white",
    )

    fig_job_title_salary.update_layout(
#        xaxis=dict(tickmode="linear"),
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False)),
    )

    st.plotly_chart(fig_job_title_salary)

    employment_type_salary_years = (
        df.groupby(['employment_type','work_year'], as_index=False)['salary_in_usd'].mean().round(0)
    )

    fig_employment_type_salary_years = px.bar(
        employment_type_salary_years,
        x="employment_type",
        y='salary_in_usd',
        color='work_year',

        barmode='group',
        orientation="v",
        title='<b> İstihdam Türüne Göre Dolar Yıllık Bazında Ortalama Maaşlar</b>',
        color_discrete_sequence= ["#0083B8"] * len(employment_type_salary_years),
        template="plotly_white",
    )

    fig_employment_type_salary_years.update_layout(
        xaxis=dict(tickmode="linear"),
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False)),

    )

    st.plotly_chart(fig_employment_type_salary_years)