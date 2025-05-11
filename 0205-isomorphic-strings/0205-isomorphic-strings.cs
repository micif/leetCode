public class Solution {
    public bool IsIsomorphic(string s, string t) {
        if (s.Length != t.Length)
        return false;

    var mapST = new Dictionary<char, char>();

    var mappedValues = new HashSet<char>();

    for (int i = 0; i < s.Length; i++)
    {
        char c1 = s[i]; 
        char c2 = t[i]; 

        if (mapST.ContainsKey(c1))
        {
            if (mapST[c1] != c2)
                return false;
        }
        else
        {
            if (mappedValues.Contains(c2))
                return false;

            mapST[c1] = c2;
            mappedValues.Add(c2);
        }
    }

    return true;
    }
}