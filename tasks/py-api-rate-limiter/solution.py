def make_rate_limiter(limit):
    counts = {}

    def allow(user_id):
        counts[user_id] = counts.get(user_id, 0) + 1
        return counts[user_id] <= limit

    return allow
