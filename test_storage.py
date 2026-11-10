from storage import save_practice_set, load_practice_set

# Load an existing practice set
practice_set = load_practice_set("data/practice_set.json")

# Save a copy to a new location
save_practice_set(practice_set, "data/practice_sets/test_set.json")

print("Test completed successfully!")

from storage import list_practice_sets

saved_sets = list_practice_sets()

for file in saved_sets:
    print(file.name)

