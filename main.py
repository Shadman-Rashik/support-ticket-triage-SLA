import csv
from collections import Counter
from datetime import datetime
from triage import classify, prioritize
from sla import sla_status
from reports import build_html

def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main():
    now = datetime.now()
    rows = load("tickets.csv")
    for r in rows:
        r["category"] = classify(r["subject"], r["description"])
        r["priority"] = prioritize(r["subject"], r["description"])
        r["sla"] = sla_status(r["priority"], r["created_at"], r["resolved_at"], now)
    order = {"Breached": 0, "At Risk": 1, "On Track": 2, "Met": 3}
    rows.sort(key=lambda r: (order[r["sla"]], r["priority"]))
    with open("triaged_tickets.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    with open("report.html", "w", encoding="utf-8") as f:
        f.write(build_html(rows, now))
    print("Tickets:", len(rows), dict(Counter(r["sla"] for r in rows)))
    print("Done: triaged_tickets.csv and report.html created")

main()