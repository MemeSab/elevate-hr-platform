---
description: Protocol for Closing Tasks and Phases in the Elevate Project
---

# Elevate – Task & Phase Closure Protocol (SOP)

This workflow must be executed by the AI agent every time a major technical task (Linear Issue) or project phase is completed.

## 🛠️ Step 1: Local Documentation Update
Update the following files in `/project_management/`:
*   `project_roadmap_and_tasks.md`: Check off the completed task.
*   `risk_register_and_log.md`: Mark any resolved risks tied to the task as "Resolved".
*   `retrospective_templates.md`: Add a fresh retrospective entry detailing what was planned vs. what was shipped.

## 🔄 Step 2: Linear Synchronization
Synchronize the local documentation changes to the corresponding **Linear Documents**:
1.  Update the "Risk Register & Issue Log" document in Linear.
2.  Update the "Retrospective Templates" document in Linear.
3.  Update the "Phase Roadmap" document in Linear.

## ✅ Step 3: Issue Closure
1.  Set the Linear Issue status to **Done**.
2.  Post a **Comment** on the issue containing the task-specific retrospective log.

## 📡 Step 4: Phase Completion Broadcast (Phase-Only)
Upon completing a full Phase (e.g., Phase 3, Phase 4):
1.  Use the `research` tool to post a **Project Status Update** to the Linear Project board.
2.  Set the project **Health** (e.g., "On Track").
3.  Provide a high-level summary of the accomplishments and the next milestone.
4.  Update the **Project Progress %** if applicable.

---
*Created: 2026-04-05*
