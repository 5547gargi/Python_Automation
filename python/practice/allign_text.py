import os

# tput cols : to find out columns in the linux terminal
# mode : to find out columns in the windows terminal
# print(os.get_terminal_size())  : cross_platform compatibility 
# print(os.get_terminal_size().columns)
t_w=os.get_terminal_size().columns
given_str=input("Enter your string: ")
print(given_str.center(t_w).title())
print(given_str.ljust(t_w).title())
print(given_str.rjust(t_w).title())

'''
# alternate option for text alignment 
import os

def center_text(text):
  """Centers the given text within the current terminal width."""
  terminal_width, _ = os.get_terminal_size()
  print(terminal_width)
  text_length = len(text)
  padding = (terminal_width - text_length) // 2  # Calculate padding on each side
  centered_text = " " * padding + text
  print(centered_text)

if __name__ == "__main__":
  text_to_center = input("Enter your string: ")
  center_text(text_to_center)
'''