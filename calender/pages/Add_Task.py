import streamlit as st
import datetime
from src.main import add_task_data

start_date = datetime.datetime.now()
end_date = datetime.datetime.now()

selected_dates = st.date_input(
    "Select a date range",
    value=(start_date, end_date),
    min_value=datetime.date(2023, 1, 1),
    max_value=datetime.date(2024, 12, 31)
)


time_range = st.slider(
    "Select time range",
    value=(datetime.time(8, 0), datetime.time(18, 0)),
    min_value=datetime.time(0, 0),
    max_value=datetime.time(23, 59),
    format="HH:mm"
)

add_task_ = st.text_input('Add Task')
priority = st.selectbox(
        "Select Priority..",
        ('1', '2', '3'),
        index=None
        )

if st.button('Add The Task'):
    add_task_data(
        {
            "title": add_task_,
            "color": "#FFBD45",
            "start": selected_dates[0].strftime('%Y-%m-%d') + 'T' + time_range[0].strftime("%H:%M:%S"),
            "end": selected_dates[1].strftime('%Y-%m-%d') + 'T' + time_range[1].strftime("%H:%M:%S"),
            "priority": priority,
            "is_completed":False
        }
    )
    st.rerun()