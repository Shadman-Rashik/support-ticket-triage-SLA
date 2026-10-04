CATEGORIES = {
    "Login/Access": ["login", "password", "locked", "access", "otp"],
    "Billing/Invoice": ["invoice", "bill", "payment", "refund", "vat", "receipt"],
    "Performance": ["slow", "timeout", "loading", "hang", "freeze"],
    "Bug/Error": ["error", "crash", "bug", "failed", "exception"],
    "How-to": ["how to", "how do", "guide", "setup", "tutorial"], 
    "Hardware/Printer": ["print", "printer", "scanner"],
}
PRIORITY_KEYWORDS = {
    "P1": ["system down", "server down", "outage", "all users", "data loss", "urgent"],
    "P2": ["cannot login", "cannot access", "error", "failed", "crash", "not working", "locked"],
    "P3": ["slow", "timeout", "delay", "wrong", "incorrect", "missing"],
}
SLA_RESOLVE_HOURS = {"P1": 4, "P2": 24, "P3": 72, "P4": 120}
AT_RISK_RATIO = 0.75