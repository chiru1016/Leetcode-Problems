class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        mini = 6 * minutes
        hour = 0 if hour is 12 else hour
        hr = (30 * hour) + (0.5 * minutes)
        out = 0
        if mini > hr:
            out = mini - hr
        else:
            out = hr - mini
        return min(out, 360- out)

        