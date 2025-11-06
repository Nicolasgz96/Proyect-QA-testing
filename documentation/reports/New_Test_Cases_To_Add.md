# New Test Cases to Add - Hello Britannica
## Immediate Priorities for Sprint 1

**Date:** November 6, 2025
**Priority:** CRITICAL (P0)

---

## SECTION 1: ADMIN - TEACHER URL GENERATION (15 Test Cases)

### Module: Admin - Teacher Management

| Test ID | Title | Priority | Pre-condition | Test Steps | Expected Result |
|---------|-------|----------|---------------|------------|-----------------|
| **AO013** | Verify successful generation of teacher invitation URL | P0 | Admin is logged in with active subscription | 1. Navigate to Teacher Management section<br>2. Click "Invite Teacher" button<br>3. Enter teacher email: teacher1@test.com<br>4. Click "Generate Invitation" | - Unique URL generated with format: https://staging.hellobritannica.eb.com/registration/teacher?code=XXXXX<br>- URL displayed on screen with copy button<br>- Success message shown: "Invitation URL generated successfully" |
| **AO014** | Verify unique URL generation for multiple teachers | P0 | Admin is logged in | 1. Generate invitation URL for teacher1@test.com<br>2. Copy generated URL code<br>3. Generate invitation URL for teacher2@test.com<br>4. Copy second URL code<br>5. Compare both codes | - Each URL has unique code<br>- Codes are alphanumeric, at least 12 characters<br>- Both URLs are valid and functional |
| **AO015** | Verify URL expiration after defined period | P0 | Admin generated teacher URL 48 hours ago | 1. Open generated URL in incognito browser<br>2. Attempt to register using expired URL | - Error message displayed: "This invitation link has expired"<br>- Option to request new invitation shown<br>- User cannot proceed with registration |
| **AO016** | Verify URL format and structure validation | P0 | Admin is logged in | 1. Generate teacher invitation URL<br>2. Inspect URL structure<br>3. Verify URL parameters | - URL contains valid code parameter<br>- URL is properly formatted<br>- No special characters that could break the link<br>- URL is accessible via HTTPS |
| **AO017** | Verify URL works in clean browser session | P0 | Admin generated teacher URL | 1. Copy generated URL<br>2. Open incognito/private browser window<br>3. Clear cookies and cache<br>4. Paste and open URL | - Registration page loads successfully<br>- School/organization pre-populated (if applicable)<br>- Teacher can proceed with registration |
| **AO018** | Verify invalid URL handling | P0 | User has manipulated URL code | 1. Take valid teacher URL<br>2. Modify code parameter to random string<br>3. Open modified URL | - Error page displayed: "Invalid invitation code"<br>- Option to contact administrator<br>- Link to login page |
| **AO019** | Verify URL can be copied and shared | P0 | Admin generated teacher URL | 1. Generate URL<br>2. Click "Copy to Clipboard" button<br>3. Paste URL in text editor<br>4. Copy URL manually (select text)<br>5. Test both copied URLs | - Copy button shows "Copied!" confirmation<br>- Both URLs are identical and functional<br>- URL can be shared via email, messaging |
| **AO020** | Verify URL generation with different account types | P0 | Multiple admin accounts exist (trial, paid, enterprise) | 1. Login as trial admin → Generate URL<br>2. Login as paid admin → Generate URL<br>3. Login as enterprise admin → Generate URL | - All account types can generate URLs<br>- URLs work correctly for each account type<br>- School association maintained |
| **AO021** | Verify email invitation containing the URL | P0 | Admin enters teacher email for invitation | 1. Navigate to Teacher Management<br>2. Enter teacher email: newteacher@test.com<br>3. Click "Send Invitation Email"<br>4. Check email inbox | - Email received with subject: "You're invited to Hello Britannica"<br>- Email contains invitation URL<br>- Email is professionally formatted<br>- URL in email is clickable |
| **AO022** | Verify regeneration of expired URLs | P0 | Admin has list of expired URLs | 1. Navigate to Teacher Management<br>2. View list of sent invitations<br>3. Identify expired invitation<br>4. Click "Resend Invitation" | - New URL generated<br>- Old URL permanently invalidated<br>- New email sent to teacher<br>- Expiration date reset to 48 hours from now |
| **AO023** | Verify URL generation limits (if applicable) | P1 | Admin account with URL generation limits | 1. Check current URL generation count<br>2. Generate URLs up to limit<br>3. Attempt to generate one more URL | - Warning message when approaching limit<br>- Error message when limit reached: "You have reached your invitation limit"<br>- Option to upgrade account or contact support |
| **AO024** | Verify URL tracking and status | P0 | Admin generated several teacher URLs | 1. Navigate to Teacher Management dashboard<br>2. View invitation status list | - List shows: Email, Generated Date, Status (Pending/Accepted/Expired)<br>- Can filter by status<br>- Can resend or revoke invitations |
| **AO025** | Verify URL revocation functionality | P0 | Admin generated teacher URL that hasn't been used | 1. Navigate to invitation list<br>2. Select pending invitation<br>3. Click "Revoke Invitation" | - Confirmation dialog: "Are you sure you want to revoke this invitation?"<br>- After confirmation, URL invalidated immediately<br>- Status changed to "Revoked"<br>- Revoked URL shows error when accessed |
| **AO026** | Verify bulk URL generation | P1 | Admin needs to invite multiple teachers | 1. Click "Bulk Invite Teachers"<br>2. Upload CSV with teacher emails (Format: email@domain.com)<br>3. Click "Generate Invitations" | - URLs generated for all valid emails<br>- Invalid emails flagged with error message<br>- Summary report: X invitations sent, Y failed<br>- Download report option available |
| **AO027** | Verify URL generation with custom message | P1 | Admin wants to personalize invitation | 1. Click "Invite Teacher"<br>2. Enter teacher email<br>3. Enter custom message in "Personal Note" field<br>4. Generate invitation | - Email includes custom message<br>- Message appears before/after invitation link<br>- Character limit enforced (500 chars)<br>- Preview option available before sending |

