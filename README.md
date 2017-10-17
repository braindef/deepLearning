### deepLearning

Die Datei beispiele.txt zeigt einige Outputs. Ich bin der Meinung, dass das mir hilft einen Überblick zu erhalten / behalten.

verwendet habe ich das gensim und word2vec das mit python pip installiert werden kann und nach der Anleitung: http://mfcabrera.com/blog/2013/11/14/word2vec-germanblogorg.html mal rumprobiert aber nicht mit den Wikipedia Artikeln wie im Tutorial beschrieben sondern mit meinen Tagebüchern.


als erstes muss man das word2vec und gensim installieren

-> **./shell/install.sh**

dann muss mann den Text umwandeln dass er keine Kommas, sonderzeichen etc hat

-> **./shell/clean.sh eingabe.txt > ausgabe.txt**

dann muss man aus der Ausgabedatei eine word2vec bin datei machen

-> **./shell/generateBin.sh ausgabe.txt**
  ->das gibt dann eine **ausgabe.txt.bin** Datei
  
dann kann man darin z.B. ähnliche Worte suchen

-> **python suchen.py --bin ausgabe.txt.bin --positive schizophrenie suizid --negative zyprexa xeplion**
    (also wenn wir zwar was über schizophrenie und suizid aber nichts von medikamenten wissen wollen)

in den Beispieldateien sieht mach auch wie man das python word2vec und gensim verwendet
