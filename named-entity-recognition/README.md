
install nltk and run
	nltk.download()

maxent_ne_chunker

	The maxent_ne_chunker contains two pre-trained English named entity chunkers trained on an ACE corpus
	It will load an nltk.chunk.named_entity.NEChunkParser object and it is used by the nltk.ne_chunk() function.

From the relation extraction code function in NLTK, it lists the following tags for the ACE tagset:

LOCATION
ORGANIZATION
PERSON
DURATION
DATE
CARDINAL
PERCENT
MONEY
MEASURE
FACILITY
GPE