import streamlit as st
from src.main import get_tasks_data, edit_task

tasks = (task['title'] for task in get_tasks_data())
option = st.selectbox(
   "Which Task You want to edit?",
   tasks,
   index=None,
   placeholder="Select Task...",
)

task_edit = st.selectbox(
   "How do you want to edit the task?",
   ('Change Priority','Change Task Status'),
   index=None,
   placeholder="Select Task...",
)

if task_edit == 'Change Priority':
    priority = st.selectbox(
    "Select Priority..",
    ('1', '2', '3'),
    index=None
    )
    is_completed = False
else:
    priority = None
    is_completed = True

if st.button('Edit Task'):
    edit_task(task_name = option, priority = priority, is_completed = is_completed)
    st.rerun()