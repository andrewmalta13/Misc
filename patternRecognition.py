#A generalized solution to a dropbox interview question: How can you tell if two strings
#follow a common pattern, e.g "a b b a" and "cat dog dog cat" where each symbol is dilineated
#by a space

#Andrew Malta 12/22/14

def serialize(exp):
  d = {}
  result = []
  count = 0
  for i in exp:
    if i in d:
      result.append(d[i])
    else:
      count += 1
      result.append(count)
      d[i] = count

  return result


# expects two strings with symbols sperated by spaces, which allows for
# a split.
def samePattern(string1, string2):
  return serialize(string1.split()) == serialize(string2.split())


