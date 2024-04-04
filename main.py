from __init__ import *


file_path = "/Users/Shmuli/Library/Application Support/Code/User/snippets/global_snippets.code-snippets"

with open(file_path, 'r') as file:
    content = file.read()


if input(f"{f.BLUE}p{f.RESET} to print out contents of current global snippets file (any other key followed by enter to skip): "):
    print(content)


name = input(f"snippet name {optionalMessage}: ")
body = handelMultiLineInput()
prefix = input(f"prefix {requiredMessage}: ")
description = input(f"description {optionalMessage}: ")
scope = input(f"scope {optionalMessage}: ")


if scope:
    scope = f'{newline}"scope": "{scope}",'
obj = f'{"{"}{newline}"prefix": "{prefix}",{scope}{newline}"body": [{longLine}"{longLineWithQuotes.join(body)}"{newline}],{newline}"description": "{description or f"a shortcut that turns {prefix} into {body}"}"\n'

if not name:
    name = autoName()

snippet = '"' + name + '": ' + obj + '},'

message(snippet)

last_bracket_index = content.rfind('}')

new_content = content[:last_bracket_index] + snippet + content[last_bracket_index:]

# Write the updated content back to the file
with open(file_path, 'w') as file:
    file.write(new_content)


print(f"you new global snippets file will look like \n{new_content}")
print(f'enter {f.BLUE}code "{file_path}{f.RESET}" to open up snippets file in your editor')