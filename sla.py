from datetime import datetime
from config import SLA_RESOLVE_HOURS, AT_RISK_RATIO

FMT = "%Y-%m-%d %H:%M"

def parse(ts):
    return datetime.strptime(ts, FMT) if ts else None

def sla_status(priority, created_at, resolved_at, now):
    limit = SLA_RESOLVE_HOURS[priority]
    created, resolved = parse(created_at), parse(resolved_at)
    if resolved:
        hours = (resolved - created).total_seconds() / 3600
        return "Met" if hours <= limit else "Breached"
    hours = (now - created).total_seconds() / 3600
    if hours > limit:
        return "Breached"
    if hours >= limit * AT_RISK_RATIO:
        return "At Risk"
    return "On Track"