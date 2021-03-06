package test;

import java.io.IOException;
import java.util.List;

import trainset.PunctuationAndDigits;
import trainset.TextReader;
import zemberek.tokenization.TurkishTokenizer;

public class TokenReader {

	public List<String> read (String file,String fileName) throws IOException
	{
		TextReader reader= new TextReader();
		String sentences=reader.readText(file, "UTF-8",fileName);
		TurkishTokenizer tokenizer = TurkishTokenizer.DEFAULT;
	    List<String> tokens = tokenizer.tokenizeToStrings(sentences);
	    PunctuationAndDigits pD= new PunctuationAndDigits();
	    List<String> RemovedPD = pD.removePD(tokens);
	    return RemovedPD;
	}
}
