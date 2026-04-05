# Intelligent OD – Master Project Plan

## 1. Project Overview
**Intelligent OD** is a premium organisational development (OD) consultancy platform built for modern leaders. It bridges the gap between high-level advisory and digital education by offering a combination of strategic service deep-dives (Bento UI) and an elite video-based learning platform.

### Core Value Proposition
- Establish immediate authority with a high-end, glassmorphic UI.
- Clarify complex OD structures using interactive, easily scannable "Bento" grids and frameworks.
- Convert visitors into users through 15-second teaser videos and seamless authentication.

---

## 2. Technical Architecture

### Tech Stack
- **Frontend Layer:** HTML5, Vanilla CSS3 (Custom Design System with Glassmorphism)
- **Logic & Dom Manipulation:** Vanilla ES6+ JavaScript (`app.js`, `navbar.js`)
- **Animations:** GSAP (GreenSock) & CSS Keyframes
- **Backend & Database:** Firebase (Authentication, Firestore, Storage)
- **Deployment Strategy:** GitHub Pages (Frontend) / Firebase Hosting

### Project File Structure
```text
/
├── index.html               # Landing page, Value Proposition
├── about.html               # Kash Haroon / Consultancy Background
├── services.html            # Core Frameworks & Bento Grid
├── insights.html            # Latest OD Insights & Articles
├── courses.html             # Video Course Library (Paywall Entry)
├── course-details.html      # Free Preview Player & Video Logic
├── dashboard.html           # Authenticated User Learning Progress
├── login.html               # Firebase Auth Interface
│
├── css/                     # Vanilla CSS style architecture
├── js/                      # Frontend logic and Firebase interactions
│    ├── firebaseClient.js   # Global Firebase Initialization & Queries
│    ├── firebaseConfig.js   # API Keys (Git Ignored)
│    └── navbar.js           # Glassmorphic responsive nav logic
├── images/                  # Static assets & compressed graphics
└── assets/                  # Additional downloads / resources
```

---

## 3. Implementation Phases & Roadmap

### ✅ Phase 1: Foundation & Brand Aesthetic (Completed)
- [x] Design global CSS variables (Slate/Navy minimal aesthetic).
- [x] Build semantic HTML structure structure for universal navigation.
- [x] Implement the mobile-first glassmorphic overlay menu (optimized for 400px width).
- [x] Construct the dynamic `index.html` landing experience.

### ✅ Phase 2: Content & Core Navigation (Completed)
- [x] **Services:** Implement the highly responsive "Bento Grid" layout.
- [x] **About:** Build authoritative profile sections.
- [x] **Insights:** Initial setup for OD articles and knowledge sharing.
- [x] Visualise the "Four-Step Framework" via interactive CSS/JS elements.

### 🟡 Phase 3: Learning Platform & Firebase Integration (In Progress)
- [x] Create the `courses.html` layout.
- [x] Build `course-details.html` with the custom 15-second trial preview logic.
- [x] Architect Firebase database structure (`firebaseClient.js`).
- [ ] Connect `login.html` to Firebase Auth (Email/Password & Google).
- [ ] Wire up `dashboard.html` to pull real-time reading/video watch progress from Firestore.

### 🔴 Phase 4: Monetization & Refinement (Upcoming)
- [ ] **Stripe Integration:** Hook Firebase up with Stripe checkout for gated course access.
- [ ] **Dynamic Insights:** Convert the hardcoded `insights.html` into a filterable blog powered by Firestore.
- [ ] **Offline Resources:** Configure Firebase Storage secure downloads for PDF Workshop resources.
- [ ] **Polish:** Dark/Light mode theme persistence using `localStorage`.

---

## 4. Key Security & Best Practices
- **Firebase Keys:** Ensure `js/firebaseConfig.js` containing the private API config stays in `.gitignore`. The `firebaseConfig.example.js` will act as the Git template.
- **RESTful Limitations:** Ensure Firebase security rules (`firestore.rules`) only permit users to read/write to their own UID's progress documents. 
- **SEO Elements:** Every page must include unique meta descriptions, title tags, and a unified semantic header hierarchy for crawler performance.

---

## Next Steps to Execute
1. Finalize the active **Firebase Authentication** loop (Login -> Redirect to Dashboard).
2. Render user-specific course progress inside the Dashboard using `user.uid`.
