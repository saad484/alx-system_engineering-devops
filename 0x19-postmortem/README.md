## Postmortem


### Incident Summary:

On Apr 15th, 2024, between 2:30 PM and 5:00 PM (WAT), our e-commerce website experienced a complete outage, rendering it unresponsive to users.

### Impact:

The outage affected all services provided by the website, including product listings, shopping cart functionality, and checkout processes. Approximately 80% of users were unable to access the site during this period.

### Root Cause:

The outage was caused by a memory leak in the web application server, leading to server overload and unresponsiveness.

### Timeline:

2:30 PM: Monitoring system alerted operations team of the issue.
2:35 PM: Operations team attempted to restart the server without success.
2:40 PM: Investigation began, focusing initially on server configuration.
3:00 PM: High memory usage indicated a potential memory leak.
3:15 PM: Code inspection commenced to identify the source of the leak.
3:45 PM: Memory leak in the application code was pinpointed.
4:30 PM: Code fix deployed, and server restarted.
4:45 PM: Website restored to full functionality.
Misleading Investigation/Debugging Paths:

Initial focus on server configuration delayed the identification of the true cause—memory leak in the application code.

### Incident Escalation:

Operations team escalated the incident to development once the code-related issue was confirmed.

### Resolution:

Memory leak in the application code was resolved through code optimization and better memory management practices. The web application server was restarted following the fix.

### Corrective and Preventative Measures:

To prevent future incidents:

Regular code reviews will be conducted to catch memory leaks.
Testing procedures will be enhanced to detect memory issues pre-production.
Monitoring tools will be improved to track server performance accurately.
Operations team will receive additional training on troubleshooting web application issues.
### Specific Tasks:

Conduct comprehensive code review of the web application.
Implement automated tests to detect memory leaks.
Update monitoring tools for better resource usage tracking.
Provide operations team with advanced troubleshooting training.
This postmortem outlines the outage incident, its causes, resolution, and measures to prevent similar occurrences in the future.