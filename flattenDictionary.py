#Pramp flatten dictionary
def flatten_dictionary(dictionary):
  ans = {}
  def helper(initialKey, dictionary):
    for key, val in dictionary.items():
      if type(val)==dict:
        if initialKey==None or initialKey=="":
          helper(key, val)
        else:
          if key==None or key=="":
            helper(initialKey, val)
          else:
            helper(initialKey + "." + key, val)
      else:
        if initialKey==None or initialKey=="":
          ans[key] = val
        else:
          if key==None or key=="":
            ans[initialKey] = val
          else:
            ans[initialKey + "." + key] = val
      
  helper(None, dictionary)
  return ans 

print(flatten_dictionary({"":{"a":"1"},"b":"3"}))
        
        