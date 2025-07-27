def count_words(the_text):
  return len(the_text.split())

def get_frequency(text):
  frequency = {}
  if len(text) == 0:
    return {}
  
  for t in text:
    lower_t = t.lower()
    frequency[lower_t] = frequency.get(lower_t, 0) + 1
      
    
  return frequency


def sorted_dict_to_list(my_dict):
  my_list = []
  for key, val in my_dict.items():
    item = {
      "char": key,
      "num": val
    }
    my_list.append(item)
  
  my_list.sort(key=lambda x: x["num"], reverse=True)

  return my_list