package trainset;

import java.util.ArrayList;
import java.util.List;

public class PunctuationAndDigits {

	public List<String> removePD(List<String> list)
	{
		List<String> rValue = new ArrayList<String>();
		for (String a:list)
		{
			String ans= a.replaceAll("[^çÇöÖğĞİışŞüÜa-zA-Z]", "");
			rValue.add(ans);
		}
	
		return rValue;
	}
}
