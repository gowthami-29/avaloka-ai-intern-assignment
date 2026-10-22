import heapq
def can_attend_all(events):
    if not events:
        return True
    sorted_events = sorted(events, key=lambda event: event[0])
    for i in range(1, len(sorted_events)):
        if sorted_events[i - 1][1] > sorted_events[i][0]:
            return False
    return True
def min_rooms_required(events):
    if not events:
        return 0
    sorted_events = sorted(events, key=lambda event: event[0])
    room_end_times = []
    for start, end in sorted_events:
        while room_end_times and room_end_times[0] <= start:
            heapq.heappop(room_end_times)
        heapq.heappush(room_end_times, end)
    return len(room_end_times)
# Example 1
events1 = [(9, 10), (10, 11), (11, 12)]
print(can_attend_all(events1))      # True
print(min_rooms_required(events1))  # 1

# Example 2
events2 = [(9, 12), (10, 11), (11, 13)]
print(can_attend_all(events2))      # False
print(min_rooms_required(events2))  # 2
