

p_in_site :int = -1
p_out_site :int = 1
def maxvisitorsonline(n,tin,tout):
    events = []
    for i in range(n):
        events.append((tin[i], p_in_site)) # приход
        events.append((tout[i], p_out_site)) # выход

    events.sort()
    online = 0
    maxonline = 0
    for event in events:
        if event[i]== p_in_site :
            online += 1
        elif event[i]== p_out_site:
            online -=1
        else:
            raise ValueError()
        maxonline = max(online, maxonline)
    return maxonline