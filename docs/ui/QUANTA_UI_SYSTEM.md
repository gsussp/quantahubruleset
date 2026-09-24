# QuantaHub UI System

## 1. Product character

QuantaHub is a dark-first cybersecurity learning platform and professional lab workspace.

Desired traits:
- technical,
- calm,
- premium,
- modular,
- responsive,
- information-dense without clutter,
- interactive without spectacle.

Avoid Matrix rain, skulls, generic hacker photography, uncontrolled neon, constant glow, random gradients, fake decorative terminals, emoji-as-icons, cartoon gamification and over-rounded consumer-SaaS styling.

## 2. Visual tokens

Starting palette; validate WCAG contrast before implementation:

| Token | Initial value |
| --- | --- |
| background.base | `#080B12` |
| background.nav | `#0B1018` |
| surface.1 | `#0E131D` |
| surface.2 | `#151C28` |
| surface.3 | `#1A2332` |
| text.primary | `#F5F7FB` |
| text.secondary | `#B8C0D4` |
| text.muted | `#7E899F` |
| accent.primary | `#6C7CFF` |
| accent.secondary | `#50D8D7` |
| status.success | `#4ED598` |
| status.warning | `#F5B942` |
| status.danger | `#FF5C72` |
| status.info | `#62A8FF` |

Spacing is 8px-derived: 4, 8, 12, 16, 24, 32, 48, 64.

Radius direction:
- small: 6px
- controls: 8px
- cards: 10–12px
- large panels: 14–16px

Pills are reserved for compact status/tags, not default containers.

## 3. Typography and icons

Preferred UI-font class: Inter, Manrope or IBM Plex Sans.
Preferred mono class: JetBrains Mono or IBM Plex Mono.

Verify licenses before bundling.

Approximate hierarchy:
- display 36px
- H1 28px
- H2 22px
- H3 18px
- body 14–16px
- small 13px
- metadata 12px

Icons are one consistent licensed outline SVG family with geometric forms and rounded joins/caps. Lucide is a candidate, not a pre-approved dependency. Typical sizes: nav 20px, cards 24px, hero/empty 40–48px.

## 4. Quanta signature motifs

**Quanta Node** — connected knowledge/network motif.

**Quanta Grid** — very subtle technical spatial background.

**Quanta Pulse** — short one-shot state/progress animation for meaningful transitions.

These motifs must remain restrained and never become permanent animated noise.

## 5. Motion system

Motion communicates hierarchy, continuity, state, progress or feedback.

Starting duration bands:
- quick: ~150ms
- standard: ~200ms
- deliberate: ~250ms
- longer only for meaningful multi-stage transitions.

Use CSS transitions for normal hover/focus/transform/opacity. Use Web Animations API where native sequencing is sufficient. Evaluate GSAP only for genuinely complex coordinated timelines that CSS/WAAPI cannot express cleanly.

GSAP is **optional**. Before adding it, verify current license, maintenance, bundle impact and exact justified use.

Always support `prefers-reduced-motion`.

## 6. Responsive shell

Use existing CTFd/Bootstrap breakpoints where practical instead of creating a conflicting breakpoint system.

Direction:
- expanded sidebar ~240px,
- collapsed sidebar ~72px,
- normal content max-width ~1440px,
- Lab Workspace may use wider/full workspace width.

Wide desktop: full sidebar + multi-pane workspace.
Laptop: collapsed/compact sidebar + reduced panes.
Tablet: drawer navigation + tabbed/contextual surfaces.
Mobile: single-column priority flow, drawer/bottom navigation where appropriate, sticky critical lab status/actions.

Critical lab status, timer, Stop action, instructions and basic terminal access must remain available on mobile.

## 7. Personalized dashboard

The dashboard answers **What should I do now?**

Priority:
1. Continue Learning
2. Active Lab
3. Recommended Next
4. Progress
5. Skill Graph preview
6. Weekly Activity
7. Recent Activity
8. optional goal/achievements

