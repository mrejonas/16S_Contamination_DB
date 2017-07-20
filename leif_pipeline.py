#!/usr/bin/python

''' This is a pipeline for contamination removal from NGS sequences commonly
    used for Microbiome analysis. Pipeline based on Laurence etal
    doi:10.1371/journal.pone.0097876'''

''' Step 1: Label bases with quality scores ≤ "%" as "incorrectly called"('N') '''

''' Step 2: Read pairs need to satisfy the following criteria:
    - ≥ 90% of bases in each read are deemed "correctly called" (see Step 1)
    - ≥ 50% of 32 base substrings in each read contain correctly called reads '''

''' Step 3: Discard read pairs sharing exactly-matching 32 base substring with
    Human, Epstein-Barr virus or phage sequences '''

''' Step 4: Discard nearly identical read pairs defined as:
    - bases 5 to 64 were compared and labeled as nearly identical
    if ≥ 57 bases matched '''

''' Step 5: Run DUST to mask low complexity sequences'''

''' Step 6: Read pairs containing too many masked low complexity DUSTed
    sequences'''

''' Step 7: '''

''' Step 8: '''

''' Step 9: '''

''' Step 10: '''
