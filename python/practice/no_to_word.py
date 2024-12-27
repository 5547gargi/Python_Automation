'''
import inflect

def number_to_words(number):
    # Create an inflect engine instance
    p = inflect.engine()
    
    # Convert the number to words
    words = p.number_to_words(number)
    
    return words

# Example usage
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(f"The number {number} in words is: {number_to_words(number)}")
'''
num=eval(input("Enetr yoyr number : "))
num_word={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
if num in [1,2,3,4,5,6,7,8,9,10] :
    print(num_word.get(num))
else:
    print("No if out of range, please select 1-10 range")