def line(string):
   vowels = ['у','е','ы','а','о','э','я','и','ю']
#   newline = string.lower()
   total = 0
   for s in string:
      if s.lower() in vowels:
         total += 1
   return total
print(line("ПРИВЕТ"))