from collections import defaultdict
def duplicate_count(text):
    duplicates = []
    tally = defaultdict(int)

    text = text.replace(" ", "").lower()
    
    for i in text:
        tally[i] += 1
        
    for k in tally:
      if tally[k] > 1:
          duplicates.append(k)
    
    return len(duplicates)