Do not build a generic KPI dashboard.

New-user copy should invite a first action. Returning-user copy may reference the last room/path. Never use guilt-inducing streak language.

### Continue Learning

Show path, current room, difficulty, estimated remaining effort, path/task progress and one primary Continue action.

### Active Lab

Show user-facing lifecycle state, remaining time, appropriate target/access summary and Resume action. Preparing/failed states must have equally deliberate UX.

### Recommended Next

Until a dedicated recommendation backend exists, use deterministic explainable logic:
current-path next room -> unfinished room -> next unlocked room -> suitable starter room.

### Progress

Prefer domain progress (Web, Linux, Networking, Blue Team, AD, etc.) over one global score when data supports it.

### Skill Graph

A Quanta Skill Graph may visualize prerequisite/progress relationships. It must not claim psychometric proficiency or professional competence beyond measured learning evidence.

### Personalization contract

Use a dashboard provider boundary, e.g.:
- `MockDashboardProvider`
- `ApiDashboardProvider`

Potential future inputs: display name, current path, last room, completed rooms, active lab, recent activity, learning goal, domain preference, bookmarks and difficulty history.

A future Customize Dashboard may support show/hide widget preferences. Complex drag/drop is not required for M1.5.

Preserve room for Comfortable/Compact density modes without making them an M1.5 blocker.

## 8. Learning experience

Path cards: category, icon, difficulty, estimated effort, room/task count, tags and progress.

Path detail is a technical roadmap with states such as completed/current/available/locked; avoid cartoon game maps.

Room desktop direction: main learning content plus contextual right rail. Smaller screens move the rail below content or into a drawer.

Preferred task flow:
Context -> Explanation -> Example -> Lab/Action -> Question/Flag -> Completion Feedback.

Use 3–5 concrete learning objectives where content supports them.

## 9. Lab Workspace

Lab Workspace is a flagship surface.

Potential areas:
- objectives/instructions,
- tasks/questions,
- target/browser,
- terminal,
- notes,
- lab state,
- timer,
- progress.

Wide desktop may use resizable multi-pane layouts if the implementation remains maintainable. Laptop reduces pane count. Tablet/mobile use clear tabs or prioritized single-pane flows.

Focus Mode may reduce sidebar/topbar/secondary navigation while preserving current room, lab status, timer, terminal/target, critical actions and accessibility.

### User-facing lifecycle mapping

| Internal state | Learner label |
| --- | --- |
| REQUESTED / QUEUED / SCHEDULING | Preparing lab |
| PROVISIONING / STARTING / HEALTH_CHECK | Starting environment |
| READY | Lab Ready |
| STOPPING / CLEANING | Stopping lab |
| TERMINATED | Lab Stopped |
| EXPIRED | Lab Expired |
| FAILED / LOST | Environment unavailable |

Do not show stale READY if status/connectivity cannot be trusted.

Provisioning may present meaningful stages and a short one-shot Quanta Pulse when READY. Never invent backend work that is not happening.

## 10. Terminal

Prefer evaluating xterm.js for the terminal renderer rather than building a styled-div imitation.

Architecture:
```text
Terminal UI
    |
    v
TerminalAdapter
    +-- MockTerminalAdapter       M1.5
    +-- GatewayTerminalAdapter    future
```

M1.5 does not connect to a real shell.

Desired terminal behaviors:
- prompt,
- history Up/Down,
- Ctrl+C,
- clear,
- scrollback,
- copy,
- resize,
- fullscreen,
- colored output,
- errors,
- basic completion where reasonable,
- font sizing,
- connection/reconnect states.

Suggested restrained prompt: `qh-lab ❯`.

The mock command engine is deterministic and scenario-aware. Candidate commands: `help`, `whoami`, `pwd`, `ls`, `cat`, `clear`, `ip`, `ip addr`, `curl`, `nmap`, `history`.

Short realistic delays may be used. Do not create long fake waits.

