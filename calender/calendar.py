import streamlit as st
from streamlit_calendar import calendar
from datetime import datetime
from src.main import get_tasks_data, add_task_data, edit_task

st.set_page_config(page_title="Demo for streamlit-calendar")

st.title('Calendar App')

mode = st.selectbox(
    "Calendar Mode:",
    (
        "daygrid",
        "timegrid",
        "list"
    ),
)

add_task_ = st.text_input('Add Task')
dates = st.text_input('Add Date', placeholder='in YYYY-MM-DD format').split(',')
times = st.text_input('Add Time', placeholder = 'in HH:MM:SS comma separated for start and end').split(',')
priority = st.text_input('Priority')

# events = []
# 
#     events.append({
#             "title": add_task,
#             "color": "#FF6C6C",
#             "start": dates[0] + 'T' + times[0],
#             "end": dates[1] + 'T' + times[1],
#             "resourceId": "a",
#         })
# print(events)
# print(get_tasks_data())
if st.button('Add The Task'):
    add_task_data(
        {
            "title": add_task_,
            "color": "#FFBD45",
            "start": dates[0] + 'T' + times[0],
            "end": dates[1] + 'T' + times[1],
            "priority": priority
        }
    )
events = [
    {
            "title": "Do coding",
            "color": "#FF6C6C",
            "start": "2024-03-15T16:00:00",
            "end": "2024-03-15T18:00:00",
            "resourceId": "a",
    },
    {
        "title": "Event 2",
        "color": "#FFBD45",
        "start": "2024-03-16T16:00:00",
        "end": "2024-03-16T18:00:00",
        "resourceId": "b",
    }
]
#     {
#         "title": "Event 3",
#         "color": "#FF4B4B",
#         "start": "2023-07-20",
#         "end": "2023-07-20",
#         "resourceId": "c",
#     },
#     {
#         "title": "Event 4",
#         "color": "#FF6C6C",
#         "start": "2023-07-23",
#         "end": "2023-07-25",
#         "resourceId": "d",
#     },
#     {
#         "title": "Event 5",
#         "color": "#FFBD45",
#         "start": "2023-07-29",
#         "end": "2023-07-30",
#         "resourceId": "e",
#     },
#     {
#         "title": "Event 6",
#         "color": "#FF4B4B",
#         "start": "2023-07-28",
#         "end": "2023-07-20",
#         "resourceId": "f",
#     },
#     {
#         "title": "Event 7",
#         "color": "#FF4B4B",
#         "start": "2023-07-01T08:30:00",
#         "end": "2023-07-01T10:30:00",
#         "resourceId": "a",
#     },
#     {
#         "title": "Event 8",
#         "color": "#3D9DF3",
#         "start": "2023-07-01T07:30:00",
#         "end": "2023-07-01T10:30:00",
#         "resourceId": "b",
#     },
#     {
#         "title": "Event 9",
#         "color": "#3DD56D",
#         "start": "2023-07-02T10:40:00",
#         "end": "2023-07-02T12:30:00",
#         "resourceId": "c",
#     },
#     {
#         "title": "Event 10",
#         "color": "#FF4B4B",
#         "start": "2023-07-15T08:30:00",
#         "end": "2023-07-15T10:30:00",
#         "resourceId": "d",
#     },
#     {
#         "title": "Event 11",
#         "color": "#3DD56D",
#         "start": "2023-07-15T07:30:00",
#         "end": "2023-07-15T10:30:00",
#         "resourceId": "e",
#     },
#     {
#         "title": "Event 12",
#         "color": "#3D9DF3",
#         "start": "2023-07-21T10:40:00",
#         "end": "2023-07-21T12:30:00",
#         "resourceId": "f",
#     },
#     {
#         "title": "Event 13",
#         "color": "#FF4B4B",
#         "start": "2023-07-17T08:30:00",
#         "end": "2023-07-17T10:30:00",
#         "resourceId": "a",
#     },
#     {
#         "title": "Event 14",
#         "color": "#3D9DF3",
#         "start": "2023-07-17T09:30:00",
#         "end": "2023-07-17T11:30:00",
#         "resourceId": "b",
#     },
#     {
#         "title": "Event 15",
#         "color": "#3DD56D",
#         "start": "2023-07-17T10:30:00",
#         "end": "2023-07-17T12:30:00",
#         "resourceId": "c",
#     },
#     {
#         "title": "Event 16",
#         "color": "#FF6C6C",
#         "start": "2023-07-17T13:30:00",
#         "end": "2023-07-17T14:30:00",
#         "resourceId": "d",
#     },
#     {
#         "title": "Event 17",
#         "color": "#FFBD45",
#         "start": "2023-07-17T15:30:00",
#         "end": "2023-07-17T16:30:00",
#         "resourceId": "e",
#     },
# ]

# calendar_resources = [
#     {"id": "a", "building": "Building A", "title": "Room A"},
#     {"id": "b", "building": "Building A", "title": "Room B"},
#     {"id": "c", "building": "Building B", "title": "Room C"},
#     {"id": "d", "building": "Building B", "title": "Room D"},
#     {"id": "e", "building": "Building C", "title": "Room E"},
#     {"id": "f", "building": "Building C", "title": "Room F"},
# ]

calendar_options = {
    "editable": "true",
    "navLinks": "true",
    "resources": [],
    "selectable": "true",
}

# if "resource" in mode:
#     if mode == "resource-daygrid":
#         calendar_options = {
#             **calendar_options,
#             "initialDate": "2023-07-01",
#             "initialView": "resourceDayGridDay",
#             "resourceGroupField": "building",
#         }
#     elif mode == "resource-timeline":
#         calendar_options = {
#             **calendar_options,
#             "headerToolbar": {
#                 "left": "today prev,next",
#                 "center": "title",
#                 "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
#             },
#             "initialDate": "2023-07-01",
#             "initialView": "resourceTimelineDay",
#             "resourceGroupField": "building",
#         }
#     elif mode == "resource-timegrid":
#         calendar_options = {
#             **calendar_options,
#             "initialDate": "2023-07-01",
#             "initialView": "resourceTimeGridDay",
#             "resourceGroupField": "building",
#         }
# else:
if mode == "daygrid":
    calendar_options = {
        **calendar_options,
        "headerToolbar": {
            "left": "today prev,next",
            "center": "title",
            "right": "dayGridDay,dayGridWeek,dayGridMonth",
        },
        "initialDate": datetime.today().strftime('%Y-%m-%d'),
        "initialView": "dayGridMonth",
    }
elif mode == "timegrid":
    calendar_options = {
        **calendar_options,
        "initialView": "timeGridWeek",
    }
elif mode == "timeline":
    calendar_options = {
        **calendar_options,
        "headerToolbar": {
            "left": "today prev,next",
            "center": "title",
            "right": "timelineDay,timelineWeek,timelineMonth",
        },
        "initialDate": datetime.today().strftime('%Y-%m-%d'),
        "initialView": "timelineMonth",
    }
elif mode == "list":
    calendar_options = {
        **calendar_options,
        "initialDate": datetime.today().strftime('%Y-%m-%d'),
        "initialView": "listMonth",
    }
    # elif mode == "multimonth":
    #     calendar_options = {
    #         **calendar_options,
    #         "initialView": "multiMonthYear",
    #     }

state = calendar(
    events=st.session_state.get("events", events),
    options=calendar_options,
    custom_css="""
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
    """,
    key=mode,
)

if state.get("eventsSet") is not None:
    st.session_state["events"] = state["eventsSet"]

# st.write(state)

# st.markdown("## API reference")
# st.help(calendar)