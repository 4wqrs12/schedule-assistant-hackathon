def format_calendar_events(calendar_json):
    formatted = []
    for email, events in calendar_json.items():
        for event in events:
            summary = event.get("Summary", "No Summary")
            start = event.get("StartTime")
            end = event.get("EndTime")
            attendees = event.get("Attendees", [])
            if attendees == ["SELF"]:
                attendees_str = "None"
            else:
                attendees_str = ", ".join(attendees)
            formatted.append(f"{email} - Event: {summary}, StartTime: {start}, EndTime: {end}, Attendees: {attendees_str}")
    return "\n".join(formatted)

# Example usage:
calendar_json = {
    'bob@example.com': [
        {
            'StartTime': '2025-07-16T18:00:00+05:30',
            'EndTime': '2025-07-17T09:00:00+05:30',
            'NumAttendees': 1,
            'Attendees': ['SELF'],
            'Summary': 'Off Hours'
        },
        {
            'StartTime': '2025-07-17T18:00:00+05:30',
            'EndTime': '2025-07-18T09:00:00+05:30',
            'NumAttendees': 1,
            'Attendees': ['SELF'],
            'Summary': 'Off Hours'
        }
    ]
}


