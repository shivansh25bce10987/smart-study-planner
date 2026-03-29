# Smart Study Planner with Dynamic Input and Performance Analysis

class StudyPlannerAgent:
    def __init__(self, subjects, ratings, hours_per_day):
        self.subjects = subjects
        self.ratings = ratings
        self.hours_per_day = hours_per_day

    def analyze_performance(self):
        report = {}
        for sub in self.subjects:
            rating = self.ratings[sub]

            if rating >= 4:
                report[sub] = "Strong"
            elif rating == 3:
                report[sub] = "Average"
            else:
                report[sub] = "Weak"

        return report

    def generate_strategy(self, report):
        strategy = "\n📊 Study Strategy:\n"

        weak = [s for s in report if report[s] == "Weak"]
        avg = [s for s in report if report[s] == "Average"]
        strong = [s for s in report if report[s] == "Strong"]

        if weak:
            strategy += f"- Focus more on weak subjects: {', '.join(weak)}\n"
        if avg:
            strategy += f"- Improve average subjects: {', '.join(avg)}\n"
        if strong:
            strategy += f"- Maintain strong subjects: {', '.join(strong)}\n"

        strategy += "\nPlan prioritizes weak subjects while maintaining balance."

        return strategy

    def generate_plan(self, report):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        weights = {}
        for sub in self.subjects:
            if report[sub] == "Weak":
                weights[sub] = 3
            elif report[sub] == "Average":
                weights[sub] = 2
            else:
                weights[sub] = 1

        total_weight = sum(weights.values())
        plan = {}

        for day in days:
            plan[day] = []
            remaining_hours = self.hours_per_day

            for sub in self.subjects:
                allocated = round((weights[sub] / total_weight) * self.hours_per_day)

                if allocated > 0 and remaining_hours > 0:
                    allocated = min(allocated, remaining_hours)
                    plan[day].append((sub, allocated))
                    remaining_hours -= allocated

        return plan


# -------- USER INPUT --------

subjects = []
ratings = {}

n = int(input("Enter number of subjects: "))

for i in range(n):
    sub = input(f"Enter subject {i+1}: ")
    rating = int(input(f"Rate your performance in {sub} (1-5): "))
    
    subjects.append(sub)
    ratings[sub] = rating

hours_per_day = int(input("\nEnter study hours per day: "))


# -------- RUN AGENT --------

agent = StudyPlannerAgent(subjects, ratings, hours_per_day)

report = agent.analyze_performance()
strategy = agent.generate_strategy(report)
plan = agent.generate_plan(report)


# -------- OUTPUT --------

print("\n📊 PERFORMANCE REPORT:")
for sub, status in report.items():
    print(f"{sub}: {status}")

print(strategy)

print("\n📅 WEEKLY STUDY PLAN:\n")

for day, tasks in plan.items():
    print(f"\n{day}:")
    for sub, hrs in tasks:
        print(f"  {sub} → {hrs} hrs")