Mock terminal/lab surfaces display a subtle **SIMULATED** or **DEMO ENVIRONMENT** indicator. Real gateway-backed sessions later use explicit **LIVE** state.

## 11. UI state harness

For deterministic visual QA, M1.5 should be able to render:
NO SESSION, REQUESTED, QUEUED, SCHEDULING, PROVISIONING, STARTING, HEALTH_CHECK, READY, STOPPING, EXPIRED, CLEANING, TERMINATED, FAILED, LOST, DISCONNECTED and STALE STATUS.

A developer-only state selector/harness is acceptable if excluded from normal production user experience.

## 12. Loading, recovery and notifications

Every major surface explicitly designs loading, empty, disabled, permission/not-found, error, disconnected and stale-data states.

Prefer skeletons for content pages over generic spinners.

Lab recovery examples:
- Connection interrupted
- Environment unavailable
- Session expired
- Status stale
- Cleanup in progress

Errors should state what happened, whether learning progress is safe when known, the next action and a correlation/reference ID when available. Never show raw stack traces to learners.

Toast/notification types: success, info, warning, error. Keep wording concise and technical.

## 13. Command palette

Preserve a future Ctrl/Cmd+K command palette for room/path search, Continue, Resume Lab, Progress, Settings and navigation. M1.5 may use mock/local data; do not invent backend search.

## 14. Provider/view-model boundaries

Where backend fields do not yet exist, use explicit provider contracts rather than hard-coded template state.

Conceptual boundaries:
- DashboardProvider
- LearningProvider
- LabUIProvider
- TerminalAdapter

Possible implementations:
- MockDashboardProvider / ApiDashboardProvider
- MockLearningProvider / ApiLearningProvider
- MockLabUIProvider / ApiLabUIProvider
- MockTerminalAdapter / GatewayTerminalAdapter

Keep abstractions small and replaceable; do not build an enterprise service layer for M1.5.

## 15. Component inventory

Conceptual reusable surfaces include:
- Sidebar / Topbar / Breadcrumb
- Button / IconButton
- Card / Badge / Status
- Progress / Timer
- Toast / Skeleton / EmptyState / ErrorState
- PathCard / RoomCard
- ContinueCard / ActiveLabCard / RecommendationCard
- ProgressOverview / SkillGraphMini / ActivityFeed / GoalCard
- LabWorkspace / LabPanel / Terminal
- CommandPalette

Names are conceptual. Implement with patterns natural to Jinja/Alpine/CTFd.

## 16. Accessibility

Target WCAG AA for normal product surfaces.

Verify:
- keyboard navigation,
- visible focus,
- semantic headings,
- accessible icon-button names,
- contrast,
- reduced motion,
- non-color-only states,
- restrained `role=status` / `aria-live` for meaningful dynamic lab status,
- terminal accessibility considerations.

## 17. Visual QA

Major UI work requires visual evidence, not pytest alone.

Representative surfaces:
- Dashboard
- Learn
- Path
- Room
- Lab Workspace
- Terminal
- Loading
- Empty
- Error
- Disconnected

Viewport matrix:
- wide desktop
- laptop
- tablet
- mobile

Check interaction/state matrix, overflow/clipping, contrast, focus, reduced motion and browser console errors.

## 18. Design debt

Use `docs/ui/UI_DEBT.md` when implementation begins. Each deferred item records ID, surface, problem, impact, reason deferred and future milestone.

## 19. M1.5 boundary

M1.5 implements the UI/UX Foundation and interactive prototype.

In scope:
design tokens, shell, dashboard, Learn/Path/Room, Skill Graph prototype, Lab Workspace, xterm.js evaluation/integration, mock terminal adapter/commands, mock lifecycle state harness, motion, Focus Mode, notifications, loading/empty/error, accessibility, responsive behavior and visual QA.

Out of scope:
real Runner, real vulnerable workloads, gVisor/Firecracker/KVM, production Lab Gateway, real shell/SSH/RDP, real recommendation AI/ML, full instructor/admin experiences, payments and certificates.
