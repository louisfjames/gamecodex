# GameCodex - Testing Documentation

This document summarises all testing completed throughout development. OUTLINE ITERATIONS?

## Table of Contents

1. [Manual Testing](#manual-testing)
2. [Automated Testing](#automated-testing)
3. [Acceptance Criteria Testing](#acceptance-criteria-testing)
4. [HTML Validator](#html-validator)
5. [CSS Validator](#css-validator)
6. [JavaScript Validator](#javascript-validator)
8. [Python Testing](#python-testing)
7. [Google Chrome Lighthouse](#google-chrome-lighthouse)
8. [Bug Fixes](#bug-fixes)


### Manual Testing
Behaviour driven development was used to guide the testing process. This method focuses on how a user expects a feature to behave and the aim is to check that the site behaves in a clear and predictable way. It also helps keep the focus on user needs rather than only on technical checks. These principles are met in the manual testing because each test follows a simple action and a clear expected result, and each one checks behaviour that matters to the user such as navigation, searching, loading data, and viewing festival details. Each feature was tested by hand to confirm that it worked as expected. This type of testing is useful because it shows how the site performs in real use and it helps find issues that automated tools may not detect. 


#### Iteration One 
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Header links | Each link loads the correct page | Clicked each link | All links load the correct pages | **✔ PASS** or FAIL |

#### Iteration Two 
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| x | x | x| x | **✔ PASS** or FAIL |

#### Iteration Three 
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| x | x | x| x | **✔ PASS** or FAIL |

### Automated Testing
Automated testing checks code behaviour by running tests through a tool or script rather than by hand. Its key principles are repeatability, consistency, and early detection of errors. Automated tests run the same steps every time, which removes human error and makes it easier to spot issues when new features are added. They are useful for checking functions, input handling, and any part of the code that should always behave in the same way. 


Automated testing to be added here.

### Acceptance Criteria Testing
This table outlines the key user stories and acceptance criteria completed during development. This demonstrates how the website meets the expectations of its target audience and ensures a satisfying user experience. All testing was carried out at the end of each iteration, with each iteration aligned to one of the three development themes to ensure focused, structured progress.

#### Iteration One 

| User Story | Acceptance Criteria | Status |
|-----------|---------------------|--------|
US 1.1.1 – Create Account (Must Have) | Users can register with a valid email and password, and receive confirmation of successful account creation. | Pass or Fail
US 1.1.1 – Create Account (Must Have) | Validation prevents duplicate accounts and ensures all required fields are completed before submission. | Pass or Fail 
US 1.1.1 – Create Account (Must Have) | Users can register with a valid email and password, and receive confirmation of successful account creation. | Pass or Fail
US 1.1.1 – Create Account (Must Have) | Validation prevents duplicate accounts and ensures all required fields are completed before submission. | Pass or Fail
US 1.1.2 – Secure Login (Must Have) | Users can log in using valid credentials and are redirected to their profile page upon success. | Pass or Fail
US 1.1.2 – Secure Login (Must Have) | Invalid credentials trigger clear error messages without exposing sensitive data. | Pass or Fail
US 1.1.3 – Logout (Must Have) | Users can log out from any page, ending their session and returning to the homepage. | Pass or Fail
US 1.1.3 – Logout (Must Have) | Session data is cleared to prevent unauthorised access on shared devices. | Pass or Fail
US 1.2.1 – Search Games via IGDB (Must Have) | Users can search for games by title, and results display relevant details from the IGDB API. | Pass or Fail
US 1.2.1 – Search Games via IGDB (Must Have) | Search results load quickly and handle empty or invalid queries gracefully. | Pass or Fail
US 1.2.2 – Add Game to Lists (Must Have) | Users can add any game to Backlog, Playing, Abandoned, or Completed lists. | Pass or Fail
US 1.2.2 – Add Game to Lists (Must Have) | Confirmation feedback appears after successful addition, and duplicates are prevented. | Pass or Fail
US 1.3.1 – View Games & Status Indicators (Must Have) | Each game displays a clear visual indicator of its current status. | Pass or Fail
US 1.3.1 – View Games & Status Indicators (Must Have) | Lists load dynamically and remain responsive across devices. | Pass or Fail
US 1.3.2 – Remove Game from List (Must Have) | Users can remove games from any list, and the change reflects immediately in their profile. | Pass or Fail
US 1.3.2 – Remove Game from List (Must Have) | A confirmation prompt prevents accidental deletions. | Pass or Fail


#### Iteration Two

| User Story | Acceptance Criteria | Status |
|-----------|---------------------|--------|
US 2.1.1 – Profile Shows Recent Games (Must Have) | Profile displays the three most recently updated games from each list. | Pass or Fail
US 2.1.1 – Profile Shows Recent Games (Must Have) | Recent‑games sections update automatically when games are added, moved, or removed. | Pass or Fail
US 2.1.2 – Move Games Between Lists (Must Have) | Users can change a game’s status using an edit or dropdown control. | Pass or Fail
US 2.1.2 – Move Games Between Lists (Must Have) | The game appears in the new list immediately and is removed from the previous one. | Pass or Fail
US 2.2.1 – Dedicated List Pages (Should Have) | Each list has its own page showing all games assigned to that category. | Pass or Fail
US 2.2.1 – Dedicated List Pages (Should Have) | Pages load with clear headings and consistent styling across all lists. | Pass or Fail
US 2.2.2 – List Stats on Profile (Could Have) | Profile page shows a count of games in each list. | Pass or Fail
US 2.2.2 – List Stats on Profile (Could Have) | Stats update automatically when games are added, moved, or removed. | Pass or Fail


#### Iteration Three

| User Story | Acceptance Criteria | Status |
|-----------|---------------------|--------|
US 3.1.1 – Clearer Loading States & Errors (Must Have) | Loading indicators appear during API calls, list updates, and page transitions. | Pass or Fail
US 3.1.1 – Clearer Loading States & Errors (Must Have) | Error messages use plain language and provide guidance on what to do next. | Pass or Fail
US 3.1.2 – Improved Visual Clarity & Layout (Should Have) | Spacing, typography, and card layouts follow a consistent visual hierarchy. | Pass or Fail
US 3.1.2 – Improved Visual Clarity & Layout (Should Have) | Key actions (add, edit, remove) are clearly visible and easy to access. | Pass or Fail
US 3.2.1 – Add Personal Ratings (Could Have) | Users can assign a rating (e.g., 1–5 stars) to any game. | Pass or Fail
US 3.2.1 – Add Personal Ratings (Could Have) | Ratings display consistently on list pages and the profile page. | Pass or Fail
US 3.2.2 – Add Notes to Game Entries (Could Have) | Users can add, edit, and view notes for any game entry. | Pass or Fail
US 3.2.2 – Add Notes to Game Entries (Could Have) | Notes are stored per user and displayed on the game’s card or detail section. | Pass or Fail


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
      <td>(1) x</td>
      <td>x</td>
      <td>✔️ Fixed or NOT</td>
      <td>Fix: x</td>
      <td>xxxxx</td>
    </tr>
  </tbody>
</table>

<sub>[*Back to contents*](#table-of-contents)</sup>