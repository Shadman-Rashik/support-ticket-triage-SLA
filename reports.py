import html
from collections import Counter

COLORS = {"Breached": "#f8d7da", "At Risk": "#fff3cd", "On Track": "#d1e7dd", "Met": "#e2e3e5"}

def build_html(rows, now):
    counts = Counter(r["sla"] for r in rows)
    summary = " | ".join(f"{k}: {counts.get(k, 0)}" for k in COLORS)
    lines = []
    for r in rows:
        cells = [r["id"], r["subject"], r["category"], r["priority"],
                 r["status"], r["created_at"], r["sla"]]
        tds = "".join(f"<td>{html.escape(str(c))}</td>" for c in cells)
        lines.append(f'<tr style="background:{COLORS[r["sla"]]}">{tds}</tr>')
    head = "".join(f"<th>{h}</th>" for h in
                   ["ID", "Subject", "Category", "Priority", "Status", "Created", "SLA"])
    return f"""<html><head><meta charset="utf-8"><title>SLA Report</title>
<style>body{{font-family:Arial;margin:24px}}table{{border-collapse:collapse;width:100%}}
td,th{{border:1px solid #ccc;padding:6px;text-align:left}}</style></head>
<body><h1>Support Ticket SLA Report</h1><p>Generated: {now:%Y-%m-%d %H:%M}</p>
<p><b>{summary}</b></p><table><tr>{head}</tr>{''.join(lines)}</table></body></html>"""