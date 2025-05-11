public class Solution {
    public bool WordPattern(string pattern, string s) {
       string[] words = s.Split(' '); 
       if(words.Length!=pattern.Length)
       return false;
       var map = new Dictionary<char, string>();
       var mappedValues = new HashSet<string>();

       for(int i=0;i<pattern.Length;i++){
        char c=pattern[i];
        string w=words[i];
        if(map.ContainsKey(c)){
            if(map[c]!=w)
            return false;
        }
        else
        {
           if (mappedValues.Contains(w))
                return false;
           map[c]=w;
           mappedValues.Add(w);

        }
       
       }
         return true;
    }
}