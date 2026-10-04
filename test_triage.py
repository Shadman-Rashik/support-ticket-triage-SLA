from datetime import datetime
from triage import classify, prioritize
from sla import sla_status

now = datetime(2026, 10, 3, 12, 0)
assert classify("Cannot login", "password locked") == "Login/Access"
assert prioritize("System down", "all users cannot access") == "P1"
assert prioritize("Question about report colors", "") == "P4"
assert sla_status("P1", "2026-10-03 06:00", "", now) == "Breached"
assert sla_status("P1", "2026-10-03 09:00", "", now) == "At Risk"
assert sla_status("P2", "2026-10-03 11:00", "", now) == "On Track"
assert sla_status("P2", "2026-10-02 09:00", "2026-10-02 20:00", now) == "Met"
assert classify("Printer not working", "scanner offline") == "Hardware/Printer"
print("All tests passed")