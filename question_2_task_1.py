#Find out if Alice submitted their assignment and attended class. HINT: How might the in keyword be of use here? 
# And how can you check to see if Alice is in both submitted and attended in one if statement?


submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
print("Alice" in submitted + attended)

student = "Alice"
if "Alice" in submitted and "Alice" in attended:
    print("congrats!")