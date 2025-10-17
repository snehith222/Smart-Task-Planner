"""
Smart Task Planner

"""

import random
import datetime

# -------- AI Mock Logic (you can replace this with OpenAI if you have an API key) ----------
def generate_task_plan(goal_text):
    # Extract a rough duration number if mentioned in goal
    duration_weeks = 2
    for word in goal_text.split():
        if word.isdigit():
            duration_weeks = int(word)

    # Example tasks — in a real AI version, these come from an LLM
    base_tasks = [
        "Define the goal and key outcomes",
        "Research and gather resources",
        "Create a plan and assign tasks",
        "Execute and monitor progress",
        "Review, test, and finalize deliverables",
        "Launch and collect feedback"
    ]

    # Generate random durations (1–3 days each)
    today = datetime.date.today()
    tasks = []
    current_day = today

    for task in base_tasks:
        duration_days = random.randint(1, 3)
        start_date = current_day
        end_date = current_day + datetime.timedelta(days=duration_days)
        tasks.append({
            "task": task,
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "duration_days": duration_days
        })
        current_day = end_date + datetime.timedelta(days=1)

    return {
        "goal": goal_text,
        "total_duration_weeks": duration_weeks,
        "tasks": tasks
    }

# ----------------------------- Main Program -----------------------------
if __name__ == "__main__":
    print("🔹 SMART TASK PLANNER 🔹")
    print("This tool converts your goal into actionable tasks.\n")
    goal_text = input("Enter your goal: ")

    print("\n🧩 Generating your plan...\n")
    plan = generate_task_plan(goal_text)

    print(f"Goal: {plan['goal']}")
    print(f"Estimated Duration: {plan['total_duration_weeks']} weeks\n")

    print("🗓️  Task Breakdown:")
    for i, task in enumerate(plan['tasks'], 1):
        print(f"{i}. {task['task']}")
        print(f"   Start: {task['start_date']}  →  End: {task['end_date']}  ({task['duration_days']} days)\n")

    print("✅ Plan successfully generated!\n")
    print("Tip: You can modify this script later to use OpenAI or another LLM for real AI reasoning.")