---

## SECTION 2: ADMIN - SCHOOL REGISTRATION (12 Test Cases)

### Module: Admin - School Management

| Test ID | Title | Priority | Pre-condition | Test Steps | Expected Result |
|---------|-------|----------|---------------|------------|-----------------|
| **AO028** | Verify school registration form field validation | P0 | Admin completed personal registration | 1. Navigate to School Registration page<br>2. Leave all fields empty<br>3. Click "Continue" | - Error messages for required fields:<br>  * "School name is required"<br>  * "School address is required"<br>  * "School type is required"<br>- Continue button remains disabled |
| **AO029** | Verify school name character limits | P0 | On school registration page | 1. Enter school name exceeding 100 characters<br>2. Observe behavior | - Field allows maximum 100 characters<br>- Character counter shown: "X/100"<br>- Cannot type beyond limit |
| **AO030** | Verify school name special characters handling | P0 | On school registration page | 1. Enter school name with special chars: "St. Mary's School & College (2023)"<br>2. Submit form | - Special characters allowed: period, apostrophe, ampersand, parentheses, hyphen<br>- No errors for valid special characters<br>- Invalid characters (e.g., @, #, $) rejected with error |
| **AO031** | Verify duplicate school name handling | P0 | School "Test High School" already exists | 1. Enter school name: "Test High School"<br>2. Fill other fields<br>3. Submit form | - Warning message: "A school with this name already exists. Is this the same school?"<br>- Options: "Yes, use existing" / "No, this is different"<br>- If different, prompt to add distinguishing info (location, district) |
| **AO032** | Verify school type selection | P0 | On school registration page | 1. Click "School Type" dropdown<br>2. View options<br>3. Select "Public School" | - Dropdown options: Public School, Private School, Charter School, International School, Other<br>- Single selection only<br>- Selected type saved |
| **AO033** | Verify school address fields validation | P0 | On school registration page | 1. Enter street address<br>2. Enter city<br>3. Enter state/region<br>4. Enter postal code<br>5. Select country | - Address line 1: Required, max 100 chars<br>- City: Required, max 50 chars<br>- State: Required, max 50 chars<br>- Postal code: Required, format validation by country<br>- Country: Required, dropdown list |
| **AO034** | Verify timezone and location settings | P0 | School address entered | 1. Complete school address<br>2. Observe timezone field | - Timezone auto-populated based on address<br>- Can manually change timezone if incorrect<br>- Dropdown shows all timezones<br>- Format: (GMT-3:00) Brasilia for Brazil |
| **AO035** | Verify school year and term configuration | P1 | School basic info completed | 1. Navigate to "Academic Calendar" section<br>2. Set school year start date<br>3. Define term/semester structure | - School year: Select start month and end month<br>- Term options: 2 semesters, 3 trimesters, 4 quarters<br>- Define term dates<br>- Configuration saved |
| **AO036** | Verify school admin assignment | P0 | School registration in progress | 1. Complete school information<br>2. Reach "Administrator" section | - Current user auto-assigned as school admin<br>- Can add additional admins (email)<br>- Role definition: Primary Admin, Secondary Admin<br>- Email invitations sent to additional admins |
| **AO037** | Verify school profile completion | P0 | All required fields filled | 1. Complete all required school information<br>2. Review summary page<br>3. Click "Complete Registration" | - Summary page shows all entered information<br>- Edit option available for each section<br>- Success message: "School registration complete!"<br>- Redirected to admin dashboard<br>- School profile accessible for editing |
| **AO038** | Verify school profile editing after creation | P0 | School registered and admin logged in | 1. Navigate to School Settings<br>2. Click "Edit School Profile"<br>3. Modify school name and address<br>4. Save changes | - All fields editable except: Creation date, School ID<br>- Changes require confirmation<br>- Audit log entry created<br>- Success message: "School profile updated" |
| **AO039** | Verify mandatory vs optional fields | P0 | On school registration page | 1. Fill only mandatory fields<br>2. Leave optional fields empty<br>3. Submit form | - Mandatory: School name, address, city, country, school type<br>- Optional: Phone, website, school logo, description<br>- Can complete registration without optional fields<br>- Can add optional info later |

---

## SECTION 3: TEACHER - REPORTING & MONITORING (20 Test Cases)

### Module: Teacher - Monitoring & Engagement

| Test ID | Title | Priority | Pre-condition | Test Steps | Expected Result |
|---------|-------|----------|---------------|------------|-----------------|
| **TE051** | Verify PDF generation for individual student report | P0 | Teacher logged in, class has students with activity data | 1. Navigate to Class Dashboard<br>2. Click on student name<br>3. Click "Download PDF Report" | - PDF generates within 10 seconds<br>- PDF filename: StudentName_Report_YYYY-MM-DD.pdf<br>- PDF contains: Student name, level, progress, completed activities, scores<br>- PDF is readable and well-formatted |
| **TE052** | Verify PDF generation for class report | P0 | Teacher has class with multiple students | 1. Go to Class Overview<br>2. Click "Class Report"<br>3. Click "Download as PDF" | - PDF generates within 15 seconds<br>- PDF filename: ClassName_ClassReport_YYYY-MM-DD.pdf<br>- PDF contains: Class summary, student list, overall progress, engagement metrics<br>- Charts and graphs rendered correctly |
| **TE053** | Verify PDF formatting and layout | P0 | Student PDF report generated | 1. Generate student PDF report<br>2. Open PDF in viewer<br>3. Check formatting | - Logo and branding present<br>- Clear section headers<br>- Tables aligned properly<br>- Charts/graphs visible and clear<br>- Page breaks appropriate<br>- Footer with generation date and page numbers |
| **TE054** | Verify PDF download functionality | P0 | On report page with PDF ready | 1. Click "Download PDF"<br>2. Check browser downloads | - PDF downloads immediately<br>- No errors or blank PDFs<br>- File size reasonable (< 5MB for typical report)<br>- File opens correctly in PDF reader |
| **TE055** | Verify PDF content accuracy vs online data | P0 | Student has completed activities | 1. Note student's online progress: 3 activities, 85% avg score<br>2. Generate PDF report<br>3. Compare data | - PDF data matches online dashboard exactly<br>- Activity counts accurate<br>- Scores accurate<br>- Dates accurate<br>- No missing data |
| **TE056** | Verify PDF generation with large datasets | P1 | Student completed 50+ activities | 1. Select student with extensive history<br>2. Generate PDF report | - PDF generates successfully (may take 20-30 seconds)<br>- All activities included<br>- PDF size < 10MB<br>- Pagination handles large data<br>- No performance issues |
| **TE057** | Verify PDF accessibility (screen reader compatible) | P1 | PDF report generated | 1. Open PDF in Adobe Reader<br>2. Enable "Read Aloud" feature<br>3. Test screen reader | - PDF is tagged for accessibility<br>- Screen reader reads content in logical order<br>- Images have alt text<br>- Tables are structured properly |
| **TE058** | Verify CSV export of student progress | P0 | Teacher on student dashboard | 1. Navigate to Student Overview<br>2. Click "Export Data"<br>3. Select "CSV Format"<br>4. Download file | - CSV file downloads: StudentName_Data_YYYY-MM-DD.csv<br>- Headers: Date, Activity, Type, Score, Time Spent, Status<br>- All student activities included<br>- Data is comma-separated<br>- Opens correctly in Excel |
| **TE059** | Verify Excel export of class data | P0 | Teacher viewing class list | 1. Go to Class Overview<br>2. Click "Export Class Data"<br>3. Select "Excel Format" | - Excel file downloads: ClassName_Export_YYYY-MM-DD.xlsx<br>- Multiple sheets: Students, Progress, Summary<br>- Formatted with headers, borders<br>- Charts included (if applicable)<br>- Opens in Excel without errors |
| **TE060** | Verify export data completeness | P0 | Export student data | 1. Count activities on online dashboard: 15 activities<br>2. Export data as CSV<br>3. Open CSV and count rows | - CSV has 15 data rows (+ 1 header row = 16 total)<br>- All dates present<br>- All scores present<br>- No missing data<br>- Data matches online dashboard |
| **TE061** | Verify export with filtered data | P0 | Teacher applied date filter | 1. Filter class view: Last 30 days<br>2. Export filtered data<br>3. Check export content | - Export contains only filtered data<br>- Date range noted in filename or header<br>- Filter criteria included in export<br>- Total records count shown |
| **TE062** | Verify export file naming conventions | P0 | Export multiple reports | 1. Export student report: CSV<br>2. Export class report: Excel<br>3. Export with date range filter | - Filenames follow pattern: Type_Name_YYYY-MM-DD.ext<br>- Special characters replaced with underscores<br>- Filenames unique (timestamp if needed)<br>- Extensions correct (.csv, .xlsx, .pdf) |
| **TE063** | Verify export of custom date ranges | P0 | Teacher wants specific date range | 1. Click "Export"<br>2. Select "Custom Date Range"<br>3. Choose start: Jan 1, 2025, end: Jan 31, 2025<br>4. Export data | - Only activities within date range included<br>- Date range shown in export header<br>- Filename includes date range if possible<br>- No activities outside range |
| **TE064** | Verify email report sharing | P0 | Teacher wants to share student report | 1. Generate student report<br>2. Click "Share via Email"<br>3. Enter recipient: parent@email.com<br>4. Add optional message<br>5. Send | - Email sent with report attached<br>- Subject: "Student Report for [Student Name]"<br>- Custom message included<br>- Teacher receives copy (BCC)<br>- Delivery confirmation |
| **TE065** | Verify shared report permissions | P1 | Teacher shared report link | 1. Generate shareable link for report<br>2. Copy link<br>3. Open link in incognito browser | - Link opens report without login (if designed that way)<br>OR Link requires authorized access<br>- Link expiration enforced (7 days default)<br>- Read-only access<br>- Cannot modify data |
| **TE066** | Verify report link generation and expiration | P0 | Teacher wants to share report via link | 1. Click "Generate Shareable Link"<br>2. Set expiration: 7 days<br>3. Copy link<br>4. Wait until expiration<br>5. Test link | - Link generated: https://staging.hellobritannica.eb.com/shared/report/XXXXX<br>- Works before expiration<br>- After expiration: "Link expired" error<br>- Option to regenerate link |
| **TE067** | Verify report preview before sharing | P0 | Teacher about to share report | 1. Click "Share Report"<br>2. Click "Preview"<br>3. Review content | - Modal or new tab opens with report preview<br>- Shows exactly what recipient will see<br>- Can cancel or proceed with sharing<br>- Preview includes all sections |
| **TE068** | Verify bulk report generation for multiple students | P1 | Teacher has class of 20 students | 1. Select all students in class<br>2. Click "Generate Reports"<br>3. Select "PDF"<br>4. Download | - Reports generate as ZIP file<br>- ZIP contains 20 individual PDFs<br>- Filename: ClassName_StudentReports_YYYY-MM-DD.zip<br>- Generation time reasonable (< 60 seconds) |
| **TE069** | Verify report generation error handling | P0 | Student with no activity data | 1. Select student with zero activities<br>2. Attempt to generate PDF report | - Warning message: "No activity data available for this student"<br>- Option to generate empty template OR cancel<br>- No broken PDF generated<br>- Suggested action: "Assign activities first" |
| **TE070** | Verify report regeneration with updated data | P0 | Student completed new activity after report generation | 1. Generate report at 9 AM (3 activities)<br>2. Student completes 1 more activity at 10 AM<br>3. Regenerate report at 11 AM | - New report includes 4 activities<br>- All data updated<br>- Generation timestamp shows 11 AM<br>- Old report not automatically replaced (unless designed that way) |

---

## SECTION 4: SECURITY TESTING (15 Test Cases)

### Module: Security - Authentication & Authorization

| Test ID | Title | Priority | Pre-condition | Test Steps | Expected Result |
|---------|-------|----------|---------------|------------|-----------------|
| **SEC001** | Verify password complexity requirements | P0 | User on password creation page | 1. Attempt password: "12345"<br>2. Attempt: "password"<br>3. Attempt: "Test@123" | - "12345" rejected: "Password must be at least 8 characters"<br>- "password" rejected: "Password must contain at least one number and one special character"<br>- "Test@123" accepted<br>- Real-time feedback as user types |
| **SEC002** | Verify password encryption in transit | P0 | User logging in | 1. Open browser Developer Tools → Network tab<br>2. Enter credentials and login<br>3. Inspect login POST request | - Password sent over HTTPS (not HTTP)<br>- Password value in request is not visible in plain text<br>- SSL certificate valid<br>- No security warnings in browser |
| **SEC003** | Verify session timeout and auto-logout | P0 | User logged in | 1. Login to application<br>2. Leave browser idle for 30 minutes<br>3. Attempt to interact with application | - After timeout period, user redirected to login page<br>- Message: "Your session has expired. Please login again."<br>- Session token invalidated<br>- Cannot use browser back button to access protected pages |
| **SEC004** | Verify protection against brute force attacks | P0 | User attempting to login | 1. Attempt login with wrong password 5 times<br>2. Note response after 5th attempt | - After 5 failed attempts: Account locked for 15 minutes<br>OR CAPTCHA required<br>- Error message: "Too many failed attempts. Please try again in 15 minutes"<br>- Lockout prevents further attempts |
| **SEC005** | Verify secure password reset flow | P0 | User initiating password reset | 1. Click "Forgot Password"<br>2. Enter email<br>3. Receive reset email<br>4. Check reset token in URL | - Reset link contains unique, random token (not user ID)<br>- Token minimum 32 characters<br>- Token expires after 1 hour<br>- Old token invalidated after password reset<br>- Cannot reuse old token |
| **SEC006** | Verify role-based access control - Admin | P0 | Admin and Teacher accounts exist | 1. Login as Teacher<br>2. Attempt to access admin URL directly: /admin/school-management<br>3. Observe response | - Access denied: 403 Forbidden<br>OR Redirected to teacher dashboard<br>- Error message: "You don't have permission to access this page"<br>- Cannot bypass with URL manipulation |
| **SEC007** | Verify role-based access control - Teacher cannot access other teachers' classes | P0 | Two teacher accounts, each with own classes | 1. Login as Teacher A<br>2. Note Teacher B's class ID from database/URL<br>3. Attempt to access Teacher B's class by direct URL | - Access denied<br>- Error: "Class not found" OR "You don't have permission"<br>- Cannot view other teacher's students<br>- Cannot modify other teacher's data |
| **SEC008** | Verify students cannot access other students' data | P0 | Two student accounts in same class | 1. Login as Student A<br>2. Note Student B's user ID<br>3. Attempt to access Student B's profile/progress via URL manipulation | - Access denied<br>- Can only view own profile and progress<br>- Cannot see other students' scores or detailed activity data<br>- Class leaderboard (if any) shows limited info only |
| **SEC009** | Verify API endpoint authorization | P0 | User with browser DevTools | 1. Login as Student<br>2. Open DevTools → Network<br>3. Find API endpoint for student data: /api/students/{id}<br>4. Copy API call<br>5. Modify {id} to another student's ID<br>6. Send request | - API returns 403 Forbidden<br>- Error response: {"error": "Unauthorized"}<br>- Cannot access other users' data via API<br>- Authorization token checked on every request |
| **SEC010** | Verify HTTPS enforcement | P0 | User attempting HTTP access | 1. Type in browser: http://staging.hellobritannica.eb.com<br>2. Press Enter | - Automatically redirected to https://staging.hellobritannica.eb.com<br>- 301 Permanent Redirect response<br>- All pages enforce HTTPS<br>- No mixed content warnings |
| **SEC011** | Verify secure cookie flags | P0 | User logged in | 1. Login to application<br>2. Open DevTools → Application → Cookies<br>3. Inspect session cookie | - Cookie has "Secure" flag: Yes<br>- Cookie has "HttpOnly" flag: Yes<br>- Cookie has "SameSite" attribute: Lax or Strict<br>- Cookie not accessible via JavaScript document.cookie |
| **SEC012** | Verify protection against XSS attacks | P0 | User can input text (e.g., student name, class description) | 1. Enter malicious script in name field: <script>alert('XSS')</script><br>2. Save<br>3. View data on page | - Script not executed<br>- Input sanitized/escaped: &lt;script&gt;alert('XSS')&lt;/script&gt;<br>- No JavaScript alert popup<br>- Data displayed as plain text |
| **SEC013** | Verify protection against CSRF attacks | P0 | User performing state-changing action | 1. Login to application<br>2. Open DevTools → Network<br>3. Perform action like "Delete Student"<br>4. Inspect POST request | - Request includes CSRF token<br>- Token is unique per session<br>- Token validated on server<br>- Request without token is rejected |
| **SEC014** | Verify input sanitization for SQL injection | P0 | User on login page | 1. Enter email: admin' OR '1'='1<br>2. Enter password: anything<br>3. Attempt login | - Login fails<br>- No SQL error exposed to user<br>- Input treated as literal string<br>- Application does not crash<br>- Prepared statements used (backend verification needed) |
| **SEC015** | Verify file upload security | P0 | User uploading profile picture or document | 1. Attempt to upload .exe file<br>2. Attempt to upload .php file<br>3. Attempt to upload 50MB file<br>4. Upload valid .jpg file | - .exe rejected: "File type not allowed"<br>- .php rejected: "File type not allowed"<br>- 50MB rejected: "File size exceeds 5MB limit"<br>- .jpg accepted<br>- File content validated (not just extension)<br>- Uploaded files not executable |

---

## SECTION 5: NEGATIVE SCENARIOS - AUTHENTICATION (10 Test Cases)

### Module: Authentication - Negative Scenarios

| Test ID | Title | Priority | Pre-condition | Test Steps | Expected Result |
|---------|-------|----------|---------------|------------|-----------------|
| **NEG001** | Verify login with empty email field | P0 | On login page | 1. Leave email field empty<br>2. Enter valid password<br>3. Click Login | - Error message: "Email is required"<br>- Login button may be disabled until both fields filled<br>- User remains on login page |
| **NEG002** | Verify login with empty password field | P0 | On login page | 1. Enter valid email<br>2. Leave password field empty<br>3. Click Login | - Error message: "Password is required"<br>- Cannot submit form<br>- Focus remains on password field |
| **NEG003** | Verify login with SQL injection in email | P0 | On login page | 1. Enter email: admin'--<br>2. Enter password: test123<br>3. Click Login | - Login fails<br>- Error: "Invalid email or password"<br>- No SQL errors displayed<br>- Application remains stable |
| **NEG004** | Verify login with XSS payload in email | P0 | On login page | 1. Enter email: <script>alert('XSS')</script>@test.com<br>2. Enter password<br>3. Click Login | - No JavaScript alert executed<br>- Email treated as string<br>- Login fails (invalid email format)<br>- No security breach |
| **NEG005** | Verify login with extremely long email (buffer overflow) | P0 | On login page | 1. Enter email: 500+ character string<br>2. Enter password<br>3. Click Login | - Email field limits input (e.g., 100 chars max)<br>OR Error: "Email is too long"<br>- Application does not crash<br>- Form validation prevents submission |
| **NEG006** | Verify expired session token handling | P0 | User has valid session token that expired | 1. Login to application<br>2. Extract session token<br>3. Manually expire token (or wait for expiration)<br>4. Make API request with expired token | - API returns 401 Unauthorized<br>- User redirected to login page<br>- Error message: "Session expired. Please login again."<br>- Cannot access protected resources |
| **NEG007** | Verify simultaneous login from multiple devices | P0 | User logged in on Device A | 1. Login as user on Device A<br>2. Without logging out, login as same user on Device B<br>3. Interact on both devices | - Option A: Both sessions active (multi-device support)<br>OR Option B: Device A session invalidated, only Device B active<br>- Behavior should be consistent and documented<br>- No data corruption |
| **NEG008** | Verify account lockout after failed attempts | P0 | Valid user account exists | 1. Attempt login with wrong password 10 times<br>2. Attempt login with correct password | - Account locked after threshold (e.g., 5 attempts)<br>- Correct password still fails: "Account locked"<br>- Lockout duration: 15 minutes<br>- Email notification sent to user |
| **NEG009** | Verify password reset with invalid/expired token | P0 | User has expired password reset token | 1. Click expired password reset link<br>2. Attempt to set new password | - Error message: "This password reset link has expired"<br>- Cannot set new password<br>- Link to request new reset<br>- Token single-use (cannot reuse) |
| **NEG010** | Verify access to protected pages without authentication | P0 | User not logged in | 1. Open browser<br>2. Navigate directly to: https://staging.hellobritannica.eb.com/dashboard<br>3. Attempt to access protected resource | - Redirected to login page<br>- After login, redirected back to originally requested page<br>- Cannot bypass authentication with URL manipulation |

---

## Implementation Notes

### Adding to Excel File:

1. **Create New Sheet** "Admin - URL & School" for AO013-AO039
2. **Add to Existing Sheet** "Teacher - Email" for TE051-TE070 (or create new "Teacher - Reporting")
3. **Create New Sheet** "Security Testing" for SEC001-SEC015
4. **Add to Respective Sheets** NEG001-NEG010 (distribute by module)

### Test Execution Priority:

**Week 1:** AO013-AO027, AO028-AO039 (Admin Critical Path)
**Week 2:** TE051-TE070 (Teacher Reporting)
**Week 3:** SEC001-SEC015 (Security)
**Week 4:** NEG001-NEG010 + Continue Negative Scenarios

### Test Data Requirements:

- **Admin Test Accounts:** 3-5 admin accounts with different configurations
- **Teacher Test Accounts:** 10+ teacher accounts
- **Student Test Accounts:** 50+ student accounts with varying progress levels
- **Test Classes:** 5 classes with 5, 10, 25 students
- **Test Emails:** Use test email service (Mailtrap, Mailhog) for invitation testing

### Environment Setup:

- Staging environment should be stable and refreshed weekly
- Test data should be consistent for report validation
- PDF viewer/reader tool for manual PDF verification
- Browser DevTools for security testing
- Screen reader tool (NVDA) for accessibility testing

---

**Total New Test Cases in This Document:** 72 test cases
**Estimated Creation Time:** 4-5 days (with 2 QA engineers)
**Estimated Execution Time:** 30-35 hours (first execution)

**Next Document:** Additional 80-100 test cases for Sprint 2 (Negative Scenarios, Cross-Browser, Accessibility)
