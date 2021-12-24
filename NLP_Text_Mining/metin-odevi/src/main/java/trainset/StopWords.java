package trainset;

import java.util.ArrayList;
import java.util.List;

public class StopWords {

	public List<String> removeStopWords(List<String> list,List<String> sWords)
	{	
		List<String> rValue = new ArrayList<String>();
		for (String a:list)
		{
			if(!sWords.contains(a))
				rValue.add(a);
		}
		return rValue;
	}
}
