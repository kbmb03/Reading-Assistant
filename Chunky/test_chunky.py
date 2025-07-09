#test_chunky
#Kaleb Davis 7/8/2025
from chunker import Chunkify

sample_text = """
– These English psychologists, who have to be thanked for having made
the only attempts so far to write a history of the emergence of morality, –
provide us with a small riddle in the form of themselves; in fact, I admit
that as living riddles they have a significant advantage over their books –
they are actually interesting! These English psychologists – just what do
they want? You always find them at the same task, whether they want to or
not, pushing the partie honteuse of our inner world to the foreground, and
looking for what is really effective, guiding and decisive for our development where man’s intellectual pride would least wish to find it (for
example, in the vis inertiae of habit, or in forgetfulness, or in a blind and
random coupling and mechanism of ideas, or in something purely passive,
automatic, reflexive, molecular and thoroughly stupid) – what is it that
actually drives these psychologists in precisely this direction all the time?
Is it a secret, malicious, mean instinct to belittle humans, which it might
well not admit to itself? Or perhaps a pessimistic suspicion, the mistrust
of disillusioned, surly idealists who have turned poisonous and green? Or
a certain subterranean animosity and rancune towards Christianity (and
Plato), which has perhaps not even passed the threshold of consciousness?
Or even a lewd taste for the strange, for the painful paradox, for the
dubious and nonsensical in life? Or finally – a bit of everything, a bit of
meanness, a bit of gloominess, a bit of anti-Christianity, a bit of a thrill and
need for pepper? . . . But people tell me that they are just old, cold, boring
frogs crawling round men and hopping into them as if they were in their
element, namely a swamp. I am resistant to hearing this and, indeed, I do
10
not believe it; and if it is permissible to wish where it is impossible to know,
I sincerely hope that the reverse is true, – that these analysts holding a
microscope to the soul are actually brave, generous and proud animals,
who know how to control their own pleasure and pain and have been
taught to sacrifice desirability to truth, every truth, even a plain, bitter,
ugly, foul, unchristian, immoral truth . . . Because there are such truths. –
2
So you have to respect the good spirits which preside in these historians of morality! But it is unfortunately a fact that historical spirit itself is
lacking in them, they have been left in the lurch by all the good spirits of
history itself! As is now established philosophical practice, they all think
in a way that is essentially unhistorical; this can’t be doubted. The idiocy
of their moral genealogy is revealed at the outset when it is a question
of conveying the descent of the concept and judgment of ‘good’.
‘Originally’ – they decree – ‘unegoistic acts were praised and called good
by their recipients, in other words, by the people to whom they were useful; later, everyone forgot the origin of the praise and because such acts
had always been habitually praised as good, people also began to experience them as good – as if they were something good as such’. We can see
at once: this first deduction contains all the typical traits of idiosyncratic
English psychologists, – we have ‘usefulness’, ‘forgetting’, ‘habit’ and
finally ‘error’, all as the basis of a respect for values of which the higher
man has hitherto been proud, as though it were a sort of general privilege
of mankind. This pride must be humbled, this valuation devalued: has that
been achieved? . . . Now for me, it is obvious that the real breedingground for the concept ‘good’ has been sought and located in the wrong
place by this theory: the judgment ‘good’ does not emanate from those to
whom goodness is shown! Instead it has been ‘the good’ themselves,
meaning the noble, the mighty, the high-placed and the high-minded,
who saw and judged themselves and their actions as good, I mean firstrate, in contrast to everything lowly, low-minded, common and plebeian.
It was from this pathos of distance that they first claimed the right to
create values and give these values names: usefulness was none of their
concern! The standpoint of usefulness is as alien and inappropriate as it
can be to such a heated eruption of the highest rank-ordering and rankdefining value judgments: this is the point where feeling reaches the
opposite of the low temperatures needed for any calculation of prudence
11
First essay
or reckoning of usefulness, – and not just for once, for one exceptional
moment, but permanently. The pathos of nobility and distance, as I said,
the continuing and predominant feeling of complete and fundamental
superiority of a higher ruling kind in relation to a lower kind, to those
‘below’ – that is the origin of the antithesis ‘good’ and ‘bad’. (The
seigneurial privilege of giving names even allows us to conceive of the
origin of language itself as a manifestation of the power of the rulers: they
say ‘this is so and so’, they set their seal on everything and every occurrence with a sound and thereby take possession of it, as it were). It is
because of this origin that from the outset, the word ‘good’ is absolutely
not necessarily attached to ‘unegoistic’ actions: as the superstition of these
moral genealogists would have it. On the contrary, it is only with a decline
of aristocratic value judgments that this whole antithesis between ‘egoistic’ and ‘unegoistic’ forces itself more and more on man’s conscience, – it
is, to use my language, the herd instinct which, with that, finally gets its
word in (and makes words). And even then it takes long enough for this
instinct to become sufficiently dominant for the valuation of moral values
to become enmeshed and embedded in the antithesis (as is the case in contemporary Europe, for example: the prejudice which takes ‘moral’,
‘unegoistic’ and ‘désintéressé as equivalent terms already rules with the
power of a ‘fixed idea’ and mental illness)."""

chunks = Chunkify(sample_text, max_tokens=50, overlap_tokens=10)

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---\n{chunk}")
