package trainset;

import java.util.ArrayList;
import java.util.List;

import zemberek.morphology.TurkishMorphology;
import zemberek.morphology.analysis.SingleAnalysis;
import zemberek.morphology.analysis.WordAnalysis;

public class Stemming {
	
	public List<String> stems(List<String> list)
	{
		TurkishMorphology morph = TurkishMorphology.createWithDefaults();
		
		List<String> rValue = new ArrayList<String>();
		for (String words : list)
		{
			WordAnalysis stem = morph.analyze(words);
			for (SingleAnalysis analysis:stem)
			{
				List<String> a=analysis.getStems();
				String ans = a.get(a.size()-1);
				if(ans.length()>1)
					rValue.add(ans);
			}
		}
		return rValue;
		
	}
}
