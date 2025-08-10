
**Objective:** Resolve the issue where the MAMP MySQL server (MySQL 5.7) was not functioning correctly. This log captures the terminal-based troubleshooting steps performed, explains each command used, and documents the root cause and solution.

---

### **1. Initial Diagnosis**

#### **Command:**

```bash
ps ax | grep mysql
```

**Explanation:** This command lists all running processes containing the term "mysql" to check if MySQL was already running via MAMP.

### **2. Force Kill Running MySQL Processes**

#### **Command(s):**

```bash
kill 6370
kill 6485
```

**Explanation:** The above commands were used to terminate MySQL-related processes (using their PIDs) which may have been preventing clean restarts.

---

### **3. Log Inspection for Errors**

#### **Commands:**

```bash
cd /Applications/MAMP/logs
cat mysql_error.log
```

**Explanation:** Navigated to MAMP logs folder and viewed the MySQL error log file to understand what errors were being thrown.

**Findings:**

- Deprecated timestamp usage
    
- Table stats mismatch errors (suggested running `mysql_upgrade`)
    
- Several access denied messages for 'root'
    

---

### **4. Server Shutdown and Reinitialization**

Repeatedly killing processes and observing behavior:

```bash
kill <mysqld or mysqld_safe PID>
ps ax | grep mysql
```

This ensures the MAMP MySQL daemon is completely shut before restarting.

---

### **5. Attempted Password Reset**

#### **Command:**

```bash
mysqladmin -u root -pYES password
```

**Error Message:**

```
Can't connect to local server through socket '/tmp/mysql.sock'
```

**Explanation:** Tried resetting MySQL root password. Error occurred because MAMP’s MySQL socket is located at `/Applications/MAMP/tmp/mysql/mysql.sock` not `/tmp/mysql.sock`. This mismatch was part of the issue.

---

### **6. Port Conflict and Network Checks**

#### **Command:**

```bash
sudo lsof -i -n -P | grep TCP
```

**Explanation:** Checks all open TCP connections to identify if any other services (like MariaDB or other MySQL services) were running and interfering with MAMP’s MySQL port.

#### **Also:**

```bash
lsof -i tcp:8888
```

**Explanation:** To see if port 8888 (used by MAMP for Apache) was occupied.

---

### **7. Cleaning Apache Processes**

#### **Command:**

```bash
kill <httpd PID>
```

**Explanation:** Manually killed old Apache processes to clear port 8888 and ensure no interference.

---

### **8. Directory & File System Navigation**

Explored:

```bash
cd /Applications/MAMP/db/mysql57
ls -lrt
```

To validate presence of critical MySQL system files and ensure integrity.

**Observation:** All default DBs and certificate files appeared intact, suggesting no corruption.

---

### **Conclusion**

- The root issue stemmed from either a conflicting process or socket misconfiguration.
    
- Reinstalling MAMP ensured a clean environment.
    
- Manually killing MySQL and Apache processes cleared lingering locks.
    
- Socket path mismatch was identified as a major point of failure.
    

**Post Fix Recommendation:**

- Always ensure the correct socket path is used (`/Applications/MAMP/tmp/mysql/mysql.sock`) when issuing MySQL commands.
    
- Use `mysql_upgrade` to fix stats mismatch warnings.
    
- Confirm port availability using `lsof` before launching services.
    

---

**Document Prepared by:** Tejaswini Damodara Kannan **Assisted by:** Abner **Date:** April 22, 2025