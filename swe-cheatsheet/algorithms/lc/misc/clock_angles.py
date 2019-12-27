
def clock_hands_angle(hour: int, minute: int) -> float:
    minute_hand = 360*minute/60
    hour_hand = hour/12*360 - minute/60 * (360/12)
    diff = abs(hour_hand - minute_hand)
    # diff = abs(30 * hour - 5.5 * minute)  # < reduces to
    return min(diff, 360 - diff)


print(clock_hands_angle(hour=3, minute=15))
print(clock_hands_angle(hour=3, minute=0))
