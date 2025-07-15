import aiml
import os

# Initialize AIML Kernel
kernel = aiml.Kernel()

# Load or learn AIML files
if os.path.exists("brain.brn"):
    print("Loading brain from brain.brn...")
    kernel.bootstrap(brainFile="brain.brn")
    print("Loading brain from brain.brn...done")
else:
    kernel.bootstrap(learnFiles="std-startup.xml", commands="LOAD AIML B")
    kernel.saveBrain("brain.brn")

print("=== Smart Course Recommender ===")
interest = input("Enter your area of interest (e.g., Data Science, Web, AI): ").strip().upper()
level = input("Enter your skill level (Beginner, Intermediate, Advanced): ").strip().upper()
style = input("Preferred learning style (Video, Theory, Hands-on): ").strip().upper()

# Normalize and construct query
query = f"{level} {interest} {style}".replace("-", " ").strip()

# Debug print (optional)
# print(f"[DEBUG] Query sent to AIML: {query}")

# Get response from AIML
response = kernel.respond(query)

# Output response
if response and response.strip() and "Sorry" not in response:
    print("\n🎓 Recommended Course:")
    print(response)
else:
    print("\nSorry, we couldn't find a matching course for your preferences.")
