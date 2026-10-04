import csv, random
from datetime import datetime, timedelta

random.seed(7)
now = datetime.now()
FMT = "%Y-%m-%d %H:%M"
templates = [
    ("Cannot login after password reset", "User is locked out after resetting password"),
    ("System down for all users", "Entire application not loading, urgent"),
    ("Invoice total is wrong", "VAT amount incorrect on invoice"),
    ("Payment not showing", "Customer payment missing from ledger"),
    ("Page is very slow", "Dashboard timeout when opening reports"),
    ("Error when saving record", "Error message appears, save failed"),
    ("How to add a new user", "Need a guide for account setup"),
    ("Receipt print is blank", "Print shows empty page"),
    ("App crash on startup", "Application crash after update"),
    ("Data loss after import", "Records missing after CSV import"),
    ("Question about report colors", "Can the colors be changed?"),
    ("Refund request for duplicate bill", "Customer charged twice on one bill"),
]
rows = []
for i in range(1, 41):
    subject, desc = random.choice(templates)
    elapsed = random.randint(2, 150)
    created = now - timedelta(hours=elapsed)
    if random.random() < 0.6:
        status = "resolved"
        resolved_at = (created + timedelta(hours=random.uniform(0.5, elapsed))).strftime(FMT)
    else:
        status, resolved_at = "open", ""
    rows.append({"id": f"T{i:03d}", "created_at": created.strftime(FMT),
                 "customer": f"Customer {random.randint(1, 12)}", "subject": subject,
                 "description": desc, "channel": random.choice(["email", "chat", "phone"]),
                 "status": status, "resolved_at": resolved_at})
with open("tickets.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
print("Created tickets.csv with", len(rows), "dummy tickets")