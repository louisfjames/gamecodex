# GameCodex - Testing Documentation

## Table of Contents

1. [Testing Approach](#testing-approach)
2. [Testing Timeline](testing-timeline)
3. [Manual Testing](#manual-testing)
4. [Automated Testing](#automated-testing)
5. [Acceptance Criteria Testing](#acceptance-criteria-testing)
6. [HTML Validator](#html-validator)
7. [CSS Validator](#css-validator)
8. [JavaScript Validator](#javascript-validator)
9. [Python Testing](#python-testing)
10. [Google Chrome Lighthouse](#google-chrome-lighthouse)
11. [Bug Fixes](#bug-fixes)

### Testing Approach
This document summarises all testing completed throughout development. Testing was carried out continuously throughout development and structured manual testing completed at the end of each iteration. Following Agile principles, each iteration delivered a meaningful slice of functionality aligned with the project’s themes and user stories. The project was organised into three major themes, each representing a focused stage of development. These themes guided the scope of each iteration and ensured that testing aligned directly with user needs and functional priorities.

Iteration Breakdown:
- **Iteration 1 – Core Platform Foundations**
  - Implemented user accounts, including signup, login, and logout.
  - Added IGDB-powered game search and the ability to add games to user lists.
  - Built the initial game library display with status indicators.
  - Added the ability to remove games from lists.
- **Iteration 2 – Personalisation & List Management**
  - Added profile page sections showing the three most recent games from each list.
  - Implemented moving games between Backlog, Playing, Abandoned, and Completed.
  - Created dedicated pages for full list history.
  - Added list statistics to the profile page.
- **Iteration 3 – Final Polish & Enhanced Customisation**
  - Improved UI/UX with clearer loading states and error messages.
  - Refined layout and visual clarity across all pages.

### Testing Timeline
A consistent testing routine was maintained throughout development to ensure each iteration met its acceptance criteria and remained stable as new features were introduced. The timeline below outlines the key testing milestones completed during the project.

| Phase  | Date |
|------------------------------------------------------------------|---------------|
| Project initiated | 8 May 2026 |
| Iteration 1 testing completed (manual testing + acceptance checks) | 23 May 2026 |
| Iteration 2 testing completed (manual testing + acceptance checks) | 30 May 2026 |
| Iteration 3 testing completed (manual testing + acceptance checks) | 6 June 2026 |
| Final testing phase (automated tests + validator checks) | 7 - X June 2026 |


### Manual Testing
Behaviour driven development was used to guide the testing process. This method focuses on how a user expects a feature to behave and the aim is to check that the site behaves in a clear and predictable way. It also helps keep the focus on user needs rather than only on technical checks. These principles are met in the manual testing because each test follows a simple action and a clear expected result, and each one checks behaviour that matters to the user such as navigation, searching, loading data, and viewing festival details. Each feature was tested by hand to confirm that it worked as expected. This type of testing is useful because it shows how the site performs in real use and it helps find issues that automated tools may not detect. 

Manual testing was carried out at the end of each iteration to ensure that newly implemented features were functioning correctly before moving forward. Following Agile principles, each iteration delivered a small but complete slice of functionality, which was then manually tested for correctness, usability, and stability. This approach ensured that issues were identified early, user flows remained coherent, and the platform evolved in a controlled, reliable way.

#### Iteration One - Navigation and Layout

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Header links | Each link loads the correct page | Clicked all header links | All links load correct pages | **✅ PASS** |
| Logo link | Returns user to landing page | Clicked logo | Landing page loads | **✅ PASS** |
| Profile navigation | Profile link loads user profile | Clicked “Profile” | Profile page loads correctly | **✅ PASS** |
| All Entries link | Loads full game list | Clicked link | All Entries page loads | **✅ PASS** |
| Back to Profile link | Returns user to profile | Clicked link | Profile page loads | **✅ PASS** |
| Footer links | Footer links open correct pages | Clicked each link | All links open correct pages | **✅ PASS** |
| Desktop layout | Layout stable on large screens | Tested on desktop | No layout issues | **✅ PASS** |
| Tablet layout | Layout adapts correctly | Tested at 768–991px | Minor spacing adjustments needed | **✅ PASS - Required fix, see commit a84fa99** |
| Mobile layout | Layout adapts to small screens | Tested at <768px | Layout clean and readable | **✅ PASS** |

#### Iteration One - User Authentication (Signup, Login, Logout)

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Signup form | Creates new user | Submitted valid signup | Account created successfully | **✅ PASS** |
| Signup validation | Shows errors for invalid input | Submitted empty/invalid fields | Clear validation errors shown | **✅ PASS** |
| Login form | Logs user in | Entered valid credentials | User logged in | **✅ PASS** |
| Incorrect login | Shows error message | Entered wrong password | Error message shown | **✅ PASS** |
| Logout | Logs user out | Clicked logout | User logged out | **✅ PASS** |
| Unwanted login messages | Login/logout messages hidden | Logged in/out repeatedly | “Signed in/out” messages no longer appear | **✅ PASS** |

#### Iteration One - Profile Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Username display | Shows logged‑in user’s name | Loaded profile page | Username displays correctly | **✅ PASS** |
| View/Edit All Entries link | Navigates to full list | Clicked link | All Entries page loads | **✅ PASS** |
| Success messages | Only relevant messages appear | Triggered actions | Only game‑related messages shown | **✅ PASS** |
| Layout | Profile content displays correctly | Checked on all devices | Layout stable | **✅ PASS** |

#### Iteration One - Game Entry Management (CRUD)

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Add Entry form | Creates new game entry | Submitted valid form | Entry created and visible | **✅ PASS** |
| Add Entry validation | Shows errors for invalid input | Submitted empty fields | Validation errors shown | **✅ PASS** |
| Delete Entry | Removes entry | Clicked delete | Entry removed from list | **✅ PASS** |
| Entry ownership | Users only see their own entries | Logged in as two users | Entries isolated per user | **✅ PASS** |
| Button layout | Buttons align correctly | Tested on tablet/mobile | Tablet spacing needed refinement | **✅ PASS - Required fix, see commit ac2815** |

#### Iteration One - All Entries Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Entry list loads | Shows all user entries | Loaded page | All entries appear | **✅ PASS** |
| Card layout | Cards display correctly | Checked cards | Layout clean and readable | **✅ PASS** |
| Delete buttons | Buttons work correctly | Clicked each | Correct pages/actions triggered | **✅ PASS** |
| Responsive layout | Cards adapt to screen size | Tested on multiple devices | Tablet layout needs small fix | **✅ PASS** |

#### Iteration One - Search Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Search input | Returns matching games | Searched for known title | Correct results shown | **✅ PASS** |
| Empty search | Shows message | Submitted empty search | Clear message shown | **✅ PASS** |
| No results | Shows “no results” message | Searched for nonsense | Message shown | **✅ PASS** |
| Special characters | Handles unusual input | Entered symbols | No errors | **✅ PASS** |
| Layout | Results display correctly | Checked on all devices | Layout stable | **✅ PASS** |

#### Iteration One - Error Handling

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| 404 page | Custom 404 appears | Entered invalid URL | 404 page loads | **✅ PASS - Impletented as part of Iteration 2 (see commit 701eb15)** |
| Permission errors | Users can’t access others’ data | Tried accessing another user’s entry | Redirected or blocked | **✅ PASS** |
| Form errors | Validation messages appear | Submitted invalid forms | Clear errors shown | **✅ PASS** |

#### Iteration One - Performance and Responsiveness

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Page load speed | Pages load quickly | Tested across pages | All pages load fast | **✅ PASS** |
| Mobile responsiveness | Layout adapts to small screens | Tested on mobile | No overlap or scroll | **✅ PASS** |
| Tablet responsiveness | Layout adapts to medium screens | Tested on tablet | Minor spacing issues | **✅ PASS** |
| No horizontal scroll | No sideways scrolling | Tested on mobile/tablet | No scroll present | **✅ PASS** |

#### Iteration Two – Profile Page – Latest Three Games Per List

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Latest three items per list | Only the three most recent games appear for each status | Added 4+ games to each list, checked profile | Correctly shows newest three only | **✅PASS - Required fix, see commit deaa770** |
| Correct ordering | Items sorted newest → oldest | Added entries with different timestamps | Order correct across all lists | **✅PASS - Required fix, see commit deaa770** |
| Empty list behaviour | Empty lists show a friendly message or remain hidden | Viewed profile with no “Abandoned” entries | Behaviour correct and clean | **✅ PASS** |
| Layout consistency | All four list sections align visually | Checked on desktop/tablet/mobile | Layout consistent and readable | **✅ PASS** |


#### Iteration Two – Moving Games Between Lists

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Change status from entry page | Updating a game’s status moves it to the correct list | Edited status for multiple entries | Entries appear in new list, removed from old | **✅ PASS** |
| Status update messages | Clear confirmation message shown | Updated several entries | Correct success messages shown | **✅ PASS** |
| Ownership protection | Users cannot move others’ entries | Tried editing another user’s entry | Access blocked or redirected | **✅ PASS** |
| Data integrity | No duplicate entries after moving | Moved same entry repeatedly | Only one entry exists at all times | **✅ PASS** |


#### Iteration Two – Dedicated Full List Pages (Backlog, Playing, Completed, Abandoned)

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Page loads correct list | Each page shows only entries with that status | Visited all four list pages | Correct entries shown per list | **✅ PASS** |
| Sorting | Entries sorted newest → oldest | Checked ordering | Sorting correct | **✅PASS - Required fix, see commit deaa770** |
| Navigation | “Back to Profile” or equivalent link works | Used return link on each page | Returns to profile page | **✅ PASS** |
| Responsive layout | Cards adapt to screen size | Tested on mobile/tablet | Layout stable | **✅ PASS** |


#### Iteration Two – List Statistics on Profile Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Count accuracy | Stats match number of entries per list | Added/moved/deleted entries | Counts update correctly | **✅ PASS** |
| Real‑time updates | Stats update immediately after changes | Changed statuses repeatedly | Stats updated instantly | **✅ PASS** |
| Layout and visibility | Stats readable and visually consistent | Checked across devices | Stats display cleanly | **✅ PASS** |


#### Iteration Two – Error Handling & Edge Cases

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Invalid status change | Prevents invalid transitions | Tried forcing invalid status via URL | Redirected or blocked | **✅ PASS** |
| Missing entries | Editing a deleted entry handled gracefully | Deleted entry then tried editing | Correct error/redirect | **✅ PASS** |
| 404 integration | New pages use custom 404 | Entered invalid list URLs | Custom 404 shown | **✅ PASS** |


#### Iteration Three – Final Polish
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Loading states | Clear visual feedback during searches and form submissions | Triggered searches and form actions | Loading spinner and messages display correctly | **✅ PASS** |
| Error messages | Errors appear clearly and consistently across pages | Forced validation and API errors | Messages readable and styled consistently | **✅ PASS** |
| Layout refinements | Improved spacing and alignment across all devices | Checked all pages on mobile/tablet/desktop | Layout clean and visually consistent | **✅ PASS** |
| Search results layout | Two‑column layout on medium screens, improved image scaling | Tested searches at multiple breakpoints | Cards display correctly and responsively | **✅ PASS** |
| Form layout polish | Cleaner alignment and spacing on edit/add forms | Tested forms on all devices | Forms display neatly with consistent spacing | **✅ PASS** |
| Button consistency | Buttons aligned and sized correctly on small screens | Checked profile, entry pages, and search results | Buttons centred and consistent | **✅ PASS** |
| Image responsiveness | Result images scale correctly on small screens | Tested various screen sizes | Images display cleanly without distortion | **✅ PASS** |
| Card spacing | Cards maintain consistent spacing across breakpoints | Reviewed search and list pages | Spacing uniform and visually balanced | **✅ PASS** |
| Final UI sweep | No visual glitches or misaligned elements remain | Performed full-site walkthrough | No remaining UI issues found | **✅ PASS** |

### Automated Testing
Automated testing checks code behaviour by running tests through a tool or script rather than by hand. Its key principles are repeatability, consistency, and early detection of errors. Automated tests run the same steps every time, which removes human error and makes it easier to spot issues when new features are added. They are useful for checking functions, input handling, and any part of the code that should always behave in the same way. 


Automated testing to be added here.

### Acceptance Criteria Testing
This table outlines the key user stories and acceptance criteria completed during development. This demonstrates how the website meets the expectations of its target audience and ensures a satisfying user experience. All testing was carried out at the end of each iteration, with each iteration aligned to one of the three development themes to ensure focused, structured progress.

#### Iteration One 

| User Story | Acceptance Criteria | Status | Evidence/Notes |
|-----------|---------------------|--------|----------------|
| **US 1.1.1 – Create Account (Must Have)** | Users can register with a valid email and password, and receive confirmation of successful account creation. | **✅ PASS** | Successfully created multiple test accounts; confirmation message displayed; redirected correctly. |
| **US 1.1.1 – Create Account (Must Have)** | Validation prevents duplicate accounts and ensures all required fields are completed before submission. | **✅ PASS** | Duplicate email attempt shows clear validation error; empty fields trigger built‑in form errors. |
| **US 1.1.2 – Secure Login (Must Have)** | Users can log in using valid credentials and are redirected to their profile page upon success. | **✅ PASS** | Logged in with valid test account; redirected to profile page as expected. |
| **US 1.1.2 – Secure Login (Must Have)** | Invalid credentials trigger clear error messages without exposing sensitive data. | **✅ PASS** | Entered incorrect password; error message shown without revealing account existence. |
| **US 1.1.3 – Logout (Must Have)** | Users can log out from any page, ending their session and returning to the homepage. | **✅ PASS** | Logout button tested from multiple pages; always redirects to landing page. |
| **US 1.1.3 – Logout (Must Have)** | Session data is cleared to prevent unauthorised access on shared devices. | **✅ PASS** | After logout, protected pages cannot be accessed via back button; session fully cleared. |
| **US 1.2.1 – Search Games via IGDB (Must Have)** | Users can search for games by title, and results display relevant details from the IGDB API. | **✅ PASS** | Search returns correct game titles, images, and metadata from IGDB. |
| **US 1.2.1 – Search Games via IGDB (Must Have)** | Search results load quickly and handle empty or invalid queries gracefully. | **✅ PASS** | Empty search shows message; invalid terms return “no results” without errors (see commit ref - 247fea1) |
| **US 1.2.2 – Add Game to Lists (Must Have)** | Users can add any game to Backlog, Playing, Abandoned, or Completed lists. | **✅ PASS** | Added multiple games to each list; all appear correctly on list pages. |
| **US 1.2.2 – Add Game to Lists (Must Have)** | Confirmation feedback appears after successful addition, and duplicates are prevented. | **✅ PASS** | Success message shown - fixed on commit 89f8092. Also, duplicate add attempts blocked with validation. |
| **US 1.3.1 – View Games & Status Indicators (Must Have)** | Each game displays a clear visual indicator of its current status. | **✅ PASS** | Status indicators display correctly all entries pages. |
| **US 1.3.1 – View Games & Status Indicators (Must Have)** | Lists load dynamically and remain responsive across devices. | **✅ PASS** | Tested on mobile, tablet, desktop; layout remains stable and responsive. |
| **US 1.3.2 – Remove Game from List (Must Have)** | Users can remove games from any list, and the change reflects immediately in their profile. | **✅ PASS** | Deleted entries disappear instantly from all entries page (and thus the profile). |
| **US 1.3.2 – Remove Game from List (Must Have)** | A confirmation prompt prevents accidental deletions. | **✅ PASS** | Confirmation modal appears before deletion; prevents accidental removal. |


#### Iteration Two

| User Story | Acceptance Criteria | Status | Evidence/Notes |
|-----------|---------------------|--------|----------------|
US 2.1.1 – Profile Shows Recent Games (Must Have) | Profile displays the three most recently updated games from each list. | **✅ PASS** | Verified by adding 4+ games per list; newest three display correctly. |
US 2.1.1 – Profile Shows Recent Games (Must Have) | Recent games sections update automatically when games are added, moved, or removed. | **✅PASS - Required fix, see commit deaa770** | Fourth backlog entry not appearing; ordering incorrect. Logged as bug. |
US 2.1.2 – Move Games Between Lists (Must Have) | Users can change a game’s status using an edit or dropdown control. |**✅ PASS** | Status dropdown works; updates save correctly. |
US 2.1.2 – Move Games Between Lists (Must Have) | The game appears in the new list immediately and is removed from the previous one. | **✅ PASS** | Verified by moving entries between all lists; behaviour correct. |
US 2.2.1 – Dedicated List Pages (Should Have) | Each list has its own page showing all games assigned to that category. | **✅ PASS** | All four list pages load correct filtered entries. |
US 2.2.1 – Dedicated List Pages (Should Have) | Pages load with clear headings and consistent styling across all lists. | **✅ PASS** | Styling consistent; headings correct. |
US 2.2.2 – List Stats on Profile (Could Have) | Profile page shows a count of games in each list. | **✅ PASS** | Counts appear correctly for all lists. |
US 2.2.2 – List Stats on Profile (Could Have) | Stats update automatically when games are added, moved, or removed. | **✅ PASS** | Verified by adding/moving/deleting entries; stats update instantly. |


#### Iteration Three

| User Story | Acceptance Criteria | Status | Evidence/Notes |
|-----------|---------------------|--------| ----------------|
US 3.1.1 – Clearer Loading States & Errors (Must Have) | Loading indicators appear during API calls, list updates, and page transitions. |**Pass** | Loading spinner added to search; form actions show feedback. |
US 3.1.1 – Clearer Loading States & Errors (Must Have) | Error messages use plain language and provide guidance on what to do next. | **✅ PASS** | Validation and API errors now consistent and readable. |
US 3.1.2 – Improved Visual Clarity & Layout (Should Have) | Spacing, typography, and card layouts follow a consistent visual hierarchy. | **✅ PASS** | Layout refinements applied across forms, cards, and search results. |
US 3.1.2 – Improved Visual Clarity & Layout (Should Have) | Key actions (add, edit, remove) are clearly visible and easy to access. | **✅ PASS** | Buttons repositioned and aligned for clarity on all devices. |
US 3.2.1 – Add Personal Ratings (Could Have) | Users can assign a rating (e.g., 1–5 stars) to any game. | **Postponed to future update** | Feature not included in Iteration 3 scope. |
US 3.2.1 – Add Personal Ratings (Could Have) | Ratings display consistently on list pages and the profile page. | **Postponed to future update** | Requires rating system implementation. |
US 3.2.2 – Add Notes to Game Entries (Could Have) | Users can add, edit, and view notes for any game entry. | **Postponed to future update** | Notes functionality deferred. |
US 3.2.2 – Add Notes to Game Entries (Could Have) | Notes are stored per user and displayed on the game’s card or detail section. | **Postponed to future update** | Requires UI and model changes. |

The “Could Have” features for this iteration were intentionally postponed to a future update. These items were explored during planning but deprioritised to ensure the core UI/UX improvements, loading states, and layout refinements were delivered to a high standard within the available time. This aligns with Agile principles where low priority enhancements are scheduled for later development once all Must and Should Haves are complete.


### HTML Validator
[HTML W3C Validator](https://validator.w3.org/) was used to validate all HTML files.

| Page | URL | Status | Screenshot | Validation Link | Notes |
|------|-----|--------|------------|----------------|-------|


### CSS Validator
 [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all CSS files.

| Page | URL | Status | Screenshot | Validation Link | Notes |
|------|-----|--------|------------|----------------|-------|

### JavaScript Validator
[JSHint](https://jshint.com/) was used to validate all JS files.

| File | Status | JSHint Screenshot | ESLint Screenshot | Notes |
|-----|--------|-------|-------|-------|

### Python Testing
TO BE COMPLETED - Potential wording: All Python files validated using multiple tools to ensure comprehensive code quality and PEP8 compliance.


### Google Chrome Lighthouse
Add performance results
| Page | Desktop Results| Notes |
|------|----------------|-------|

Analysis performance results

### Bug Fixes
This section documents the issues found during development and how each one was resolved. It provides a clear record of problems and fixes highlighted during manual testing.

<table>
  <thead>
    <tr>
      <th>Bug Title</th>
      <th>Bug Description</th>
      <th>Fixed?</th>
      <th>Fixed Description</th>
      <th>GitHub Commit Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>(1) Fourth backlog entry not visible</td>
      <td>Adding a fourth game causes it not to appear on the profile page, despite being saved in the database.</td>
      <td>✅ PASS</td>
      <td>Fix: Ensure backlog entries are ordered by -date_modified so the three most recently updated items appear on the profile page. All entries remain accessible on the full backlog page. This resolves the issue where older items pushed newer ones out of the visible slice.</td>
      <td>deaa770</td>
    </tr>
    <tr>
      <td>(2) Backlog ordering incorrect</td>
      <td>Games added to the backlog display oldest first instead of newest first. Expected newest entries to appear on the left.</td>
      <td>✅ PASS</td>
      <td>Fix: Update backlog queryset to order by -date_modified instead of date_added. This ensures the most recently edited backlog items appear first, matching expected behaviour.</td>
      <td>deaa770</td>
    </tr>
    <tr>
      <td>(3) All Entries page not showing newest items first</td>
      <td>Newly added games do not appear at the top of the All Entries page. Ordering is incorrect, showing older entries before newer ones.</td>
      <td>✅ PASS</td>
      <td>Fix: Update the All Entries queryset to order by -date_modified so the most recently updated games appear at the top. This aligns the All Entries page with the profile page ordering.</td>
      <td>deaa770</td>
    </tr>
  </tbody>
</table>

<sub>[*Back to contents*](#table-of-contents)</sup>