import random

# Step 1: Read the text file
with open("input.txt", "r") as f:
    text = f.read().lower()

# Step 2: Split text into words
words = text.split()

# Step 3: Build the Markov chain dictionary
markov_chain = {}
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    if current_word not in markov_chain:
        markov_chain[current_word] = []
    markov_chain[current_word].append(next_word)

# Step 4: Generate random text
current_word = random.choice(list(markov_chain.keys()))
generated_text = current_word

for _ in range(100):  # generate 100 words
    next_words = markov_chain.get(current_word, None)
    if not next_words:
        break
    current_word = random.choice(next_words)
    generated_text += " " + current_word

# Step 5: Print the generated text
print("\nGenerated Text:\n")
print(generated_text)
# Save the generated text to a file
with open("generated_text.txt", "w") as f:
    f.write(generated_text)

print("\nGenerated text saved to 'generated_text.txt'")

