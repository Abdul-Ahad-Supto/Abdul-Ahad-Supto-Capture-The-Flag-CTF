# Welcome to Emoji Stack

## Question:
Welcome to Emoji Stack, the brand new stack-based emoji language! Instead of other stack-based Turing machines that use difficult-to-read and challenging characters like `+`, `-`, and `[]`, Emoji Stack uses our proprietary patent-pending emoji system.

### Emoji Commands:
- **👉**: Move the stack pointer one cell to the right
- **👈**: Move the stack pointer one cell to the left
- **👍**: Increment the current cell by one, bounded by 255
- **👎**: Decrement the current cell by one, bounded by 0
- **💬**: Print the ASCII value of the current cell
- **🔁##**: Repeat the previous instruction 0x## times

The Emoji Stack is 256 cells long, with each cell supporting a value between 0 - 255.

### Example:
The program `👍🔁47💬👉👍🔁68💬👉👍🔁20💬` would output `Hi!` with the following execution flow:

1. Initial state: `[0, 0, 0, 0]` `👍🔁47`
2. After increment: `[0x48, 0, 0, 0]` `💬👉`: H
3. After next increment: `[0x48, 0x69, 0, 0]` `💬👉`: i
4. Final increment: `[0x48, 0x69, 0x21, 0]` `💬`: !

### Implementation:
Firstly We can notice in text Editor that its format is UTF-16LE. so we decode it first using cyber chef and get a pile of emojis to work With
```python
emoji_string = '''👉👉👉👉👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👉🔁08👍🔁34👈👈👈👈👈👈👈👈👈👈👍🔁48👉🔁15👍🔁5e👈🔁07👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👉🔁02👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👍🔁42👉🔁02👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👉🔁17👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👈🔁14👍🔁20👉🔁06👍🔁51👉🔁0c👍🔁34👉👉👍🔁46👈🔁14👍🔁4d👈🔁01👍🔁51👉🔁04👍🔁20👉🔁03👍🔁2f👉👉👉👉👉👉👉👉👍🔁4d👈🔁17👍🔁42👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👍🔁7c👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👉🔁0c👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👉👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👈👈👈👈👈👈👈👈👈👈👈👈👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👉🔁0c👍🔁32👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👉🔁04👍🔁5e👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👍🔁47👈🔁0f👍🔁46👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👉👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👈🔁03👍🔁20👈🔁08👍🔁5e👉🔁10👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👈🔁1d👍🔁40👉🔁10👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👉👉👉👉👍🔁5e👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬👉💬'''
# Example emoji

memory = [0 for _ in range(256)]
pointer = 0        # Keeps track of the current memory cell (index)
emoji_index = 0    # Keeps track of the current emoji in the string
previous_command = None  # Stores the last command to repeat if needed

# Process each emoji in the string
while emoji_index < len(emoji_string):
    current_emoji = emoji_string[emoji_index]

    if current_emoji == '👉':
        # Move pointer to the right
        pointer += 1
        previous_command = '👉'

    elif current_emoji == '👈':
        # Move pointer to the left
        pointer -= 1
        previous_command = '👈'

    elif current_emoji == '👍':
        # Increment the value at the current memory cell
        memory[pointer] += 1
        previous_command = '👍'

    elif current_emoji == '👎':
        # Decrement the value at the current memory cell
        memory[pointer] -= 1
        previous_command = '👎'

    elif current_emoji == '💬':
        # Output the character corresponding to the ASCII value at the current memory cell
        ascii_value = int(memory[pointer])
        print(chr(ascii_value), end="")

    elif current_emoji == '🔁':
        # Repeat the last command based on the next two hexadecimal digits
        emoji_index += 1
        hex_digit1 = emoji_string[emoji_index]
        hex_digit2 = emoji_string[emoji_index + 1]
        hex_str = hex_digit1 + hex_digit2

        # Convert hex string to an integer (repeat count)
        repeat_count = int(hex_str, 16)
        emoji_index += 1

        # Execute the previous command 'repeat_count' times
        while repeat_count != 0:
            if previous_command == '👉':
                pointer += 1
            elif previous_command == '👈':
                pointer -= 1
            elif previous_command == '👍':
                memory[pointer] += 1
            elif previous_command == '👎':
                memory[pointer] -= 1
            repeat_count -= 1

    emoji_index += 1
```
# flag
CACI{TUR!NG_!5_R011!NG_!N_H!5_GR@V3}
